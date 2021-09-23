#!/usr/bin/env python3
import os
import cgi
import cgitb
import json
from secret import username, password
from templates import secret_page, after_login_incorrect

#cgitb.enable()

form = cgi.FieldStorage()

u_name = form.getvalue("username")
p_word = form.getvalue("password")

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello again</title>")
print("</head>")
print("<body>")
print("<p><b>Username:</b> %s <b>Password:</b> %s</p>" % (u_name, p_word))
print("</body>")
print("</html>")


# json_back = json.dumps(dict(os.environ), indent = 4)
# print(json_back)
#print(u_name, username, p_word, password)
if u_name == username and p_word == password:
	print("Content-Type: text/html")
	print("Set-Cookie: username={};".format(u_name))
	print("Set-Cookie: password={};".format(p_word))
	print(secret_page(u_name, p_word))

json_back = json.dumps(dict(os.environ), indent = 4)
print(json_back)





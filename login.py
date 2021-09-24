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

c_user = None
c_pwd = None

cookie_info = os.environ.get("HTTP_COOKIE")
cookie_sepa = cookie_info.split("; ")
if len(cookie_sepa) >= 2:
	c_user = cookie_sepa[0][9:]
	c_pwd = cookie_sepa[1][9:]



if c_user and c_pwd:
	print("\n####################################\n")
	print(secret_page(c_user, c_pwd))
	json_back = json.dumps(dict(os.environ), indent = 4)
	print(json_back)

# json_back = json.dumps(dict(os.environ), indent = 4)
# print(json_back)
#print(u_name, username, p_word, password)
elif u_name == username and p_word == password:
	
	print("Set-Cookie:Username = {};".format(u_name))
	print("Set-Cookie:Password = {};".format(p_word))
	# print("Content-Type:text/html\r\n\r\n")
	# print("<html>")
	# print("<head>")
	# print("<title>COOKIES SET - FIRST</title>")
	# print("</head>")
	# print("<body>")
	# print("<h2>ALL Done!</h2>")
	# print("</body>")
	# print("</html>")
	print(secret_page(u_name, p_word))

	json_back = json.dumps(dict(os.environ), indent = 4)
	print(json_back)

else:
	print(after_login_incorrect())







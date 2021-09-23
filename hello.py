#!/usr/bin/env python3
import os, json
import cgitb
import cgi

from templates import login_page, _wrapper

cgitb.enable()
print("Content-type:text/html\r\n\r\n")
print("<title>Test CGI</title>")
print("<p>Hello World!</p>")


#print(os.environ)
#print("\n####################################\n")

json_back = json.dumps(dict(os.environ), indent = 4)
#print(json_back)
#print("\n####################################\n")

for param in os.environ.keys():
	if param == "QUERY_STRING":
		print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

for param in os.environ.keys():
	if param == "HTTP_USER_AGENT":
		print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

print(login_page())


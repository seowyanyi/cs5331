redirect_url = 'http://www.google.com'

# do POST to the form
url = 'http://www.wsb.com/Assignment2/case18/case18.php?LANG=' + redirect_url


import webbrowser
new = 2 #open in new window
webbrowser.open(url,new=new)
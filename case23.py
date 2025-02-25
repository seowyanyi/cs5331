import urllib, urllib2, cookielib
import os
import hashlib
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# for this test case, just set admin=true in url after registering account.

import time

def sha512hash(plaintext):
    return hashlib.sha512(plaintext).hexdigest()
password = 'studentaZ0'
hashedpassword = sha512hash(password)
username = "seowyanyi"
email = "seow.yanyi@gmail.com"

# do POST to the form to create account
values = dict(username=username, email=email, p=hashedpassword)
data = urllib.urlencode(values)

print 'creating account'
register_url = 'http://www.wsb.com/Assignment2/case23/register.php'
req = urllib2.Request(register_url, data)
rsp = urllib2.urlopen(req)
content = rsp.read()

# login
print 'logging in'
driver = webdriver.Firefox()
driver.get('http://www.wsb.com/Assignment2/case23/login.php')

def find_by_xpath(locator):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, locator))
    )

    return element


find_by_xpath('//input[@name = "email"]').send_keys(email)
find_by_xpath('//input[@name = "password"]').send_keys(password)
find_by_xpath('//input[@type = "button"]').click()
bad_url = 'http://www.wsb.com/Assignment2/case23/protected_page.php?admin=true'
print 'getting bad url'
driver.get(bad_url)
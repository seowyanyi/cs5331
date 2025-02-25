import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

password = sys.argv[1]

print 'logging in case 20 with password {}'.format(password)
driver = webdriver.Firefox()
driver.get('http://www.wsb.com/Assignment2/case20/login.php')

def find_by_xpath(locator):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, locator))
    )

    return element


find_by_xpath('//input[@name = "email"]').send_keys('admin@admin.com')
find_by_xpath('//input[@name = "password"]').send_keys(password)
find_by_xpath('//input[@type = "button"]').click()
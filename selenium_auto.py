#// Don't forget to hit SUBSCRIBE and LIKE and COMMENT, and LEARN. ...It's good to learn :)

'''imports'''
from selenium import webdriver
import time

url = 'https://outlook.live.com/'

driver = webdriver.Chrome(r'C:\Users\ncorb\Documents\All THING PYTHON\tmp\chromedriver')
driver.get(url)

driver.find_element_by_class_name('linkButtonSigninHeader').click()
time.sleep(2)


driver.find_element_by_id('MemberName').send_keys('TESTINGuserigmanstname123')
time.sleep(2)

driver.find_element_by_id('iSignupAction').click()
time.sleep(2)

driver.find_element_by_id('PasswordInput').send_keys('TESTINGpassword123')
time.sleep(2)

driver.find_element_by_id('iSignupAction').click()
time.sleep(2)

driver.find_element_by_id('FirstName').send_keys('John')
time.sleep(2)

driver.find_element_by_id('LastName').send_keys('keets')
time.sleep(2)

driver.find_element_by_id('iSignupAction').click()
time.sleep(2)

driver.find_element_by_id('BirthDay').send_keys('11')
time.sleep(2)

driver.find_element_by_id('BirthMonth').send_keys('07')
time.sleep(2)

driver.find_element_by_id('BirthYear').send_keys('1992')
time.sleep(2)


driver.close()


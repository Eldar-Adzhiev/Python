# pip3 install selenium -  установка библиотеки селениум

from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver.exe')
driver.get('http://itcareer.pythonanywhere.com/')
time.sleep(2)

name_field = driver.find_element_by_id('name')
name_field.send_keys('Inna')
time.sleep(1)

surname_field = driver.find_element_by_id('surname')
surname_field.send_keys('Didenko')
time.sleep(1)

email_field = driver.find_element_by_id('email')
email_field.send_keys('Didenko@mail.ru')
time.sleep(1)

password_field = driver.find_element_by_id('password')
password_field.send_keys('1234qaza')
time.sleep(1)

submit_button = driver.find_element_by_tag_name('button')
submit_button.click()
time.sleep(1)

# success_message = driver.find_element_by_tag_name('strong')
# print(success_message.text)

message_path = '/html/body/div[2]/div/div/div/strong'
success_message_2 = driver.find_element_by_xpath(message_path)

if 'Success' in success_message_2.text:
    print('Test_success_message - Passed')
else:
    print('Test_success_message - Failed')

time.sleep(3)

driver.close()


from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import  BeautifulSoup
from time import sleep
from tqdm import tqdm
from webdriver_manager.chrome import ChromeDriverManager
from Settings import chrome_bin_location
from Settings import webdriver_location
from Settings import url
from Settings import username, password


svc = Service(webdriver_location)
opt = Options()
opt.binary_location = chrome_bin_location

driver = webdriver.Chrome(service=svc, options=opt)
driver.get(url)


def auth_with_login_email(login_email, password):
    driver.find_element(By.CLASS_NAME, 'Button2_view_default').click()
    sleep(3)
    login_input = driver.find_element(By.NAME, 'login')
    login_input.clear()
    login_input.send_keys(login_email)
    sleep(3)
    driver.find_element(By.CLASS_NAME, 'Button2_type_submit').click()
    sleep(3)
    if driver.current_url == 'https://passport.yandex.ru/auth/welcome':
        password_input = driver.find_element(By.NAME, 'passwd')
        password_input.clear()
        password_input.send_keys(password)
        sleep(3)
        submit_buttion = driver.find_element(By.CLASS_NAME, 'Button2_type_submit').click()


    sleep(10)

def auth_with_phone(phone_number):
    pass

add_link = url + r'\add'
sleep(5)
# driver.get(add_link)
if driver.current_url == 'https://passport.yandex.ru/auth/welcome':
    driver.delete_cookie('my_cookie')
    sleep(5)
    driver.get(add_link)


auth_with_login_email(username, password)

driver.close()
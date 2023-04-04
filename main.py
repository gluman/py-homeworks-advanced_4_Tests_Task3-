from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from Settings import chrome_bin_location
from Settings import webdriver_location

url = 'https://www.ya.ru'


options = Options()
options.binary_location = chrome_bin_location
driver = webdriver.Chrome(chrome_options=options, executable_path=webdriver_location)

driver.get(url)
print(driver.title)
driver.close()
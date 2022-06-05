import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='D://DRIVERS//chromedriver.exe')

driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://opensource-demo.orangehrmlive.com/')
print(driver.title)
driver.close()
driver.find_element(By.ID, 'Admin')
# login_form = driver.find_element(By.ID, 'Admin')
driver.find_element(By.ID, 'admin123')
# driver.find_element(By.ID, 'admin123')
driver.find_element(By.ID, 'btnLogin').click()
time.sleep(10)
driver.quit()

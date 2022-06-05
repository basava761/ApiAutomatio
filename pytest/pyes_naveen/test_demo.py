from selenium import webdriver
import pytest

global driver

driver = webdriver.Chrome(executable_path='D://DRIVERS//chromedriver.exe')

@pytest.fixture()
def test_seup():
    driver.get('https://www.rahulshettyacademy.com/#/practice-project')
    driver.implicitly_wait(3)
    driver.maximize_window()
    print(driver.title)
    yield
    driver.close()
    print('test completed')


def test_login(test_seup):
    print('eter username')
    print('prining pssword')





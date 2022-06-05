from selenium import webdriver
from selenium.common import exceptions

session = webdriver.Chrome()
print("Current session is {}".format(session.session_id))
session.quit()

try:
    session.get("https://opensource-demo.orangehrmlive.com/")
except exceptions.InvalidSessionIdException as e:
    print(e.message)
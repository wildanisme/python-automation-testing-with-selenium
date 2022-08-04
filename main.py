from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
from time import sleep

class TestigSauceDemo(unittest.TestCase):

  # Define browser
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
  
  # start of test area

  # the test methode must use (test_) as prefix 
  def test_login_capture(self):
    driver = self.driver
    driver.get('https://www.saucedemo.com/') # url will be tested
    driver.save_screenshot('./images/saucedemo-login.png')
    sleep(5)

  def test_login_failed(self):
    driver = self.driver
    driver.get('https://www.saucedemo.com/') # url will be tested
    driver.find_element("name", "user-name").send_keys("username") # finding element, input tag with name attribute and insert wrong credential
    driver.find_element("name", "password").send_keys("password") # finding element, input tag with name attribute and insert wrong credential
    sleep(5)
    driver.find_element("name", "login-button").click() # click login button
    driver.save_screenshot('./images/saucedemo-failed-login.png')
    print(driver.title)
    sleep(5) # waiting for 5 seconds to browser quit

  def test_login_success(self):
    driver = self.driver
    driver.get('https://www.saucedemo.com/') # url will be tested
    driver.find_element("name", "user-name").send_keys("standard_user") # finding element, input tag with name attribute and insert true credential
    driver.find_element("name", "password").send_keys("secret_sauce") # finding element, input tag with name attribute and insert true credential
    sleep(5)
    driver.find_element("name", "login-button").click() # click login button 
    print(driver.title)
    sleep(5) # waiting for 5 seconds to browser quit

  def test_login_success_dashboard(self):
    driver = self.driver
    driver.get('https://www.saucedemo.com/inventory.html') # url will be tested
    driver.save_screenshot('./images/saucedemo-dashboard.png')
    sleep(5)

  # End of test area
  
  # Close the browser when the command has successfully executed
  def tearDown(self):
    self.driver.close()

if __name__ == '__main__':
  unittest.main()
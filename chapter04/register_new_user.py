import unittest
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Opera(executable_path = '../operadriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()

        # navigate to the application Home page
        driver.get('http://demo-store.seleniumacademy.com')

    def test_register_new_user(self):
        driver = self.driver

        # click on Log In link to open Login page
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[1]').click()
        driver.find_element_by_link_text('Log In').click()

        # get the Create Account Button
        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')

        # check if the Create Account Button is visible
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())

        # click on Create Account Button
        create_account_button.click()

        # check title
        self.assertEquals('Create New Customer Account', driver.title)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)
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
        self.assertEqual('Create New Customer Account', driver.title)

        # get all the fields from Create an Account form
        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button')

        # check maxlength of first name and last name textbox
        self.assertEqual('255', first_name.get_attribute('maxlength'))
        self.assertEqual('255', last_name.get_attribute('maxlength'))

        # check all fields are enabled
        self.assertTrue(first_name.is_enabled()
            and last_name.is_enabled()
            and email_address.is_enabled()
            and news_letter_subscription.is_enabled()
            and password.is_enabled()
            and confirm_password.is_enabled()
            and submit_button.is_enabled())

        # check Sign Up for Newsletter is unchecked
        self.assertFalse(news_letter_subscription.is_selected())

        # fill out all the fields
        first_name.send_keys('Test')
        middle_name.send_keys('Testing')
        last_name.send_keys('User1')
        news_letter_subscription.click()
        email_address.send_keys('test_user2@testmail.com')
        password.send_keys('tester')
        confirm_password.send_keys('tester')
        submit_button.click()

        # check new user is registered
        self.assertEqual('Hello, Test Testing User1!', driver.find_element_by_css_selector('p.hello > strong').text)
        self.assertTrue(driver.find_element_by_css_selector('p.welcome-msg').is_displayed())

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)
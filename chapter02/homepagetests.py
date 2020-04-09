import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Opera session
        cls.driver = webdriver.Opera(executable_path = '../operadriver')
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window

        # navigate to application home page
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_field(self):
        # check search field exists on Home page
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_language_option(self):
        # check language options dropdown on Home page
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))

    def test_shopping_cart_empty_message(self):
        # check content of My Shopping Cart block on Home page
        shopping_cart_icon = self.driver.find_element_by_css_selector('div.header-minicart span.icon')
        shopping_cart_icon.click()

        shopping_cart_status = self.driver.find_element_by_css_selector('p.empty').text
        self.assertEqual('You have no items in your shopping cart.', shopping_cart_status)

        close_button = self.driver.find_element_by_css_selector('div.minicart-wrapper a.close')
        close_button.click()

    @classmethod
    def tearDownClass(cls):
        # close browser window
        cls.driver.close()

    def is_element_present(self, how, what):
        '''
        Utility method to check pressence of an element on page
        :params how: By locator type
        :params what: locator value
        '''
        try: self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True

if __name__ == "__main__":
    unittest.main(verbosity = 2)
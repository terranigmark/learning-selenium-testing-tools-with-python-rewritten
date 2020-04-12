import unittest
from selenium import webdriver

class CompareProducts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Opera(executable_path = '../operadriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')

    def test_compare_products_removal_alert(self):
        # get the search textbox
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        # enter search keyword and submit
        search_field.send_keys('tee')
        search_field.submit()

        # click the Add to compare link
        driver.find_element_by_link_text('Add to Compare').click()

        # click on Remove this item link, this will display
        # an alter to the user
        driver.find_element_by_link_text('Clear All').click()

        # switch to the alert
        alert = driver.switch_to_alert()

        # get the text from alert
        alert_text = alert.text

        # check alert text
        self.assertEqual("Are you sure you would like to remove all products from your comparison?", alert_text)

        # click on Ok button
        alert.accept()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)
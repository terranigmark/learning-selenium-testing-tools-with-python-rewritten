import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CompareProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Opera(executable_path = '../operadriver')
        self.driver.get('http://demo-store.seleniumacademy.com')

    def test_compare_products_removal_alert(self):
        driver = self.driver
        # get search textbox
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        # enter search keyword and submit
        search_field.send_keys('tee')
        search_field.submit()

        # click the Add to compare link
        driver.find_element_by_link_text('Add to Compare').click()

        # wait for Clear All Link to be visible
        clear_all_link = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Clear All')))

        # click on Clear All link,
        # this will display an alert to the user
        clear_all_link.click()

        # wait for the alert to present
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

        # get the text from alert
        alert_text = alert.text

        # check alert text
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)

        # click on Ok button
        alert.accept()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)
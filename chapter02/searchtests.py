import unittest
from selenium import webdriver

class SearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Opera(executable_path = '../operadriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()

        # navigate to the application home page
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_by_category(self):
        driver = self.driver
        # get the search textbox
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        # enter search keeywords and submit
        search_field.send_keys('tee')
        search_field.submit()

        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        print(f'Found {len(products)} products')

        for product in products:
            print(product.text)

        self.assertEqual(5, len(products))

    def test_search_by_name(self):
        driver = self.driver

        # get the search textbox
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        # enter search keyword and submit
        search_field.send_keys('salt shaker')
        search_field.submit()

        # get all the anchor elements which have
        # product names displayed
        # currently on result page using
        # find_elements_by_xpath method
        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2')
        self.assertEqual(1, len(products))

    def tearDown(self):
        # close the browser window
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)
import unittest
from ddt import ddt, data, unpack
from selenium import webdriver

@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Opera(executable_path = '../operadriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()

        # navigate to the application home page
        driver.get('http://demo-store.seleniumacademy.com/')

    # specify test data using @data decorator
    @data(('dress', 6), ('music', 5))
    @unpack

    def test_search(self, search_value, expected_count):
        driver = self.driver
        # get the search textbox
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        # enter search keeywords and submit
        search_field.send_keys(search_value)
        search_field.submit()

        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        print(f'Found {len(products)} products')

        for product in products:
            print(product.text)

        # check count of products shown in results
        self.assertEqual(expected_count, len(products))

    def tearDown(self):
        # close the browser window
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)
import csv, unittest
from ddt import ddt, data, unpack
from selenium import webdriver

def get_data(file_name):
    #create an empty list to store rows
    rows = []
    # open the csv file
    data_file = open(file_name, 'r')
    # create a csv reader from csv file
    reader = csv.reader(data_file)
    # skip the  headers
    next(reader, None)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows

@ddt
class SearchCsvDDT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Opera(executable_path = '../operadriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()

        # navigate to the application home page
        driver.get('http://demo-store.seleniumacademy.com/')

    # get the data from specified csv file
    # calling the get data_function
    @data(*get_data('testdata.csv'))

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

        expected_count = int(expected_count)
        if expected_count > 0:
            #check count of products shown in results
            self.assertEqual(expected_count, len(products))
        else:
            msg = driver.find_element_by_class_name('note-msg')
            self.assertEqual('Your search returns no results.', msg.text)

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
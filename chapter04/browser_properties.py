import unittest
from selenium import webdriver

class BrowserProperties(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Opera(executable_path = '../operadriver')
        driver = cls.driver
        driver.get('https://www.platzi.com')

    def test_browser_properties(self):
        driver = self.driver
        site_url = driver.current_url
        print(site_url)

        window_handle = driver.current_window_handle
        print(window_handle)

        site_name = driver.name
        print(site_name)

        """ site_orientation = driver.orientation
        print(site_orientation) """

        source = driver.page_source
        print(source)

        site_title = driver.title
        print(site_title)

        handles = driver.window_handles
        print(handles)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)
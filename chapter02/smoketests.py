import unittest
from searchtests import SearchTests
from homepagetests import HomePageTest

# get all tests from SearchTests and HomePageTest classes
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suite combining search_tests and home_page_tests
smoke_tests = unittest.TestSuite([home_page_tests, search_tests])

# run test suite
unittest.TextTestRunner(verbosity = 2).run(smoke_tests)
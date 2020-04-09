from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from searchtests import SearchTests
from homepagetests import HomePageTest

# get all tests from SearchTests
search_tests = TestLoader().loadTestsFromTestCase(SearchTests)
home_page_tests = TestLoader().loadTestsFromTestCase(HomePageTest)

# create test suite combining search_test and home_page_test
smoke_tests = TestSuite([home_page_tests, search_tests])

kwargs = {
    "output": 'smoke-reports',
    "report_name": 'smoke-tests-report',
    "failfast": True
}
runner = HTMLTestRunner(**kwargs)
runner.run(smoke_tests)
"""
This script call get_tests with module sequential.
"""
from app.tests.meta_test import BaseTest, get_tests

TESTS = get_tests('selenium_tests')

for test_name in TESTS:
    globals()[test_name] = type(test_name, (BaseTest,), {'test_case': TESTS[test_name]})

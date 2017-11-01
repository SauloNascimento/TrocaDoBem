# -*- coding: utf-8 -*-
"""This script runs the tests using PhantomJS as Driver, and based on
the execution module (Sequential or Parallel), starts a searching the test files."""
import os
import subprocess
from threading import Timer

from django.conf import settings
from django.test import LiveServerTestCase

if os.name == 'nt':
    SELENESE = 'selenese-runner.bat'
else:
    SELENESE = 'selenese-runner'


class BaseTest(LiveServerTestCase):
    """
    Base implementation to Selenium tests.
    """

    def test_execute(self):
        """
        This method superclass run_test.
        """
        try:
            return_code = self._run_test(self.test_case, self.live_server_url)
            tries = 1
            while return_code != 0 and tries < 3:
                tries += 1
                print("Test " + self.test_case + " failed. Executing again (try " + str(tries) + ")")
                return_code = self._run_test(self.test_case, self.live_server_url)
            self.assertEqual(0, return_code, "Test " + self.test_case + " failed.")
        except AttributeError:
            pass

    @classmethod
    def _run_test(cls, test, url):
        proc = subprocess.Popen([SELENESE,
                                 '--driver', 'phantomjs',
                                 '--rollup=%s' % os.path.join(settings.BASE_DIR, 'app', 'tests',
                                                              'selenium_tests',
                                                              'user-extensions.js'),
                                 '--screenshot-on-fail=' + settings.BASE_DIR,
                                 '--baseurl=%s' % url, test])

        data = {'timeout': False}
        timer = Timer(180, kill_proc, [proc, data])
        timer.start()
        proc.communicate()
        timer.cancel()
        return proc.returncode


def get_tests(module):
    """
    Depending on the module, this function search the test files to run.
    :param module: a string (sequential or parallel).
    :return: test files.
    """
    tests = {}
    for root, dirs, files in os.walk(os.path.join(settings.BASE_DIR, 'app', 'tests', module)):
        for file_test in files:
            if file_test.endswith('.html'):
                tests[file_test.replace('.html', '')] = os.path.join(root, file_test)
    return tests


def kill_proc(proc, timeout):
    """
    Kill the process.
    :param proc: Process to be killed.
    :param timeout: timeout.
    :return:
    """
    timeout['timeout'] = True
    proc.kill()

#!/usr/bin/env python
from coverage import coverage
import os
import unittest


class Coverage:

    def __enter__(self):
        self.cov = coverage()
        os.environ['COVERAGE_PROCESS_START'] = '.coveragerc'
        self.cov.start()

    def __exit__(self, type, value, traceback):
        self.cov.stop()
        self.cov.save()
        self.cov.combine()
        print('\nCoverage Report:\n')
        self.cov.report()

        self.cov.html_report()
        print('\nHTML version: htmlcov/index.html')

        self.cov.erase()


if __name__ == '__main__':
    with Coverage():
        from test_cobrand import TestCobrand
        from test_error import TestError
        from test_user import TestUser
        unittest.main(verbosity=2, buffer=True)

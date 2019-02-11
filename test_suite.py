import unittest

import pack1.test_suite


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(pack1.test_suite.suite())
    return test_suite


if __name__ == '__main__':
    mySuit = suite()
    runner = unittest.TextTestRunner()
    runner.run(mySuit)

import unittest

import pack1.test.test_mod1
import pack1.test.test_mod2


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(pack1.test.test_mod1.mod1_test))
    test_suite.addTest(unittest.makeSuite(pack1.test.test_mod2.mod2_test))
    return test_suite


if __name__ == '__main__':
    mySuit = suite()
    runner = unittest.TextTestRunner()
    runner.run(mySuit)

import unittest

import pack1.mod2 as m2

class mod2_test(unittest.TestCase):
    def test(self):
        self.assertEqual('mod2_func', m2.mod2_func())

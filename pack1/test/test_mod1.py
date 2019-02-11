import unittest

import pack1.mod1 as m1

class mod1_test(unittest.TestCase):
    def test(self):
        self.assertEqual('mod1_func', m1.mod1_func())


__author__ = 'hawker'

import unittest
from individual import Individual

class MyTestCase(unittest.TestCase):
    def test_constr(self):
        ind = Individual("10101")
        self.assertEqual(ind.genome, "10101")
        self.assertEqual(ind.fitness, 100000)



if __name__ == '__main__':
    unittest.main()

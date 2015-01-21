__author__ = 'hawker'

import unittest
from individual import Individual

class MyTestCase(unittest.TestCase):
    def test_constr(self):
        ind = Individual("10101")
        self.assertEqual(ind.genome, "10101")
        self.assertEqual(ind.fitness, 100000)

    def test_random(self):
        ind1 = Individual.random_ind()
        ind2 = Individual.random_ind(20)
        self.assertEqual(len(ind1.genome), 10)
        self.assertEqual(len(ind2.genome), 20)
        self.assertEqual(ind1.fitness, 100000)

    def test_class(self):
        self.assertEqual(Individual.mutation_factor, 5)

    def test_mutation_decision(self):
        self.assertIn(Individual.decide_if_mutate(), [True, False])

    def test_breeding(self):
        ind1 = Individual("111")
        ind2 = Individual("111")
        child1, child2 = ind1.breed_with(ind2)
        self.assertEqual(len(child1.genome), len(child2.genome))
        self.assertEqual(len(child1.genome), 3)

    def test_fight(self):
        ind1 = Individual("111")
        ind2 = Individual("1000")
        f1 = ind1.count_fitness()
        f2 = ind2.count_fitness()
        self.assertEqual(f1, 2*(7-567)**2)
        self.assertEqual(f2, 2*(8-567)**2)
        self.assertEqual(ind1.fitness, 2*(7-567)**2)
        self.assertEqual(ind2.fitness, 2*(8-567)**2)


if __name__ == '__main__':
    unittest.main()

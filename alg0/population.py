__author__ = 'hawker'

from individual import Individual


class Population:
    def __init__(self, size):
        self.size = size
        self.pop = []
        self.selected = []
        self.fitness_table = []
        Individual.mutation_factor = 5
        for i in xrange(size):
            self.pop.append(Individual.random_ind())

    def __repr__(self):
        return self.__str__()
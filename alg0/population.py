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

    def evaluate(self):
        self.fitness_table = []
        for i in xrange(0, self.size):
            self.fitness_table.append(self.pop[i].count_fitness())
        return self.fitness_table

    def __str__(self):
        result = ""
        for i, ind in enumerate(self.pop):
            result += str(i)+";"+str(ind)
        return result

    def __repr__(self):
        return self.__str__()
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

    def selection(self):
        newlist = sorted(self.pop, key=lambda x: x.fitness, reverse=True)
        self.selected = newlist[(len(self.pop)/2):]
        return self.selected

    def breed(self):
        new_population = []
        for i in xrange(0, len(self.selected), 2):
            child1, child2 = self.selected[i].breed_with(self.selected[i+1])
            child3, child4 = self.selected[i].breed_with(self.selected[i+1])
            new_population.append(child1)
            new_population.append(child2)
            new_population.append(child3)
            new_population.append(child4)
        self.pop = new_population
        self.selected = []
        self.fitness_table = []
        return new_population

    def evolve(self):
        self.evaluate()
        self.selection()
        self.breed()

    def __str__(self):
        result = ""
        for i, ind in enumerate(self.pop):
            result += str(i)+";"+str(ind)
        return result

    def __repr__(self):
        return self.__str__()
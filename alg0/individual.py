__author__ = 'hawker'
import random
import tools

class Individual(object):
    mutation_factor = 5

    def __init__(self, genome):
        self.genome = genome
        self.fitness = 100000

    @staticmethod
    def random_ind(genome_length = 10):
        genome = ''.join([random.choice("01") for _ in xrange(genome_length)])
        return Individual(genome)

    def __str__(self):
        return "genome:"+self.genome+";fitness:"+str(self.fitness)+"\n"

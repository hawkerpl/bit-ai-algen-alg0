__author__ = 'hawker'
import random
import tools

class Individual(object):
    mutation_factor = 5

    def __init__(self, genome):
        self.genome = genome
        self.fitness = 100000


    def __str__(self):
        return "genome:"+self.genome+";fitness:"+str(self.fitness)+"\n"

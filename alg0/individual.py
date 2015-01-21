__author__ = 'hawker'
import random
import tools

class Individual(object):
    mutation_factor = 5

    def __init__(self, genome):
        self.genome = genome
        self.fitness = 100000

    def count_fitness(self):
        x = int(self.genome, 2)
        self.fitness = 2*(x-567)**2
        return self.fitness

    @staticmethod
    def random_ind(genome_length = 10):
        genome = ''.join([random.choice("01") for _ in xrange(genome_length)])
        return Individual(genome)


    def mutate_random_gene(self):
        which_one = random.randint(0, len(self.genome)-1)
        gene_list = list(self.genome)
        #print self.genome
        #print gene_list, which_one
        gene_list[which_one] = random.choice("01")
        self.genome = "".join(gene_list)
        return which_one

    @staticmethod
    def decide_if_mutate():
        return Individual.mutation_factor <= random.randint(0, 100)

    def breed_with(self, another_ind):
        child1_genome, child2_genome = tools.binary_crossover_from_string(self.genome, another_ind.genome)
        child1 = Individual(child1_genome)
        child2 = Individual(child2_genome)
        child1.mutate_random_gene()
        child2.mutate_random_gene()
        return child1, child2



    def __str__(self):
        return "genome:"+self.genome+";fitness:"+str(self.fitness)+"\n"

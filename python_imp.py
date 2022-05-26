from cv2 import split
import pygad
import numpy
import random
from torch import randint
import time
NQUEENS=8
desired_collisions = 0
total_sols = []
def fitness_func(genome,genome_id):
    col= 100
    for x in range(0,len(genome)):
        for y in range(x+1,len(genome)):
            if y-x == abs(genome[x] - genome[y]):
                col -=1
                break
    if col == 100:
        if (genome.tolist() in total_sols) == False:
            total_sols.append(genome.tolist())
            print("Total unique solutions found: " + str(len(total_sols)))
    return col
def mutation_func(genome, ga_inst):
    choices = [0,1,2,3,4,5,6,7]
    index1,index2 = random.sample(choices,2)
    genome[index1], genome[index2] = genome[index2], genome[index1]
    return genome

# def crossover_func(parents,offsprings,ga_instance):


def populationMaker():
    population_size = 500
    population = []
    for pop in range(0,population_size):
        genome = numpy.random.choice(numpy.arange(0,8),replace=False,size=8)
        population.append(genome)
    return population

def check_fitness(ga_inst):
    solution, solution_fitness, solution_idx = ga_inst.best_solution()
    # print(solution)
    # print(solution_fitness)
    if solution_fitness == 100:
        if (solution.tolist() in total_sols) == False:
            total_sols.append(solution.tolist())
            print("Total unique solutions found: " + str(len(total_sols)))

def crossover_func(parents, offspring_size, ga_instance):
    offspring = []
    idx = 0
    while len(offspring) != offspring_size[0]:
        parent1 = parents[idx % parents.shape[0], :].copy()
        parent2 = parents[(idx + 1) % parents.shape[0], :].copy()
        parent3 = [-1,-1,-1,-1,-1,-1,-1,-1]
        splitpoints = numpy.random.choice(numpy.arange(0,8),replace=False,size=2)
        for x in range(min(splitpoints),max(splitpoints)+1):
            parent3[x] = parent1[x]
        for y in range(0,8):
            if parent2[y] not in parent3:
                parent3[parent3.index(-1)] = parent2[y]
        offspring.append(parent3)

        idx += 1

    return numpy.array(offspring)


def main():

    runcount=0
    start = time.time()
    while len(total_sols) != 92:
        genome = populationMaker()
        ga_obj = pygad.GA(num_generations=50,
                num_parents_mating=50, 
                fitness_func=fitness_func, 
                initial_population=genome,
                crossover_type=crossover_func,
                mutation_type=mutation_func,
                parent_selection_type="rank",
                stop_criteria=["saturate_5"],
                gene_type=int,
                mutation_percent_genes=0.05)
        ga_obj.run()
        solution, solution_fitness, solution_idx = ga_obj.best_solution()
        ga_obj.best_solutions
        runcount+=1
        print("Run count: " + str(runcount))
        if solution_fitness == 100:
            if (solution.tolist() in total_sols) == False:
                total_sols.append(solution.tolist())
                print("Total unique solutions found: " + str(len(total_sols)))
    for x in total_sols:
        print(x)
    end = time.time()
    print(end-start)

main()

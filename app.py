from cv2 import split
import pygad
import numpy
import random
from torch import randint
NQUEENS=8
desired_collisions = 0
total_sols = []
def fitness_func(genome,genome_id):
    col= 100
    for x in range(0,len(genome)):
        for y in range(x+1,len(genome)):
            if (y-x == abs(genome[x] - genome[y]) or genome[y] == genome[x]):
                col -=1
    if col == 100:
        col = 1000000000
    return col
def mutation_func(genome, ga_inst):
    choices = [0,1,2,3,4,5,6,7]
    index1,index2 = random.sample(choices,2)
    genome[index1], genome[index2] = genome[index2], genome[index1]
    return genome

# def crossover_func(parents,offsprings,ga_instance):


def populationMaker():
    population_size = 92
    population = []
    for pop in range(0,population_size):
        genome = numpy.random.choice(numpy.arange(0,8),replace=False,size=8)
        population.append(genome)
    return population

def check_fitness(ga_inst):
    solution, solution_fitness, solution_idx = ga_inst.best_solution()
    # print(solution)
    # print(solution_fitness)
    if solution_fitness == 1000000000:
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
        # print("Parent 1st: " + str(parent1))
        # print("Parent 2st: " + str(parent2))
        splitpoints = numpy.random.choice(numpy.arange(0,8),replace=False,size=2)

        for x in range(min(splitpoints),max(splitpoints)+1):
            parent3[x] = parent1[x]
        # print("Min: " + str(min(splitpoints)) + " , Max: " + str(max(splitpoints)))
        # print("Parent 1: " + str(parent1))
        # print("Parent 2: " + str(parent2))
        # print("Parent 3 first: " + str(parent3))
        for y in range(0,8):
            if parent2[y] not in parent3:
                parent3[parent3.index(-1)] = parent2[y]
        # print("Parent 3 second: " + str(parent3))
        offspring.append(parent3)

        idx += 1

    return numpy.array(offspring)


def main():

    runcount=0
    while len(total_sols) != 92:
        genome = populationMaker()
        ga_obj = pygad.GA(num_generations=50000,
                num_parents_mating=50, 
                fitness_func=fitness_func, 
                initial_population=genome,
                crossover_type=crossover_func,
                mutation_type=mutation_func,
                parent_selection_type="rank",
                stop_criteria=["saturate_15"],
                on_generation=check_fitness,
                mutation_num_genes=2,
                allow_duplicate_genes=False,
                gene_type=int,
                mutation_percent_genes=0.04)
        ga_obj.run()
        solution, solution_fitness, solution_idx = ga_obj.best_solution()
        ga_obj.best_solutions
        runcount+=1
        print("Run count: " + str(runcount))
        if solution_fitness == 1000000000:
            # print("Here")
            # print(solution)
            # print(total_sols)
            # print(solution in total_sols)
            if (solution.tolist() in total_sols) == False:
                total_sols.append(solution.tolist())
                # print("Parameters of the best solution : {solution}".format(solution=solution))
                # print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
                print("Total unique solutions found: " + str(len(total_sols)))
    for x in total_sols:
        print(x)

main()
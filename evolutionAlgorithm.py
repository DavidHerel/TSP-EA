import random
from tspUtils import *
from localSearches import *


def ea_run(pop_size, mutation_rate, starting_node, problem, edges, optimal_solution, max_gen):
    #create population of pop size
    population = []
    fitness_score = []
    generations = 0;
    best_fitness_global = 0

    print("Generating " + str(pop_size) + " random solutions: ")
    for i in range(pop_size):
        population.append(createRandomValidSolution(starting_node, problem))
        fitness_score.append(countFitness(population[i], problem, optimal_solution))

    best_fitness_global = print_stats(population, generations, fitness_score, best_fitness_global)

    #keep iterating till we get solution
    while (any(fitness_score) >= 1):
        #break loop
        if (generations >= max_gen):
            break
        population, fitness_score = generate_new_population(population, problem, optimal_solution, edges, mutation_rate, fitness_score)
        generations+=1
        #printing and saving best solution
        best_fitness_global = print_stats(population, generations, fitness_score, best_fitness_global)


def natural_selection(population, problem, optimal_solution, fitness_score):
    matingPool = []

    for i in range(len(population)):
        fitness = fitness_score[i]

        #add them to mating pool depending on how big fitness they have
        for j in range(int(fitness*100)*int(fitness*100)):
            matingPool.append(population[i])

    return matingPool

def generate_new_population(population, problem, optimal_solution, edges, mutation_rate, fitness_score):
    matingPool = natural_selection(population, problem, optimal_solution, fitness_score)
    new_population = []
    new_fitness_score = []
    #create new population
    for i in range(len(population)):
        #choose two parents
        parentA = random.choice(matingPool)
        parentB = random.choice(matingPool)

        #crossover
        baby = order_crossover(parentA, parentB)

        #mutate
        baby = mutate(mutation_rate, edges, baby)

        #count fitness
        new_fitness_score.append(countFitness(baby, problem, optimal_solution))
        #replace it
        new_population.append(baby)

    return new_population, new_fitness_score

def mutate(mutation_rate, edges, baby):
    for i in range(len(baby)):
        if (random.uniform(0,1) < mutation_rate):
            baby, swapped = mutationTwoPlaces(baby, edges, i, random.randint(0, len(baby)-1))
    return baby

def order_crossover(parentA, parentB):
    #choose points to slice
    start = random.randint(0, len(parentA)-2)
    end = random.randint(start+1, len(parentA)-1)
    baby = parentA[start:end]

    for i in range(len(parentB)):
        city = parentB[i]
        if not(city in baby):
            baby.append(city)

    #baby = parentA;
    return baby

def print_stats(population, generations, fitness_score, best_fitness_global):
    print("Generation: " + str(generations))
    print("Best fitness: " + str(max(fitness_score)))
    print("Average fitness: " + str(sum(fitness_score)/len(fitness_score)))
    if(best_fitness_global < max(fitness_score)):
        best_fitness_global = max(fitness_score)
    print("Best fitness globally: " + str(best_fitness_global))
    """
    print("---Population---")
    for i in range(len(population)):
        print("Solution " + str(i))
        print("Path: " + str(population[i]))
        print("Fitness: " + str(fitness_score[i]) + "\n")
    """
    print("----------")
    return best_fitness_global
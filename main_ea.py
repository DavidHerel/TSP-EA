from evolutionAlgorithm import *
from localSearches import *

#Loading 3 TSP instances
problem_a280 = tsplib95.load('a280.tsp')
problem_bayg29 = tsplib95.load('bayg29.tsp')
problem_bays29 = tsplib95.load('bays29.tsp')

#setting one as active
problem = problem_bayg29

#loading solutions to 3 instances
optimalSolution_a280 = 2579
optimalSolution_bayg29 = 1610
optimalSolution_bays29 = 2020

#chosing one as active
optimalSolution = optimalSolution_bayg29

print("Evolution algorithm experiments: \n")
#get edges
edges = list(problem.get_edges())

#Hyper parameteres
#starting node
startingNode = 1;
#max generations
max_gens = 1000
#mutation rate
mutationRate = 0.1
#popsize
population_size = 5000

#run ea algorithm
ea_run(population_size, mutationRate, startingNode, problem, edges, optimalSolution, max_gens)
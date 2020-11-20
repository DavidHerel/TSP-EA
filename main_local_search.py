from localSearches import *

#Loading 3 TSP instances
problem_a280 = tsplib95.load('a280.tsp')
problem_bayg29 = tsplib95.load('bayg29.tsp')
problem_bays29 = tsplib95.load('bays29.tsp')

#setting one as active
problem = problem_bays29

#loading solutions to 3 instances
optimalSolution_a280 = 2579
optimalSolution_bayg29 = 1610
optimalSolution_bays29 = 2020

#chosing one as active
optimalSolution = optimalSolution_bays29

print("Local search experiments: \n")
#get edges
edges = list(problem.get_edges())
startingNode = 1;

#create random valid solution
nodes = createRandomValidSolution(startingNode, problem)

print("Random naive solution: ")
print("TSP length: " + str(countSum(nodes,problem)))
print("Fitness: " + str(countFitness(nodes, problem, optimalSolution)))
print("")

#optimize it through local search
print("Optimized solution: ")
nodes,sum = localSearchSwap2Places(nodes, problem, edges)
print("TSP length: " + str(countSum(nodes,problem)))
print("Fitness: " + str(countFitness(nodes, problem, optimalSolution)))

#try to start from multiple positions
print("")
print("Starting from multiple random solutions and optimize each of those and choose the best:")
best = 0
multiple_solutions = 100
print("Number of multiple starts is: " + str(multiple_solutions))
for i in range(multiple_solutions):
    #create random valid solution
    nodes = createRandomValidSolution(startingNode, problem)

    nodes,sum = localSearchSwap2Places(nodes, problem, edges)
    if (best < countFitness(nodes, problem, optimalSolution)):
        best = countFitness(nodes, problem, optimalSolution)
print("Best solution: " + str(best))



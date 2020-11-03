import tsplib95
import random
from tspUtils import *

#zkusime prohodit vsechny 2 uzly (prohodime jen pokud budou lepsi nez predesle reseni)
def localSearchSwap2PlacesUtils(nodes, problem, edges):
    #no swap possible
    if (len(nodes) <= 2):
        return nodes
    sum = countSum(nodes, problem)
    #lets keep improving
    improved = True

    while improved:
        improved = False

        for i in range(len(nodes)):
            for j in range(i+2, len(nodes)-1):

                delta = checkWorthSwap(nodes, problem, i, j)

                #if delta is negative
                if delta < 0:
                    #print(delta)
                    #nodes[i], nodes[j] = nodes[j], nodes[i]
                    nodes, swapped = mutationTwoPlaces(nodes, edges, i, j)
                    if (swapped):
                        sum += delta
                        improved = True
        return nodes, sum

#Jedeme az do lokalniho minima - tedy dokud nebudou uz lepsi reseni
def localSearchSwap2Places(nodes, problem, edges):
    nodes, sum = localSearchSwap2PlacesUtils(nodes, problem, edges)
    improved = True
    while improved:
        improved = False
        #print(list(problem.get_nodes()))

        newNodes, newSum = localSearchSwap2PlacesUtils(nodes, problem, edges)
        if (newSum < sum):
            improved = True
            sum = newSum
            nodes = newNodes
            #print("Sum:" + str(sum))

    return nodes, sum


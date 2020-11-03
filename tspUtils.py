import random

def createRandomValidSolution(startingNode, problem):
    nodes = []
    while len(nodes) != len(list(problem.get_nodes()))+1:
        # sled uzlu
        nodes = []
        # rest nodes which we can randomly choose from
        restNodes = list(problem.get_nodes())
        # put there startingNode
        nodes.append(startingNode)
        # remove starting node
        restNodes.remove(startingNode)
        i = 0
        # sum
        sum = 0
        # loop till we have all nodes
        while i < len(list(problem.get_nodes())) - 1:
            # take random node
            randomNode = random.choice(restNodes)

            # if randomNode is not in nodes
            if (not (randomNode in nodes)):

                # check if there  is valid path from previous to this
                edge = (nodes[i], randomNode)
                if edge in list(problem.get_edges()):
                    # append and remove
                    nodes.append(randomNode)
                    restNodes.remove(randomNode)
                    # increase i
                    i += 1
        edge = (nodes[i], startingNode)
        #there is connection between last to first
        if (edge in problem.get_edges()):
            nodes.append(startingNode)
            break
    return nodes

def countFitness(nodes, problem, optimal):
    sum = 0
    i = 0
    for i in range(len(nodes)):
        if (i > 0):
            edge = (nodes[i-1], nodes[i])
            sum += problem.get_weight(*edge)
    return optimal/sum

def countSum(nodes, problem):
    sum = 0
    i = 0
    for i in range(len(nodes)):
        if (i > 0):
            edge = (nodes[i-1], nodes[i])
            sum += problem.get_weight(*edge)
    return sum

def mutationTwoPlaces(nodes, edges, i, j):
    num1 = i
    num2 = j
    swapped = False
    #if there exists edge between these twos
    if (num1-1 < 0):
        edge1 = (nodes[len(nodes)-1], nodes[num2])
    else:
        edge1 = (nodes[num1-1], nodes[num2])
    if (num1+1 > len(nodes)-1):
        edge2 = (nodes[num2], nodes[0])
    else:
        edge2 = (nodes[num2], nodes[num1+1])
    #check if we can swap first node
    if(edge1 in edges and edge2 in edges):
        if (num2 - 1 < 0):
            edge3 = (nodes[len(nodes)-1], nodes[num1])
        else:
            edge3 = (nodes[num2-1], nodes[num1])
        if (num2+1 > len(nodes) - 1):
            edge4 = (nodes[num1], nodes[0])
        else:
            edge4 = (nodes[num1], nodes[num2+1])
        #check if we can swap the second node
        if (edge3 in edges and edge4 in edges):
            #swap them
            nodes[num1], nodes[num2] = nodes[num2], nodes[num1]
            swapped = True
    return nodes, swapped

def checkWorthSwap(nodes, problem, i, j):
    #puvodni
    a_edge = (nodes[i-1], nodes[i])
    b_edge = (nodes[i], nodes[i+1])
    c_edge = (nodes[j-1], nodes[j])
    d_edge = (nodes[j], nodes[j+1])
    a = problem.get_weight(*a_edge)
    b = problem.get_weight(*b_edge)
    c = problem.get_weight(*c_edge)
    d = problem.get_weight(*d_edge)
    sum = a+b+c+d

    #nove
    a_edge = (nodes[i - 1], nodes[j])
    b_edge = (nodes[j], nodes[i + 1])
    c_edge = (nodes[j - 1], nodes[i])
    d_edge = (nodes[i], nodes[j + 1])
    a = problem.get_weight(*a_edge)
    b = problem.get_weight(*b_edge)
    c = problem.get_weight(*c_edge)
    d = problem.get_weight(*d_edge)

    worth = -sum +a +b +c +d

    return worth
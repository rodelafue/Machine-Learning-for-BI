#%% [markdown]
# # Knapsack and Graph Optimization Problems
# 
# Whenever you set about solving a problem that involves finding the biggest, the smallest, the most, the fewest, the fastest, the least expensive, etc., there is a good chance that you can map the problem onto a classic optimization problem.
# 
# In general an optimization problem has two parts:
# 
# * An **objective function** that is to be maximized or minimized. For example, the airfare between Boston and Istambul
# * A **set of constraints** (possibly empty) that must be honored. For example, and upper bound an a travel time.
#%% [markdown]
# ## Knapsack Problems
# 
# What's a poor bulgar do? He/She needs to find the set of things that provides the most value without exceeding his carrying capacity
# 
# ### Greedy Algorithms
# 
# The simplest way to find a solution to the poor bulgar's problem is to use a **greedy algorithm**. The thief would choose the best item first, then the next best, and continue until he reached his limit.

#%%
class Item(object):
    def __init__(self, n, v, w):
        '''
        n is the name and must be an string
        v represents the value an can be either an int or float
        w is the weight an must be a float
        '''
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '< '+self.name+', '+str(self.value)                + ', '+str(self.weight) + ' >'
        return result

def value(item):
    '''
    hgjjkjhkjhk
    '''
    return item.getValue()

def weightInverse(item):
    return 1.0/item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()

def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    vals = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    return Items


#%%
def greedy(Items, maxWeight, keyFcn):
    assert type(Items) == list and maxWeight >= 0
    ItemsCopy = sorted(Items, key=keyFcn, reverse=True)
    result = []
    totalVal = 0.0
    totalWeight = 0.0
    i = 0
    while totalWeight < maxWeight and i < len(Items):
        if (totalWeight + ItemsCopy[i].getWeight()) <= maxWeight:
            result.append(ItemsCopy[i])
            totalWeight += ItemsCopy[i].getWeight()
            totalVal += ItemsCopy[i].getValue()
        i += 1
    return (result, totalVal)

def testGreedy(Items, constraint, getKey):
    taken, val = greedy(Items, constraint, getKey)
    print('Total value of item taken = '+ str(val))
    for item in taken:
        print(' ', item)
        
def testGreedys(maxWeight= 25):
    Items = buildItems()
    print('Use greedy by value for knapsack of size max Weight')
    testGreedy(Items, maxWeight, value)
    print('\nUse greedy by weight to fill knapsack of size max Weight')
    testGreedy(Items, maxWeight, weightInverse)
    print('\nUse greedy by density for knapsack of size max Weight')
    testGreedy(Items, maxWeight, density)
    
testGreedys()

#%% [markdown]
# ### Exponential Solution to the 0/1 Knapsack Problem
# 
# Suppose we decide that an approximation is not good enough and we want the best possible solution to this problem. This is an instance of a classic optimization problem, called **0/1 Knapsack problem**

#%%
def getBinaryRep(n, numDigits):
    '''
    Assumes n and numDigits are non-negative ints
    returns a numDigits str that is a binary representation of n
    '''
    result = ''
    print('n =', n)
    while n > 0:
        result = str(n%2) + result
        print('result =', result)
        n = n//2
    if len(result) > numDigits:
        raise ValueError('not enough digits')
    for i in range(numDigits - len(result)):
        result = '0'+ result
        print('result2 =', result)
    return result
        
def genPowerSet(L):
    '''
    Assumes L is a list
    Returns a list of lists that contains all possible combinations
    of the elements of L. e.g, if L = [1,2] it will return a list
    with elements [1], [2], [1,2]
    '''
    powerSet = []
    for i in range(0, 2**len(L)):
        binStr = getBinaryRep(i, len(L))
        subset = []
        for j in range(len(binStr)):
            if binStr[j] == '1':
                subset.append(L[j])
        powerSet.append(subset)
    return powerSet
    
def chooseBest(pset, constraint, getVal, getWeight):
    bestVal = 0.0
    bestSet = None
    for Items in pset:
        ItemsVal = 0.0
        ItemsWeight = 0.0
        for item in Items:
            ItemsVal += getVal(item)
            ItemsWeight += getWeight(item)
        if ItemsWeight <= constraint and ItemsVal > bestVal:
            bestVal = ItemsVal
            bestSet = Items
    return (bestSet, bestVal)

def testBest(maxWeight = 20):
    Items = buildItems()
    pset = genPowerSet(Items)
    taken, val = chooseBest(pset, maxWeight, Item.getValue, Item.getWeight)
    print("Total value of items taken = " + str(val))
    for item in taken:
        print(item)
        
testBest()

#%% [markdown]
# ## Graph Optimization Problems
# 
# Suppose you had a list of the pieces of all of the airline flights between each pair of cities in the United States. Suppose also that for all cities, A, B, and C, the cost of flying from A to C by the way of B was the cost of flying from A to B plus the cost of flying from B to C. A few questions you might like to ask are:
# 
# * What is the fewest number of stops between two pair of cities?
# * What is the least expensive airfare between some pair of cities?
# * What is the least expensive airfare between some pair of cities involving no more than two stops?
# * What is the least expensive way to visit some collection of cities?
# 
# All these problems (and many others can be formalized as graph problems
# 
# A **graph** is a set of objects called **nodes** connected by a set of **edges**. If the edges are uniderectioanl the graph is called **directed**
# 
# The first documentation of a graph in mathematics was given by the Swiss mathematician Leonhard Euler who used what has come to be known as **graph theory** to formulate and solve the **[Konigsberg bridges problem](https://en.wikipedia.org/wiki/Seven_Bridges_of_K%C3%B6nigsberg)**

#%%
class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)
    
class WeightedEdge(Edge):
    def __init__(self, src, dest, weight = 1.0):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return str(self.src) + '->(' + str(self.weight) + ')' + str(self.dest)

#%% [markdown]
# An important  design decision is the choice of data structure used to represent a Digraph. One common representation is an n x n **[adjacency matrix](https://en.wikipedia.org/wiki/Adjacency_matrix)**, where n is the number of nodes in the graph. Another common representation is an **[adjancecy list](https://en.wikipedia.org/wiki/Adjacency_list)** which will be used here

#%%
class Digraph(object):
    def __init__(self):
        self.nodes = []
        self.edges = {}
        
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError("Duplicate node")
        else:
            self.nodes.append(node)
            self.edges[node] = []
    
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
        
    def childrenOf(self, node):
        return self.edges[node]
    
    def hasNode(self, node):
        return node in self.nodes
    
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res+str(k)+'->'+str(d)+'\n'
        return res[:-1]

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

#%% [markdown]
# ### Shortest Path, Depth-first search, and Breadth-first search

#%%
def printPath(path):
    # a path is a list of nodes
    result = ''
    for i in range(len(path)):
        if i == len(path)-1:
            result = result + str(path[i])
        else:
            result = result + str(path[i])+'->'
    return result

def DFS(graph, start, end, path =[], shortest = None):
    print('start :', start, 'end :', end)
    # Assumes graph is a Digraph
    # Assumes start and end are nodes in the graph
    path = path + [start]
    #print('path', path)
    print('Current dfs path: ', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest)
                #print('this is new path =', newPath)
                if newPath != None:
                    #print('hi')
                    shortest = newPath
    #print('End')
    return shortest

def testSP():
    nodes = []
    for name in range(10):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))### Error I had 4
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[3],nodes[1]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    sp = DFS(g,nodes[0], nodes[5])
    print(sp)
    print('Shortest path found by DFS: ', printPath(sp))
    
testSP()


#%%


#%% [markdown]
# Take aways:
# 
# * Many problems of real importance can be simply formulated in a way that leads naturally to a computational solution.
# * Reducing a seemingly new problem to an instance of a well-known problem allows one to use pre-existing solutions.
# * Exhaustive enumeration algorithms provide a simple, but often computationally intractable, way to search for optimal solutions.
# * A greedy algorithm is often a practical approach to finding a prety good, but not always optimal, solution to an optimization problem.
# * Knapsack problem and graph problems are classes of problems to which other problems can be reduced


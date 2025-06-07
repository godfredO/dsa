"""  The first step in the solution is to turn the 2d- matrix into a graph that has the negative logarithm of the edge weights. 
This way detecting an arbitrage gets turned into detecting a negative weight cycle of a connected graph and we can use the 
Bellman-Ford algorithm to find the shortest path from a chosen source node to all other node in n-1 iterations. If the connected 
graph doesnt contain negative weight cycles, the shortest distance from source will be found for all nodes in at most n-1 iterations. 
This is because in the limiting case where a graph is a linked list, each node is at most n-1 edges from the head node where n-1 
represents the total edges in a linked list with n nodes.Thus what we need to do is run the Bellman Ford algorithm after taking the
negative logarithm of all exchange rates which will become the edge weights in the graph. We run through the steps of relaxing all of 
these edges, n - 1one times, the reason being that there should only be at most n minus one edges in the shortest path from one node 
to any other node. And then after we've done that, we have this array of distances telling us potentially the shortest distance to any 
of the nodes. Now we go through this one more time, and if we update any of these distances that tells us we have any negative 
weight cycle.  """
import math
#O(n^3) time | O(n^2) space - where n = the number of currencies, n^2 is the size of the matrix, we go through matrix n-1 times
def detectArbitrage(exchangeRates):
    logExchangeRates = convertToLogMatrix(exchangeRates) #convert edge  weights (exchanges) to -log(edge weight)
    return foundNegativeWeightCycle(logExchangeRates,0)  #converted matrix,starting node or row position

def convertToLogMatrix(matrix):
    newMatrix = []
    for row, rates in enumerate(matrix): #rowIdx,row
        newMatrix.append([]) #initialize empty array for each row
        for rate in rates: #loop through each row
            newMatrix[row].append(-math.log10(rate)) #convert to -log(e) and append to output
    return newMatrix #output of -log(edges) 2-d matrix

def foundNegativeWeightCycle(graph,start):
    distancesFromStart = [float("inf") for _ in range(len(graph))] #shortest distances to node at index from start node
    distancesFromStart[start] = 0  #initialize distance from start node to start node

    for _ in range(len(graph) -1) : #need to relax each edge n-1 times
        if not relaxEdgesAndUpdateDistances(graph,distancesFromStart): #True if made update, False if no updates made
            return False #if relaxEdgesAndUpdateDistances = False, then no arbitrage, so return False immediately
    return relaxEdgesAndUpdateDistances(graph,distancesFromStart) #True if arbitrage, False if no arbitrage

def relaxEdgesAndUpdateDistances(graph,distances): #Bellman-Ford algorithm for shortest path from source node 
    updated = False
    for sourceIdx,edges in enumerate(graph): #loop through the row , rowIdx is the sourceNodeIdx
        for destinationIdx, edgeWeight in enumerate(edges): # loop through the columns of current row, colIdx is destinationIdx
            newDistanceToDestination = distances[sourceIdx] + edgeWeight #distances[startNode] = 0 so its edges will be updated
            if newDistanceToDestination < distances[destinationIdx]: #make update with newDistance is less than stored distance
                updated = True #this is used to determine if an update is made or not
                distances[destinationIdx] = newDistanceToDestination
    return updated  #return updated boolean variable

exchangeRates = [
    [1, 0.8631, 0.5903],
    [1.1586, 1, 0.6849],
    [1.6939, 1.46, 1]
  ]
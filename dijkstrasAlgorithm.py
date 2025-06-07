"""You're given an integer start and a list edges of pairs of integers ie an adjacency list and a startNode. The adjacency list represents
a graph and the number of vertices in the graph is equal to the length of edges, where each index i in edges contains vertex i's outbound
(directed) edges in no particular order. Each edge is represented as [destination, distance] ie a destination denotes the destination 
vertex and distance is a positive integer representing the length of the edge from vertex i to vertex destination. That is the edges
are weighted and directed from vertex i to vertex destination. The question is to write a function that computes the lengths of the 
shortest paths between startNode and all the other vertices in the graph using Dijkstra's algorithm. If no path is found from startNode
to vertex i, then output[i] should be -1. We are also assured that the graph represented by this adjacency list won't contain any self-
loops and will only have positively weighted edges ie no negative distances.

Dijkstra's algorithm is pretty straightforward and depends on a few observations. One, we know that the startNode is a distance of 0
from itself. Second thing is that to get from the startNode to any particular node we will have to travel down an edge either directly
from the startNode it it has an edge to the vertes of interest or from the startNode to another node that has an edge to the vertex of
interest. And since the distances are weighted, the edges wont be the same distance and even it is possible for a path consisting of the
sum of edges to be shorter than one really long edge distance. The final observation is that the distance from the startNode to a vertex
of interest can be summed up in two parts, the distance to the vertex of interest from some node that has an edge to it, and the distance
from the startNode to this middle node. So if we minimize the distance from the distance from the startNode to this middle node and then
minimize the distance from a middle node to the vertex of interest, we will have minimized the distance from the startNode to the vertex
of interest.

So that is what Dijkstra's algorithm does. It initializes an output of +inf distance (for easy minimum comparisons) in the output array 
for every vertex index in the adjacency list, then updates the distance at the startNode index to 0. We also initialize a visited set for 
constant time access. Then at each stage in Dijkstra's Algorithm, we select the unvisited node with the minimum output distance as the
'middle node', go through its edges and for each destination, we calculate the distance from the startNode by adding the edge distance
from the 'middle node' to the destination plus the distance from the startNode to the 'middle node' ie the middle node's distance in
the output, making sure to add this 'middle node' to the visited set so we don't consider its edges again. When we calculate each 
distance, we update the output[destination] by first comparing if the distance from startNode>middleNode>destination is lower than the
current destination distance in the output. When we start the algorithm, the 'middle node' will be the startNode since it has an output
distance of 0 and every other node starts off at +inf. We go through its edges, update each destination vertex's output distance as
output[destination] = 0 + edge weight, after of course comparing with the current output distance which will be +inf. After updating 
the output distance for all of the startNode's edges, we are done with the startNode and never go through its edges again, because
we added it to the visited set before going through its edges. Then we go through the output for the unvisited node with the minimum
output distance as our new middle node and go through its edges, calculate their output distance with that middle node and update the
output distance if it is lower than the current output distance. Thus by always choosing the unvisited node with the minimum distance,
we minimize the distance the distance between the startNode and a middle node and because we also do a minimum comparison with the 
current output distance before updating it, we mimimize the distance between the middle node and any vertex i to ensure that we always
end up with the mimimum possible distance from startNode to vertex i. We keep going as long as we haven't every node ie as long as the
size of the visited set is not equal to the number of vertices in the adjacency list, which is the while loop condition. Also, in the
case of a disconnected graph, there will come a point where the minimum distance remaining for the unvisited nodes is still +inf, 
and when this happens we break out of the while loop because we are finished with it. So we keep running the loop as long as we havent
chosen every node as the  'middle node' to consider its edges or as long as the minimum output distance for unvisited nodes isnt +inf.
At the end of the loop, we go through the output array and replace any +inf with -1 like the question asks, here done with a map()
and custom lambda function. The function for getting the unvisited node with the minimum output distance takes the visited set and
ouptut as inputs, initializes a vertex and minDistance variables as None and +inf respectively, then in a for loop enumerates over the
output distance. Enumeration provides the vertex index. The first check is that if the vertex index is in the visited set, we continue
to the top of the loop. If its not, it compares the vertex's output distance to the initialized minDistance for the minimum distance. 
If the vertex's output distance is minimum, it updates the minDistance and vertex variables to the vertex's output distance and the 
vertex index. At the end of the loop it returns the vertex and distance variables as the unvisited node with the minimum distance.
In the main loop we would use the vertex index to go through its edges and the minDistance to calculate the new output distances for
each destination in its edges. Also when calculating distances for the destinations in a vertex's edges ie looping over the destinations
in a for loop, we can add a small optimization that if the destination is in visited, we continue to the top of the for loop. This is
because we know that the current calculation will not yield a minimum distance. This is because we already found a minimum distance to
the destination that is why it was visited before the current node, so adding a positive edge distance to the already greater current
distance will not yield a minimum distance so why bother. 

Dijkstra's algorithm is a simple depth-first search algorithm that starts with the unvisited node with the mimimum output distance. If
we use an array to obtain the minimum output distance, that is a linear O(v) time algorithm giving Dijkstra's algorithm as a whole
a time complexity of O(v^2 + e) and space complexikty of O(v) due to the output array. However, we could use a minHeap, to obtain the
vertex distance with a minimum output distance and it will take O(v ) time to initialize the minHeap and log(v) time to get the 
minimum output distance node giving an overall time complexity of O((v+e)*log(v)) and a space of O(v) space. This optimization of
Dijkstra's will thus run as long as the minHeap is non-empty or the minimum distance is +inf. This optimal version of Dijkstra's is
contained in dijkstrasAlgorithmII.py. 

This is a regular dfs traversal of a graph but we dont start from a popped node from a stack, we make an informed heuristic decision
to start from the unvisited node with a minimum distance, which also informs our decision to skip over any destination in a node's
edges that has previously been visited. So instead of checking if a node is visited (with the exception of destinations), we only 
check if its time to break out of the loop if distance is +inf. Elegant !!!"""


"""Inoptimal solution, using an array instead of a heap to store minimum distances to nodes
and at each step finding the node with the minimum distance to it and traversing its edges"""
#O(V^2 + e) time | O(V) space

# Find the lowest cost node that has not been processed yet
def find_lowest_cost_node(costs, processed):
    lowest_cost = float('inf')      # initialize lowest cost so far at infinity for easy comparison
    lowest_cost_node = None         # None will be returned if infinity is the lowest cost
    for node in costs:              # Go through each node in the cost's hashtable
        cost = costs[node]
        if cost < lowest_cost and node not in processed:    # if unprocessed and has a lower cost
            lowest_cost = cost                              # update lowest cost so far   
            lowest_cost_node = node                         # update lowest cost node
    return lowest_cost_node                                 

def dijkstra(start, edges):

    costs = {}                      # initialize costs hashtable
    for i in range(len(edges)):
        costs[i] = float("inf")     # unknown cost to get to each node from start node
    costs[start] = 0                # cost of getting to start node from itself is 0

    parents = {}                    # initialize parents hashtable
    processed = {}                  # initalize processed hashtable
    
    node = start                    # initialize current node as starting node

    while node is not None:         # if current node is None, all nodes have been processed
        cost = costs[node]          # cost to get to current node
        neighbors = edges[node]     # hashtable containing current node's neighbors mapped to weights
        for n, n_cost in neighbors:
            new_cost = cost + n_cost        # cost of current path to neighbor
            if new_cost < costs[n]:         # if current path is lower cost to neighbor
                costs[n] = new_cost         # update the minimum cost to neighbor from start
                parents[n] = node           # update the parent of neighbor
        processed[node] = True              # track that you've checked current node
        node = find_lowest_cost_node(costs, processed) # next current node is the unprocesseed lowest cost
    
    return list(map(lambda x: -1 if x[1] == float("inf") else x[1], costs.items()))

#O(V^2 + e) time | O(V) space
def dijkstrasAlgorithm(start,edges):
    numberOfVertices = len(edges)
    minDistances = [float("inf") for _ in range(numberOfVertices)] #array to store min distances to node, initialized with inf
    minDistances[start]  = 0  #add the distance from the root or start node to itself, 0 , so that we start looking at its edges first
    visited = set() #initialize a set to store the nodes already visited, constant time lookup

    while len(visited) != numberOfVertices: #we will be adding nodes to visited set as we go, stop when we have visited all nodes, O(v)
        vertex, currentMinDistance = getVertexWithMinDistance(minDistances, visited) #get unvisited node with shortest distance to it, O(v*v)
        if currentMinDistance == float("inf"): #if the unvisited node is disconnected, we are done
            break
        visited.add(vertex) #add the returned vertex since we are about to visit its edges

        for edge in edges[vertex]: #look through the current node's edges and the distances from current node to its edges, O(v*v+e))
            destination, distanceToDestination = edge #unpack edge, edge distance 

            if destination in visited: #if the current node's edge has already been visited, (constant time set lookup)
                continue    #we wont find a shorter path so no need looking, since we know all distances are positive 

            newPathDistance = currentMinDistance + distanceToDestination
            currentDestinationDistance = minDistances[destination]
            if newPathDistance < currentDestinationDistance: #minDistances[destination] = min(minDistances[destination], newPathDistance)
                minDistances[destination] = newPathDistance
    return list(map(lambda x: -1 if x == float("inf") else x, minDistances))
    


def getVertexWithMinDistance(distances, visited):#cruxof dijkstra's algorithm, looking at the edges of nodes with shortest distances first
    currentMinDistance = float("inf") #for tracking min distance seen as we loop through minDistances array
    vertex = None                     #for storing the node with the min distane seen so far, to be returned
    for vertexIdx, distance in enumerate(distances):
        if vertexIdx in visited:#using a set for visited ensures constant time lookup here, instead of an additional linear time operation
            continue
        if distance <= currentMinDistance: #the equal to ensures that if we have a disconnected node we can visit it when distance = inf
            vertex = vertexIdx
            currentMinDistance = distance
    return vertex, currentMinDistance

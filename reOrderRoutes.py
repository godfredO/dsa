"""There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this 
network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow. Roads 
are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi. This year, there will be a big 
event in the capital (city 0), and many people want to travel to this city. Your task consists of reorienting some roads such that each city 
can visit the city 0. Return the minimum number of edges changed. It's guaranteed that each city can reach city 0 after reorder.

Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]             Output: 3
Explanation: Reverse the direction of 3 edges ie [1,0], [3,1], [5,4] such that each node can reach the node 0 (capital).

Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]                   Output: 2
Explanation: Reverse the direction of 2 edges ie [2,1] such that each node can reach the node 0 (capital).

Input: n = 3, connections = [[1,0],[2,0]]                               Output: 0           Explanation:All nodes can reach node 0 as is

So this is a breadth first search question. Basically the algorithm is as follows. We want to know if each node can reach city 0. So we
create a graph with a hashmap and for each city we store the other cities that that have roads between them and the current city. So 
because we know that there is no loop, and there are n-1 edges and there is only one way between two cities ie no duplicate edges, this
graph is basically saying is there a road between two cities. So for edge [1,0] graph[0] = [1] and graph[1] = [0], so we are effectively
storing directionless information here. We still need direction based information so we add all our edges as tuples into a set for 
constant time access to road directions. Then we start a breadth first search from the capital, city 0. And we go through its neighbors,
after adding city 0 to a visit set and checking if the neighbor is unvisited. For each unvisited neighbor, we know there is some road 
between it and city 0 but we want to know the direction of that road. If it is from the neighbor to city 0 ie (neighbor, 0) then we know 
that the neighbor can reach city 0. Otherwise the direction must be from city 0 to the neighbor ie (0, neighbor), in which case we need to 
reverse it. We would have initialized a numRoadsToBeReversed variable before bfs so we increment this variable by 1 as a way of reversing 
this road. Nowwe know that all of city 0's neighbor's can reach it. So we need to look at city 0's neighbor's neighbors and see if they 
can reach their respective city 0 neighbor. Lol, what I mean is that lets say city 1 and city 2 are both neighbor's of city 0 and we 
reverse the road between city 0 and  city 2, so our numRoadsToBeReversed variable will be 1 then we add both city 1 and city 2 to the bfs 
queue and check their unvisited neighbors. If city 1's neighbor can reach city 1, then they can reach city 0 after gettting to city 1, 
otherwise we will have to reverse that neighbor's road to go to city 1. Similarly if city 2's neighbor can reach city 2, then they can 
reach city 0 via city 2 otherwise we would have to reverse that neighbor's road to go to city 2. Whether we reverse or not, we add the 
unvisited neighbor to the queue. To put it simply if the edge that exists between a current node and its neighboring node is from the
current node to the neighboring node, ie if (current, neighbor) is in our edges, we reverse that road. Alternatively we could say that 
if (neighbor, current) is not in our edges, the the road must be (current, neighbor) and so we must reverse it. Whether we reverse or
not we need to check that neighbor's neighbor's if those can reach the neighbor who we know can reach the target either originally or
after reversals. To allow constant time access of this direction based information we add tuples of edges into a set, since tuples are 
hashable.

Like all breadth-first search questions and approaches, we first start at the node of interest (city 0 in this case, beginWord in 
wordLadder.py, or targetNode in NodesDistanceK.py), and looking at neighboring nodes in a way that treats our graph as if its undirected.
To go through neighbors in an undirected way, we create a graph, where graph[node] = [neighbor1, neighbor2]. In this nodesDistanceK we 
create a map of node:parent in order to move through the graph in an undirected way. Then after processing the unvisited neighbors of
our target node, we look at those node's neighbors one level at a time and each level will be the same distance from the target. So the
first step in any bfs is to grab our targetNode if we dont already know it, then find some way of creating an undirected graph out of our
directed graph before processing our nodes one level at a time, start from the targetNode and expanding outwards level by level. With 
that said we could also use depth first search to solve this problem since we already have our target node. Also google breadth-first 
search tag on leetcode and then go through them with youtube explanations.
"""

"""Breadth first search approach"""
from collections import deque
def minReorder(n, connections):

    graph = {i:[] for i in range(n)}  #convert our directed graph into an undirected graph
    connections_set = set()

    for edge in connections:
        source, destination = edge
        graph[source].append(destination)
        graph[destination].append(source)
        connections_set.add((source,destination)) #for constant time check if road leads from neighbor to currentNode 

    #good practice to initialize sets and deques with value in iterable especially for strings to avoid splitting or u can initialize it
    #empty and then call .add(value) for set or .append(value) for deque
    visited = set()
    queue = deque([0]) 
    numRoadReversals = 0

    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)

        for neighbor in graph[current]:
            if neighbor in visited:
                continue
            if (current,neighbor) in connections_set:
                numRoadReversals += 1
            queue.append(neighbor)
    return numRoadReversals

    
    
class NumRoadReversals:
    def __init__(self, value):
        self.value = value
        
def minReorder(n, connections):
    graph = {i:[] for i in range(n)}  #convert our directed graph into an undirected graph
    connections_set = set()

    for edge in connections:
        source, destination = edge
        graph[source].append(destination)
        graph[destination].append(source)
        connections_set.add((source,destination)) #for constant time check if road leads from neighbor to currentNode 
    
    visited = set()
    reversals = NumRoadReversals(0)  #Since value is going to be passed around in recursion use a mutable obejct to store value
    explore(0,graph, visited, reversals, connections_set) #start dfs from targetNode which we already have.
    return reversals.value

def explore(node, graph, visited, reversals, connections_set):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor in visited:
            continue
        if (neighbor, node) in connections_set:
            reversals.value += 1
        explore(neighbor,graph, visited, reversals, connections_set)
    

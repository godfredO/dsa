"""You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges 
times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source 
to target. We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is 
impossible for all the n nodes to receive the signal, return -1.

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2      Output: 2
Input: times = [[1,2,1]], n = 2, k = 1                      Output: 1
Input: times = [[1,2,1]], n = 2, k = 2                      Output: -1




This is a Dijkstra's algorithm pattern question as this is a shortest path from a start node question. So we are going to find the shortest
time (path) from the start node , k , to each node. The question asks to find the minimum time it takes for all nodes to receive the signal
sent from start node, k. This request is actually like the apartmentHunting.py question in that after finding the shortest time from start
node, k to all the other nodes, we return the maxiumum of these minimum times as the representative time for all nodes to receive the signal.
The reason is that since the signal is being sent from start node, k , and takes the minimum time to reach each node, the minimum time it 
takes or all nodes to receive the signal is the time of the node with the largest minimum time because by that time, all the other nodes 
would have also receieved their signal. 
So this question is an implementation of dijkstra's algorithm and the optimal implementation of Dijkstra's uses a minimum heap to choose the
unvisited node with the minimum time and then traverse its edges and update those if the unvisited node's time plus the edge weight to any
other node, is the less than the current time stored for that destination node. If the graph is disconnected then there would be no way for 
the signal from the start node to reach the disconnected and so whenever the univisited node with minimum distance has a distance of +inf,
we just return -1, since its impossible for all the n nodes to receive the signal.
It is important to note that dijkstra's algorithm is a breadth-first search algorithm with the addition choosing the unvisited node with the 
miniumum distance as the current node and when we have the current node, we go through all of its edges and destination nodes, update their 
distances. 
In dijkstrasAlgorithmII.py, we implement an entire minHeap, but in this question we will actually be using an in-built min heap 
class and its methods. This module in python is called heapq so we have to first import heapq, and it typically takes in an array of numbers
and then converts this array into a heap by calling the heapify method ie array = [num1, num2, num3], heapq.heapify(array),in which case 
heapq, shifts the numbers in the array around to turn it into a heap. But in this question, we need to access both the node id's and their 
distances, ie when we need to heapify based on a node and its attribute, heapq requires that we supply it a list of tuples and it will build 
the heap based on the first value, with the first value being the attribute of interest, in this case minDistance from the start node. So we 
will build our heap as array = [(0,k)] , heapq.heapify(array) which will build a heap based on the first values in the tuples. To remove the 
root node, we supply the heapified array to the heappop() method ie minDistance, node = heapq.heappop(array). When we calculate, we need to
update distance, but heapq doesnt have a way to do that, ie replace the attribute of a node. But that is where our visited set comes in, in
that we can push updated tuples with new distances for the same node onto the heap and we make sure to keep track of the visited nodes. So 
whenever we pop the root node, we add it to the visit set so that if we encounter a node we already visited we just continue to the top of
the while loop, and this will ensure that if we have duplicate nodes, we just keep popping, find the are visited and keep returning to the
top of the while loop until the heap is empty. If the current popped root is not visited, then we go through its edges, and for each edge,
we push a new tuple unto the heap with the updated distance of [(minDistance + edgeWeight, neighboringNode)], and when we pop, its will be
the node with the minimum minDistance on the heap. And because of how dijkstra's works, if we later find a new path to an already visited
node, its sure to be a worse minDistance otherwise, that path would have been visited first. Also to actually answer the question, we 
initialize a maxNodeDistance at 0, the distance of the start node, k from itself. Then after popping a node, we check if its visited and if
we find the node to be unvisited, we do a max comparison with this maxNodeDistance. How do we know that, the graph is disconnected, if the
while loop terminates because the heap is empty, we check if we visited all n nodes. If we did, then we return  maxNodeDistance, if not we
return -1. 
With all this information, it is still essential to review dijkstrasAlgorithm.py to understand the algorithm albeit with an inoptimal array 
based way of finding the unvisited node with the minDistance and more importantly dijkstrasAlgorithmII.py to understand the inner workings 
of a modified minHeap used to provide access to the unvisited node with minDistance. Anyway, using heapq will be useful in an interview.
Finally search google for Dijkstra's leetcode questions, there is either an official tag, or a discussion board with list of questions. """

import heapq
def networkDelay(times, n, k):
    graph = { i:[] for i in range(1,n+1)}  #we need this in case of a disconnected graph, every node is accounted for

    for triplet in times: #convert list of edges to adjacency graph
        sourceNode, destinationNode, edgeWeight = triplet  
        graph[sourceNode].append([destinationNode, edgeWeight])
    
    visited = set()
    minHeap = [(0,k)]
    heapq.heapify(minHeap)
    maxNodeDistance = 0

    while minHeap:
        minDistance, currentNode = heapq.heappop(minHeap)
        if currentNode in visited:
            continue
        visited.add(currentNode)
        maxNodeDistance = max(maxNodeDistance, minDistance)

        for neighbor, neighborDistance in graph[currentNode]:
            if neighbor in visited:
                continue
            heapq.heappush(minHeap, (minDistance+neighborDistance, neighbor))
    
    return maxNodeDistance if len(visited) == n else -1

    
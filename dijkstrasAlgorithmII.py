"""This is solution II to dijkstras algorithm question discussing the optimal solution of using a heap to obtain the unvisited node with
the miniumum output distance. For a general description of the logic of Dijkstras algorithm, check dijkstrasAlgorithm.py. Anyway after
initializing an output array with +inf and updating the output[start] = 0, the minHeap version deviates from the array version of 
dijkstra's algorithm. 

First of all let's start by discussing how we modify a standard minHeap class for use in Dijkstras Algorithm. The first thing to realize
is that since the minHeap is supposed to return [nodeIdx, distance] for the unvisited node with the minimum output distance, we build the
minHeap with an array of tuples (nodeIdx, distance) and this distance is first initialized to +inf for all nodes. The next thing is that
to track the position of a nodeIdx's tuple in the minHeap, we add a vertexMap dictionary on the class definition. This map is tracks the
position as {nodeIdx : PositionIdx in Heap}, thus if need to update a node's distance we first use this map to find its position in the 
heap and then use that position index to access its tuple in the heap before updating the distance. Also note that siftUp and siftDown
will arrange the minHeap nodes according to the distance stored in the tuple. So we initialize the minHeap with an array of tuples ie 
[(node1, +inf),(node2, +inf),...], and this is done in order ie node index 0, then node index 1 etc so that we also initalize the vertex
map with {0:0,1:1} meaning that node index 0's tuple is currently at positon 0 in the heap. That is to say, the list comprehensiion used
to generate an array of tuples with initial distances of +inf must be done in order so that the the when the vertexMap is initialzed
with self.vertexMap ={idx:idx for idx in range(len(array))}, we know that they match. Also we initialize the output array with +inf
so that the output, the heap and the vertex map are all in sync when we start the algorithm.

Since we know that the distance of the start node from itself is 0, we need to update its distance value in the minHeap and the output
array. Updating the output array is trivial output[start] = 0. To update the minHeap, we write a method on the minHeap class called 
update() that takes in a node index and a distance value and updates the distance value of that node index in the minHeap. This method 
accesses the position of the node's tuple in the heap using the vertex map and then uses this positionIdx to update the tuple 
ie self.heap[vertexMap[nodeIdx]]= (nodeIdx, distance). Notice here that since tuples are immutable we simply replace the tuple object. 
If lists were used instead ie [nodeIdx, +inf], we could have said self.heap[vertexMap[nodeIdx]][1] = distance. After updating the
tuple object or distance, this method calls the siftUp method ie self.heap[vertexMap[nodeIdx], self.heap], and you can see that where
we would have currentIdx in a regular heap we are using the position index stored in the vertex map. We call siftUp because we only
make updates to minimize the distance ie the node now has a lower distance and hence should be higher up the tree, or in the least
should switch places with its parent node. As such, this update method is also used to update the distance of a node in the minheap 
when we go thorough a node's edges, calculates distances to the destinations in those edges and determine that the calculated distances 
are lower than the current distance in the output and hence the distance value of that destination in the minHeap. This is so that the 
minHeap and the output are always comparing the same values for any vertex. Note that update effectively replaces insert() method of a 
regualar minHeap, since we initialize our heap with all the nodes, and we insert nothing, just update.

The siftUp() method called by update() is pretty similar to a regualr heap just that instead of comparing heap[currentIdx] and 
heap[parentIdx], since we know that at currentIdx and parentIdx in the heap we have tuple object and what we mean to be comparing is
the distance stored inside those tuples, we compare heap[currentIdx][1] and heap[parentIdx][1]. When distance at the currentIdx tuple
is less we call the swap method. So how is this swap() different. Well when the swap method swaps the elements at the passed indices
in the heap, ie heap[i], heap[j] = heap[j], heap[i], it is actually swapping tuple objects, but before it does that it has to update
the vertex map to reflect the new positions. So first is to use the heap position indices to access the tuples, read the nodeIdx inside
each tuple, and update the positonIdx stored for that nodeIdx ie self.vertexMap[heap[i][0]] = j and self.vertexMap[heap[j][0]] = i before
actually swapping the tuple objects' positions in the heap. 

In addition to the vertexMap, the heap is also an attribute on the minHeap class itsel ie self.vertexMap, self.heap, and self.heap is
created by calling the buildHeap method which calls the siftDown method. The buildHeap method is the same as the regular minHeap, the
siftDown method like the siftUp method compares the tuple distances at the heap parent and child indexes ie heap[idxToSwap][1] and
heap[currentIdx][1] before calling the swap method and updating currentIdx and childOneIdx.

There is one more method added to minHeap which is isEmpty() which simply returns a boolean representing whether the miHeap is empty
and is used as the while loop condition in the main function. So the final method in the minHeap is the remove() method which will
remove the root of the minHeap ie the tuple object with the minimum distance value and return it to the main function. How does this
method work? We first check if the tuple is empty in which case we return. This is a fail safe of sorts since the while loop in the 
main function, checks if the heap is empty as its loop condition. The we swap the first and last tuple objects in the heap, then 
pop from the heap, this new last tuple object, similar to what we do in a regular heap. Since the pop value is actually a tuple, we
unpack it into the nodeIdx, and distance (which will later be returned), but we use the vertex to pop that key:position pair from 
the vertexMap dictionary. So it turns out that in Python you can remove a key:value pair from a dictionary by calling the pop() method
on the dictionary with the key as input ie dict.pop(key) and this will remove the key:value pair and return the value. We dont need
the position for anything so we dont store a reference to it ie self.vertexMap.pop(vertex). We then do the standard thing of sifting
down the 'new' root into its correct position and then we return vertex,distance as the unvisited node with the minimum value. 

So how does the main dijkstra's algorithm function differ. Well, after instantiating the heap with +inf distances and updating the
start distance we then enter the while loop whose condition is as long as the heap is non-empty ie while not heap.isEmpty(). First
thing is to remove the root of the heap, by calling the remove method, unpack the tuple returned into vertex, distance and check
if the distance is +inf, and if it is we know that the algorithm is done and we break out of the while loop. If its not, we access
the vertex's outbound edges ie edges[vertex], calculate the new distance using the vertex's distance + destinationEdgeDistance. We
then compare this new distance to the output[destination]. If the new distance is lower, we update output[destination] and update
the heap by calling the update method with the destination and new distance as inputs ie minHeap.update(destination, newDistance).
At the end of the main algorithm, we loop over the output and replace all +inf with -1 before returning. We do this simply with
a map() and a lambda function. Finally unlike the other solution where we need to ensure our helper function returns the minimum
output distance of unvisited nodes, here we remove a node objects tuple entirely with the remove method so no need for a visited
array. We are in no danger of re-visiting a node. In the other solution, that is essential otherwise we would be choosing the start
node over and over and over again since the lowest non-negative distance possible is 0. Here when we remove the start node and 
consider it edges its never going back to the minHeap again so no need for a visited set.
"""

#Min heap that whose root node has the minimum distance from start node in dijkstra's algo
class MinHeap:
    def __init__(self,array):
        #Holds the position in the heap that each vertex is at ie node:heapIdx for constant time update of (vertex, distanceToTheVertex)
        self.vertexMap ={idx:idx for idx in range(len(array))} #at initialization will be node0:position 0 etc check line 146
        self.heap = self.buildHeap(array)
    
    def isEmpty(self):
        return len(self.heap) == 0
    
    #O(n) time | O(1) space
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)): # + 1 to include firstParentIdx, and start from firstParentIdx and sift
            self.siftDown(currentIdx, len(array) - 1, array) #compare firstParentIdx and sift by comparing to children nodes
        return array #return array to be stored as self.heap
    
    #O(log(n)) timw | O(1) space
    def siftDown(self,currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx][1] < heap[childOneIdx][1]: #[node, distance] ie choose child node is smallest distance
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            
            if heap[idxToSwap][1] < heap[currentIdx][1]: #compare distance values in heap
                self.swap(currentIdx, idxToSwap, heap) #if child node has a lower distance, swap positions with parent node
                currentIdx = idxToSwap #parent node's new position, to compare with new children
                childOneIdx = currentIdx * 2 + 1 #calculate new childOneIdx
            else:
                return #done sifting
    
    #O(log(n)) time | O(1) space
    def siftUp(self,currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2  #calculate the parentNodeIdx of currentIdx childNode
        while currentIdx > 0 and heap[currentIdx][1] < heap[parentIdx][1]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    #O(log(n)) time | O(1) space
    def remove(self):
        if self.isEmpty():
            return
        self.swap(0, len(self.heap) - 1, self.heap)
        vertex, distance = self.heap.pop()  #heap is storing (vertex, distanceToVertex)
        self.vertexMap.pop(vertex)          #remove vertex for vertex map
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return vertex, distance
    
    def swap(self, i, j, heap): #i,j is childIdx , parentIdx each idx stores [node, distance], so access node to update vertexMap
        self.vertexMap[heap[i][0]] = j   #update the vertex map, with node ie [node, distance], node: position in heap
        self.vertexMap[heap[j][0]] = i   #update the vertex map
        heap[i], heap[j] = heap[j], heap[i]  #swap (vertex, distance) in heap for positions i,j

    def update(self,vertex, value):
        #access vertex's heapIdx using vertexMap to change vertex distance in heap
        self.heap[self.vertexMap[vertex]] = (vertex,value) #O(1), replace the tuple in heap at position stored for vertex in vertexMap
        self.siftUp(self.vertexMap[vertex], self.heap)  #O(log(n)), call siftUp, from the position



#O((v + e)*log(v)) time | O(V) space
def dijkstrasAlgorithm(start,edges):
	numberOfVertices = len(edges)
	minDistances = [float("inf") for _ in range(numberOfVertices)]
	minDistances[start] = 0
	
	minDistancesHeap = MinHeap([(idx,float("inf")) for idx in range(numberOfVertices)]) #(node, distance)
	minDistancesHeap.update(start,0) #update startNode distance from inf to 0
	
	while not minDistancesHeap.isEmpty():
		vertex, currentMinDistance = minDistancesHeap.remove()
		
		if currentMinDistance == float("inf"):
			break
		
		for edge in edges[vertex]:
			destination, distanceToDestination = edge
			
			newPathDistance = currentMinDistance + distanceToDestination
			currentDestinationDistance = minDistances[destination]
			if newPathDistance < currentDestinationDistance:
				minDistances[destination] = newPathDistance
				minDistancesHeap.update(destination, newPathDistance)
	return list(map(lambda x:-1 if x == float("inf") else x, minDistances))
        
start = 3
edges = [
    [
      [1, 2],
      [3, 3],
      [4, 2]
    ],
    [
      [0, 1],
      [6, 3]
    ],
    [
      [3, 9]
    ],
    [
      [0, 3],
      [1, 4],
      [4, 4],
      [8, 7]
    ],
    [
      [0, 1],
      [10, 3]
    ],
    [
      [7, 1],
      [8, 4]
    ],
    [
      [8, 1]
    ],
    [],
    [
      [7, 1]
    ],
    [
      [10, 2]
    ],
    []
  ]

print(dijkstrasAlgorithm(start,edges))
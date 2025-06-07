class Node:
  def __init__(self,row,col,value):
    self.id = str(row) + "_" + str(col) #hashable unique identifier for node
    self.row = row #store the node's row
    self.col = col #store the node's column
    self.value = value  #value stored at node in graph, 0 is free space, 1 is obstacle
    self.distanceFromStart = float("inf") #G-score, distance from start node, initialize to inf
    self.estimatedDistanceToEnd = float("inf") #F-score, ie G-score + H-score, initialize to inf
    self.cameFrom = None #origin node

class MinHeap:
  def __init__(self,array):
    #Holds the position in the heap that each node is at
    self.nodePositionsInHeap = {node.id:idx for idx,node in enumerate(array)} #map node id to initial position in heap, 
    self.heap = self.buildHeap(array) #positions in nodePositionsInHeap will be updated from initial in swap method during buildHeap
  
  def isEmpty(self):
    return len(self.heap) == 0
  
  #O(n) time | O(1) space
  def buildHeap(self,array):
    firstParentIdx = (len(array) - 2) // 2
    for currentIdx in reversed(range(firstParentIdx + 1)):
      self.siftDown(currentIdx,len(array)-1, array)
    return array
  
  #O(log(n)) time | O(1) space
  def siftDown(self,currentIdx,endIdx,heap):
    childOneIdx = currentIdx * 2 + 1
    while childOneIdx <= endIdx:
      childTwoIdx = currentIdx * 2 + 2 if currentIdx *2 + 2 <= endIdx else -1
      if childTwoIdx != -1 and heap[childTwoIdx].estimatedDistanceToEnd < heap[childOneIdx].estimatedDistanceToEnd: #compare F-values
        idxToSwap = childOneIdx
      else: 
        idxToSwap = childOneIdx
      if heap[idxToSwap].estimatedDistanceToEnd < heap[currentIdx].estimatedDistanceToEnd:
        self.swap(currentIdx,idxToSwap, heap)
        currentIdx = idxToSwap
        childOneIdx = currentIdx * 2 + 1
      else:
        return
  
  #O(log(n)) time | O(1) space
  def siftUp(self,currentIdx,heap):
    parentIdx = (currentIdx - 1) // 2
    while currentIdx > 0 and heap[currentIdx].estimatedDistanceToEnd < heap[parentIdx].estimatedDistanceToEnd: #compare by F-values
      self.swap(currentIdx,parentIdx,heap)
      currentIdx = parentIdx
      parentIdx = (currentIdx - 1) // 2

  #O(log(n)) time | O(1) space
  def remove(self):
    if self.isEmpty(): #if the heap is empty
      return #do nothing just return
    self.swap(0,len(self.heap)-1, self.heap)
    node = self.heap.pop()
    del self.nodePositionsInHeap[node.id] #remove from id:heap_position map
    self.siftDown(0,len(self.heap) -1, self.heap)
    return node
  
  #O(log(n)) time | O(1) space
  def insert(self,node):
    self.heap.append(node)
    self.nodePositionsInHeap[node.id] = len(self.heap) - 1 #add node's id:heap_position to map, sift will update position 
    self.siftUp(len(self.heap)-1, self.heap) #this method will call the swap method which will update node's nodePositionsInHeap
  
  def swap(self,i,j,heap):
    self.nodePositionsInHeap[heap[i].id] = j #update the node's id:position in map before swapping for siftUp and siftDown
    self.nodePositionsInHeap[heap[j].id] = i #update the node's id:position in map before swapping for siftUp and siftDown
    heap[i], heap[j] = heap[j], heap[i] #swap in heap step
  
  def containsNode(self,node):
    return node.id in self.nodePositionsInHeap #if node is in heap, its id will be in map
  
  def update(self,node): # update position if F or G score is updated by sifting up bcos we only update G to lower value
    self.siftUp(self.nodePositionsInHeap[node.id], self.heap) #if a lower G score is found, siftUp based on new F-score

"""In A* pathfinding algorithm we use three factors to traverse the graph, G score which is the distance from the start node,
H score which is the predicted or estimated distance to the end node and F score which is the sum of the two and at each stage
we choose to visit the node with the lowest F score. The H score is calculated using L1 or Manhattan distance. We also store
in some data structure, for each node, the node that we came from ie the node that cause the G score to be updated. Obviously
the algorithm will begin from the start node, whose G score is 0 and we would get all of its neighbors, update their G score by
setting it to 1 plus the G score of whatever node caused the update, (start node 0 in this case). We add these nodes to the min
Heap which arranges the nodes based on their F score, and then mark the origin node(in this case start node) as visited as well
as store the origin node in the data structure for the chosen node. Thus by using a minHeap to choose the node with the lowest
F score we move in the most probable shortest distance from start node to end node and at the end of the algorithm, we can 
retrace the origin nodes to reconstruct the shortest path.Note the G-score accounts for obstacles while the H-score doesnt. This
is because the G-score of a node is 1+G(origin node) so how many steps around obstacles taken while H-score is a prediction of
unobstructed path which may not actually be the case, but if at each point we choose the node with the shortest distance from start
node and shortest predicted distance to end node, we will end up taking the overall shortest distance from start to end. In other
words if it takes as a lot of steps around obstacles to get to a node from the start node, those steps contribute to the overall
distance to end node. Thus when we update a node's origin, its because we found a shorter distance from the start node through all 
the obstacles and if this nodes ends up being on the shortest path , we want to take the shorter distance to to start node."""
#O(w*h*log(w*h)) time | O(w*h) space
def aStarAlgorithm(startRow,startCol,endRow,endCol,graph):
  nodes = initializeNodes(graph) #helper function to create nodes for every positon and value in input graph

  startNode = nodes[startRow][startCol] #grab the node object representing the start position
  endNode = nodes[endRow][endCol]       #grab the node object representing the end position

  startNode.distanceFromStart = 0 #update the G-score for the start node,distance from itself to itself
  startNode.estimatedDistanceToEnd = calculateManhattanDistance(startNode,endNode) #calculate H-score, update F= G+H = 0+H = H

  nodesToVisit = MinHeap([startNode]) #create MinHeap of node objects, initialized with start node
  
  while not nodesToVisit.isEmpty(): #while the minheap is not empty,use method since nodesToVisit isnt just a list
    currentMinDistanceNode = nodesToVisit.remove() #remove the current root of F-score minHeap
    if currentMinDistanceNode == endNode: #if we are at the endNode
      break #break out of while loop, even if the minheap is not empty because we found our destination

    neighbors = getNeighboringNodes(currentMinDistanceNode,nodes) #otherwise get the neighbor nodes of current node
    for neighbor in neighbors:
      if neighbor.value == 1: #if the neigbor is an obstacle
        continue #continue to next neighbor

      tentativeDistanceToNeighbor = currentMinDistanceNode.distanceFromStart + 1 #tentaive g-score for neighbor
      if tentativeDistanceToNeighbor >= neighbor.distanceFromStart: #if tentative distance is not shorter
        continue #continue to next neighbor, no need to update g-score 

      neighbor.cameFrom = currentMinDistanceNode #update origin node if tentative distance is shorter, neighbor is  non-obstacle
      neighbor.distanceFromStart = tentativeDistanceToNeighbor #update g-score if tentative distance shorter, non-obstacle neighbor
      neighbor.estimatedDistanceToEnd = tentativeDistanceToNeighbor + calculateManhattanDistance(neighbor,endNode) #update F-score

      if not nodesToVisit.containsNode(neighbor):#add neighbor to minHeap if neighbor is not already in the minHeap
        nodesToVisit.insert(neighbor)
      else: #if neighbor existed then update its position since g-score has changed
        nodesToVisit.update(neighbor)
  return reconstructPath(endNode) #use node.cameFrom to reconstruct path. If endNode is reached , it will have cameFrom (as neighbor)

def initializeNodes(graph): #create node object to represent the 0,1's in the graph
  nodes = []
  for  i, row in enumerate(graph): #unpack each row and add a row index
    nodes.append([]) #append an empty list to hold node objects for current row
    for j, value in enumerate(row): #read and index the values in the current row of graph
      nodes[i].append(Node(i,j,value)) #add the node object to the subarray holding nodes in its row
  return nodes #2-d array of node objects in same structure as original graph, holding nodes instead of 0's ad 1's


def calculateManhattanDistance(currentNode,endNode):
  currentRow = currentNode.row #access the current node's row from node object
  currentCol = currentNode.col #access the current node's column from node object
  endRow = endNode.row         #access the end node's row from node object
  endCol = endNode.col         #access the end node's column from node object
  return abs(currentRow - endRow) + abs(currentCol - endCol) #return calculated L1 distance

def getNeighboringNodes(node,nodes):
  neighbors = [] #list of neighbors
  numRows = len(nodes)  #last row in the nodes graph, since border nodes don't have all 4 neighbors, up,down,right,left
  numCols = len(nodes[0]) #last column in the nodes graph, since border nodes don't have all 4 neighbors,up,down,right,left

  row = node.row #acess current node's row from node object attribute
  col = node.col #access current node's column from node object attribute

  if row < numRows - 1: #if the current node is not in the last row, it will have a down neighbor
    neighbors.append(nodes[row+1][col]) #append down neighbor
  
  if row > 0: #if the current node is not in the first row, then it will have an up neighbor
    neighbors.append(nodes[row -1][col])
  
  if col < numCols - 1: #if current node is not in the last column, then it will have a right neighbor
    neighbors.append(nodes[row][col+1])

  if col > 0: #if the current node is not in the first column, then it will have a left neighbor
    neighbors.append(nodes[row][col-1])
  
  return neighbors

def reconstructPath(endNode):
  if not endNode.cameFrom: #do we have a node we came from on the endNode, if we dont
    return [] #empty list because there is no path to endNode if endNode doesnt have a cameFrom attribute
  
  currentNode = endNode #start from end node
  path = [] #initalize output list

  while currentNode: #while currentNode is not None, startNode will have a None cameFrom, so loop exits after startNode is added
    path.append([currentNode.row,currentNode.col]) #append current node's row and column
    currentNode = currentNode.cameFrom #then move up to the currentNode's origin
  return path[::-1] #reverse path before returning since endNode was added first and startNode was added last

  



startRow = 0
startCol = 1
endRow = 4
endCol = 3
graph = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0]
  ]
print(aStarAlgorithm(startRow,startCol,endRow,endCol,graph))
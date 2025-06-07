"""The naive solution to this question is to conduct a depth-first search repeatedly by removing each edge and if the dfs 
reaches every node then the graph is connected otherwise its not. Thus since dfs takes O(e+v) times repeating it e times 
after removing an edge will make this O(e*(v+e)). Now the optimal way of solving this problem involves classifying edges
as tree edges, back edges, forward edges and cross edges. A tree edge discovers new nodes from the current node, a back edge 
goes back to a discovered ancestor node and a forward edge takes you to an already discovered descendant node, a cross edge
doesnt matter for this problem because it goes from one node to another node where the two nodes are rooted in different 
subtrees. A bridge edge is an edge that is the only way to reach a node. Thus if a bridge exists in the graph, it means if
that bridge is removed, there will be no way to reach that node, making the graph disconnected and therefore not two-edge
connected. Thus the idea is that if during the dfs we detect a bridge, we know that the input graph is not two-edge connected
but if there are no bridges and the graph is connected then it is two-edge connected. Thus by using the concepts of foward,
back, tree, brige edges we don't have to test if each edge is a brige by repeating dfs multiple times; we just have to repeat
it once. The way this solution goes about this is that when we visit a node with a tree edge, we set an arrival time and we 
return the minimum ancestor arrival time we are able to reach with a back edge. We initialize the minimum arrival times equal
to the node's arrival time until a back edge gives us a lower ancestor arrival time, taking the minimum ancestor arrival time
if multiple are found, proving that the tree edge that discovered the node is not a bridge. If however, only forward edges
exist from a particular node; which we determine if the ancestor arrival times from a node are actually descendant arrival times
since those arrival times are greater than the node's arrival time; then it means that the tree edge that discovered that node'
is a bridge and we bubble this up by setting the minimum ancestor time to be -1. This ensures that this value will bubble up the
tree, because we initialize the minimum ancestor time to be equal to a node's arrival/discovery time /order."""
#O(v+e) time | O(v) space
def twoEdgeConnectedGraph(edges):
    if len(edges) == 0:  #handle edge case of empty graph
        return True #an empty graph is theoretically two-edge connected so handle this edge case by returning True
    
    arrivalTimes = [-1]*len(edges)  #initialize arrival times as -1 for all nodes in adjacency list, for easier comparison 
    startVertex = 0 #start dfs at first node, ie node 0 since a non-empty graph will at least contain that otherwise line 22
    if getMinimumArrivalTimeOfAncestors(startVertex,-1,0,arrivalTimes,edges)== -1: #recursive dfs function
        return False #if recursive func returns -1 ie bridge , return False. Note parent node of startVertex 0 is set to be -1
    
    return areAllVerticesVisited(arrivalTimes) #if no bridge detected above, check that graph is connected ie all node visited

def areAllVerticesVisited(arrivalTimes): #to prove thatt the graph is connected, check that all arrival times are updated
    for time in arrivalTimes:
        if time == -1: #if any arrival time is -1, it was unvisited in dfs because graph is actually disconnected
            return False #a disconnected graph is not two-edge connected
    return True   #if all nodes were visited and no bridge was detected, return True for two-edge connected

def getMinimumArrivalTimeOfAncestors(currentVertex,parent,currentTime,arrivalTimes,edges):
    arrivalTimes[currentVertex] = currentTime #set the arrival time at current vertex/node
    minimumArrivalTime = currentTime #initialize the min ancestor arrival time as the discovery time of current vertex
    for destination in edges[currentVertex]: #dfs of outbound edges of current vertex
        if arrivalTimes[destination] == -1 : #if destination isnt discovered yet ie arrival time is initial value
            minimumArrivalTime = min(minimumArrivalTime, getMinimumArrivalTimeOfAncestors(
                destination,currentVertex,currentTime+1,arrivalTimes,edges
                )) #call dfs on descendant and update the minimum ancestor time with minimum ancestor reachable by descendant
        elif destination != parent: #if destination already visited and is not the parent whose tree edge discovered current
            minimumArrivalTime = min(minimumArrivalTime, arrivalTimes[destination]) #then update with its min ancestor time
    if minimumArrivalTime == currentTime and parent != -1:#a bridge was detected if forward edges and not at startVertex
        return -1
    return minimumArrivalTime




edges = [
    [1, 2, 5],
    [0, 2],
    [0, 1, 3],
    [2, 4, 5],
    [3, 5],
    [0, 3, 4]
  ]
print(twoEdgeConnectedGraph(edges))
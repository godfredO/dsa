""" So the general steps for graph problems are
    - visited data structure, could be a single variable (count) or a set or a matrix
    - an outer loop to ensure that we call dfs on every node even if the graph is disconnected, we may filter out some nodes in outer loop
    - inside the dfs function, we initialize a stack with the call node. Dfs runs as long as the stack is non-empty
    - inside the dfs, we check if the current node is visited. If it is we might continue to the next node on the stack or even return
    - if current node is unvisited we mark as visited
    - we use a getNeighbors function to collect the neighbors of the current node and use a for loop to add them to the stack
    - when the dfs stack is empty, we may return something or store something in outside the loop, then back to the outer loop

The input to this question is a list of edges, representing an unweighted, directed graph with at least one node and we are tasked with
writing a function that returns a boolean representing whether the given graph contains a cycle. A cycle is defined as any number of
vertices, including just one vertex, that are connected in a closed chain. A cycle can also be defined as a chain of at least one vertex
in which the first vertex is the same as the last. The adjacency list represents a graph. The number of vertices in the graph is equal to
the length of edges, where each index i in edges contains vertex i's outbound edges in no particular order. Each individual edge is 
represented by a positive integer that denotes a destination vertex index in the list, that the source vertex index is connected to.
Since these edges are directed, you can only go from source vertex index to destination vertex index. We would have thus found a cycle,
if we discover a self loop ie a destination vertex same as the source vertesx ie if at index 0 in the adjacency list we had [0], then we
have a self loop and thus a cycle. Similarly we would have found a cycle if the destination vertex index also has a directed edge to the
source vertex index eg at index 0 we have [1] and at inde 1 we have [0]. A cycle can include any number of vertices.

So now we come to cycles question. There are two solutions here that I will not discuss, because i have seen a better solution so I am 
going to discuss that ie solution one. So again this solution hinges on clever modifications and implementations of the general steps.
For one we follow the question's definitions of a cycle and thus formulate our solution as one of finding cycles starting from and ending 
at each node in the adjacency list. That is if we started at a node in the adjacency list, will we cycle back to it. Here we are not 
concerned about detecting a cycle in general per se but specifically a cycle from the starting node and back to the starting node. This way 
we will only discover a cycle if we start a dfs from any of the nodes involved in the cycle but not from any other node. This specific 
constraint works to really simplify the code. So our outer loop is basically going to choose each node in turn as the starting node and check 
if we ever get back to that same node in the dfs starting from it. Second, the dfs function actually returns a boolean; True for we found a 
cycle back to the starting node, False for we did not find a cycle back to the starting node. So in the outer loop we say that if we receive 
True from the dfs function, meaning we found that the current starting node is involved in a cycle, we return True. If we go through all the 
nodes as the starting node and never find a cycle that starts and ends at that particular starting node, we return False ie. when the outer for 
loop terminates, we return False. Notice that the outer loop here actually does what its said to do in the steps with no modifications, ie it 
ensures that we start a dfs from every node in the adjacency list.

So from the outer loop we call the dfs function on each starting node index. And we know from the definition of the cycle we are using that
we would have found a cycle back to the starting node index if in the course of the dfs we discover the starting node index in the outbound
edges either as a self loop or a cycle involving other nodes. That is inside our while loop if startingNode in edges[currentNode] for any
currentNode, we have fond a cycle back to the starting node. Since dfs in O(v+e), this is simply another e step ie O(v+e+e) and hence doesnt
worsen our time complexity. The second thing of note is that we initialize a seen set for each dfs call. This seen set is serving the same
function as a visited set but instead of initializing it in the main loop, we initialize it inside the dfs function. Why? Because we are 
only interested in cycles back to our starting nodes. And how do we use this seen set? In the loop for adding destination nodes (neighbors),
we only add child nodes that are unvisited. This is are not interested in cross edges. An edge that leads to an alread discovered node that
isnt its ancestor is a cross edge and the seen set is there to ensure we don't add cross edges to our stack. A cycle exists if a back edge
to the starting node is found, so to not mistake a cross edge for a back edge.
"""


"""Solution one"""
#O(v+e) time | O(d) space
def cycleInGraph(edges):
	for i in range(len(edges)): #choose each index as the starting node
		if hasCycle(edges, i): #if back edge to starting node is discovered, a cycle has been discovered
			return True #return True for back edge to current starting node hence cycle
	return False #return False if no back edge is discovered for any starting node
	
def hasCycle(edges, target):
	stack = [target] #recursive stack
	seen = set()    #visited set used here to separate cross edges from tree edges
	while stack:
		current = stack.pop()
		if target in edges[current]: #this is a back edge to the starting node
			return True #return True for backedge discovered to the starting node
		seen.add(current) #add to seen ie already discovered, to avoid mistaking a cross edge for a backedge
		
		for child in edges[current]: #access the destination nodes at current index in edges adjacency list
			if child not in seen: #this represents a cross edge, we are only interested in tree edges and back edge
				stack.append(child) #this is a tree edge, ie discovers a new node
	return False  #if stack is empty and we didnt find a back edge, return False

""""Solution one different variable names"""
#O(v+e) time | O(v) space
def cycleInGraph(edges):
	for startNode in range(len(edges)):
		if hasBackEdge(edges, startNode):
			return True
	return False

def hasBackEdge(edges, startNode):
	stack = [startNode]
	seen = set()
	
	while stack:
		currentNode = stack.pop()
		if startNode in edges[currentNode]: # a back edge
			return True
		seen.add(currentNode)
	
		for destinationNode in edges[currentNode]:
			if destinationNode not in seen: #only add tree edges, no back edges.
				stack.append(destinationNode)
	return False


"""Solution three, preferred solution"""
#O(v + e) time | O(v) space
def cycleInGraph(edges):
    numberOfNodes = len(edges) #number of vertices, equal to length of adjacency list
    visited = [False for _ in range(numberOfNodes)] #ds to keep track of visited nodes
    currentlyInStack = [False for _ in range(numberOfNodes)] #ds to keep track of nodes in recursive stack

    for node in range(numberOfNodes):
        #this loop ensures we go through every node in case the graph is disconnected
        if visited[node]:
            continue #if visited skip
        #dfs to find cycles    
        containsCycle = isNodeInCycle(edges, node,visited,currentlyInStack)
        #if a backedge is discovered isNodeInCycle returns True, 
        #backedge exists if a "neighbor" is already in recursive stack, meaning its an ancestor of the node that called it
        if containsCycle:
            return True
    return False


def isNodeInCycle(edges,node,visited,currentlyInStack):
    visited[node] = True #first thing is to mark node as visited
    currentlyInStack[node] = True
    neighbors = edges[node]
    for neighbor in neighbors:
        #if the current descendant is unvisited, make recursive dfs call
        if not visited[neighbor]: 
            containsCycle = isNodeInCycle(edges,neighbor,visited,currentlyInStack)
            if containsCycle:
                return True #if there is a cycle, a descendant's call will be true for containsCycle
        #if visited descendant is still in recursive stack, theres a backedge and a cycle
        elif currentlyInStack[neighbor]: 
            return True #this is where isNodeInCycle returns True, when a backedge is discovered
    #at end of function call, take node off recursive stack
    currentlyInStack[node] = False 
    return False #this is where isNodeInCycle returns False

#O(v+e) time | O(v) space
WHITE,GREY,BLACK = 0,1,2 #white = unvisited, 1= visited still in recursive stack, 2 = visited and finished call
def cycleInGraph(edges):
    numberOfNodes = len(edges)
    colors = [WHITE for _ in range(numberOfNodes)]  #ds to keep track of visited, unvisited, finished

    for node in range(numberOfNodes):
        if colors[node] != WHITE: #we only call dfs on unvisited (white node) ie != WHITE means visited
            continue
        containsCycle = traverseAndColorNodes(node,edges,colors)
        if containsCycle:
            return True
    return False
    
def traverseAndColorNodes(node,edges,colors):
    colors[node] = GREY #global variable
    neighbors = edges[node]

    for neighbor in neighbors:
        neighborColor = colors[neighbor]
        if neighborColor == GREY: #found a backedge, 
            return True
        if neighborColor != WHITE: #if black, skip
            continue
        #if white, call dfs
        containsCycle = traverseAndColorNodes(neighbor,edges,colors)
        if containsCycle:
            return True
    #at the end of function call, mark visited node as black
    colors[node] = BLACK # global variable
    return False



"""Solution three, preferred solution"""
#O(v + e) time | O(v) space
def cycleInGraphVIII(edges):
    numberOfNodes = len(edges) #number of vertices, equal to length of adjacency list
    visited = set() #ds to keep track of visited nodes
    currentlyInStack = set() #ds to keep track of nodes in recursive stack

    for node in range(numberOfNodes):
        #this loop ensures we go through every node in case the graph is disconnected
        if node in visited:
            continue #if visited skip
        #dfs to find cycles    
        containsCycle = isNodeInCycle(edges, node,visited,currentlyInStack)
        #if a backedge is discovered isNodeInCycle returns True, 
        #backedge exists if a "neighbor" is already in recursive stack, meaning its an ancestor of the node that called it
        if containsCycle:
            return True
    return False


def isNodeInCycle(edges,node,visited,currentlyInStack):
    if node in visited:
        return False
    if node in currentlyInStack:
        return True
    currentlyInStack.add(node)
    neighbors = edges[node]
    for neighbor in neighbors:
        #if the current descendant is unvisited, make recursive dfs call
        if neighbor in visited: 
            continue
        if neighbor in currentlyInStack:
            return True
        containsCycle = isNodeInCycle(edges,neighbor,visited,currentlyInStack)
        if containsCycle:
            return True #if there is a cycle, a descendant's call will be true for containsCycle
    currentlyInStack.remove(node) 
    visited.add(node)
    return False #this is where isNodeInCycle returns False


def cycleInGraph(edges):
    nodes = len(edges)

    visited = set()
    visiting = set()
    for node in range(nodes):
        if inCycle(node, edges,visited, visiting):
            return True
    return False

def inCycle(node, edges, visited, visiting):
    if node in visiting:
        return True
    if node in visited:
        return False
    visiting.add(node)
    for neighbor in edges[node]:
        if inCycle(neighbor, edges, visited, visiting):
            return True
    visiting.remove(node)
    visited.add(node)
    


edges = [
    [1, 3],
    [2, 4],
    [],
    [],
    [5],
    []
  ]

print(cycleInGraphVIII(edges))
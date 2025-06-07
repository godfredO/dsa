"""Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether 
these edges make up a valid tree. You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is 
the same as [1, 0] and thus will not appear together in edges.
Example
Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.

Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.

Now a tree is an acyclic connected graph so since we are assured that there will be no duplicate edges (even though this is an undirected 
graph, we dont expect [0,1], [1,0] as is typical of undirected graphs), this question is reduced to whether or not we are able to detect a 
a cycle during a dfs and whether we are able to detect that the graph is disconnected. So using the visited/visiting pattern we are able to
detect loops in directed graphs. How do we detect a disconnected graph and how do we detect cycles in undirected graphs. 

First we will create an undirected (adjacency) graph out of the input, { 0: [1,2,3], 1:  [0,4], 2: [0], 3: [0], 4: [1] } ie an adjacency 
list as a graph. Then we will conduct a dfs. If the graph is connected, after each dfs, the number nodes in the visited set will be equal 
to the total number of nodes, because in a connected graph we are able to reach every node from every other node. Now an edge case, if the 
input is empty, ie an empty graph, then an empty graph does count as a  valid tree. Now even after converting to an adjacency list, we still 
will get a false positive for a loop since by converting to an adjacency list node 1 is in node 0's adjacency list and node 0 is also in node 
1's adjacency list. So to avoid going back to 1 from 0, we will pass in a previous node which is the node we came from again this is an 
undirected graph so detecting a cycle is a little trickier than in a directed graph. So when we call dfs on a node, we add it to the visited 
set then we call dfs on each of its neighbors except prevNode, the node we are coming from. If we reach a node that doesnt have any non-prev 
neighbors, we return True to the prevNode so that the prevNode can look at other neighbors and also and when a node finishes going through its 
non-prev neighbors we also return True to its prevNode so its prevNode continues its dfs also. So what prevNode do we feed the first node we 
start from? We provide an impossible value like -1. So during the dfs, if we ever find a neighbor that is in the visited set, then we found a 
loop  and so not a valid Tree and if after the conclusion of any dfs we check if the visited set size equals number of nodes, if not we no its 
not a valid Tree but if every dfs yields true then we have a valid tree. To the idea of detecting cycles in undirected graph is to pass the
prevNode we just came from and skip that particular node in the list of edges

Thus we can say we use visited/prevNode pattern to detect a loop in an undirected graph. The use of the visted set to detect connectedness is
the foundational idea behind number of connected components where we count 1 connected component every time we start a dfs from an unvisited
node because we know that node will visit every node in this connected circle. The time complexity and space complexity is O(v+e) due to 
recursive stack and adjacency list. 

The following explanation is designed to test for connectivity and cycles in an undirected graph. Suppose the graph is assured connected, then
we can simplify the solution to only test for cycles. To do this we don't need to check if from every node, we are able to reach every other 
node, so we can just initialize the visit set once and skip all visited set in the outer loop.

The most optimized solution uses some very important facts about trees. One a tree of n nodes has n-1 edges. Two a tree has no cycles. And 
finally a tree is connected; meaning we can get to any node from any other node (even for directed graphs we can do the whole parent map thing
in nodesKAway.py question). Now because we are dealing with an undirected graph, the edge [0,1] will be represented in the adjacency graph as
0 : [1], 1 : [0], these means if we start a dfs from 0, we will visit 1 and vice versa. This is important for the connectedness portion. This
means if the graph is undirected and connected, we don't need to repeat the dfs several times. We can do the dfs to test for cycles once and
after that single run, we should have visited every node. If that is so we know the graph is connected because a dfs from every other node will
also visit all the other nodes. So in the optimized version, we first check if the unique edges in our input equals n-1, if not we return False.
If True, we continue and we start a dfs from node 0 and then return if this dfs found a cycle and if the length of the visited set after that 
is equal to n ie if every node was visited.

 """

"""Solution one, creates an undirected graph and tests for connectedness and cycles in an undirected graph."""
#O(n^2) time | O(n) space
def validTree(n, edges):
    if not n: #if None node is passed, return True that graph is valid
        return True
    
    adj = { i:[] for i in range(n)}
    for n1, n2 in edges:  #creating an undirected adjacency graph
        adj[n1].append(n2)  #undirected graph has the same edge in the first and second node's adjacency lists ie no source, destination
        adj[n2].append(n1)  #undirected graph has the same edge in the first and second node's adjacency lists ie no source, destination
    
    
    for nodeIdx in range(n): #outer loop to start dfs #O(n)
        visiting = set()
        #make sure to visit each node once
        if containsCycle(nodeIdx,-1, adj, visiting): #O(n)
            return False
        if len(visiting) != n:
            return False
    return True

def containsCycle(current, prev, adj, visiting): #O(n)
    if current in visiting:
        return True
    visiting.add(current)
    for neighbor in adj[current]:
        if neighbor == prev:
            continue
        if neighbor in visiting:
            return True
        if containsCycle(neighbor, current, adj, visiting):
            return True
    return False


"""Solution two same as first, with the use of the fact that we wont have duplicate edges in our edges list so we check
for exactly n-1 nodes before checking for the existence of cycles."""
# O(n^2) time | O(n) space
def validTree(n, edges):
    if not n: #if None node is passed, return True that graph is valid
        return True
    
    if len(edges) != n - 1:
        return False
    
    adj = { i:[] for i in range(n)}
    for n1, n2 in edges:  #creating an undirected adjacency graph
        adj[n1].append(n2)  #undirected graph has the same edge in the first and second node's adjacency lists ie no source, destination
        adj[n2].append(n1)  #undirected graph has the same edge in the first and second node's adjacency lists ie no source, destination
    
    visiting = set()
    for nodeIdx in range(n): #outer loop to start dfs
        if nodeIdx in visiting:
            continue
        #make sure to visit each node once
        if containsCycle(nodeIdx,-1, adj, visiting):
            return False
    return True

def containsCycle(current, prev, adj, visiting):
    if current in visiting:
        return True
    visiting.add(current)
    for neighbor in adj[current]:
        if neighbor == prev:
            continue
        if neighbor in visiting:
            return True
        if containsCycle(neighbor, current, adj, visiting):
            return True
    return False

"""Further simplification where we only do one dfs check to check for cycles and then check if we didnt find any cycles and if we were
able to visit every single node in the one dfs ie connectedness."""
#O(n) time | O(n) space
def validTreeII(n, edges):
    if not n: #if None node is passed, return True that graph is valid
        return True
    
    if len(edges) != n-1:
        return False
    
    adj = { i:[] for i in range(n)}
    for n1, n2 in edges:  #creating an undirected adjacency graph
        adj[n1].append(n2)  #undirected graph has the same edge in the first and second node's adjacency lists ie no source, destination
        adj[n2].append(n1)  #undirected graph has the same edge in the first and second node's adjacency lists ie no source, destination
    
    visiting = set()

    return not containsCycle(0,-1, adj, visiting) and len(visiting) == n #O(n) time  , space

def containsCycle(current, prev, adj, visiting):
    if current in visiting:
        return True
    visiting.add(current)
    for neighbor in adj[current]:
        if neighbor == prev:
            continue
        if neighbor in visiting:
            return True
        if containsCycle(neighbor, current, adj, visiting):
            return True
    return False

n = 5 
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(validTreeII(n,edges))
"""You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai,bi] indicate that there is an edge 
between ai and bi in the graph. Return the number of connected components in the graph.
Input : n= 5, edges = [[0,1],[1,2],[3,4]] Output = 2 ie 0,1,2 and 3,4 are connected groups
Input : n=5 edges [[0,1], [1,2], [2,3], [3,4]] Output = 1 ie 0,1,2,3,4 are all connected
"""
"""You have a graph and you are supposed to count the number of groups in the graph. So every connected group of components equals one 
group. So the first step is to create a graph of all the components and do a dfs.  To create the graph, we convert the list of edges into 
an adjacency graph. The question just says that [ai,bi] indicates that there is an edge between ai and bi in the graph. Because the question
says an 'edge between' and not 'edge from ai to bi' it means this is an undirected graph. So the adjacency graph we create will be that of
an undirected graph. So the whole idea of connectedness is that if you start a dfs from a connected componenet, you will visit every node 
in the conected group. So if the graph is fully connected, in the very first dfs, we would visit every component, and you would have only 
one group. That is to say, after the very first dfs, every node will be added to the visited set. If the graph is completely disconnected, 
each dfs would only add the start node to the visited set and there will be as many groups as there are nodes in the graph. So keep track of 
what nodes you visit is key to defining connectedness. A fully connected graph will have a full visited set after each dfs. A semi connected 
graph will only add some of the components after each dfs; the components that belong to the same connected group as the start node. Since 
a fully disconnected graph will have a maximum number of groups that equal the number of nodes, we initialize our number of groups as zero,
and whenever we start a dfs with an unvisited start node in the outer loop, we increment the number of groups by 1. Therefore before you start 
the dfs, you check if the startNode is in the visited set. If it is you continue to the top of the loop, since its group would have already 
counted. If its not, you have found the start of one group so you increment your count variable by one and you begin the dfs. In the dfs, we
could implement a stack and visit nodes 'iteratively' or implement the dfs recursively and use the recursive stack. If using the stack 
implementation, you add the current node to the stack and you enter your while loop. If the currentNode is in visited you continue otherwise, 
you mark it as visited. Then you get its neighbors and add all of its unvisited neighbors to the stack. This is what we mean when we say that
the keeping track of visited avoids getting caught in a loop or doing repeated work ie cycling endlessly between connected componenets.

So the idea of the algorithm is basically that whenever you start a dfs from an unvisited node, you have found one group. And the reason for 
this is that, inside the dfs, you mark all the nodes that are part of a group as visited. 
I imagine that if we were to return the max components in a group or something we could take a size variable for the visited set and use this
to subtract from the size of the visited set after each dfs to get the component in the group, do a max comparison with a maxSize variable and
then update the size variable to be the new size of the visited set. Hmm just saying.

The second solution to this question uses an algorithm called union-find and that is described below the first solution's code.

"""

#O(v+e) time | O(v) space
def countComponents(edges, n):
    adj = {i:[] for i in range(n)} #O-indexed

    for n1, n2 in edges: 
        adj[n1].append(n2)   #an undirected graph, add bi to ai's list
        adj[n2].append(n1)   #an undirected graph, add ai to bi's list
    
    groups = 0
    visited = set()
    for nodeIdx in range(n):
        if nodeIdx in visited:
            continue
        groups += 1        # if nodeIdx has not already been visited, its the start of a new connected components 
        dfs(nodeIdx, adj, visited)
    return groups

def dfs(nodeIdx, adj, visited):  #this is a basic dfs to mark all components in a group
    if nodeIdx in visited: #for edge [ai,bi], we visit ai then dfs goes to bi and from visiting bi, dfs is back to visited ai, just return
        return             #don't do repeated work , note that in undirected graphs [ai,bi], [bi,ai] isnt a cycle 
    visited.add(nodeIdx)  #mark current node as visited
    for neighbor in adj[nodeIdx]:  #go through current node's neighbors
        if neighbor in visited: #skip visited nodes
            continue
        dfs(neighbor, adj, visited) #start dfs from each neighbor


"""Using an actual stack for an iterative dfs approach."""
# O(v+e) time | O(v) space
def countComponents(edges, n):
    adj = {i:[] for i in range(n)}

    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)
    
    groups = 0
    visited = set()
    for nodeIdx in range(n):
        if nodeIdx in visited:
            continue
        groups += 1
        dfs(nodeIdx, adj, visited)
    return groups

def dfs(nodeIdx, adj, visited):
    stack = [nodeIdx]
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        for neighbor in adj[current]:
            if neighbor in visited:
                continue
            stack.append(neighbor)



"""Union-Find. In the union find algorithm, instead of transforming the input list of edges into an undirected graph that is represented as
an adjacency hashmap, we convert the list of edges into a forest of trees where one group of connected nodes is basically one forest of trees
and each forest (group) is represented by the root. And so we will have as many roots as there are unique groups in the graph. Starting off we 
know that the maximum number of groups we  can have is equal to the number of nodes if the graph is completely disconnected. So suppose that 
the input is as  follows Input: n=5, edges = [[0,1],[1,2],[3,4]], we convert these into a two forest of trees or groups with one forest having 
root 0 which contains nodes 0,1,2 and another forest with root 3 which contains the nodes 3,4, and so two unique roots, give 2 groups.

Union Find is done using two arrays a parent array and a rank array and each array will store a value for each node in the graph. And we are
using arrays here because our nodes are integers so the index 0 in the parent array will store the parent for node 0, and by parent we really
mean the root of the forest that a node belongs to. And we initialize this array with the index values ie at index 0 we have 0 at index 1 we 
have 1, meaning that we initialize the array with each node as its own parent. The rank array stores the rank of each index node in its tree 
with the root of the tree having the highest rank all the way to the leaf nodes, and rank in this context means the number of nodes in the
(sub) tree rooted at a node. So union-find starts with a bunch of trees ( initially we n trees since each node is its own parent) and as we go 
through the list of edges we merge these trees into forests of trees, by using two functions , the union function and the find functiion. And 
we do this by going through the list of edges and updating the parent of each node and the rank of each node to reflect each node's parent and 
position in the tree it belongs to. So say for edge [0, 1] we start with Parent = [0,1] and Rank = [1,1] and merge these to Parents = [0,0] and 
Rank=[2,1]. So we merge node 0 and node 1's initial trees my making the node 1 the child of node 0 meaning both node 0 and 1 will have node 0 
as parent (root) and the (sub)tree rooted at node 0 will have 2 nodes in it and the (sub)tree rooted at node 1 will have 1 node in it. So how 
exactly does the union and find functions merge all the trees that have edges between them in the list of edges.

So in constructing the merged trees we aim to minimize the length of the tree so that if the next edge were [1,2], we get the parents of
node 1 and node 2 and here the parents will be node 0 and node 2. node 0 will have at this point has a rank of 2 and node 2 has a rank of 1.
Then to minimize the height we actually add node 2 as a child of node 0. So Parents = [0,0,0] and Rank = [3,1,1] so we are effectively, adding 
an edge between node 0 and node 2 in order to yield the forest and since all we care about is grouping the nodes thats okay. So we make the 
lower ranked parent the child of the higher ranked parent and then increment the higher ranked parent's rank with the lower ranked parent's 
rank, to reflect the new number of node's rooted at the highter ranked parent and to minimize the forest of trees. So we have described how 
the union function works. But how does the find function work? This function can be done recursively but the iterative approach is still very 
simple. The aim of this function is to return the parent (root) of the forest a node currently belongs to. So we know that every node in the
forest will differ from the root node except the root node ie the root of a forest is its own parent and the parent of every other node in
the forest. So whenever we find a node that is its parent we know that we have our answer. Now the recursive version simply does that it says
that while the current node is not the same as its parent (as stored in the parent array), call the find function on the whatever is stored
as the parent and when we find its parent, we need to update the parent stored at that node index in the array. In the iterative version, 
we initialize the result variable as the current node, then in a while loop that runs as long as the result variable is not equal to the 
parent of the result variable ie node stored at the result index of the parent array, we first set the parent of result variable to be the
parent of the parent variable ie we set it equal to its grand parent, then we update the result to the updated variable stored. So for 
example, the first time we encounter 0, 1, the will return 0,1 as parents and we set 1's parent as 0, so 0, 0. Then when we encounter 1, 2,
we go find the parent of 1 and we first initialize the result to 1, then while the result is not the same as the stored parent, we read that
the stored parent of 1 is 0 and the stored parent of 0 is 0 so we store the value 0 at index 1 before setting the result as 0. Getting the
parent's parent ensures that we are reading the root node since the forest of trees will generally be one layer deep. This is because the
root node is the only node that will be its parent. Why do we update the stored parent at a node with the parent stored at its parent's node
index. This is because maybe we merged its parent with another tree and so its parent has a new parent that isnt equal to it. So we update
the parent stored at a node with the node stored at its parent before checking if the parent is itself its parent and like was said earlier
a tree is one-layer away from the true parent as stored in its parent. 
Also in the union function, since we minimzie the height of the tree by merging the tree with the lower amount of nodes into the tree with the
higher amount of nodes, what do we do in the case where the ranks are the same. Well in that case , we generally want to make the second parent 
the child of the first parent, so we bundle that logic in with the situation where the first parent's rank is higher.

So how do we use union find to find the number of connected components. We initialize our groups to the number of nodes, ie assuming that each
node is its own parent. Then we have an outer loop, that goes through the list of edges and calls the union function on the nodes of that edge.  
The union function will first call the find function to find the current parents of each node and if the returned parents are different ie do a
a union operation, and we return 1 to be used to decrement the number of groups variable by 1. This is because, we started with two nodes, 
assumed they are their own parent and it turns out they are not and have 1 parent between them. And if the same parent is returned by when 
our union function calls the find function for two nodes, ie the already belong to the same group we return 0 and we decrement the number of 
groups by 0 ie it doesnt really change. 

There are several other depth-first search problems that can actually be solved using union find such as graphValidTree.py, numberOfIslands 
etc. Union find can be used to count connected components and detect a cycle.
"""
def countComponentsII(edges, n):
    parent = [i for i in range(n)]
    rank = [1]*n
    
    groups = n
    for edge in edges:
        n1, n2 = edge
        groups -= union(n1, n2, parent, rank)
    return groups

def find(n, parent):
    res = n
    while res != parent[res]:
        parent[res] = parent[parent[res]] #first update the stored parent of the result variable
        res = parent[res]                 #then update the result variable as the stored parent for the while loop updated comparison
    return res

def union(n1, n2, parent, rank):
    p1, p2 = find(n1, parent), find(n2, parent)

    if p1 == p2:
        return 0  #they have already been grouped and -1 subtracted from both already
    
    if rank[p2] > rank[p1]:
        parent[p1] = p2
        rank[p2] += rank[p1]
    else:
        parent[p2] = p1
        rank[p1] += rank[p2]
    return 1

# edges = [[0,1],[1,2],[2,3],[3,0]]
# print(countComponentsII(edges, 4))
n= 5
edges = [[0,1],[1,2],[3,4]]
print(countComponentsII(edges, n))
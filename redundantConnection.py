""" In this problem, a tree is an undirected graph that is connected and has no cycles. You are given a graph that started as a tree with 
n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an 
edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge 
between nodes ai and bi in the graph. Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are 
multiple answers, return the answer that occurs last in the input.

Input: edges = [[1,2],[1,3],[2,3]]                          Output: [2,3]
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]              Output: [1,4]

Hey another bfs question. So a tree is an acyclic connected graph meaning that there are no cycles and there is a path from any node to 
any other node in the graph. Trees such binary trees and binary search trees are special trees that are directed and rooted in addition
to being acyclic and connected. But in general, a tree is undirected. Check out undirected tree questins twoEdgeConnectedGraph.py and
graphValidTree.py. A tree of n nodes should have n-1 edges but in this question we have 1 additional edge for a total of n edges. So in
fact the key is realising that the additional edge creates a cycle and so this becomes cycle detection with union find. There is an 
approach of using dfs but that is O(n^2) using cycle prevention but we discuss the union find solution first here.

Anyway this question can be solved using union find. This is because the question is basically asking if we can detect a cycle. So as we
go through the edges, the last edge that is deemed a cycle is the answer, so we use the union find solution in graphValidTreeII.py. The
only modificaition we do is that we since are parent and rank arrays are 0-indexed in graphValidTree.py, we cast the 1-indexed nodes in
this question to 0-indexed nodes. Thus as we iterate through edges and unpack edges, ie n1, n2 = edge, we pass in n-1 and n-2 into the
union question. We also initialize a variable additional to an empty list, and whenever the union function returns True for a cycle edge
due to the input nodes having the same returned parent ie no merge needed, we set this additional variable to the edge that returned True
from the union function. Since we iterate through the edges in order, the last edge to return True, we be the last value the additional 
variable is set to. At the end we return whatever edge this additional variable is pointing to. Another option is to just leave index 0
as a buffer in the parents and rank array, then we can just use 1-indexing to solve the question. Also, since we know that there are only
n edges, ie only one cycle edge, the moment we detect a cycle, we can just return that edge. So we can say that if not union(n1,n2):
return edge. This will be solution 3, even though solutions 1,2,3 are literally the same thing, I am just trying to demonstrate the 
thinking behind different incorporating different observations to the most optimized solution even though they are all the same. So when
the question says to return the last cycle edge, that is actually a trick if you use the union find method but maybe useful for dfs method.

The dfs solution is actually more of a cycle prevention than a cycle detection. The basic idea is that we will be creating an adjacency
hashmap for this undirected graph . So we iterate though our edges and unpack each edge into source, destination node. Now before we add
this edge to the list values of the source and destination nodes in the hashmap, we first check if we can reach the destination with a 
dfs from the source node. If we can already reach the destination from the  source the the current edge is a cycle edge and since we know
that there are exactly n nodes and therefore only 1 cycle edge, we can return the first edge for which we can already reach the destination
from the source. If the dfs concludes without reaching destination from source, then the current edge is a tree edge and we add it to the
list values of both source and destination maps in the adjacency hashmap ie undirected edges appear for both nodes. Since we can start dfs 
from the same node for each of its edges, we initialize the visited set anew for each new dfs kinda like solution one of graphValidTree.py
but since this is cycle prevention and not cycle detection, we don't need to use the prevNode. We are just trying to see if a given dfs
eventually reaches destination node or not. The dfs is O(n) and its repeated for each of the n edges so O(n^2) time and O(n) space.

So it seems like basically union-find can be used for cycle detection questions, by realising that if the nodes of an edge already have
the same parent then the current edge must be a cycle edge.
"""

"""Using 0 indexing"""
def findRedundantConnection(edges):
    n = len(edges)
    parent = [i for i in range(n)] 
    rank = [1]*n

    additional = []
    for edge in edges:
        n1, n2 = edge
        if not union(n1-1, n2-1, parent, rank):
            additional = edge
    return additional


def find(n, parent):
    
    if n != parent[n]: #the root node will be the only node that equals its parent
        parent[n] = find(parent[n], parent) #first update the stored value, by recursively calling on the current parent              
    return parent[n]

def union(n1, n2, parent, rank):
    p1, p2 = find(n1, parent), find(n2, parent)

    if p1 == p2:
        return False
    
    if rank[p2] > rank[p1]:
        parent[p1] = parent[p2]
        rank[p2] += rank[p1]
    else:
        parent[p2] = parent[p1]
        rank[p1] += rank[p2]
    return True

"""Using 1-indexing instead of 0-indexing"""
def findRedundantConnection(edges):
    n = len(edges)
    parent = [i for i in range(n+1)] 
    rank = [1]*(n+ 1)

    additional = []
    for edge in edges:
        n1, n2 = edge
        if not union(n1, n2, parent, rank):
            additional = edge
    return additional


def find(n, parent):
    
    if n != parent[n]: #the root node will be the only node that equals its parent
        parent[n] = find(parent[n], parent) #first update the stored value, by recursively calling on the current parent              
    return parent[n]

def union(n1, n2, parent, rank):
    p1, p2 = find(n1, parent), find(n2, parent)

    if p1 == p2:
        return False
    
    if rank[p2] > rank[p1]:
        parent[p1] = parent[p2]
        rank[p2] += rank[p1]
    else:
        parent[p2] = parent[p1]
        rank[p1] += rank[p2]
    return True

"""Returning the first cycle edge because we know there is only 1 cycle edge. T"""
def findRedundantConnection(edges):
    n = len(edges)
    parent = [i for i in range(n+1)] 
    rank = [1]*(n+ 1)

    
    for edge in edges:
        n1, n2 = edge
        if not union(n1, n2, parent, rank):
            return edge


def find(n, parent):
    
    if n != parent[n]: #the root node will be the only node that equals its parent
        parent[n] = find(parent[n], parent) #first update the stored value, by recursively calling on the current parent              
    return parent[n]

def union(n1, n2, parent, rank):
    p1, p2 = find(n1, parent), find(n2, parent)

    if p1 == p2:
        return False
    
    if rank[p2] > rank[p1]:
        parent[p1] = parent[p2]
        rank[p2] += rank[p1]
    else:
        parent[p2] = parent[p1]
        rank[p1] += rank[p2]
    return True



"""DFS solution"""
#O(n^2) time | O(n) space
def findRedundantConnection(edges):
    graph = {i:[] for i in range(1,len(edges)+1)} # nodes are 1-indexed

    for edge in edges:
        source, destination = edge
        visited = set()
        if foundTarget(source, visited, destination, graph):
            return edge
        graph[source].append(destination)
        graph[destination].append(source)

def foundTarget(node, visited, target, graph):
    # if node in visited: #if we travel the other way in an undirected graph to prevNode just return
    #     return False
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor in visited: #skip visited nodes ie going the other way of an undirected edge
            continue
        if neighbor == target:
            return True
        if foundTarget(neighbor, visited, target, graph):
            return True
    return False


edges = [[1,2],[1,3],[2,3]]   
print(findRedundantConnection(edges))
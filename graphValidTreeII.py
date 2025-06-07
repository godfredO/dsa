"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether 
these edges make up a valid tree. You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is 
the same as [1, 0] and thus will not appear together in edges.
Example
Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.

Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.

This question can also be solved by union find algorithm. For a description of union find, see numberOfConnectedComponents.py. Basically any
question that can be solved by dfs and counting components can also be solved by union find. So in order for the list of graph to be a valid
tree, it must be connected and there must be no cycles. For connectedness, there must be exactly n-1 edges, so even for the dfs solutions, we
can first check that the number of distinct edges is not equals n-1. If there are fewer edges than n-1, its definitely not connected but if 
there are more than n-1 distinct edges, there is a cycle, now this optimization can only happen since we are assured of non-duplicate edges.
So if the graph is connected, how do we use union find to detect cycles. Well in the union function, whenver we find an edge and the returned
parents of the nodes of that edge are already equal, meaning they already belong to the same forest of trees, then the current edge will 
constitute a cycle, so we return return False. In this particular question, I will also use the recursive implementation of find function.
"""

def validTree(n, edges):
    parent = [i for i in range(n)]
    rank = [1]*n

    for edge in edges:
        n1, n2 = edge
        if not union(n1, n2, parent, rank):
            return False
    return True


def find(n, parent):
    
    if n != parent[n]:
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

n = 5 
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(validTree(n,edges))

"""There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array 
graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i]. A 
node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a 
terminal node (or another safe node). Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending 
order. The graph may contain self-loops. graph[i] is sorted in a strictly increasing order.

Example 1:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.

Example 2:
Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation: Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
 

So we are given an adjacency list of n nodes, from 0 to n-1 representing a directed graph, where graph[i] is the list of nodes representing
outgoing edges for node i. The adjacency list of each node graph[i] is also sorted in strictly ascending order, strictly here means no nodes
are the same which of course makes sense. We are also told the graph may contain self-loops. And we are told that terminal nodes are nodes
that have no outgoing edges from them. We are told to return a list of safe nodes and a safe node is a node where all paths from its outgoing
edges eventually end up at a terminal node. So right of the bat, this question is giving me topological sort, where the terminal nodes are
like courses / jobs without prerequisites. Now a particular complication to using the standard topological sort algorithm such as the one in 
courseScheduleII.py is that in those question a valid topological sort, if we detected a cycle, we returned an empty array because there was 
no valid topological order. But here, we know that there will likely be cycles, and we don't mind that, we just need to only add the nodes 
that are not involved in cycles to our result array and to ensure that that resulting array is in ascending order. Now the question doesnt 
explicitly say that we will always have terminal nodes, so if we are in the situation where all nodes are involved in cycles, then we would
have an empty array. We will of course need an outer loop for starting dfs, to handle disconnected nodes, since we are not assured that the
nodes will be connected either. 

So one thing to realize about safe nodes is that all the paths starting from their outgoing edges must eventually reach a terminal node. In
otherwords if a node has two outgoing edges and the path from the first edge leads to a terminal node but the second path is involved in a
cycle, then the original node is not a safe node. So in order for us to decide that a node is safe, we have ensure that none of it edges 
lead to a cycle. However the moment we find that one of its edges is involved in a cycle, we can conclude that the node in question is not
a safe node. So the idea here Reverse/ Complement thinking Cycle Detection (topological sort). Yup!!!. If you think about it topological 
sort is just an application of cycle detection. In seeking a valid topological order if we detect a cycle, we return an empty array, if we 
dont we build our valid topological order. In this case if we detect a cycle, we know we have an unsafe node, so if we can collect all of 
our unsafe nodes into a set (for constant-time access and to avoid duplication) we can then loop over our input nodes (ascending order), 
and if a node is in the unsafe nodes set, we do nothing. Otherwise we add it to our output array. Because we loop over the nodes in 
ascending order, we are assured that our output will be in ascending order, and that loop will simply be O(v). The cycle detection /
topological sort dfs will be O(v+e), so our overall time complexity is O(v+e) and a space complexity of O(v). Note bad. Thus the crux
of this elegant solution is the reversing our thinking or thinking 'complementally' (sheiii) to look not for safe nodes but rather for
unsafe nodes, by cleverly modifying an algorithm we alredy know. A description of the actual mechanics of the coded solution is best gained
from reading courseScheduleII.py. 

Below the optimized solution, I also have one that stores the safe status for all nodes, False if a cycle is detected, True is no path
leading from the node is involved in a cycle. Then I loop over the nodes in ascending order and append them if they have a True safe 
status.
"""
#O(v+e) time | O(v) space
def eventualSafeNodes(graph):
    nodes = len(graph)
    unsafeNodes = set()
    visited = set()
    visiting = set()
    for node in range(nodes):
        if node in visited:
            continue
        if containsCycle(node, visited, visiting, graph, unsafeNodes):
            unsafeNodes.add(node)
    
    output = []
    for node in range(nodes):
        if node in unsafeNodes:
            continue
        output.append(node)     
    return output
  
def containsCycle(node, visited, visiting, graph, unsafeNodes):
    if node in visited:
        return False
    if node in visiting:
        unsafeNodes.add(node)
        return True
    visiting.add(node)
    for neighbor in graph[node]:
        if containsCycle(neighbor, visited, visiting, graph, unsafeNodes):
            unsafeNodes.add(node)
            return True
    visiting.remove(node)
    visited.add(node)
    return False

"""Solution II where I store the safe status of each node in a hashtable, and only return the nodes that have a safe status of True """

def eventualSafeNodes(graph):
    nodes = len(graph)
    safeStatus = {}
    visited = set()
    visiting = set()
    for node in range(nodes):
        if node in visited:
            continue
        if containsCycle(node, visited, visiting, graph, safeStatus):
            safeStatus[node] = False
    
    output = []
    for node in range(nodes):
        if safeStatus[node]:
            output.append(node)     
    return output
  
def containsCycle(node, visited, visiting, graph, safeStatus):
    if node in visited:
        safeStatus[node] = True
        return False
    if node in visiting:
        safeStatus[node] = False
        return True
    visiting.add(node)
    for neighbor in graph[node]:
        if containsCycle(neighbor, visited, visiting, graph, safeStatus):
            safeStatus[node] = False
            return True
    visiting.remove(node)
    safeStatus[node] = True
    visited.add(node)
    return False


graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output = [2,4,5,6]
print(eventualSafeNodes(graph))
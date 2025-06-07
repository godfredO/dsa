"""Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains
a value and a list of its neighbors. Now by a clone we mean the copy must have the same values and structure as the input graph, and you 
cant just return the input reference node either as a copy of the graph either. Since the graph is connected, it doesnt matter the node
returned by the copy, if the copy is done right, we can start from any node and reach any node.

So the idea is quite simple, we are going  to use a hashmap to map the old nodes to the new nodes. So starting with the reference node we
create a new node that has the same value as the old node, and then map the old node to its new clone in the hashtable. But this new node 
will not have any neighbors at this point. So we look throughthe old node's neighbors and call the recursive call on each neighbor for that 
neighbor's clone to be created so that it will be mapped to  the new node's neighbors attribute. Now when we call the recursive function on
the old node's first neighbor, we will first check if a clone of any of this neighbor's neighbors exist. This way we would find the first 
clone that was created in the hashmap since this is an undirected graph so if 1 has an edge to 2, then 2 has an edge to 1. So if a neighbor
exists in the hashtable, we add its mapped value aka its clone to the newly created clone's neighbors attribute. If it doesnt we make a
recursive call for the neighbor to create its clone and when that call is created we use the hashmap to add the mapped value of the 
neighbor node aka its clone to the current old node's clone's neighbor attribute. Since we know that the first thing to be done is to 
create a node and map the old node to the new node, we can use the old neighbor as key to access its clone  and add this clone as new
neighbor to the current old neighbor's clone's neighbors attribute. Phew!!! lots of tripping over words but thats recursion for you.
In other words, the recursive function returns a clone, either from the hashmap or after it has filled up the clone's neighbor attribute.

Thus we use depth-first search to clone the input graph. Our base case is that if the old node is in our hashmap, then return its value in
the hashmap ie hashMap[oldNode] aka the mapped clone. Otherwise, we create the clone using the old node's value and add the old node as a 
key to the hashmap pointing to its clone. Then in a for loop, we go through the old node's neighbors and append the result of calling the 
recursive function on each of the old node's neighbors, to its clone's neighbors attribute, since this result will be the clone of those
neighbors. Then outside of the for loop we return the clone, to another recursive call or to the outer loop when everything is done. This way 
there are two situations where a neighbor returns its clone either its already in the hashmap or it just finished populating its clone's 
neighbors attribute. We also have to handle the edge case where the reference node itself is None, where we just return None.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

#O(v+e) time | O(v+e) space
def cloneGraph(node):
    if node is None:
        return None
    oldToNew = {}
    return dfs(node, oldToNew)

def dfs(node, oldToNew):
    if node in oldToNew:
        return oldToNew[node]
    
    clone = Node(node.value)
    oldToNew[node] = clone
    for neighbor in node.neighbors:
        clone.neighbors.append(dfs(neighbor, oldToNew))
    return clone



#O(v+e) time | O(v+e) space - exact same solution as above
def cloneGraph(self, node: 'Node') -> 'Node':
    if node is None:
        return None
    hashMap = {}
    return getDeepCopy(node, hashMap)

    
def getDeepCopy(node, hashMap):
    if node in hashMap:
        return hashMap[node]
    
    hashMap[node] = Node(node.val)
    for neighbor in node.neighbors:
        hashMap[node].neighbors.append(getDeepCopy(neighbor, hashMap))
    return hashMap[node]
    
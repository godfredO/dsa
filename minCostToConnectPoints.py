"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi]. The cost to connect
two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val. 
Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20

This question is an example of a question that uses Prim's algorithm. Basically Prim's and Kruscal's algorithm takes a graph of points with
weighted edges and transforms it into a tree with no cycles and with minimum cumulative weight cost, a concept called minimum spanning trees.
In this question, the edge weight or connection cost between two points in the manhattan distance between them. So we will need to create a
data structure to store edges between points and then implement Prim's algorithm to find the minimum cost to connect all points without cycles.
Prim's like Dijkstra's chooses the unvisited node with minimum edge weight and as such we will need a MinHeap to give logarithm access to this
information.

Prim's algorithm is an algorithm to find minimum spanning trees ie find a way of connecting n nodes with exactly n-1 edges so that there are
no cycles and the total edge weight cost in minimized. Prim's algorithm is a breadth-first search algorithm (again like Dijkstra's) and we 
can start from any node in the graph. We will need a visit set to track visited nodes so as to avoid cycles and a minHeap to access minimum 
edge weights. So when we visit a node we add its frontier, which is basically all the nodes we can reach from and the edge weights associates 
ie all (edgeWeight, destination) to our minHeap ( we will be using heapq instead of implementing a custom minHeap, but you can do that boo! ).
So when we pop from the minHeap, we get the node that can be connected with the minimum possible cost. The we add the frontier of the popped
node to the minHeap. So our start node will be a distance of 0 from itself, we add it to our minHeap, pop it, add it to the visted set and then
add its frontier to the minHeap and repeat the process. As we pop nodes, we will be updating a cost variable to track the total cost to connect 
all nodes, and we increment this variable with the edge weight of the popped node. When do we stop our algorithm? When the length of the visit 
set equals the number of nodes ie we have connected all the nodes. 

The time complexity of O(n^2*log(n)). And the n^2 portion comes from the fact that we could have up to n^2 nodes on the minHeap since every node 
can be connected to every other (using manhattan distance) hence duplicate edgeweights to the same node from different nodes, and of course the 
minHeap will choose the edge weight for any (destination)node that is the minimum regardless of the source of that edge. Now I am using source 
here in the sense of the visited node that added the edge weight to the minHeap (the resulting tree is actually undirected). And of course when 
adding the edge weights from a node, we only add the edge weights to unvisited nodes. Also we could add multiple edges to a node before visit it, 
so if we ever pop an edge to a visited node, we just skip. To generate the edges we use an adjacency graph where the key will be the point index 
in the points array given us. So at index 0, we have the x,y coordinates of point0 and we calculate its edge weights to every other point and 
append (edgeWeight, destinationNode) to point 0's key list value in the adjacency hashmap. And since these are undirected edges, we append the 
same distance to both node's adjacency lists in the adjacency hashmap.

"""
import heapq
def minCostConnectPoints(points):
    numPoints = len(points)
    adj = {i:[] for i in range(numPoints)}

    for i in range(numPoints):
        x1, y1 = points[i]
        for j in range(i+1, numPoints):
            x2, y2 = points[j]
            edgeWeight = abs(x1-x2) + abs(y1-y2)
            adj[i].append([edgeWeight,j])
            adj[j].append([edgeWeight,i])
    
    minHeap = [(0,0)]  #choosing startNode of node 0, distance to itself 0
    heapq.heapify(minHeap)  
    visited= set()
    minCost = 0
    while len(visited) < numPoints:
        distance, node = heapq.heappop(minHeap)
        if node in visited:
            continue
        visited.add(node)
        minCost += distance
        neighbors = adj[node]
        for edgeWeight, destination in neighbors:
            if destination in visited:
                continue
            heapq.heappush(minHeap, (edgeWeight, destination))
    return minCost


points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
print(minCostConnectPoints(points))
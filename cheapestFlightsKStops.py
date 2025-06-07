"""There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates 
that there is a flight from city fromi to city toi with cost pricei. You are also given three integers src, dst, and k, return the cheapest 
price from src to dst with at most k stops. If there is no such route, return -1. There will not be any multiple flights between two cities.

Example 1:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

Example 2:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Example 3:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

The solution here uses the Bellman-Ford algorithm. To review this algorithm, look at detectArbitrage.py. BellmanFord algorithm is a breadth
-first search algorithm. Now the first thing to note is that the question asks to calculate the cheapest price from source to destination 
with at most k stops. And "at most k stops" is the key here. This is because without this restriction, we can model this question as finding
the shortest path or cheapest flight from source to destination, and we already know an algorithm that can determine the shortest distance
from a source node, Dijkstra's algorithm. Now in general the Bellman-Ford algorithm runs in O(E*V) time, but because of the condition to 
visit at most k cities, this solution will take O(E*k) time. We are also assured of no cycles fyi.

So how does the Bellman-Ford algorithm help us to solve this problem? Breadth-first search algorithms start at our node of interest in this
case that will be our source node. During the Bellman-Ford algorithm, for each node, we keep track of the minimum cost it will take to reach 
that node from the source node, using a prices array. And another thing to note is that we are going to be going through k+1 layers of 
breadth-first search (as opposed to the n-1 layers done to detect arbitrages or negative weight cycles in detectArbitrage.py).

So we initialize the prices array with +inf everywhere and update the value for the source node to 0. This is because the cost to reach the
source node from the source node is 0. Now if you look at detectArbitrage.py, you will note that Bellman-Ford algorithm isnt the standard
breadth-first search algorithm, in that for each iteration of the algorithm, we go through the entire graph, and update the distances array
values by first reading the prices value for the startNode of each directed edge, add that to the edgeWeight and update the pricesValue for
the destination if this sum is less than the current priceValue ie minimum comparison of the newPrice vs currentPrice.
 
Now to sort of clearly demarcate the prices after each stop or layer of bfs, we use a temp array which starts out as the prices array. Now
for each edge, we unpack the edge into startNode, endNode, edgeWeight, and we make sure to read the currentPrice for startNode from the
prices array, add it to the edgeWeight as the newPrice to reach endNode. Then to ensure that we get the minimum price for the current 
iteration, we compare the newPrice to the currentPrice for endNode in the temp array and if the newPrice is less, we make an update by 
updating newPrice[destination] inside this temp array. Then when we finish going through all of our edges, we copy the values from this temp 
array into the prices array. This way, at the end of each iteration, the prices array represents those values that use the price of each 
startNode from the previous iteration. And we still make sure to use to use the compare newPrice to temp[endNode] in case another edge in
the current iteration update the value for endNode, but we found a lower price using the current edge but within the same iteration or number
of stops.
Eg If source node is A and destination is C, suppose we have an edge from A to B and B to C, when we update price[B] for edge AB, we 
dont want to read that updated value for B when considering edge BC, as that would actually mean a stop at B ie A>B>C. So we make sure to
read from prices array for startNode of B for edge BC. Now suppose we have another edge A to C, after reading startNode from prices array, we
want to ensure that we compare that to the result of considering edge BC so when comparing the newPrice, we compare it to the value in temp
array which would reflect the update made at edge BC. So we use the temp array to make sure that we only look at k+1 stops, no matter the k 
or the edges in the graph. This style of using a temporary array and copying into a main array is used in the optimal approach of mergeSort.py.

So why do we do k+1 iterations? Say we go from A > B > C we made a 1 stop along the way but we actually made 2 stops in total. So our algorithm 
is looking at the total stops at each iteration so by adding 1, we include the additonal stop to reach our destination which we dont count when 
we talk about stops "along the way". Finally at the end of the algorithm, after copying from temp array to prices array, we return the 
prices[destination], where destination is the one in our question, if prices[destination] is not +inf otherwise ,we return -1, since that 
represents the fact that we are unable to reach destination in at most k stops.
"""
def findCheapestPrices(n, flights, src, dst, k):
    prices = [float("inf")]*n
    prices[src] = 0
    
    for i in range(k+1): #we run the Bellman-Ford algorigthm, relaxEdges() k+1 times
        relaxEdges(flights, prices)
    
    return prices[dst] if prices[dst] != float("inf") else -1


def relaxEdges(flights, prices): #this is the core Bellman-Ford algorithm
    temp = prices[:] #make a copy of prices for the temp array

    for edge in flights:
        start, end, edgeWeight = edge
        newPrice = prices[start] + edgeWeight  #read startNode's value from prices array, to calculate newPrice
        if newPrice < temp[end]: #compare newPrice with endNode's value in temp, to ensure we get the minimum of previous updates
            temp[end] = newPrice #if newPrice is less, make an update
    
    for i in range(len(prices)): #copy from temp array to prices array
        prices[i] = temp[i]


# n = 3
# flights = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0
# dst = 2
# k = 1


# n = 4
# flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
# src = 0
# dst = 3
# k = 1


n = 7
flights = [[0,3,7],[4,5,3],[6,4,8],[2,0,10],[6,5,6],[1,2,2],[2,5,9],[2,6,8],[3,6,3],[4,0,10],[4,6,8],[5,2,6],
            [1,4,3],[4,1,6],[0,5,10],[3,1,5],[4,3,1],[5,4,10],[0,1,6]]
src = 2
dst = 4
k = 1


print(findCheapestPrices(n, flights, src, dst, k))
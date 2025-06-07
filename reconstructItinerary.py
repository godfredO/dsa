"""You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. 
Reconstruct the itinerary in order and return it. All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin 
with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a 
single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"]. You may assume all tickets form at 
least one valid itinerary. You must use all the tickets once and only once.

Constraints: 1 <= tickets.length <= 300 ; tickets[i].length == 2 ; fromi.length == 3 ; toi.length == 3 ; fromi and toi consist of uppercase 
English letters. fromi != toi

Example 1:
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
 
Its important to note the two caveats given; namely that each ticket should be used once and if there are two different valid itineraries, 
we should return the one that comes first in sorted or lexical order. A ticket is the same as edge in the graph so we cannot use the same 
edge twice, but we could still use the same airport twice. Also if we had two valid itinerairies, ['A', 'B'] and ['A', 'C'] we should 
return ['A','B'] since B comes before C in lexical order ie alphabetical order. So obviously we are going to create some sort of directed 
graph from our input, traverse this graph to create valid itineraries and return the itinerary that has the smallest lexical order.

So we build our graph where we map each airport node to a outbound edges representing destinations that can be reached from the airport node
ie with the airport as the source in one of our input edges. Because of the constraint to return the answer that is of smallest lexical order
we will make sure that the list of destinations for each node is in sorted order. And the way we would do that will be to sort the input list
according to the destination airport of each edge ie input.sort(key=lambda x: x[1]) or airports = sorted(inputs, key=lambda x: x[1]) that is 
we will sort the edges by the destination, since the source is going to be the key in the graph. Or really simply sort the input array ie 
ticket.sort() which will sort all the sources in lexical order and for the same source will sort all the destinations in lexical order.This 
way when we create the adjacency list of destinations for each node in the graph, we will automatically be creating each adjacency list in 
sorted order, because the smallest lexical order destinations will come earlier in the sorted input. This step will take O(nlogn), but if we 
naively create the graph and the and then sort each adjacency list of destination, we will be looking at O(n*nlogn). Also, as we go through 
our edges to create the graph, we have to remember to initialize an empty array for the airports. Since we are not given a list of airports, 
ideally we should be initialize an empty array for each souce and edge for each edge, in case there is some destination that is never a 
source. However the solution as described on youtube, neetcode, doesnt add the destinations and this helps write the code cleanly.

So we are going to start a dfs from our "JFK" since the question says we are building the itinerary of a man starting from "JFK", and of 
course as we will be building the itinerary along the way. So the question is basically saying to write an algorithm that starts from "JFK" 
and traverses each edge once. So lets say there are only two nodes, "JFK" and "ATL" and there is a cycle between them ie an edge from "JFK" 
to "ATL" and an edge from "ATL" to "JFK", and this cycle would be tickets representing a return flight ie [["JFK","ATL"],["ATL","JFK"]] is 
the input. So we would start from "JFK", travel along the first edge to "ATL" and then along the second edge back to "JFK" giving an valid
itinerary of ["JFK", "ATL", "JFK"] which is what the two edges represent here. Take a moment here to realize that this is a question where 
the cycles are actually important, and not to be detected or avoided or prevented. Wow za!!!. This question is actually asking to traverse 
cycle(s) starting from a particular node, without getting stuck in the cycle(s) . The airline itineray is just one such application in life 
which is a cycle and where we traverse each edge once ie we dont get stuck in the cycle. You can think of going from home to work and coming 
from work to home as a cycle where you traverse each path once. It is important that we are given the start ie home is "JFK". Note that for 
a valid itineray we dont have to always return to the start node at the end. We just have to traverse exactly len(edges) + 1 nodes without 
traversing each edge twice. Say we have edges [[A,B], [B,C]] then the valid itineray is ['A','B','C'] which is exactly len(edges) + 1 
without returning to start node. So this poses a couple of challenges to the general way of solving graph problems with dfs. First we could 
be visiting the same node multiple times if it is part of multiple cycles. Second how do we know to stop our algorithm. In other words how 
do we keep traversing the graph, in cycles, without ever traversing the same edge twice and know when to stop.

Now to ensure that we don't consider the same edge twice, when we add a destination to the itinerary we will be 'removing' that destination 
from the adjacency list. So in the example above, we start the itinerary from "JFK", add it to our itinerary, the go through its neighbors,
'remove' 'ATL', and start a dfs from 'ATL'. At 'ATL', we add it to our itinerary, go through its neighbors, 'remove' 'JFK' and add it to
our itinerary,  and start a dfs from 'JFK'. When we get to this call, we add 'JFK' to the itinerary, but the neighbors list is empty at this
point so we return on this call, up the recursive tree. So when do we know to stop our algorithm? Whenever the length of the itinerary is
equal to length of the tickets array + 1. This is because we know that each edge in tickets represents two edges and we are assured that all
tickets form at least one valid itinerary. In fact len(itinerary) = len(tickets) + 1 is the definition of a valid itinerary if you think about 
it in real life. So if we ever get to a point where we end up at a node that has no edges and as such dfs will return but the len(itinerary) 
< len(tickets) + 1 we know that is not a valid itinerary. Take the example of three nodes A,B,C , there is edge AB, AC, CA, and we start from 
A, to to B and since B has no edges, the itineray = [A,B] which is less than len(tickest)+ 1  ie 4 so we know that can't be a valid itinerary 
and as such cant be the solution even though its the first in lexical order. But the other itineray where we travel along AC first will yield 
a valid itinerary ie [A,C,A,B] which is len(tickets) + 1. Now this solution involves graph backtracking, like in sudoku.py, wordSearch.py,
boggleBoard.py. We will backtrack when we determine that a path cannot yield a valid itinerary. The time complexity is O(v+e)^2 due to the
backtracking involved. The space complexity is O(v+e) due to the graph and recursive stack. 

This is the first non-board graph problem I can remember, that involves backtracking. We use True / False backtracking to indicate valid / 
invalid path, and since we sorted the inputs, we know that the first valid itinerary is what we should return and so the first time we 
return True we bubble the result up the tree. To make the code cleaner we only add sources to our graph so that if we call the dfs on a node 
that is not a source we know we have an invalid path ie no outgoing edges, so we just return False which will go up the tree and remove 
destination we appended to our result array and re-insert it at the appropriate index in the adjacency list, ie backtracking. Also, we create 
a temporary copy of our adjacency list to loop over, since we will be popping from an index and appending our destinations to our itinerary 
and if a dfs call from a destination returns False, we re-insert it at the index it was previously at. If none of the destination dfs calls 
from a node return a True, then outside of the for loop we return False for that dfs call. This means that each destination call returned 
False, and we have re-inserted the destinations and popped them from the result array. Also, we first seed our result with "JFK" before we 
make the initial dfs call starting from "JFK". If the length of the result array is equal to the number of tickets + 1 we return True, for 
valid path found. Whenever this happens we return results array. Finally, below solution I, we have solution II, where we add a an empty array 
for each airport, and as such we change the first False return condition to when the node has no adjacency list. This works well because even 
in the first solution, if we make a call to an airport where we popped all the destinations, we would still return False outside the for loop. 
So in solution II the return False outside of the for loop would also handle this case too. Not adding destinations to the graph, cleans up 
the solution a bit but not by a lot. This question is thus classic backtracking technique in a graph. I find in backtracking problems, it is 
essential to have the True base case come before the False base case and thus is true in this solution.

"""

def findItinerary(tickets):
    graph = {departure:[] for departure, arrival in tickets}
    numEdges = len(tickets)

    #build directed graph
    tickets.sort(key=lambda x: x[1])
    for ticket in tickets:
        departure, arrival = ticket
        graph[departure].append(arrival)
    
    #make dfs call starting from "JFK"
    result = ["JFK"]
    buildItinerary("JFK", result, numEdges, graph)
    return result

def buildItinerary(node, result, numEdges, graph):
    if len(result)== numEdges + 1:
        return True
    if node not in graph: 
        return False

    temp = graph[node][:]
    for idx in range(len(temp)):
        dst = graph[node].pop(idx)
        result.append(dst)
        if buildItinerary(dst, result, numEdges, graph):
            return True  #the True return statement is used to terminate execution when a valid is found
        #if buildItinerary(dst) returns False
        graph[node].insert(idx, dst)
        result.pop()
#     return False


"""   -------      --------     -------       -------      --------   """

def findItinerary(tickets):
    graph = {}
    numEdges = len(tickets)

    #build directed graph
    tickets.sort(key=lambda x: x[1])
    for ticket in tickets:
        departure, arrival = ticket
        if departure not in graph:
            graph[departure] = []
        if arrival not in graph:
            graph[arrival] = []
        graph[departure].append(arrival)
    
    #make dfs call starting from "JFK"
    result = ["JFK"]
    buildItinerary("JFK", result, numEdges, graph)
    return result

def buildItinerary(node, result, numEdges, graph):
    if len(result)== numEdges + 1:
        return True
    if len(graph[node]) == 0: 
        return False

    temp = graph[node][:]
    for idx in range(len(temp)):
        dst = graph[node].pop(idx)
        result.append(dst)
        if buildItinerary(dst, result, numEdges, graph):
            return True  #the True return statement is used to terminate execution when a valid is found
        #if buildItinerary(dst) returns False
        graph[node].insert(idx, dst)   #backtrack by re-adding the destination
        result.pop()                   #backtrack by removing it from the itinerary 
    return False  #if none of the paths from node lead to True, then return False


tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output = ["JFK","MUC","LHR","SFO","SJC"]
print(findItinerary(tickets))
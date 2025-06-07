"""You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. 
The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning 
one wheel one slot. The lock initially starts at '0000', a string representing the state of the 4 wheels. You are given a list of 
deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable 
to open it. Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns 
required to open the lock, or -1 if it is impossible. Note that target will not be in the list deadends and target and deadends[i] 
consist of digits only.

Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: 
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".

Example 3:
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck.
 

So right of the bat, the minimum total number of turns required to open the lock is giving shortest path of unweighted edges, so bfs
like wordLadder.py. Now take the Example 1 above where the target is "0202" and we could naively say "0000" > "0100" > "0200" > "0201"
at which point we would be stuck because "0201" is a deadend and we cannot get to "0202" this way. Now it is important to notice that we
can turn whichever wheel we want at any time, we don't have to go in order of first - fourth wheel. However when turning a particular 
wheel, it has in order of the turn possibilities, in a wrap around manner ie 0>9>8>7 or O>1>2>3 ie you can decrement or increment in a
wrap around manner. Also turning a particular Also note that target, deadends are all strings.

Now since we can decrement or increment a wheel in wrap around manner, when we start from '0000', first wheel can be incremented to 1 or
decrement in a wrap around manner to 9, giving '1000' or '9000'. And this is the same thing for each of the other wheels, '0100' or '0900', 
'0010' or '0090' , '0001' or '0009'. So starting from '0000', there are 8 possiblities for the first turn ie we choose one wheel and either
decrement or increment it in a wrap around manner and since there are four wheels, we get 8 total possibilities. And whatever we choice we
make the next turn has 8 different possibilities. That is if our first turn is '1000' the next turn could be '0000' or '2000', or '11000' 
or '19000',  '1010'  or '1090', '1001' or '1009' and of these none is the target or in the deadend list. And we can have as many turns 
until we find the target or find a deadend, and each turn will have 8 possiblities to increment or decrement in wrap around manner. Now 
you might have noticed that  if we start from '1000' and choose to decrement the first wheel we go back to the original '0000' so obviously
we dont want to be stuck in a cycle like that, so we will need visited data structure to determine if we have already seen a particular
combination. 

So how would we use bfs to achieve the minimum number of turns to achieve target. Well first realize that if we could use backtracking to
get all the paths that lead to target and return the shortest path. But we are not going to do that here. Instead we can realize that the
initial '000' represents 0 moves; all of its 8 possibilities represent 1 move ; all of their 8 possiblities represent 2 moves. So we can
use bfs to go through our graph (and we will need to represent the decision tree as a graph) and each layer of the graph is 1 move. If we
find the target, we return the minimum number of moves so far, if we find a deadend string, we continue and don't add its neighbors. Now
that I think about it, I wonder how many recursion / backtracking questions may be solved in a bfs style of thinking since backtracking
is a dfs approach. Well the answer to that lies in the time complexity. 

So what is the time complexity of this solution. It is the number of possiblities. To calculate the number of possiblities, we can do that 
with a backtracking (dfs recursion) approach. There are four wheels each wheel has 10 possiblities so 10*10*10*10 ie 10,000 giving a time 
and space complexity (due to the queue) of O(10,000). And this is why backtracking or recursion is preferred to some problems because in 
recursion backtracking, (like in permutations.py), the time and space complexity is determined not by the total number of possibilites but 
rather by the height of the decision tree. However since backtracking in this case would go through each possiblity to collect all paths 
that lead to target and calculate the path with the minimum turns, backtracking (recursion dfs) is a more inefficient than bfs in this case, 
especially with the knowledge that bfs is a shortest path algorithm since it goes one entire layer (or step) at a time. For the visit data 
structure, we will be using a hashset and that will also take the same amount of space O(10,000). And since the lock will always have four
wheels with 10 possibilities each, effectively this is a constant time /space complexity algorithm
 
Also an edge case is if the starting point '0000' is in the deadend list, then there is no path forward so we return -1 immediately. Also, 
how do we decrement and increment in wrap around manner. First off to increment, we do this by adding 1 and modulo dividing the result by 
10 ie (9+1) % 10 = 0. What about decrementing? When we are decrementing a number, we subtract 1, add 10 to the result and then modulo 
divide by 10 ie 0 -1 = -1 + 10 = 9 % 10 = 9, 8-1 = 7 + 10 = 17 % 10 = 7. Now in the coded solution, instead of implementing bfs in the 
style where we take the size of the queue in the beginning and increment it only after we have decremented size to 0, we are going to use
another technique of coding out bfs solutions, a technique used in nodeDepths.py, where we bundle the level/ layer information with the 
node and we add this list to the queue ie queue.append(["0000", 0]) ie 0 depth, 0 level, 0 layer, 0 turns. So even in tree questions we
are either applying dfs or bfs. Also, we will use a set to keep track of visited nodes. So we also use a helper function, you know the
eschewed getNeighbors function although here we call this function  children() to capture the decision tree nature of the actual solution.
To give constant time access to checking if a child node is a deadend, we convert the deadends to a set and use it for our check. Now I 
typically like to be pedagogically verbose, and add visited nodes before looping through the child nodes, skipping visited nodes and adding
only unvisited nodes. But there is a cleaner, adding the unvisited nodes to the  queue and then the visited set and then not doing the 
preceding visited check. In the question shortestBridge.py this is really simplifies the solution, since we start our bfs with visited nodes
from a dfs. Anyway, the point here is that we will be using that type of technique here, in that we will be adding all of the deadends to 
the visit set in addition to the start node, and when we find an unvisited child that is not a deadend, we add it to the queue and then to
the visit set. This way we don't have to do a visit check before looping through the children and we are able to start our algorithm with
pre-visited nodes. By adding all the deadends to the visit set we also dont have to do a deadend check. Again same idea, but the skill in 
coding out the solution is actually pretty essential.
"""

from collections import deque
#O(1) time | O(1) space - O(1) because its always O(10,000)
def openLock(deadends, target):
    if "0000" in deadends:   #edge case
        return -1
    
    queue = deque()
    queue.append(["0000", 0]) #add the start node and the number of turns at the start node to queue
    visit = set(deadends) #visit set to avoid getting stuck in loops, initialized with deadendss list
    visit.add("0000")

    while queue:
        lock, turns = queue.popleft()

        if lock == target: #check if we reached our target
            return turns
        
        for child in children(lock): #go down the eight possiblities from current position
            if child in visit:
                continue
            visit.add(child)
            queue.append([child, turns + 1])

    return -1 #if our bfs while loop terminates without finding target, return -1. 



def children(lock):
    result = []

    for i in range(4):
        digit = str((int(lock[i]) + 1 )% 10)                #increment
        result.append( lock[:i] + digit + lock[i+1:] )

        digit2 = str((int(lock[i]) - 1  + 10)% 10)          #decrements, though in python value - 1 % 10 also gives the correct answer
        result.append( lock[:i] + digit2 + lock[i+1:] )
    
    return result


    
deadends = ["0201","0101","0102","1212","2002"] 
target = "0202"
print(openLock(deadends,target))
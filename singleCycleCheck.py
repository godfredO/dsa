"""This question gives an array of integers where each integer represents a jump of its value in the array. For instance 2 represents a jump
of two indices forward in the array; -3 represents a jump of three indices backward in the array. If a jump spills past the array's bounds, 
it wraps over to the other side. Eg a -1 at index 0 brings us to the last index in the array (thankfully in a array of length 8, -1 % 8 
gives 7 in Python, however when doing wrap arounds with negative numbers you add the length of the array before modulo diving ie (0 -1 + 8)
%8 = 7). The question is to write a function that returns a boolean representing whether the jumps in the array form a single
cycle. A single occurs if, starting at any index in the array and following the jumps, every element in the array is visited exactly once 
before landing back on the starting index.

The first thing to realize is that each index in the array is a node but instead of storing a list like we see in an adjacency list, each
node index stores a jump. We are told that a single cycle exists if after jumps, we arrive back at the starting node index after
exactly len(array) number of jumps. That is what is meant that we visit each index once, since there are len(array) (node) indices in the 
array, so visiting each once before gettting back to the starting node index, means after len(array) jumps we have to be back at the 
starting node index othewise we don't have a single cycle, so that is our first base case. The reason why this simplification works is the
we always make the same jump from each index, and so if two or more nodes are involved in their own little cycle, we will stay in that
cycle so that by len(array) jumps we be on some node in the cycle. So the only caveat is if that cycle involves the start node in which 
case we need to detect if we ever get back to the start node before we have made len(array) jumps.

We keep track of the number of nodes visited and whenever this visited count equals len(array), we check if we are back at the starting 
node index. There is a second base case however, which is that if we visit the starting idx twice before we have done len(array) jumps. So 
in the code there is a while loop which terminates when we have visited exactly len(array) node indices and when the loop terminates we check 
if the current node index is equal to the starting node index, thus we also initialize a starting node index at index 0 and start our current 
node index there too. Inside the loop we check if we have visited the starting index twice before len(array) visits. To avoid confusion with 
the start of the function, we say if visited > 0 and currentIdx == startingIdx , we return False because we dont have a single cycle. Now it 
is worth noting that this is a common pattern, we have a visited count or visited set, we have a check and then we increment or add to the 
visited count or set. After incrementing the visited count we go get the get the destination from the current node index. This is also a 
common pattern, ie we do a check, add to visited, then go get the destination(s) of the current node index. Getting the destination index 
using the jump stored at current node index in the array, is where the wrap around comes in. We add the current node index + jump at current 
node index % len(array) = destination index. The modulo ensures the wra around."""

#O(n) time | O(1) space
def hasSingleCycle(array):
    numElementsVisited = 0
    startingIdx = 0  #our array should have at least one element, so safe to start at 0
    currentIdx = startingIdx

    while numElementsVisited < len(array): #we visit up to n elements
        #if loop is still running(visted < n) and we already at the starting element
        if numElementsVisited > 0 and currentIdx == startingIdx:
            return False
        numElementsVisited += 1
        currentIdx = getNextIdx(currentIdx,array)

    return currentIdx == startingIdx

def getNextIdx(currentIdx,array):
    jump = array[currentIdx]
    #we need to handle wrap-arounds, negative jumps and  huge jumps
    nextIdx = (currentIdx + jump) % len(array) 
    #accessing with a negative number will raise errors(only -1 works in python)
    return nextIdx if nextIdx >=0 else nextIdx + len(array)



"""Same solution as above but shorter and less pedagogical, and also realising that in python -1 % 8 == -1+ 8 % 8"""
#O(n) time | O(1) space
def hasSingleCycle(array):
    startNode = 0
    visited = 0
    currentNode = 0

    while visited < len(array):
        if visited > 0 and currentNode == startNode:
            return False
        currentNode = ( currentNode  + array[currentNode]) % len(array)
        visited += 1
    return currentNode == startNode  

array = [2,3,1,-4,-4,2]
print(hasSingleCycle(array))
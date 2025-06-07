""" You are given the root node of a binary tree, a target value of a node that's contained in the tree, and a positive integer k.
The question asks to write a function that returns the values of all the nodes that are exactly distance k from the node with target
value k. We are also assured that each node's value will be unique in this tree. Two solutions are discussed below. 

The first uses breath first search and the second uses depth first search. In the breadth first search solution, we first create a map 
of {childNodeValue:parentNode} ie mapping child node objects to parent node objects. Then we use this map to grab the target node ie the 
node with target value (unique values) and then starting from this target node we conduct a breadth first search. At each step of the 
breadth first search, going up the tree using the map, left subtree, and right subtree. We start this search knowing that the target is 
a distance of 0 from itself so each call will receive as input, a distance of currentDistance + 1. When the input distance is ever equal 
to k, we append the node's value to an array and we return the array at the end. The distance between two nodes is defined as the number 
of edges that must be traversed to go from one node to the other. In this solution because we go up, left and right at each node, when 
we go up to the parent and the parent goes left/right they would be doing repeated work. So to avoid this we keep a visited / seen set 
so that we avoid repeated calls.

The mapping function works as follows, when we first call this function with the root of the tree and an empty dictionary, we also pass
in a default parent=None. And then we say if the passed node is not None,update the dictionary with dict[node.value] = parent and then
call on the children nodes with node as parents ie rec(node.left,dict,node) and rec(node.right, dict, node). When this mapping is 
returned, how do we use it to find the target node? Well we first handle the edge case that the root value is the target node itself. 
In that case we return the root node. Otherwise with the target value, we access its parent node from the dictionary mapping ie 
dict[targetValue]. Then we say, if parentNode.right and parentNode.right.value == targetNode return parentNode.right else parentNode.left. 
That is since we can't check the value of a None node, we first check that the right child (in this case) is not None before checking if 
it's value is the targetvalue, if it is we return the right child else the left child. The reason why we need to first handle the edge case 
of the the target being the root node is that the root node's parent is None valuein the parentMap and so if we dont handle that edge case, 
we throw an error when we try to get parentNode.right/left. And that is a general specification, before you check for something's value, 
first check that is not None or handle the None case first. So with the target Node and mapping, how do we conduct bfs to discover nods k 
away? We use a queue of course.

So we call the bfs function with the targetNode, the parentMap and k. Now the bfs described here is not necessarily whats in the code
but what is most intuitive and more in line with standard coding practice in other questions. So we initialize an empty visited set,
we add the targetNode with a distance of 0 to the queue and we initialize an empty output array. Inside the while loop, we keep looping 
as long as the while loop is non-empty. We pop, unpack node and distance and the first thing we check if the current node is None, if it
is we continue to the top of the loop. Next thing we check is if the node's value is in the visited set, and if it is we continue to the
top of the loop. If not we add its value to the visited set. Then we check if its distance is equal to k, if it is, we append its value 
to the output array and continue to the top of the loop. If not we collect its neighbors, ie left child, right child, parentNode using 
the parentMap and add each of these to the stack with an updated distance of currentDistance + 1. When the loop terminates we return
the output. The actual logic folloed in the code is slightly different and the different checks are done in different places, but i 
find this to be so much more intutitive. In Python if you initialize a {} with a value single {a}, then Python interprets it as a set, 
otherwise if initialized with no value, just empty {} or a a key:value pair {a:b}, the Python interprets it as a dictionary.

"""

class BinaryTree:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

"""Breadth-first search approach. I start by creating a hashmap of node.value:Parent object. This hashmap will 
help me in expanding in the parent direction during my depth first search. It will also help in easily locating 
the target node object. With the parent mapping done, we locate our target node object and begin a breadth first 
search starting with this node's parent, left child and right child and using the fifo principle of a queue. Note 
that the target nodeis 0 distance from itself. So when we call breadth first search on a node'sneighbors we increase 
the distance by 1. And whenever the incoming node has a distance of k, we return that object together with all the 
nodes currently of the breadth-first search queue because they will also be of k distance. Finally because we explore
the neighbor's of nodes in a breadth-first search we create a seen set to store all the nodes we have already explored
This way when we explore a child from a parent, we dont explore that same parent from the child. """
#O(n) time | O(n) space
def findNodesDistanceK(tree,target,k):
    nodesToParents = {} #dictionary of node.value:Parent object
    populateNodesToParents(tree,nodesToParents) #filll the dictionary with node.value=Parent object
    targetNode = getNodeFromValue(target,tree,nodesToParents) #with dictionary filled, locate the target node object

    return breadthFirstSearchForNodesDistanceK(targetNode,nodesToParents,k) #now do bfs starting from target node 

def breadthFirstSearchForNodesDistanceK(targetNode,nodesToParents,k): #bfs expanding outward from target object
    queue = [(targetNode,0)] #(node object, distance from target node) target node object is 0 distance from itself
    seen = {targetNode.value} #add node's value to seen hashset, in python both sets and dicts us {} diff methods tho
    while len(queue) > 0: #bfs condition, while the queue is non-empty
        currentNode,distanceFromTarget = queue.pop(0) #using list for queue makes this O(n), for O(1) use deque.popleft()

        if distanceFromTarget == k:#first time we get a node with distance k
            nodesDistanceK = [node.value for node, _ in queue] #add the values for the remaining nodes in the queue
            nodesDistanceK.append(currentNode.value) #add the current node's value too
            return nodesDistanceK #return the solution
        
        connectedNodes = [currentNode.left,currentNode.right,nodesToParents[currentNode.value]] #get a list of neighbors
        for  node in connectedNodes:
            if node is None: #if the current connected node is none, ie child of leaf node or parent of root node
                continue # move on to next connected node
            if node.value in seen: #if the current connected node has already been processed, its value will be in seen
                continue #move on to next connected node
            seen.add(node.value) #if current connected node is neither None or previously processed,then add value to set
            queue.append((node,distanceFromTarget + 1)) #then, increment the distance by 1 and add it to the queue

    return [] #if we break out of while loop, then there are no nodes taht are distance k from target node so empty list


def getNodeFromValue(value,tree,nodesToParents):
    if tree.value == value: #edge case, if the root node is the value we're looking for, since root has None parent
        return tree #then no need to go further, we already found our target node object

    #with the exception of the root which has a None parent every node value has a binary tree object parent
    nodeParent = nodesToParents[value] #locate the target node's parent object using the target node value and hashmap
    if nodeParent.left and nodeParent.left.value == value: #if the left child is not None and has the target value
        return nodeParent.left #then target node object is left child of target nodes' parent so return left child
    return nodeParent.right #else target node object must be the right child of the target node's parent


def populateNodesToParents(node,nodesToParents,parent=None):#we pass in an initial value for the root node's parent
    if node: #if node is not None, ie if we call the none child of a leaf node, nothing happens and we're done
        nodesToParents[node.value] = parent #set node.value = Parent object, None for root node
        populateNodesToParents(node.left,nodesToParents,node) #for current node's childiren we set current node as parent
        populateNodesToParents(node.right,nodesToParents,node) #for current node's childiren we set current node as parent



"""Depth first search approach. In this approach we start from the root node and run a dfs looking for the target node
and the distance from target node. The dfs search returns 1 if we are at the target node's parent representing a distance of 1 
from target. We also return -1 if we reach a leaf node without finding the target node. If the dfs reaches the target node, we do a second 
recursive function that finds all the distance k neighbors in the subtree rooted at the target node. If the dfs returns 1 meaning
that we found the parent, then we check if the target node is the right child or the left child. If the target node is the right
child of its parent, we call the second recursive function on the parent's left subtree and vice-versa. Since the dfs of the target's
parent was called by the target's parent's parent we need to return a distance of 2 ie 1+1 so that this parent can continue its dfs until
it either reaches -1 for leaf node child or a distance of k at which point we just append the node k away to our output. Thus depending
on the value of k and the location of the target node in our tree, nodes k away from target could be in the subtree rooted at target, in 
the other child subtree rooted at target's parent, or in the rest of the tree. If both dfs return -1 to a parent it return -1 to its parent.

In the depth-first search solution we use two recursive solutions, the first one returns the distance of a node from the node with target
value and the otherr recursive function takes this distance, keeps incrementing it during each recursive call until the call distance equals 
k. In the first recursive solution, we need to distinguish if we found the target node in a particular subtree or not. That is when a node 
makes a recursive call to left/child, the target node is going to be found in the subtree rooted at only one node. If the target node is in 
the right child the recursive call from that child will eventually return the parent's distance from the target node. But how will the left 
child indicate that it arrived a a leaf node's None child without finding the target node? It will return -1. So -1 is our indicator that the 
target node was not found in a particular subtree. So in the first recursive call the first base case is that if the passed node is None ie 
child of a leaf, we return -1. The other base case is if the passed node is the target we return a distance of 1 to the parent. Then in 
addition the target node will make a call to the second recursive function to search both its left and right subtree for node's k away 
knowing that it is a distance of 0 from itself. Thus the target node makes the unique step of supplying itself as the starting node for the 
second recursive function so that that function will search both of its subtrees. Thus the second function takes this distance, keeps 
incrementing it for each recursive call. When the passed distance is k, this second recursive function adds the node values. After nodes 
distance k away in both subtrees of the target are added, it returns a distance of 1 to its parent. So what does the parent do with this? Well 
if the target node is the left child, it calls the function the recursive function on its right child with a passed distance of 2 and when all
nodes distance k in its right subtree are added to the output and execution is returned to it, it returns a distance of 2 to its parent. And 
what does that parent do with ths information? You guessed it, make a call to the second recursive function on one of its child node, (if it 
received 2 from the left child, it calls on the right child) so that all nodes distance k in that subtree are added with a passed distance of 
currentDistance + 1, then returns to its parent. So after calls are made on children node's, we know one child will return a distance and the 
other will return -1. So if the left returns a distance ( meaning the right returned -1 meaning the target's not in that subtree), we make a 
recursive call to add nodes distance k away in the right subtree, starting with a right child distance of currentDistance + 1 or vice versa if 
the right returns a distance. This way we know that we will never visit any node twice. The target will search both it subtrees, its parent
will search the other subtree and all other parent's will do the same. Finally what happens if a parent receives a distance k. Yep it appends
its value to the output and still calls the second recursive function on the other child node with a distance of k+1 and sends a distance of
k+1 to its parent which will check the other subtree with a distance of k+2 but nothing will be found so no worries there. We allow the 
program to work this way because if we return None the parent will try to add 1 to it and throw and error. But since the second recursive 
function will go until go until leaf nodes, find nothing and return we are covered. Finally in the first recursive function we have a return
-1 at the bottom if both left distance and right distance are -1. This happens for a leaf node since the target is not found in either is
left subtree (None so returned -1) and right subtree (None so returned -1).

"""
#O(n) time | O(n) space
def findNodesDistanceK(tree,target,k):
    nodesDistanceK = [] #output array
    findDistanceFromNodeToTarget(tree,target,k,nodesDistanceK) #find distances and populate nodesDistanceK
    return nodesDistanceK

#some node will receive -1 from both subtrees, ie target is not in either subtree, so we return -1 at the bottom for those 
#some nodes will receive -1 from one subtree and a distance from the other subtree. eg if the target is in the left subtree, it
#will look in both of targets subtrees and return 1 so no need to go look in the left subtree, addNodes() called from target is
#doing that. Instead look in right subtree with distance of leftDistanct + 1 called with right child ie all left and right subtrees that 
# are rooted at the right child, because addNodes() looks in both subtrees, then return leftDistance + 1 to parent. 
#If a call reaches None then the target wasnt found and -1 is how we 
def findDistanceFromNodeToTarget(node,target,k,nodesDistanceK): #returns the distance a node is from target via subtrees
    if node is None:#if at the child of a leaf then we didnt find target in current subtree and - 1 is our indicator
        return -1 #-1 is our indicator that we didnt find the target node in the child subtree of the parent that received - 1

    if node.value == target: #when we call on our target node or if k is 0
        addSubtreeNodesAtDistance(node,0,k,nodesDistanceK) #populate nodesDistanceK with nodes k away in subtree rooted at target 
        return 1 #when target is done populating nodesDistanceK, return a  distance of 1 to target's parent 

    leftDistance = findDistanceFromNodeToTarget(node.left,target,k,nodesDistanceK) #if called from target's parent 1 is received else -1
    rightDistance = findDistanceFromNodeToTarget(node.right,target,k,nodesDistanceK) #if called from target's parent 1 is received else -1

    #so the recursive call on child nodes themselves have a base case here
    if leftDistance == k or rightDistance ==k: #case where either child node returns that current node is k away from target
        nodesDistanceK.append(node.value)   #in which case append their values, one child will return k, the other -1 but doesnt matter
    
    if leftDistance != -1: #if leftDistance is not -1 then the target node is in the left subtree of the node that received not -1 or k = 1
        #if the received value is 1 its target's parent which will send 2 to its parent but both will look in their right subtrees
        addSubtreeNodesAtDistance(node.right,leftDistance+1,k,nodesDistanceK) #in which case look in the right subtree for nodes k away
        return leftDistance + 1 #return updated distance to keep dfs going until leftDistance or rightDistance = k in rest of tree
    
    if rightDistance != 1: #target's parent will receive 1 from target and will send 2 to its parent which will send 3 to its parent till leaf
        addSubtreeNodesAtDistance(node.left,rightDistance+1,k,nodesDistanceK) #since we found target in the right subtree, look in left subtree
        return rightDistance + 1 #and return updated distance to the appropriate node for dfs to continue to search for nodes k away

    return -1 #-1 is our indicator that we didnt find the target node in either child subtree of the parent that received - 1


def addSubtreeNodesAtDistance(node,distance,k,nodesDistanceK): #this function looks in both subtrees of node with increasing distance
    if node is None: #if we call on a right or left child which is None
        return #do nothing and return 
    
    if distance > k: #if the node is further than distance k away, no need in looking, since after reaching k, subsequent calls distance+1
        return
    
    if distance ==k: #if we call on a node k away from target, fill the 
        nodesDistanceK.append(node.value) #append node value
        return
    #by adding base case for distance > k, this only runs when distance < k
    addSubtreeNodesAtDistance(node.left,distance+1,k,nodesDistanceK) #else keep calling on child nodes and incrementing distance
    addSubtreeNodesAtDistance(node.right,distance+1,k,nodesDistanceK) #else keep calling on child nodes and incrementing distance
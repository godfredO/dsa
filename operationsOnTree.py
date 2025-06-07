"""You are given a tree with n nodes numbered from 0 to n - 1 in the form of a parent array parent where parent[i] is the parent of the 
ith node. The root of the tree is node 0, so parent[0] = -1 since it has no parent. You want to design a data structure that allows users 
to lock, unlock, and upgrade nodes in the tree. The data structure should support the following functions:

Lock: Locks the given node for the given user and prevents other users from locking the same node. You may only lock a node using this 
function if the node is unlocked.
Unlock: Unlocks the given node for the given user. You may only unlock a node using this function if it is currently locked by the same user.
Upgrade: Locks the given node for the given user and unlocks all of its descendants regardless of who locked it. You may only upgrade a node 
if all 3 conditions are true:
The node is unlocked, It has at least one locked descendant (by any user), and It does not have any locked ancestors.

Implement the LockingTree class:
LockingTree(int[] parent) initializes the data structure with the parent array.
lock(int num, int user) returns true if it is possible for the user with id user to lock the node num, or false otherwise. If it is 
possible, the node num will become locked by the user with id user.
unlock(int num, int user) returns true if it is possible for the user with id user to unlock the node num, or false otherwise. If it 
is possible, the node num will become unlocked.
upgrade(int num, int user) returns true if it is possible for the user with id user to upgrade the node num, or false otherwise. If it 
is possible, the node num will be upgraded.
 

Example 1:
Input
["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]
[[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]
Output
[null, true, false, true, true, true, false]

Explanation
LockingTree lockingTree = new LockingTree([-1, 0, 0, 1, 1, 2, 2]);
lockingTree.lock(2, 2);    // return true because node 2 is unlocked.
                           // Node 2 will now be locked by user 2.
lockingTree.unlock(2, 3);  // return false because user 3 cannot unlock a node locked by user 2.
lockingTree.unlock(2, 2);  // return true because node 2 was previously locked by user 2.
                           // Node 2 will now be unlocked.
lockingTree.lock(4, 5);    // return true because node 4 is unlocked.
                           // Node 4 will now be locked by user 5.
lockingTree.upgrade(0, 1); // return true because node 0 is unlocked and has at least one locked descendant (node 4).
                           // Node 0 will now be locked by user 1 and node 4 will now be unlocked.
lockingTree.lock(0, 1);    // return false because node 0 is already locked.


So first off, we are given an input array, parent which will be passed into the LockingTree initialization method, and the value at 
index i, represents the parent of node i. We are told there are n nodes, from 0 to n-1 and that the root node will always be 0 and
since it has no parent, parent[0]= -1 otherwise every value in parent is a valid node from 0 to n-1. We are told to write build the
LockingTree structure that has lock, unlock and upgrade methods. The question clearly states the conditions under which a node may
be locked, unlocked and upgraded.

The locking method takes a node and a user and locks the node by user if the node is unlocked. If a locking operation is succesful,
the method should return True. Otherwise if the node is already locked, return False. The unlocking method takes a node and a user
and unlocks the node if the node is locked and the user is the one who locked it, in which case True is returned. If we call unlock
on a node that is not locked or the passed user is not the one who locked the node, then we return False. The upgrade is the more
tricky method. Anyway it takes a node and a user to upgrade means the current node is locked for the given user and then the node's
descendants are unlocked irrespective of who locked it. A node can be upgraded only if it is unlocked, has at least one locked 
descendant and no locked ancestors. Upgrading thus involves going down the tree through a given nodes descendants as well as going
up the tree through a given node's ancestors. Going up is going to be easier because we are given a parents array but going down 
will require that we build our own children data structure.

The lock and unlock methods are constant time , O(1) and the upgrade method is O(n). So in the initialization method we bind the 
parent array to our data strucuture attribute, parent. Then we have a locked attribute which is an array the length of parent and
is initialized with None values signifying that the nodes are not locked initially and when a node is locked, the value at the
node index will be replaced by the id of the user who locked it (yeah user is also an integer). Then we have a child attributes which
is bound to a hashmap that stores a list of child nodes for each node, initialized with empty child arrays and followed by a for 
loop, which loops over the parent array (skipping root node 0) and for each node index, reads its parent from the parent array and
appends the current node index to the parent's child array.

The locking method returns false if the value stored at a node is not None ie the node is already locked. Otherwise, locks by
replacing the None with the user integer and returning True. Using a simple if statement, an integer value for user in locked array
evaluates to True, None evaluates to False. The unlocking function checks if the value stored at the node's position in the locked
array, matches the user; if it doesnt we return False; if it does we reset the node's lock to None and return True. This way if a 
node is unlocked then None will not match the current user so we will still return False.

The upgrade method first uses a while loop and the parent array, to go up the tree up to the root node. So our while loop condition
is that while the currentNode is not equal to -1 ( the root's parent), the we update the current node to the current node's parent,
but before we update currentNode we first check its locked status. If its locked ie the value in the locked array is not None, the
we return False ie checking if the uprade node has a locked ancestor. If we go all the way to the root node without finding a locked
ancestor, then we have to find if the current node has at least 1 locked descendant, and at the same time unlock all of its descendants.

To do this we use breadth-first search. We initialize the queue with the user and initialize our locked variable to count the number of
locked descendants and inside we popleft, if the node is locked, we unlock it, and increment the count. Outside the if statement we
extend the queue with the node's children. At the conclusion of our bfs while loop, we check if the locked count is greater than 0 and
if it is we lock the passed node by the current user and return the result of checking if there were any locked descendants. Thus by
this point the passed node had to be unlocked otherwise we would have returned False in the first while loop. And so even though we 
'unlock' it in the second while loop, we dont affect our logic. 



"""
from collections import deque
class LockingTree:

    def __init__(self, parent):
        self.parent = parent
        self.locked= [None]*len(parent)
        self.child = {i:[] for i in range(len(parent))}
        for i in range(1, len(parent)):
            self.child[parent[i]].append(i) 
        

    def lock(self, num, user) :
        if self.locked[num]:        #if already locked, integer stored here not None
            return False            #return False, locking operation failed
        self.locked[num] = user     #otherwise replace None, with user integer
        return True                 #return True, locking operation successful
        

    def unlock(self, num, user) :
        if self.locked[num] != user:    #locked by diffeent user or currently unlocked
            return False
        self.locked[num] = None
        return True

        

    def upgrade(self, num, user) :
        i = num
        while i != -1:
            if self.locked[i]:
                return False
            i = self.parent[i]
        
        locked, queue = 0, deque([num])
        while queue:
            n = queue.popleft()
            if self.locked[n]:
                self.locked[n] = None
                locked += 1
            queue.extend(self.child[n])

        if locked > 0:
            self.locked[num] = user
        return locked > 0
        
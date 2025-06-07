"""Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are 
performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a 
circle. It is also called "Ring Buffer". One of the benefits of the circular queue is that we can make use of the spaces in front 
of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front 
of the queue. But using the circular queue, we can use the space to store new values.

Implement the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language. 

Example 1:
Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
 
Constraints:
1 <= k <= 1000 ; 0 <= value <= 1000 ; At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.


So the first thing to realize about this class object is that when first instantiate the MyCircularQueue class, we provide
a size, which is the fixed size for the object. So if we call circ = MyCircularQueue(3), this instantiated object can only
have three total objects. When we enQueue(), we add to the end of the object. However when we deQueue(), we remove according
to FIFO principle. Now after we remove the first object added, the next enQueue() call will actually insert the value at the
front of the object since there is space in the front but not at the end. In otherwords, when instantiate with a fixed size
of 3 we are effectively declaring a fixed size array _,_,_ and then say we enQueue() three values 1,2,3 then deQue() one
value _,2,3, according to FIFO, then when we enQueue again 4,2,3. Now with the queue currently at 4,2,3, whenwe call 
deQueue() again, following the FIFO principle, we remove 2, so 4,_,3. The Rear() method should return the value currently 
at the end of the circular queue and the Front() method should return the value currently at the front of the array, and 
this is where the idea of the Ring Buffer comes in. When we had 1,2,3, Front is 1, Rear() is 3, . When we had 4,2,3, Front() 
is 2, Rear() is 4. When the queue is 4,_,3, Front() is 3, Rear is 4. Finally, when we are able to find a position to enQueue()
a value, we return True otherwise if the queue is full we return False. Similarly if there are values on the queue, then when
we call deQueue(), it should return True , otherwise False. Finally, if the queue is empty both Front() and Rear() should 
return -1. Methods isEmpty() and isFull() should return boolean signifying if the queue is empty or full respectively; these
are also helper functions we can use in implementing enQueue() and deQueue() methods.

The solution to this problem involves using two pointers, left and right, two dummy nodes, and a doubly linked list. So
initially our dummy nodes, left and right will point to one another left-><-right. Then when we enQueue() a new node with 
value 1, we insert it in front of right so left-><-1-><-right. When we enQueue another node, we insert before right so 
left-><-1-><-2-><-right. For Front() we return left.next if it exists. For Rear() we return right.prev if it exists. For
deQueue(), we remove left.next if it exists and the reason is that we enQueue by inserting before right, so according to 
FIFO, the oldest node in the list will be left.next ie the Front() node. And of course we will update pointers in sequentially
so that we dont lose references. Finally we keep a space variable which is initialized at k, but is decreased when we add a
node until it reaches 0, and we increase this variable when we remove a node. Thus our isFull() helper method just checks if
this varialbe is 0. We could use this variable for isEmpty(), by checking if it equals the initial k, but here we just check
if the left dummy node's next pointer is still the right dummy node ie no nodes in the middle of the doubly linked list.

"""
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
            
        node = ListNode(value)
        node.next = self.right
        node.prev = self.right.prev

        self.right.prev.next = node
        self.right.prev = node

        self.space -= 1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left

        self.space += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.space == 0

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
"""The question asks to implement an LRU cache class that supports a series of constant-time methods. To do this
we merge the constant time access of the head and tail a doubly linked list, and the constant time access of keys
in a hashtable. We make the head of the doubly linked list always point to the most recently used and the tail 
always point to the least recently used. The doubly linked list node also stores both the key and the value and
each key in the hashtable points to the node object. Whenever a key is accessed it becomes the most recently used
and also the LRU cache evicts a key:node if a new key,value is to be inserted when the LRU is at maximum size"""
class DoublyLinkedListNode:
    def __init__(self,key,value):
        self.key = key #a doubly linked list node for LRU cache has a key,value,next,prev attributes
        self.value = value
        self.prev = None
        self.next = None

    def removeBindings(self): #remove the prev,next bindings on an instane of doubly linked list node (dlln)
        if self.prev is not None: #if node is not head, since the head node doesnt have a prev node
            self.prev.next = self.next #then set the next attribute of the prev node to the current node's next
        if self.next is not None: #if node is not tail, since tail node doesnt have a next node
            self.next.prev = self.prev #then set the prev attribute of the next node to the current node's prev
        self.prev = None #then remove node bindings by overwriting prev and next properties to None
        self.next = None #then remove node bindings by overwriting prev and next properties to None

class DoublyLinkedList:
    def __init__(self):
        self.head = None #the head of the doubly linked list will store the most recently used node in lru cache
        self.tail = None #the tail of the doubly linked list will store the leas
    
    def setHeadTo(self,node):
        if self.head == node: #if the node is already the head of doubly linked list
            return #return because there is nothing to do, since node is already head of linked list
        elif self.head is None: #if the doubly linked list is empty, set node to head 
            self.head = node #set the node as the head of the doubly linked list
            self.tail = node #and set node to tail to satisfy doubly linked list property
        elif self.head == self.tail: #if the doubly linked list has a single node which will be both head and tail
            self.tail.prev = node #then map the prev attribute on tail to node
            self.head = node #then set the node as the head
            self.head.next = self.tail #then set the next property on head to tail
        else: #if the linked list has head and a tail that are separate nodes
            if self.tail == node: #then if the node in question is already in the dll and is the tail of the dll
                self.removeTail() #call this class method to remove the current tail of dll
            node.removeBindings() #remove node bindings. Note this is called on node(dlln) not self(dll)
            self.head.prev = node #after removing bindings, set the current head's prev attribute to point to node
            node.next = self.head #then set node's next attribute to current head
            self.head = node #finally update the doubly linked list head attribute to point to node
    
    def removeTail(self): #the removeTail dll method will be used when evicting lru node and setting its prev as tail
        if self.tail is None: #if the dll is empty, tail will be None so nothing to remove
            return
        if self.tail == self.head: #if the dll has only one node, this node will be both head and list
            self.head = None    #then removing tail means removing head also, set both to None
            self.tail = None    #then removing tail means removing head also, set both to None
            return
        self.tail = self.tail.prev #otherwise set tail's prev node as the new tail
        self.tail.next = None      #then update new tail's next node to point to None, like all tail nodes


class LRUCache:
    def __init__(self,maxSize):
        self.cache = {} #add cache hashtable
        self.maxSize = maxSize or 1 #initialize maximum cache size to passed maxSize or 1 (in case maxSize is 0)
        self.currentSize = 0 #initialize size to 0
        self.listOfMostRecent = DoublyLinkedList() # instantiate a doubly linked list to access head / tail properties
    
    #O(1) time | O(1) space
    def insertKeyValuePair(self,key,value):
        if key not in self.cache: #if key is new, the either currentSize < maxSize or currentSize == maxSize
            if self.currentSize == self.maxSize: #if there is currently no room
                self.evictLeastRecent() #evict least re key:node in cache and node in dll, size effectively same
            else: #if there is room for a new key
                self.currentSize += 1 #then update current size
            self.cache[key] = DoublyLinkedListNode(key,value) #add key:node to cache after, evicting or size update
        else: #if key is already in the cache hashtable
            self.replaceKey(key,value) #then replace the value stored at key in doubly linked list
        self.updateMostRecent(self.cache[key]) #after replacing value or adding new node, make it most recent and head

    #O(1) time | O(1) space
    def getValueFromKey(self,key):
        if key not in self.cache:
            return None
        self.updateMostRecent(self.cache[key]) #accessing the value at key makes it the most recent so make it dll head
        return self.cache[key].value #access key:node and then value attribute of doubly linked list node

    #O(1) time | O(1) space
    def getMostRecentKey(self):#to get the most recent key, just access head of doubly linked list
        if self.listOfMostRecent.head is None: #if the dll is empty , there will be no key property on head node 
            return None #so return None as the most recent key
        return self.listOfMostRecent.head.key #access dll head and then that node's key
        
    #O(1) time | O(1) space
    def replaceKey(self,key,value): 
        if key not in self.cache:#if somehow replaceKey is called on a non-existent key
            raise Exception("The provided keyy isn't in the cache") #raise Exception, cant replace value if key non-existent
        self.cache[key].value = value #just update the value of doubly linked list node pointed to by cache key (hashtable)
    
    def evictLeastRecent(self):#the least recent will be the tail of the doubly linked list
        keyToRemove = self.listOfMostRecent.tail.key #dll node has a key attribute, access the dll tail and then the key
        self.listOfMostRecent.removeTail() #remove the current tail of the dll and make current tail prev the new tail
        del self.cache[keyToRemove] #delete the key from the dictionary
    
    def updateMostRecent(self,node):
        self.listOfMostRecent.setHeadTo(node) #dll head is the most recent node so call setHeadTo dll method on added node
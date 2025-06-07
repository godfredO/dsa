"""Recursive approach"""
"""The main difference between the iterative and recursion versions of the BST class methds start with the fact that in the
iterative version you initialize a currentNode as the object on which the method is called (root node) and at each BST
property comparison (O(log(n)) time as a result), you move the current node reference to the right / left child ie update
the current node reference. In the recursive version you don't initialize a currentNode reference at all and thus there is no
currentNode pointer update step. Instead, after a BST property comparison you call the method on the right / left child node
object as the way to advance down the tree. And finally in order for the result of the method (contains, getMinValue) on 
a left/right child to bubble up the tree to the original call, you need to return the result of the method call on the left/
right child. For the insert method where you want to actually return the root node for example, and thus just call the method 
on the child and after the value is inserted return the object the method was called on. This will return the child node itself
to the parent and the parent will return itself to the grandparent thus each node will return itself up the tree ie execution 
is passed up the tree, until you get to the root node itself where you return the original or root self object. """

"""The remove method first of all can be broken up into find and remove, meaning when asked to remove a node of a certain value, 
(only remove the first instance) of a node with said value, we first have to find it. Any way if the node's value is in the tree, 
we remove it, and if its not the tree we do nothing. So once the node to be removed is found, what do we do? Well, that depends on 
the number of BST node children it has. Is it a leaf node (None values as children), does it have 1 BST node child or does it have 
two BST node children. If the node to be removed is a leaf node, we replace it with None. If it has 1 BST node child we replace it 
with that child. If it has two children, we overwrite the node to be removed value with the value stored in the leftmost node in its 
right subtree to maintain the BST property of the tree before finally replacing the leftmost value in right subtree with None since 
this node will be a leaf. The reason we choose the leftmost node in the right subtree is because it is the only node whose value will 
100% maintain the BST property. This is because that value will be greater than the node's left subtree node value and be less than or 
equal to the right subtree nodes. 

Now replacing a found node actually involves overwriting its parent left/ right child attribute with the appropriate value depending 
on whether the node to be removed is its parent's left/ right child. If it has 1 BST child and 1 None child, depending if it is the 
right child or left child of its parent, we replace the left / right child of its parent with the node's only BST child (left/right). 
If it has 0 BST children, then depending on if it is the right / left child of its parent, we replace the left/right child of its parent,
which ever child it is, with None.

In the code we first use the BST property to find the node, making sure to keep track of the parent node . Once found we handle the case 
of two BST children. This involves calling the getMinValue() method on its right child which will return the leftmost child in the right
subtree and we use the value of the returned node to overwrite the removal node's value attribute, followed by calling the remove method
on the returned node.

Next we handle case where the node to be removed is the root and it 1 or 0 bst child. Since the root has None parent, if it has 1 child we 
make that child the new root by overwriting the root node object's value attribute with the child's values and moving the child node's own 
children up ie making them the left and right children of the 'newly overwritten root node object. The order of operations is essential, 
ovrerwrite value and it the right child is BST child, overwrite value, then update root object left child attribture first before the right 
child attribute. If the left  child is the BST child, overwrite value, then update the root object right child attribute first before the
left child attribute. Hence when parent is None, we handle the case of self.right is not None separate and self.left if is not None 
separate.If the root node has 0 children we just pass, we do nothing otherwise we would lose any reference to the tree.

Finally the general case , a node with a parent and 1 or 0 (ie not the root node) bst child nodes. In either case we overwrite it parent's 
child attribute with the BST child. So we say that if it is the left child of the parent , the overwrite the left attribute of the parent 
with the node's left child if the left child is not None else overwrite the left attribute of the paretnt with the right child. This way if 
the left child is None and the right child is None, the parent's left child attribute will be overwritten with None. If one child is a BST 
child, the left child of the parent will be overwritten with that instead. Then we repeat that same code for if the found node is the right 
child of its parent. At the end of the removal method we return self, which will have the effect of bubbling nodes up the tree until
we get to root node.

In the code, during the find step, we make sure to check if the left/ child is not None before attempting a call from there which will have
the same effect of if the current node's value is equal to the target. That is, if the target value is not in the tree, the remove step is
skipped entirely and the nodes are returned up the tree until the root node is returned. 

 """

class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self,value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
                
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
                
            else:
                self.right.insert(value)
        return self  #return the root node after inserting value
    
    def contains(self,value):
        if value < self.value:
            if self.left is not None:
                return self.left.contains(value)
        elif value > self.value:
            if self.right is not None:
                return self.right.contains(value)
        else: #this else is for when value == self.value
            return True
        return False #return false when value < self.value and self.left is None or when value > self.value and self.right is None
    
    def getMinValue(self):
        if self.left is not None:  #the min Value will be the leftmost leafnode in the tree so keep going left until left child is None
            return self.left.getMinValue()  #if the left child is not None go left
        return self.value #when the leftmost leaf node is reached, return its value
    
    

    def remove(self,value,parentNode=None):
        if value < self.value:
            if self.left is not None:   #if self.left is None, target value node not in tree, so do nothing and return self 
                self.left.remove(value,self)
        elif value > self.value:
            if self.right is not None: #if self.right is None, target value node not in tree, so do nothing and return self 
                self.right.remove(value,self)
        else:
            if self.right is not None and self.left is not None:
                self.value = self.right.getMinValue()
                self.right.remove(self.value,self)
            elif parentNode is None: #root node with 1 or 0 BST child or
                if self.right is not None:  # 1 BST child, the right child of root
                    self.value = self.right.value   #overwrite root object value with BST child value
                    self.left = self.right.left     #update self.left first, not to lose referecence
                    self.right = self.right.right   #update self.right second, not to lose reference
                elif self.left is not None:     # 1 BST child, the left child of root
                    self.value = self.left.value    #overwrite root object value with BST child value
                    self.right = self.left.right    #update self.right first, not to lose referecence
                    self.left = self.left.left      #update self.left second, not to lose reference
                else:                               #root node with 0 BST child
                    pass #do nothing
            elif parentNode.left == self:   #regular node with 1 or 0 BST child, here if node is its parents left child
                parentNode.left = self.left if self.left is not None else self.right
            elif parentNode.right == self:  #regular node with 1 or 0 BST child, here if node is its parents right child
                parentNode.right = self.left if self.left is not None else self.right
        return self   #this will eventually return the root node.
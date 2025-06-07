"""The whole idea is that you create a bst node object, making sure you store a reference to it, such as root
and then on this BST node object you can call methods like insert, contains and delete. So to create
a BST, i first root = BST(1) and then root.insert(2), which will still return the root node, then
root.delete(2). Thus self in these methods refer to the root BST node. """


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    """Iterative Implementation"""
    # Average: O(log(n)) time | O(1) space
    # Worst : O(n) time | O(1) space

    def insert(self, value):
        currentNode = self  # self is a node ie an instance of class BST
        while True:
            if value < currentNode.value:  # if currentNode's value is greater, our new node should be in its left subtree
                if currentNode.left is None:  # if currentNode is a leaf, assign the value to be its left child
                    # create and insert bst() node as left child when final position reached
                    currentNode.left = BST(value)
                    break  # break after successful insertion
                else:
                    currentNode = currentNode.left  # if currentNode's value is lesser, our new node should be in its right subtree
            else:  # if value is less than or equal to
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break  # break after successful insertion
                else:
                    currentNode = currentNode.right
        return self  # return input root node at the end of algorithm

    """Iterative Implementation"""
    # Average: O(log(n)) time | O(1) space
    # Worst : O(n) time | O(1) space

    def contains(self, value):
        currentNode = self
        while currentNode is not None:  # keep traversing until we reach the ennd of the tree ie child of leaf is None
            if value < currentNode.value:  # if value is less than currentNode's value, it must be in the left subtree if its in the tree
                currentNode = currentNode.left
            elif value > currentNode.value:  # if value is greater than currentNode's value, it must be in the right subtree if its in the tree
                currentNode = currentNode.right
            else:  # if value is equal to currentNode's value, we've found the tree contains a node of said value so True
                return True
        return False  # if we reach the end and we dont find the value, tree doesnt contain it so False

    """Iterative Solution"""
    # Average: O(log(n)) time | O(1) space
    # Worst : O(n) time | O(1) space

    # add parentNode as default because ofcurrentNode.right.remove(currentNode.value, currentNode),
    def remove(self, value, parentNode=None):
        currentNode = self

        # First find the node to be removed, keeping track of its parentNode due to reassignment of childNode
        while currentNode is not None:
            # 1.0 Search for the node
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            # 2.0 Node has been found, removal method depends on number of non-null children and whether node is the root
            else:  # value == currentNode.value
                # 2.1 Node has two non-null children, (this includes a root with two non-null children)
                if currentNode.left is not None and currentNode.right is not None:
                    # 2.1.1 Update its value with the smallest value in right subtree
                    # call getMinValue on right child, func gets leftMost node in a subtree
                    currentNode.value = currentNode.right.getMinValue()
                    # 2.1.2 Remove the value's node source
                    currentNode.right.remove(currentNode.value, currentNode)

                # 2.2 Node has one or two null children and is the root node
                elif parentNode is None:    # parentNode was not updated ie root node is to be removed
                    # 2.2.1 Replace root with left child if only left child is not None, moving left child's children up a level
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value  # value update
                        # do in special order, right then left if leftchild of root is not None
                        currentNode.right = currentNode.left.right
                        # assign leftchild last since we are using it to update others; it removes child
                        currentNode.left = currentNode.left.left
                    # 2.2.2 Replace root with right child if only right child is not None, moving right child's children up a level
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        # do in special order, right then left if rightchild of root is not None
                        currentNode.left = currentNode.right.left
                        # assign rightchild last since we are using it to update others; removes child
                        currentNode.right = currentNode.right.right
                    # 2.2.3 if both children of root are null just remove the node or pass, ask interviewer since its the root of a one node tree
                    else:
                        pass  # a single node tree, donn't overwrite root node

                # 2.3 Node has one or two null children and is not the root
                        # 2.3.1 Node is the left child of its parent
                elif parentNode.left == currentNode:  # 1 child node or two null child nodes, where 1 child node is the left child
                    # if it has one child node assign that node to parentnodes left otherwise assign the right value otherwise null value
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:  # 1 child node or two null child nodes, where 1 child node is the right child
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                # After finding value and repalacing it, break
                break
        return self  # return the root node of bst after removal operation is complete

    # function to find the min value in right subtree, called with the right child node
    def getMinValue(self):
        currentNode = self
        # keep moving left until you reach the leaf node which will be the smallest value in the BST
        while currentNode.left is not None:  # need to access value
            currentNode = currentNode.left
        return currentNode.value

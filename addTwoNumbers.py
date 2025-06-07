"""
Tag: Linked List; Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. You may assume the
two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

This question is the same as algoexpert's sum_of_linked_lists.py, so read that first for a deeper explanation. This uses
the standard 2-pointer technique, one for traversing each list. We also create a dummy node to store an access point to
our final head node. The point of this file is to have a filename that matches the leetcode question name.
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = ListNode(0)         # initialize dummy with any val; to track head of output linked list

    current = dummy             # pointer for current node of output linked list; starts at dummy node
    nodeOne = l1                # pointer for list 1
    nodeTwo = l2                # pointer for list 2
    carry = 0                   # carry value initialized at 0

    while nodeOne or nodeTwo or carry:              # while there is a value to add
        valOne = nodeOne.val if nodeOne else 0      # list 1 current node value; initialize at 0
        valTwo = nodeTwo.val if nodeTwo else 0      # list 2 current node value; initialize at 0

        sumOfVals = valOne + valTwo + carry         # current sum of values
        nodeVal = sumOfVals % 10                    # remainder after modulo 10 goes into new node value
        current.next = ListNode(nodeVal)            # add remainder value node to output linked list
        current = current.next                      # update current node to remainder value node

        carry = sumOfVals // 10       # floor operation to get next carry value (maybe 0)

        nodeOne = nodeOne.next if nodeOne else None  # update list one to next /None (while loop)
        nodeTwo = nodeTwo.next if nodeTwo else None  # update list one to next /None (while loop)

    return dummy.next   # the dummy itself is not part of final value; its its next pointer node

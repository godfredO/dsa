"""
Tags: Binary Search; Medium

Binary Search is quite easy to understand conceptually. Basically, it splits a sorted search space into two halves and
only keeps the half that probably has the target and throws away the other half that could not possibly have the answer.
In this manner, we reduce the search space to half the size at every step, until we find the target. Binary Search helps us
reduce the search time from linear O(n) to logarithmic O(log n).

A rather common misunderstanding of binary search is that people often think this technique could only be used in simple
scenario like "Given a sorted array, find a specific value in it". As a matter of fact, it can be applied to much more
complicated situations. Below is a powerful binary search template that can be used to solve a wide range of problems,
simply by making minor changes to the template.

Most Generalized Binary Search
Suppose we have a search space. It could be an array, a range, etc. Usually it's sorted in ascending order. For most tasks,
we can transform the requirement into the following generalized form:

Minimize k , s.t. condition(k) is True

The following code is the most generalized binary search template when a question is posed as the minimum value that returns
True from the condition function:

def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left             # when minimizing return left

- If we wanted to explicitly define the result value, we could write binary search as below

def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    res = some initial value, 0 or "" or whatever
    while left <= right:
        mid = left + (right - left) // 2
        if condition(mid):      # if condition is True
            res = mid
            right = mid - 1     # minimize search space if condition is true
        else:                   # condition is False
            left = mid + 1      # move in the opposite direction
    return res



- Correctly initialize the boundary variables left and right to specify search space. Only one rule: set up the boundary to
include all possible elements;
- Decide return value. Is it return left or return left - 1? Remember this: after exiting the while loop, left is the minimal
k satisfying the condition function;
- Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice. The condition is
trying to find the minimal k that is True for the condition;
- An example of a valid condition the relationship between the root node  and the leftmost node in its right subtree of a binary
search tree. The leftmost node in the right subtree is the minimal node value that is greater than or equal to the root node. So
here the condition would be node.val >= root.val and the leftmost node will be the minimal value for which this is True.
- The key here is that the binary search space has to be in ascending order. And we return the minimal k (value, index, subarray
sum etc) for which some carefully considered condition is True.
- Now why do we move the left and right pointers the way we do. If we find a value that returns True for the condition function,
its either our final answer (the minimal such value) or greater than the final answer. If its greater, then it means our
answer is in the left subarray so we need to move our right pointer, and since the current value, mid , could be the answer we
move our right pointer to mid. On the other hand, if the current mid returns False, we know its not the answer and we know the
answer is greater than the current mid value so we move our left pointer inwards to mid + 1 , no need to include mid.


The following code is the most generalized binary search template when a question is posed as the maximum value that returns
True from the condition function:

def binary_search(array) :
    def condition(value) :
        pass

    left, right = min(search_space), max(search_space) # could be [0, n], [1, n], [1, max(array)], [max(array), sum(array)] etc.

    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            left = mid
        else:
            right = mid -1
    return left

- Check out guessNumberHigherOrLower.py for a question that demonstrates standard, minimum True, maximum True algorithm variants.
- Check out findFirstAndLastPositionOfElementInSortedArray.py for a question that demonstrates min/max/standard algorithm solution.

"""

"""Generalized binary search where we search for the minimal k, that makes some condition True. Here since
the search space is sorted in ascending order. the condition is the minimum index whose value is greater than
 or equal to the target value. At the end we check if the value at left index when the while loop breaks is
 equal to the target value in which case we return the left index, otherwise we return -1.

"""


def binarySearch(array, target):
    left, right = 0, len(array) - 1     # search space bounds

    while left < right:
        mid = left + ((right - left)//2)    # guess
        if condition(array, mid, target):   # condition is true
            right = mid                     # minimize search space
        else:                               # condition is false
            left = mid + 1                  # search in other half
    return left if array[left] == target else -1    # check if left index contains target


def condition(array, i, target):
    return array[i] >= target  # condition: value at guess index is equal or greater than target


array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 22

""""
Tags: Binary Search; Medium

Binary search requires a sorted array, we initialize a startIdx at 0 and endIdx at len(array) -1. Then inside a while loop ,
while start <= endIdx or inside a recursive function, we calculate a middle idx, compare the array value at this middle idx to
the target and if they are equal we return middle idx. if target is less than the middle idx value it means there is no need
looking inside the right subarray, so we move endIdx to middleIdx - 1 and repeat the process. If target is grater than middleIdx
value, we move the startIdx to middleIdx + 1 and repeat the process since we know the target if in the sorted array has to be to
the right of middleIdx. We are able to do this clever movement due to the sorted nature of the input array. Finally if we terminate
the while loop without finding the target value, or hit the base case of the recursive function startIdx > endIdx, we return -1
to signify that the target value is not in the sorted input array. Since we move cleverly through the array, we only ever
traverse at most half the array values ie O(log(n)) and if we implement it recursively, there will be at most log(n) calls on the
recursive call stack before we hit the base case or find the element, giving the recursive implementation a space complexity of
O(log(n)). However if implemented iteratively, binary search takes O(1) space."""

"""Recursive implementation"""
# O(log(n)) time | O(log(n)) space


def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)


def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2
    potentialMatch = array[middle]
    if target == potentialMatch:
        return middle

    elif target < potentialMatch:
        return binarySearchHelper(array, target, left, middle-1)

    else:
        return binarySearchHelper(array, target, middle+1, right)


"""Iterative Solution"""
# O(log(n)) time | O(1) space


def binarySearchHelper(array, target, left, right):
    while left <= right:  # again we need <= instead of = so that we hit the return statement inside this while loop.

        middle = (left + right) // 2
        potentialMatch = array[middle]

        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle - 1
        else:
            left = middle + 1
    return -1


array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
print(binarySearch(array, target))

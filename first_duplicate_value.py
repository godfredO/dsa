"""This question gives an array of integers between 1 and n where n is the length of the array and asks to find the first duplicate value. Now
the first duplicate value is somewhat of a misnomer. It will better be described as the duplicate value with the earliest index. In the first
solution we use a double for loop to find the duplicate of each number and whenever we find a duplicate we store the index. Then we have an
initialized index, (at an impossible index like len(array) that will ease minimum comparisons), and if the current duplicate index is lower,
we update this initialized index. This way, we will store the index of the first duplicate and finally return the value at this index if the
initialized value was updated else -1. The second approach uses a set, loops through the array and stores each value from left to right inside
the set. Before adding the current number however, we check if the current value is in the set. The first time this check yeilds True, it is
because it is the first time we encounter a duplicate value so we return the current loop value. The double loop method is O(n^2) time
complexity and O(1) space, the set method is O(n) time and O(n) space. The final and optimal approach uses the fact that the array can only
contain integers between 1...n where n is the length of the array. If there are no duplicates in the array then each of the distinct possible 
values from 1...n will be present otherwise, not all the distinct possible values will be present in the array because of the duplicates. For
example if n is 5 and there are no duplicates then the array must be some version of  [ 5,2,3,1,4]. However with duplicates the array could
be something like [5,2,3,2,3]. Now the idea is that since an array with no duplicates must contain all the integers 1...n, if we converted
these integers to Python indices by subtracting -1, and then mutate the value at that index by negating it, each value in the array, will
yield a unique Python index before we convert the value at that index to negative. Therefore if the value at a generated Python index is
negative before we have converted it, then it means the current value must be a duplicate and occured earlier in the array, and that earlier
occurrence was the one that converted the value at the generated Python index to negative since all the duplicate values will yield the same
Python index ie value - 1 is the same index for all duplicates and since we are looping from left to right, the first time we see an exisiting
negative number before converting must be the first time we encounter a duplicate in the array. This solution shares similarities with the
set solution, improves the space complexity to O(1) and only works if we are allowed to mutate the input array. Because a particular value,
may have negated by another earlier value that generated its index, we first take the absolute value of each current value before generating
its own Python index."""


"""
Brute force approach using a nested for loop to find duplicate and store 
the index of the duplicate with  lowest index. We first initialize our minimum
index variable to the length of the array which is an impossible index value 
for the list in Python. If at the end of the nested for loops the minimum index variable
is the same as the length of the array we return -1 otherwise we return the value at 
that index.
This solution is O(N^2) time and O(1) space
"""
def firstDuplicateValue(array):
    minDupIndex = len(array)

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                currentDupIndex = j
                if currentDupIndex < minDupIndex:
                    minDupIndex = currentDupIndex
    
    if minDupIndex != len(array):
        return array[minDupIndex]
    else:
        return -1


"""
This solution uses the fact that sets store distinct unordered elements and 
that checking if a value is in a set is a constant time operation.
time complexity O(N), space complexity O(N)
"""

def firstDuplicateValueII(array):
    seen = set()

    for i in range(len(array)):
        if array[i] in seen:
            return array[i]
        seen.add(array[i])
    return -1


"""
This solution is O(N) time and O(1) space. Space complexity
comes from the fact that we are allowed to mutate the input arrays
"""
def firstDuplicateValueIII(array):

    for i in range(len(array)):
        absValue = abs(array[i])
        index = absValue -1
        if array[index] < 0:
            return absValue
        array[index] *= -1 
    return -1




array = [2,1,5,2,3,3,4]
arrayII = [2,1,5,3,3,2,4]
print(firstDuplicateValueIII(arrayII))
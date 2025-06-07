"""This solution uses three key concepts introduuced in the two sum question. sorting, using multiple pointers and complements. We first
start by sorting the array in ascending order. Sorting allows us to move through the array in a meaningful way. Second we use multiple
pointers, a first pointer to choose the first of the triplets, we then calculate the complement of this first number ie the added needed
to reach the target sum with the first number. The uses the second and third pointers to loop through the array again a second time to 
select appropriate addends that sum up to reach the complement of the first number. Alternatively, without calculating the complement
we could sum up the first, second, third number. Anyway, we compare the sum of second and third to the complement of the first or the
sum of the first, second and third and compare to the target sum. These two statements are equivalent since complement = targetSum -
first. Anyway, if the currentSum is equal to complement/targetSum, we append the triplets, increment the second pointer and decrement 
the third pointer to find other elements in the array that add up to the complement of the current outer loop number. If the sum is less 
than complement/ targetSum, we increment the second pointer only to get closer to finding a viable triplet with the current outer loop
number. If the sum is more, we decrement the third pointer to get closer. Thus at each element in the outer for loop we find all pairs
that add to this outer loop number's complement to yield a valid triplet. We keep doing this until the two pointers of the while loop
cross. The loop condition is left < right and not left<= right because we never want to add a single element to itself for complement
of the outer loop number. Also note that while right is always intialized at the end of the array, the left is idx + 1. Thus the outer
loop goes till len(array) -2. This solution effectively superimposes the complement idea on top of the sorted two pointer iteration. 
There is also the brute force approach of using three for loops to choose each number of a possible triplet."""

#O(n^2) time | O(n) space
def threeNumberSum(array, targetSum):
    array.sort()    #O(nlog(n)) time
    triplets = []   #O(n) space
    
    for first in range(len(array)-2): #O(n^2)
        complement = targetSum - array[first]
        second = first + 1
        third = len(array) - 1

        while second < third:
            currentSum = array[second] + array[third]
            if currentSum == complement:
                triplets.append([array[first], array[second], array[third]])
                second += 1
                third -= 1
            elif currentSum < complement:
                second += 1
            elif currentSum > complement:
                third -= 1
    return triplets

def threeNumberSum(array, targetSum):
    """
    Writing a solution using three for loops. Sorting the array first ensures
    that each triplet array is sorted within itself and that the triplet arrays are
    themselves in ascending order with respect to the numbers they hold
    It is also important that k = j + 1 not i+2 which will cause repetition.

    This solution is O(n^3) time and O(n) space
    """
    array.sort() # O(nlogn)
    triplets = []


    # For loop is O(n^3)
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            for k in range(j+1, len(array)):
                if array[i] + array[j] + array[k] == targetSum:
                    # Dynammic array for O(1) appending
                    triplets.append([array[i], array[j], array[k]])
    return triplets
   

def threeNumberSumII(array,targetSum):

    """
    This solution sorts the array and uses two loops to iterate the array, the range of which is up to 
    the third number from the right. There is also a left pointer on the number right next to our current
    iterant and a right pointer at the end of the sorted array. At each step we test if the current sum
    of iterant, left pointer number and right pointer number equals the target sum. If it is, we store the 
    triplet of numbers and shift each pointer in the correct direction. If the current sum is larger than the 
    target sum, we only shift right pointer to minimize the sum. If the current sum is less than the target sum,
    we only shift the left pointer. At the end we return the stored triplets list. 

    This solution is O(n^2) time and O(n) space
    """


    array.sort()       # O(nlogn)
    triplets = []      # O(n) space

    for i in range(len(array)-2):
        l = i + 1
        r = len(array) - 1
        while l < r:
            currentSum = array[i] + array[l] + array[r]
            if currentSum == targetSum:
                triplets.append([array[i], array[l], array[r]])
                l +=1
                r -= 1
            elif currentSum > targetSum:
                r -= 1
            elif currentSum < targetSum:
                l += 1
    return triplets






array = [12,3,1,2,-6,5,-8,6]
targetSum = 0

print(threeNumberSumII(array, targetSum))
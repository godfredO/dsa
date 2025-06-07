"""Amazon Shopping recently launched a new item whose daily customer ratings for n days is represented by the array ratings. They monitor 
these ratings to identify products that are not performing well. Find the number of groups that can be formed consisting of 1 or more 
consecutive days such that the rating continuously decreases over the days. The rating is consecutively decreasing if it has the form: 
r, r-1, r-2, ... and so on, where r is the rating on the first day of the group being considered. Two groups are considered different if
they contain the ratings of different consecutive days. Also note that a group can contain a single element so if the ratings are [1.2],
the number of consecutively decreasing groups are [1] and [2] so the answer is 2. In the ratings array [4,3,5,4,3], there are 9 groups that
are consecutively decreasing ie 5 one day periods [4],[3],[5],[4],[3], 3 two day periods [4,3], [5,4], [4,3] and 1 three day period [5,4,3].
"""

"""So the question is asking about the number of consecutively decreasing subarrays in a ratings array and consecutively decreasing means
if r is the first rating, the second rating is exactly r - 1 and the third rating is r - 2. Thus we are not just talking about decreasing,
but the decrease has to be by 1 as we move in consecutive order. So first the brute force approach where we generate all subarrays of the
ratings array, and test if the subarray is consecutively decreasing. We realize that at the first element in the array, we can have subarrays
of size 1, 2,...n and when we are at the second element in the array, we can have subarrays of size 1,2,.., n-1, and when we are at the
last element in the array, we can have a subarray of size 1 ie the last element only. So to generate all subarrays, we choose the starting
index and a size in the range(1, len(ratings) + 1 - startIdx) ie +1 for range()'s end-exclusivity and minus startIdx to ensure that we have
the only available sizes for any starting index. Now from here there are three different versions of the brute force approach that all have
the same time complexities. In the first we slice the ratings array from startIdx to startIdx + size (end-exclusive) and then feed the sliced 
subarray to a helper function to determine if the sliced subarray is consecutively decreasing. In the second version we dont slice, instead
we generate an endIdx from startIdx and size ie endIdx = startIdx + size - 1 and feed the ratings array, startIdx and endIdx to the helper
function. In the third version, instead of calculating endIdx, we generate endIdx directly with the inner for loop instead of using the 
inner for loop to generate size and calculating endIdx from it. To do this we say endIdx from range(startIdx, len(ratings)). The helper 
function starts from the last element in the sliced array or endIdx for version 2,3 as the currentIdx ie currentIdx = endIdx and checks if 
the preceding element consecutively decreases to the element at currentIdx or not ie array[currentIdx - 1] - 1 != array[currentIdx]. When we 
slice, the while loop condition in the helper function is while currentIdx > 0 and when we pass startIdx, endIdx, the while loop condition in 
the helper function is while currentIdx > startIdx. So if we ever find that array[currentIdx - 1] - 1 != array[currentIdx] we know return 
False to the main function and the main function does nothing if it receives False. However if it is equal ie array[currentIdx -1 
== array[currentIdx], we decrement currentIdx and if we break out of the while loop without hitting the return False statement then it means
the subarray is consecutively decreasing, and we return True outside the while loop. Whenever the main function receives a True, it increments
the numGroups variable and at the end we return this variable. 

The optimal approach is very Kadane's algorithm in nature. We first switch from thinking of all subarrays starting at an index to thinking of 
all subarrays ending at an index. So at say the second element, index 1, there are two subarrays ending at it , one subarray only contains
the second element and the other subarray contains the first and second element. We know that the subarray containing the second element only
qualifies as consecutively decreasing so we know that is at least one group. In fact when considering the subarray ending at any index, we
will always have a subarray of size 1, containing only the element at that index and that subarray is a valid consecutively decreasing 
sub-array. So we know that the numGroups will at least always be equal to the number of elements in the ratings array due to the single 
element subarray ending at any index. So we initialize an array of 1's, the size of the ratings array called numGroups array. Then starting 
from the second element, we say that if the preceding number consecutively decreases to the current number, the we increment the value in the 
numGroups array at the current index with the value stored at the preceding index in the numGroups array. This has the effect of finding all 
sizes of subarrays that are consecutively decreasing and ends at the current index. At the end we sum the numGroups array elements and return.
Thus the optimal approach uses the helper function from the brute force approach without the need of slicing, a startIdx or endIdx. This is
why it is always essential to first write out the brute force approach before optimizing parts of it with observations one step at a time 
till we get to an optimal approach."""

#O(n^3) time | O(1) space
# def countDecreasingRatings(ratings):
    
#     numGroups = 0
#     for startIdx in range(len(ratings)): #O(n)
#         for size in range(1,len(ratings)+ 1 - startIdx): #O(n)
#             slice = ratings[startIdx : startIdx + size] #O(n)
#             if isConsecutivelyDecreasing(slice): #O(n)
#                 print(slice)
#                 numGroups += 1
#     return numGroups

# def isConsecutivelyDecreasing(array): #O(n)
#     iterator = len(array) - 1
#     while iterator > 0:
#         if array[iterator - 1] - 1 != array[iterator]:
#             return False
#         iterator -= 1
#     return True
    
#O(n^3) time | O(1) space
# def countDecreasingRatings(ratings):
#     numGroups = 0
#     for startIdx in range(len(ratings)): #O(n)
#         for size in range(1,len(ratings)+ 1 - startIdx): #O(n)
#             endIdx =  startIdx + size - 1 #O(n)
#             if isConsecutivelyDecreasing(ratings, startIdx, endIdx): #O(n)
#                 numGroups += 1
#     return numGroups

# def isConsecutivelyDecreasing(array, startIdx, endIdx): #O(n)
#     iterator = endIdx
#     while iterator > startIdx:
#         if array[iterator - 1] - 1 != array[iterator]:
#             return False
#         iterator -= 1
#     return True



def countDecreasingRatings(ratings):
    numGroups = 0
    for startIdx in range(len(ratings)): #O(n)
        for endIdx in range(startIdx,len(ratings)): #O(n)
            if isConsecutivelyDecreasing(ratings, startIdx, endIdx): #O(n)
                numGroups += 1
    return numGroups

def isConsecutivelyDecreasing(array, startIdx, endIdx): #O(n)
    iterator = endIdx
    while iterator > startIdx:
        if array[iterator - 1] - 1 != array[iterator]:
            return False
        iterator -= 1
    return True




# def countDecreasingRatings(ratings):
#     array = [1]*len(ratings)

#     for i in range(1, len(ratings)):
#         if ratings[i-1] - 1 == ratings[i]:
#             array[i] += array[i-1]

#     return sum(array)




ratings = [2,1,3]
#ratings = [4,2,3,1]
print(countDecreasingRatings(ratings))
"""Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
The result should also be sorted in ascending order. An integer a is closer to x than an integer b if:
|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 
Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 
Constraints:
1 <= k <= arr.length  ;  1 <= arr.length <= 104  ;  arr is sorted in ascending order  ; -104 <= arr[i], x <= 104

So we have a sorted integer array and a target x and an integer k, and we are to return an array of the k closest
elements in the array to x. There are three solutions discussed below. 

In the first solution, we first find the insert position of the target, the subject of searchInsertPosition.py and
once we have this we can use two pointer, and expand outwards. The insert position is the minimum index whose value
in the array is equal to or greater than the target; if the target is greater than all elements in the array its
insert position will be out of bounds ie len(arr). So finding the insert position can be done with a O(n) function
but since it satisfies the generic binary search monotonicity property of "minimum for which condition is True" we
can use binary search to find the insert position with bounds, 0 and len(arr). Once we have the insert position we
can initialize a left pointer = insertIdx - 1 and a right pointer = insertIdx. Now the remaining step is to expand
outward and include the k closest elements to target inside the left and right pointers. 

Now there are some edge cases; if the target is less than all elements in the array, left = 0 -1 = -1, right = 0. 
Similarly if target is larger than all elements in the array, the left = len(arr) - 1 and right = len(arr). That 
is in the first case, left is out of bounds and in the second case right is out of bonds. We also know that in the 
first case, the k closest elements will be the first k elements so we need to move right pointer k times. In the 
second case, the k closest elements will be the last k elements so we need to move left k times. So we put those 
in there. However in the general case where the insert index of target in somewhere inside the array, we compare 
the left and right pointer values and which ever one is closer to target, we include in the k subarray by advancing 
it. Thus if the right pointer value is closer, we increment right, if left pointer value is closer, we decrement 
left. And each time we increment or decrement a pointer, we increment a step count for a total of k steps. At the 
end of the k stpes, the k closest elements will be arr[left+1:right] (think of if k=1 and left = idx - 1, right = 
idx after 1 step we have the left pointer just before the first closest element and right just outside it). Since 
we take k expansion steps, If we use a linear method to search for target's insert position, this solution is O(n+k) 
but if we use binary search to find the target's insert position, this solution is O(log(n)+k). I have several 
writings of this solution in code.

Whereas solution one, finds the search index of the target and expands outward k times, solution two approaches
the problem as finding the closest subarray of size k to the target. It is cleaner and sort of reverses solution
one. Basically, we start with two pointers, left, right at 0 and len(arr) - 1. Then we compare the values at these
pointer values and whichever is farthest from target, we move in, so this is where we reverse the logic of solution
one. And we keep moving the fartherst pointer inside until the subarray or window between the two pointers is k.
Thus when we get to the end, the left pointer will be pointing to the first element of the k closest elements 
followed by the remaining k closest elements. Thus we can slice the k closest elements using arr[left:left+k]. Note
that since these are slice indices, the element at left+k is actually not a part of the k closest elements but the
outer boundary like the final position of right in solution one. This point is actually pretty useful for the next
solution.

The next solution uses binary search only, and only seeks to find the index of the first element of the k closest
elements, knowing that once we have this element, we can slice it out with arr[left:left+k]. As such, the possibl
search space for the left most index is from 0 to len(arr) - k as from any of these starting positions we can slice
out the k closest elements with arr[left:left+k]. The next thing to realize is that the element at left+k itself is
not a a part of the k closest elements. At this point, we can look at the array as divided into three different 
parts (like in solution one). So if we use binary search to take a guess, arr[mid] and this value is greater than or
equal to the target, then arr[mid+k] is greater than the target and we need to move the search for the left index
to the left subarray so we move the right pointer to mid (since mid can be equal to x and if k=1, x's index is the
left index we are looking for). Similarly, if arr[mid+k] is less than or equal to x, then it means that arr[mid] is
also less than x and we need to move our search to the right subarray by moving the left pointer to mid + 1 (here 
since arr[mid+k] is the one that could be equal to target, we know mid is not in the k closest elements). In the
general case, where arr[mid] and arr[mid+k] either start somewhere or end somewhere in the k closest elements, we
know that the true left idx is the minimum index for which arr[mid] is closer to target than arr[mid+k], so we can
use our standard binary search algorithm. If we start with the actual left idx, construct a window of size k and
slide it forward, we realize that arr[mid] is closet to target than arr[mid+k](which is out of bounds), and our
true left idx is the minimum index for which this is true. Simlarly if we were to start from the same position and
slide to the right, immediately we will realize that the new left is no longer a part of k closest elements, and
is actually farther from the target than the new arr[left+k]. Now, like solution one, there are simpler ways of
writing this solution and more detailed ways. In the more general manner we realize that in the last case, x is
greater than arr[mid] but less than arr[mid + k]. So we can use this to calculate the distances directly to tie
in the other cases.

"""




#Solution One
"""Search Insert Position using Linear Search followed by Linear Two Pointer expansion for k closest elements"""
#O(n + k ) time | O(k) space
def findClosestElements(arr, k, x):
    idx = len(arr)
    for i,num in enumerate(arr):
        if num >= x:
            idx = i
            break

    left = idx - 1
    right = idx
    steps = 0
    return getKClosest(arr, k, left, right, steps)

#Explicit writing of two pointer expansion
def getKClosest(arr, k, left, right, steps,x):
    while steps < k:
        if left < 0:
            right += 1
        elif right == len(arr) :
            left -= 1
        else:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:      #abs(arr[left] - x) > abs(arr[right] - x)
                right += 1
        steps += 1
    return arr[left + 1 : right]

#Cleaner re-writing of getKClosest, where right move conditions are written together
def getKClosest(arr, k, left, right, steps):
    while steps < k:
        if left < 0 or (right < len(arr) and abs(arr[left]-x) > abs(arr[right] - x)):
            right += 1
        else :
            left -= 1
        steps += 1
    return arr[left + 1 : right]

#Cleaner re-writing of getKClosest, where left move conditions are written together
def getKClosest(arr, k, left, right, steps):
    while steps < k:
        if right == len(arr) or (left >= 0 and abs(arr[left] - x) <= abs(arr[right] - x)):
            left -= 1
        else :
            right += 1
        steps += 1
    return arr[left + 1 : right]


"""Search Insert Position using Binary Search followed by Linear Two Pointer Expansion for k closest elements"""

#O(log(n) + k) time | O(k) space
def findClosestElements(arr, k, x):
    idx = searchInsert(arr,x)

    left = idx - 1
    right = idx
    steps = 0
    while steps < k:
        if left < 0:
            right += 1
        elif right == len(arr) :
            left -= 1
        else: #left >= 0 and right < len(nums)
            if abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:      #abs(arr[left] - x) > abs(arr[right] - x)
                right += 1

        steps += 1
    return arr[left + 1 : right]

def searchInsert(nums, target) :
    left, right = 0, len(nums)
        
    while left < right:
        mid = left + (right - left) // 2
            
        if condition(nums, mid, target):
            right = mid
        else:
            left = mid + 1
    return left

def condition(nums, mid, target):
    return nums[mid] >= target


"""Solution Two"""
#O(n) time | O(k) space
def findClosestElements(arr, k , x ) :
    left , right = 0, len(arr) - 1
        
    while right + 1 - left > k:
        if abs(arr[left] - x) <= abs(arr[right] - x):
            right -= 1
        else:
            left += 1
    return arr[left:left+k]


"""Solution Three"""
#O(log(n)) time | O(k) space
def findClosestElements(arr, k, x) :
    left , right = 0, len(arr) - k
        
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] >= x:
            right = mid
        elif arr[mid+k] <= x:
            left = mid + 1
        else:
            if abs(arr[mid] - x) <= abs(arr[mid+k] - x):
                right = mid
            else:
                left = mid + 1
    return arr[left:left+k]


#Using mathematical thinking to combine the conditions for moving right and left pointers
#O(log(n)) time | O(k) space
def findClosestElements(arr, k, x):
    left , right = 0, len(arr) - k
        
    while left < right:
        mid = left + (right - left) // 2
        if x - arr[mid] <= arr[mid+k] - x:
            right = mid
        else:
            left = mid + 1
    return arr[left:left+k]
    
        
    


arr = [1,2,3,3,3,4,5]
x = 3
k= 3
print(findClosestElements(arr, k, x))
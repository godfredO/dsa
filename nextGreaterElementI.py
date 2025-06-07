"""The next greater element of some element x in an array is the first greater element that is to the right of x in the 
same array. You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of 
nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1. Return an array ans of length 
nums1.length such that ans[i] is the next greater element as described above.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 
Constraints:
1 <= nums1.length <= nums2.length <= 1000 ; 0 <= nums1[i], nums2[i] <= 104 ; All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.

Reading and understanding monotonicStacks.py is a prerequisite for solving this problem. Basically this question is based 
on the next greater element algorithm described in monotonicStacks.py with the added twist that we are to determine the next
greater element for nums2 but only return a result array for those elements in nums2 that are in nums1, since we are told that 
nums1 is a subset of nums2. In otherwords, we will need to check if a value in nums2 occurs in nums1 and for constant time 
checks we use a hashmap. In otherwords, when we find the next greater elements for nums2, we store the answers not in an array, 
but rather in a hashmap. Then, we can go through nums1, and update the actual result array with the values in the hashmap. And 
this works because we are assured that each integer in nums1 and nums2 are unique. The other thing is to realize that we store 
the unique integers as the keys and values in the hashmap instead of using the indices as is described in the next greater 
element algorithm of monotonicStacks.py. Another thing to realize is that unlike the algorithm in monotonicStacks.py where we
store -1 for each value that doesnt have a next greater element, here if a value in nums2 doesnt have a next greater element
we don't add it to the hashmap. This means that when we initialize our final answer, we initialize it with -1 and so that so
that if a value in nums1 isnt in the hashmap, its index in the final array is -1 and we only update the indices whose nums1
element appears as a key in the hashmap and we update with the value of that key.

This is a linear time and space algorithm O(n+m), where n is the length of nums1 and m is the length of nums2. The final answer 
will have the same length as nums1 and the hashmap will have the same size as nums2.

"""
#O(n +m) time | space
def nextGreaterElement(nums1, nums2) :
    nextHash = {}
    stack = []
        
    for num in nums2:
        while stack and stack[-1] < num:
            peek = stack.pop()
            nextHash[peek] = num
        stack.append(num)
        
        
    ans = [-1]*len(nums1)
    for i in range(len(nums1)):
        num = nums1[i]
        if num in nextHash:
            ans[i] = nextHash[num] 
    return ans
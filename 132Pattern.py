"""
Tag: Stack, Monotonic Stack, Previous greater, Medium

Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and
nums[k] such that i < j < k and nums[i] < nums[k] < nums[j]. Return true if there is a 132 pattern in nums,
otherwise, return false.

Example 1:
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].


Constraints:
n == nums.length  ; 1 <= n <= 2 * 105 ; -109 <= nums[i] <= 109 ;


The brute force solution is to consider every triplet (i,j,k) and check if the corresponding numbers satisfy the 132
criteria. If any such triplet is found, we can return a True value. If no such triplet is found, we need to return a
False value. This brute force approach is O(n^3) time | O(1) space. When choosing the first index, we loop from index
0 up to but not including len(nums) - 2 (end-exlusive). When choosing the second index, we loop from index
firstIdx + 1 up to but not including len(nums) - 1 (end-exlusive). When choosing the third index, we loop from index
secondIdx + 1 until the end of the array, len(nums).

The stack solution makes some important observations about the nature of the solution. This is a solution that depends
on examples. A valid solution, is a subsequence that posesses the 132 pattern. If i<j<k are indices, arr[i] < arr[k]
< arr[j] , there are three indices and corresponding values. So something like say well arr [1,3,2] is used, we can
ask ourselves how we may characterize the relationships between the indexes values  arr[i] < arr[k] < arr[j]
given we know that i<j<k are indices.

First we can say that since j<k and arr[k]<arr[j], that at index k, the value at index j is the previous greater element.
This is because index j comes before index k but the value at index j is greater than the value at index k. Then we look
at index i, we realize that i<j, arr[i] < arr[j] and i<k, arr[i] < arr[k]. Now its not sufficient for the value at index
i to be smaller than both j and k; it has to be the previous smaller both j and k. This is because the previous smaller
is the first number to the left of an index that is smaller than the value at that index. So in [0,1,2], the previous
smaller is [null,0,1]. See that 0 is not the previous greater of the value 2 because the first value to the left of 2
that is less than 2, is 1. Meaning, you can have a situation where arr[i] is smaller than both arr[j] and arr[k], but
its not a 132 pattern, because arr[j] is the smaller or equal to arr[k]. However, if arr[i] is the absolute minimum
of i,j,k and arr[k] is the previous greater of arr[k], we have a  valid 132 pattern. Both assertions have to hold
since its possible to have [0,1,1] where arr[i] is the absolute minimum of i,j,k but arr[j] is not previous greater
of k.


Otherwise stated, we have a 132 pattern, for indices i,j,k if j is the previous greater of k, and i is the absolute
minimum of both j and k. However we can say that i is the absolute minimum value seen by the time we get to k, and
j is the previous greater of k. In otherwords, we need to know for each index k, the absolute minimum i seen so far,
and j the previous greater of k. This solution is thus from the viewpoint of index k.

So in solution one we use a two-step approach involving dynamic programming (DP) and a stack. First, for every j we
find the absolute minimum for the subarray ending at that j. Then, using a stack, for every k, we find a previous
greater j, and when we do, we compare the value at k to the absolute minimum for the subarray ending at that j, thus
ensuring that i is indeed the absolute minimum of k too. So we know that the absolute minimum at index 0 is the value
at index 0. Otherwise the absolute minimum for the subarray ending at any index is the minimum of the current number
and the absolute minimum of the subarray ending at the preceding index. So if for any k, we find a previous greater
element j, and for j, we find that its minimum so far by index i, is also less than the value at index k, we have a
valid 132 pattern. This solution can be done by doing a first pass using the dyanammic programming technique to store
the minimum for the subarray ending at each index, ie minimize index i for each value at index j. This is because value
at index i only really be the previous smaller of values at index j, k. Value at i can also be characterized as the
absolute minimum of the values i,j,k. So when the stack is used to find j from the perspective of k, we can use the
dynamic programming solution to compare the absolute minimum at j to the value at the current k.

Alternatively, the stack could store a pair of values, an index j and the absolute minimum for the subarray ending at
that index j. So when we iterate through the array, for each possible index k, we pop all previous lists whose index 0
(k value) is less than or equal, until the previous greater of our current index k is the value at index 0 of the peek
value list of the stack. Then we can check if the current index k is also greater than the value at index 1 of the peek
value list, if so we return True. If not, we update the absolute minimum before pushing a list of the current loop
index and the updated absolute minimum onto the stack. The absolute minimum being the minimum of the value at index k
and the previous absolute minimum at index j.

Now there is another way of finding previous greater. In fact in monotonicStacks.py, we hinted at this when describing the
previous greater algorithm. Basically, if we loop backwards, ie from right to left, we can apply the same algorithm as for
next greater to get the previous greater. That is we add indices from right to left and if the value at the top of the
stack is less than the current, the current value is the previous greater of the value on top of the stack ie the stack
peek is index k, and the current value is index j. So we pop and store a reference to our index k value, keeping the values
on the stack in non-increasing order and by so doing we maximize index k as much as possible. That is to say if index i is 1,
index k is 8, index j could be 7,6,5,4,3,2 but to make sure our algorithm works we want to store a reference to the maximum
value. Then like the previous solution if we find an index i which is also less than index k, since we know that index k is
less than index j, then index i must also be less than index j, so we have a valid 132 pattern. So we use a reversed previous
greater to store a reference to index k, and if we find an index i which is less than the stored index k we return True
otherwise we return False. To ensure that we dont return a premature True, we initialize our index k at -inf so that we cant
return True until we have updated index k for some index j and found a valid index i which is less than index k.
"""


"""Brute force approach"""
# O(n^3) time | O(1) space


def find132pattern(nums):
    for i in range(len(nums) - 2):  # possible indices of first index; up to last but two (end-excluded)
        for j in range(i + 1, len(nums) - 1):  # possible indices of second index; up to last but one (end-excluded)
            for k in range(j + 1, len(nums)):  # possible indices of third index; up to last (end-excluded)
                if nums[i] < nums[k] < nums[j]:
                    return True
    return False


"""Optimized Solutions"""


# O(n) time | O(n) space


def find132pattern(nums):     # this solution uses DP for abs mins and stack for prev greater

    minimumsIdxs = [0]*len(nums)        # minimum of subarray ending at index 0 is value at index 0
    for j in range(1, len(nums)):       # find the absolute minimum of subarray ending at remaining indices
        minimumsIdxs[j] = j if nums[j] < nums[minimumsIdxs[j-1]] else minimumsIdxs[j-1]  # update

    stack = []                          # the stack like minimumsIdx stores index values only
    for k in range(len(nums)):          # solution from the pov of index k (ijk)
        while stack and nums[stack[-1]] <= nums[k]:  # pop till stack peek is prev greater of k
            stack.pop()
        if stack:                   # if prev greater of k on stack, stack will not be empty
            j = stack[-1]           # j is the index of previous greater to index k
            i = minimumsIdxs[j]     # i is the absolute minimum by index k
            if nums[i] < nums[k]:   # check that i is the absolute minimum of subarray ending at k too
                return True
        stack.append(k)             # append current index in for loop, index k
    return False


# O(n) time | O(n) space

def find132pattern(nums):       # this solution tracks the abs min value
    stack = []
    absMin = nums[0]            # initialize absMin as index 0 value; only prev absMin needed
    for k in range(1, len(nums)):   # solution from the pov of index k (ijk)
        while stack and nums[stack[-1][0]] <= nums[k]:  # peek j is not previous greater of current k
            stack.pop()  # if stack top falls to be previous greater then pop
        if stack:   # if peek j is previous greater of current k
            if nums[stack[-1][1]] < nums[k]:    # check absMin i ending at j is less than value k
                return True
        absMin = min(nums[k], absMin)   # update absMin of previous index for next k
        stack.append([k, absMin])       # k and absMin at subarray ending at k
    return False

# O(n) time | O(n) space


def find132pattern(nums):
    stack = []
    indexK = float('-inf')    # lowest possible value for return True boolean check before update

    for j in reversed(range(len(nums))):  # solution from the pov of index j (ijk)
        if nums[j] < indexK:  # this new index j is actually the index i for a previous j,k
            return True    # index i has to be absolute minimum, so less than a previous k,
        while stack and nums[stack[-1]] < nums[j]:  # if j is previous greateer of j, pop n store ref
            indexK = nums[stack.pop()]  # store reference to maximum k seen for bool check with i
        stack.append(j)
    return indexK


arr = [1, 0, 1, -4, -3]
print(find132pattern(arr))

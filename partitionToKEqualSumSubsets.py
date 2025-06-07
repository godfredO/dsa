"""Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose 
sums are all equal.

Example 1:
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:
Input: nums = [1,2,3,4], k = 3
Output: false
 
Constraints:
1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].


So the question gives an array of integers, nums, and another integer k and asks if its possible to divide the array into k subsets
where the sum of each subset's elements totals to the same. So in Example 1 above, nums = [4,3,2,2,5,2,1] , k = 4 and the subsets
are (5), (1,4), (2,3), (3,2) and each subsets totals to 5. Now looking at this example it is clear that the subsets can have varying
lengths and also these are subsets not a subsequence meaning the elements in a subset dont need to be in a particular order, we just
need each element to belong to some subset of the input array and there has to be exactly k subsets, of the same total. So hmm a lot.

Now read the last sentence above again and notice something. Each element has to belong to some subset and all these subsets have to
add up to the same total. So can we make an enlightening and simplifying realization about the total? Yes its sum(nums) / k. So the
first observation is that sum(nums)// k == 0 ie cleanly divisible otherwise we don't have a total to work with since we are dealing
with integers.

So what is our decison tree going to decide? We know that we need exactly k subsets, so for each number we will need to decide which
subset it goes in so that we have k valid subsets ie all subsets sum total to sum(nums) / k. So for this n-ary decision tree, our 
base is k andthe height of the tree is going to be n ie O(k^n). Below we add the O(k^n) solution which is based on actually building 
the subsets and representing each subset by its sum. So we iterate through the numbers and try placing them in one of the subsets. 
We first realize that the target sum of each subset is the sum of the input divided by k and k must cleanly divide the input array 
without carry-overs because the input array only contains integers. So first of we test if this division results in carryovers. If 
it does, we return False without even calling our backtracking function. If there are no carryovers, then it means we only return 
True if we are able to form k subsets whose total equals the result of this division. To test for carryovers, we use the modulo 
operator which returns 0 (False) if there is no carryovers otherwise some carryover number (True). So with our target sum, we also 
initialize a subset array of length k, which is going to store the subset sums as we place integers into different.

A number can go into a subset if adding it to the current subset sum results in a new sum that is less than or equal to the target. 
At the first subset for which this is true, we tentatively place the number in that subset and make a call to place the next number. 
If we are able to place all numbers in a subset, then we return True. Thus we clad our recursive call in an if statement to 
immediately bubble True up the tree if a subsequent recursive call returns True. If however we get to a number and we find that we 
cant place it in any of the k subsets, we return False, which will trigger backtracking from a previous call ie the last number that 
was placed will be removed from its subset and placed in another one and a new recursive call will be made. If however, that number
cant be placed in any of the remaining subsets, then it will return False. There is an important optimization that greatly speeds 
up the algorithm and reduces the number of recursive calls we make. If we backtrack from the first number that was added to a subset
ie after removing this number from the subset, the subset sum is now 0, then there is no point in trying to place that number in
any other subsets. Clearly if we find another empty subset and place it there, we know that we will not be able to place the next
number anyway. Similarly, if the other subsets are partially filled, then this number will likely exceed the target if we try to
add it. So after we backtrack we check if the subset sum is 0, in which case we dont need to try any new subsets and make futile
recursive calls, we just break out of our loop and return False immediately. And that is the optimal solution. However since we
were able to use an n-ary decision tree to solve this question, just for kicks, lets try using a binary decision tree. The main 
difference between the n-ary decision tree and the binary decision tree is that in the n-ary decision tree solution, we build all
k subsets at the same time. In the binary decision tree decision, we build one subset at a time. In either the n-ary or binary
decison tree approach we also first sort the input in descending order so that we can more quickly find False and True cases.


So what decision will the binary decision tree make? We include a number or we dont include a number to our current subset depending
if total will be greater than, equal to or less than sum(nums) / k. If we can include a number if the new total of the path is not
greater than sum(nums) / k. If total == sum(nums)/k, we found one valid subset. So the decision to find a valid subset is 2^n times
and we will need to find k valid subsets. So in the example above we start from 4 and to find the valid subset that includes 4 we
go down our 2^n binary decision tree and we find that 4 belongs in a valid subset with 1. So when finding the next subset, we can't
use 4 or 1, and we will achieve this by storing a visited array for each element. Finding all k valid subsets, gives an overall time 
complexity of O(2^k*n) and a space complexity of O(k*n). Also we will need to track how many partitions or subsets we have built so
far, and we can do this by incrementing a count from 0 to k or decrementing a count from k to 0. Here we go with the decrementing 
approach. So our first base case is that if we build all k valid subsets then the remaining subset to build will be 0 in which case 
we return True. The next base case reminds of trimBinarySearchTree.py. That is we build each subset one by one and when we finish 
building the current subset, ie if the current subset sum equals target (sum(nums)/k) we return the result of building the next 
subset, ie we decrement subsets in the recursive call the we will be returning. This type of backtracking can be called partition
backtracking. Another example of it is the brute force solution of splitArrayLargestSum.py and matchsticksToSquare.py.

The recursive case is that of building the current subset, and we use a for loop to iterate over the nums array and we check if the
current value is already in a subset or adding it to the current subset goes over target, we continue to the next value. Otherwise,
we mark it as visited and  make a recursive call from the next index and a subset sum incremented with the chosen value, trying to 
find if other values need to be added to the current subset, to reach the target. And of course we backtrack by setting the visited 
status to False again, in case we are unable to hit the True case in any path before running out of values, and then we go right ie 
the recursive call where we dont choose the current value. Of course we need to return True, the first time we hit that base case, 
so we clad our subsequent recursive call in an if statement before we do the backtracking. When we complete the current subset, we
pass an index of 0 into the next recursive call ie base case 2, so we dont if we return False and unvisit a value in the recursive
case ie set visited = False, it will be available to build the next subset so we don't need a second recursive call after that for
the case where the current value was not chosen down this path. We also need add a couple of optimizations. First we sort the nums
array in descending order, so that if say our target is 5 and we have a 5 we will quickly finish that call. Secondly by sorting
the values, we know that duplicate values will be stuck together, so if the first time we encounter a value, we return False and
unvisit it, then there is no point starting a dfs() with the other duplicate values for the current subset. So we say that if the
current index is greater than 0 and the previous value is unvisited and the current value is equal to the previous value, then 
don't even bother adding the current value to the current subset, so continue to the next value. 




"""


#O(k^n) time | O(n) space
def canPartitionKSubsets(nums, k) :
    if sum(nums) % k :   
        return False   

    target = sum(nums)/ k   
    subsets = [0]*k                   
    nums.sort(reverse=True)    
    return backtracking(0, target, subsets, nums, k)


def backtracking(i, target, subsets, nums, k):
    if i == len(nums):
        return True

    for j in range(k): #we can put currentMatchstick in one of four sides
        
        if subsets[j] + nums[i] <= target:  #if we can add the current matchstick to the current side
            subsets[j] += nums[i]    #add the current match stick to the stored value for the current side
            if backtracking(i + 1, target, subsets, nums, k):  #try placing next matchstick
                return True
            subsets[j] -= nums[i]

            if not subsets[j]:  #optimizatioon
                break
    return False



#O(2^k*n) time | O(n) space
def canPartitionKSubsets(nums, k) :
        if sum(nums) % k :   
            return False     
        nums.sort(reverse=True)
        target = sum(nums)/ k
        visited= [False]*len(nums)     #visited think used / chosen or not used / not chosen
        return backtracking(0, k, 0, target, visited, nums)


def backtracking(i, subsets, subsetSum, target, visited, nums):
    if subsets == 0: #if we built all subsets
        return True
    
    if subsetSum == target:
        return backtracking(0, subsets - 1, 0, target, visited, nums)
    

    for j in range(i, len(nums)): #try to place the remaining numbers in the current subset,
        if j > 0 and not visited[j -1] and nums[j] == nums[j-1]: #if previous and current number are the same and prev isnt in current subset
            continue                                             #dont even bother num in subset and making a rec call, we know it wont work       
        if visited[j] or subsetSum + nums[j] > target:          #otherwise if current number is already chosen or sum will exceed target
            continue                                            #just skip and try another number
        visited[j] = True   #if none of the above is true, choose current element 

        if backtracking(j+1, subsets, subsetSum + nums[j], target, visited, nums):  #update sum and make call to add next number to subset
            return True #if this path returns True, go no further, return True up the tree

        visited[j] = False #if current path returns False, unchoose number
        
    return False   #return False because path didnt find a valid subset
        



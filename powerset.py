"""The question is to write a function that takes in an array of integers and returns its powerset. The powerset P(x) of a set is the 
set of all subsets of X. For example, the powerset of [1,2] is [ [], [1], [2], [1,2]]. So looking at the example, it is clear that there 
is a base case which is every set, including the empty set will have the empty set as a subset and thus in its powerset. Now our question
doesnt assure us that the array is non-empty so even if we are given an empty set, we should return a powerset that with the empty set.
Now, if we are given a single-element set [1], the P(x) = [ [], [1] ] . If we are given a two-element array [1,2], then P(x) = [[],
[1], [2], [1,2] ]. And there is a pattern which is that in the two-element array we were iterating over the existing powerset for the 
single element array for each subset, we made a copy of the subset and appended the current element and added the results to the 
existing powerset. In the algorithm instead of making a copy and appending we can just put the current element in an array and 
concatenate with the subset. It is also essential also to use a range to generate indices for the existing powerset, select the subset
at that index in the powerset and concatenate it with a list of the current element in the array. Since there are going to be 2^n subsets,
for an array of n and since we use an O(n) array to create by iterating over up to 2^n subsets, the time complexity is O(n*2^n). The
reason why there are 2^n powerset is that when n=0 we have 1 choice , [], if n=1, we have [], [1] ie we can include the element or not.
For each new element in the input we have this choice, don't include the element  or do for each exisiting path ie [],[2] and [1],[1,2] 
in otherwords leave the pre-existing subsets in the current path as is or add the new elements to the pre-existing subsets in the current 
path. Also note that order or duplicates dont matter with subsets. Since there are 2^n subsets and each subset could be up to size n, 
that is why the time/space complexity is O(n*2^n).

This questin is 78. Subsets on leetcode. The iterative/dynamic programming solution is sort of breadth-first search like in its 
implementation, in that we are effectively creating a snapshot of the current size of the output (think queue), looping over the first 
size elements, creating a new array by concatenating each of these and a list of the current input value and appending it to the output. 

The backtracking search  approach can be explained by looking at the explanation for why the number of subsets is 2^n. That is for each 
element in the array, we can choose to add it to the exisiting subsets or not add it to the existing subset. So we can start from the 
first element ie index 0 and our base case of an empty set's powerset, one path is add it to the exisiting powerset, the other path is 
don't add it to the existing powerset, so [], [1]. Then at index 1, for each of the paths thus far we can add it or not . So for path [1] 
we can add [1,2] or not add [1], then for path [] we can add, [2] or not add [] and so on and so forth.  So how is this solution coded up 
with different techniques resembling a pre-order dfs vs post-order dfs. 

The backtracking solution can be created in a preorder type syle dfs or a post order style dfs. In the preorder style dfs, we start with 
index 0 and the base case of the empty set's existing powerset [[]], and with the current subset of the current path, we choose to add the 
element at our index or not. Not adding the index simply means making a copy of the current subset and then a recursive call with an 
increment of the index. Adding the index simply mean concatenating the current subset and a list of the element at index to yield a new 
subset and making a dfs call with the incremented index. In pre-order style dfs our base case is at the top of the recursive tree. Thus 
we use a binary decision tree to work our way from the base case to the question's solution. There is another version where we dont make 
copies of our subsets as we build them but append the current number to the subset to choose and then pop from the subset to not choose
it. As a result when we get to the base case we append a copy of our current subset since we are going to be backtracking and popping.

The post-order style dfs more closesly resembles the iterative/bfs/dynamic programming solution. We start with index equal to the last 
index in the array. We make a recursive call by decrementing the index and the call should return the subsets ending at that index. 
So the base case is that if the index is less than 0, we return [[]]. Then with the returned subsets, loop over them, create new
subsets by concatenation with each subset with the value at index, appending the new subset to the existing subsets and we return the
updated subsets. In post-order style dfs, our base case is at the bottom of the recursive tree.
"""



""" Breadth-first search style technique / Iterative / Dynamic programming solution """
def subsets(nums) :
    output = [[]] #base case
        
    for num in nums:
        size = len(output)    
        for i in range(size):
            newSubset = output[i] + [num]
            output.append(newSubset)            
    return output
        
"""Pre-order Depth-First Search Backtracking technique- making copies along the way to demonstrate the binary decision making"""
def subsets(nums):
    result = [] #output array
    subset = [] #initial subset of the empty subset
    dfs(nums, 0, result, subset)
    return result

def dfs(nums, idx, result, subset):
    if idx >= len(nums):
        result.append(subset)               #append the subset because its a copy and we can backtrack without it
        return

    choose = subset + [nums[idx]]           #make a copy, when choosing not to add the current element
    dfs(nums, idx + 1, result, choose)

    dontChoose = subset[:]                  #make a copy, when choosing not to add the current element
    dfs(nums, idx + 1, result, dontChoose)

    


"""Pre-order Depth-First Search Backtracking technique - no unnecessary copies along the way"""
def subsets(nums):
    result = [] #output array
    subset = [] #initial subset of the empty subset
    dfs(nums, 0, result, subset)
    return result

def dfs(nums, idx, result, subset):
    if idx >= len(nums):
        result.append(subset[:])            #append a copy of the subset because we will be popping when backtracking
        return

    subset.append(nums[idx])                #choose by appending, then make a recursive call for next number
    dfs(nums, idx + 1, result, subset)      

    subset.pop()                            #backtrack by popping, then make a recursive call for next number
    dfs(nums, idx + 1, result, subset)


"""Post-order Depth-First Search Backtracking technique"""
def subsets(nums):
    idx = len(nums) - 1
    return dfs(nums, idx)

def dfs(nums, idx):
    if idx < 0:
        return [[]]
    
    subsets = dfs(nums, idx - 1)

    size = len(subsets)
    for i in range(size):
        newSubset = subsets[i] + [nums[idx]]
        subsets.append(newSubset)
    
    return subsets





"""Algo Expert solutions"""
# O(n*2^n) time | O(n*2^n) space
def powerset(array):
    output = [[]]
    for num in array:
        for i in range(len(output)): #use the range(len(subset)) function because we start with an empty list
            #print(len(output))
            newSubset = output[i] + [num] #use concatenation because we start with an empty list
            output.append(newSubset)
            #print(output)
    return output


"""Recursive solution"""
# O(n*2^n) time | O(n*2^n) space  
def powerset(array, idx=None):
    #pass idx as none first time its called 
    if idx is None:
        idx = len(array) -1 #initialize idx to the end of array

    if idx < 0: #base case is an empty set
        return [[]]
    ele = array[idx]  # the element to add to existing subsets
    subsets = powerset(array,idx-1)  # recursively call powerset till base case is reached

    #once the subsets are returned, go ahead and add ele
    for i in range(len(subsets)):
        newSubset = subsets[i] + [ele]
        subsets.append(newSubset)
    return subsets




array = [1,2,3]
print(powerset(array))
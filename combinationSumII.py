"""Given a collection of candidate numbers , candidates, and a target number, target, find all unique combinations in candiates where the 
candidate numbers sum to target. Each number in candidates may only be used once in the combination. The solution must not contain duplicate 
combinations. 
Review permutations.py, permutationsII.py powerset.py and combinationSum.py. 

So this is similar to the combinationSum.py question, just that we can only use each element once, if you go to that solution, we can just
pass in idx+1 to both left and right branches (instead of only the right branch), but that would lead to duplicate combinations if our
candidates have duplicate values (note that in combinatinsSum.py we are assured of distinct values but not here). Now in the first question
we improved a regular decision tree to avoid duplicate combinations by restricting a value to be chosen on in the left branch but not in
the right branch. Here, since we are not assured of distinct values, how do we avoid something like [1,7] and [7,1] where each 1 refers to
a different 1 ie candidates =  [10,1,2,7,1,6,5] and target = 8 while still ensuring we can still have [1,1,6] using the different 1's.
Another possible duplicate combination that uses different instances of a duplicate value is [1,2,5] and [2,1,5]. Another way of saying this
is how can we ignore duplicates?

So we start by doing something similar, in that we have a left branch where we include instances of the element at index i, as many instances 
as there are in the original candidates array, and a right branch where we include no instances of the element at index i. So in the example
above, where we have duplicate 1's, the left branch is allowed to contain 1's (not unlimited but as many duplicate 1's as there are in the
input) and the left branch is not allowed to contain any 1's.

So the first thing we do is to sort the candidates array. This will have the effect of sitting duplicates side by side. Second thing is that
in the left branch we pass in idx + 1, so that we don't use the same candidate twice, but we can use another duplicate candidate which will 
be the next value in the sorted candidates array. Then to go right we use a while loop to keep incrementing index i as long as we are not at
the last element and the next element is equal to the current element. This will have the effect of moving index i along to the last instance
of the duplicate, then when we pass idx+1, we will be looking at a value that contains no instance of the value chosen in the left subtree. 
Going left we are allowed to choose a different element even if it has the same value as our current element. Going right we can only choose
elements that have a diffeent value from our current element. In either case we are not choosing the same element again.

This a backtracking dfs because as we go right, we use the previous total and combination (without the value chosen on left subtree). This
is effectively like subtracting the value at idx and popping a value. The last solution demonstrate this point. As such when we find a 
valid combination we append a copy of it, before returning and popping values as we backtrack from the left subtree to the right subtree."""


#O(2^target ) time | O(t) space
def combinationSum2(candidates, target):
    result = []
    comb = []
    candidates.sort()  #sort so that duplicate candidate values are next to one another
    dfs(0, candidates, target, comb, 0, result)
    return result


def dfs(idx, candidates, target, comb, total, result):
    if total == target:   #in this case, the True case has to come first in case we are at the last element but we have a valid sum
        result.append(comb)
        return

    if idx == len(candidates) or total > target:
        return
    
    val = candidates[idx]

    leftTotal = total + val   #as we go left we include current candidates's value, as many instances of current candidate's value
    leftComb = comb + [val]
    leftIdx = idx 

    dfs(leftIdx + 1, candidates, target, leftComb, leftTotal, result) #choose another element

  
    rightTotal = total  #as we go right we don't include current candidate's value even if there are duplicates of current candiddate
    rightComb = comb    #backtracking
    rightIdx = idx
    while rightIdx < len(candidates) - 1 and candidates[rightIdx+1] == candidates[rightIdx]: #skip duplicate values
        rightIdx += 1

    dfs(rightIdx + 1, candidates, target, rightComb, rightTotal, result) #choose another element after skipping duplicates



#O(2^target ) time | O(t) space
def combinationSum2(candidates, target):
    output = []
    candidates.sort()
    helper(0, candidates, target, [], 0, output)
    return output


def helper(idx, candidates, target, current, total, output):
    if total == target:
        output.append(current[:])
        return
    
    if idx == len(candidates) or total > target:
        return
    
    newCurrent = current + [candidates[idx]] #choose the element at index i
    helper(idx+1, candidates, target, newCurrent, total+candidates[idx], output) #left branch, add +1 since we can use element once
    
    while idx < len(candidates) - 1 and candidates[idx+1] == candidates[idx]:
        idx += 1
    helper(idx+1, candidates, target, current, total, output) #go right by incrementing idx and passing in original current



#O(2^target ) time | O(t) space
def combinationSum2(candidates, target) :
    result = []
    comb = []
    candidates.sort()
    dfs(0, candidates, target, comb, 0, result)
    return result


def dfs(idx, candidates, target, comb, total, result):
    if total == target:
        result.append(comb[:])
        return
    
    if idx == len(candidates) or total > target:
        return
    
    
    val = candidates[idx]

    total += val
    comb.append(val)
    dfs(idx + 1, candidates, target, comb, total, result)


    total -= val
    comb.pop()
    while idx < len(candidates) - 1 and candidates[idx+1] == candidates[idx]:
        idx += 1

    dfs(idx + 1, candidates, target, comb, total, result)



candidates = [10,1,2,7,1,6,5]
target = 8
print(combinationSum2(candidates, target))
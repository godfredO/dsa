"""Given an array of distinct integers, candidates , and a target integer, target , return a list of all unique combinations of candidates 
where the chosen numnbers sum to target. You may return the combinations in any order. The same number may be chosen from candidates an
unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different. It is
guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input. 
2 <= candidates[i] <= 40. All elements of candidates are distinct. 1 <= target <= 40. That is the candidates and target are all positive
numbers, candidates between 2 and 40 inclusive, target between 1 and 40 inclusive. This means that our sum is always going to converge
either at the target in which case we store the combination or exceed the target and in either case we return.

Eg candidates = [2,3,6,7], target = 7 Answer = [[2,2,3], [7]]. Explanation 2 and 3 are candidates and 2 + 2+ 3 = 7. Note that 2 can be used
multiple times. 7 is a candidate, and 7 = 7. Note that [2,2,3] and [3,2,2] are the exact same combination, just in a different order so we 
cant have both in the output. So what we are saying is that we want combinations not permutations that sum up to the target value  
Review permutationsII.py and powerset.py.

The brute force approach would be to use a decision tree where we can choose each element an unlimited number of times. However using this
approach we soon realize that it is impossible to avoid permutations of the same combination that sums to the target. eg 2,2,3 and 2,3,2 
and 3,2,2 will both be down distinct paths in this tree. So how do we get the combinations without repeating.

We can say that the first left branch of this tree contains at least one 2, then the rest of the branches to its right will not contain any 
2's. That is for each index, we have a left branch were we can always choose the value at that index an unlimited number of times and a
right branch where we cannot choose the value at that index at all.

Then down the left branch we would go left add another two and for that branch going down we only consider combinations that contain
at least two 2's etc. So effectively we say that whatever we choose on the left, we are not allowed to choose it on the right and so on 
and so forth. At each point if the combination sum is less than the target we can keep choosing, if the combination sum is equal to the
target we store the combination sum and if the combination sum exceeeds, we dont keep going down the path. 

Another way of saying is that as we go right, we are reducing the number of elements that we can choose. Thus we will have a base case of 
calling the recursive function with an empty array. To avoid slicing a new array, we can use a pointer i, which shifts rightward until it 
goes out of bounds. As far as time complexity, at each point in the decision tree, we have the left branch which contains the chosen element's 
subtree and the right branch which does not contain the left branch elements. So we have two branches and the height of the tree is at least 
target, since we keep going until we find the target or we exceed it then we stop.

So in the code we have a recursive function that takes an index, candidates, target, a current combination array, the total of the current
combination array and the output array. So we initially call with an index of 0, an empty combination array, a total of zero and an empty
output array. In the recursive function, we first check the base case where the total of the current combination equals the target in which
case we append a copy of the current combination to the output array and return. We append a copy so as to not modify the current 
combination which will need to stay as is as we go back up the tree. Next we check the base case where we stop pursuing a path ie when index 
equals the length of candidates (out of bounds) or the total exceeds target, in which case we return. Otherwise we have first go left and 
generate combinations that contain the element at index i. To do this we create a new array which is a concatenation of the current combination 
and an array of the element at index i. Then we pass this new array into a recursive function in place of the original current array, and we 
also update total by adding the element at index i. This will have the effect of recursively going down the left branch for all combinations 
that the as many occurrences of the element of i as there are in the new array. We use concatenation to create a new array so that we back up
the tree, we would not have modified the passed current array because we need that as is to go right. To go right, we increment the index
by 1 and that's it. This will have the effect of choosing the next element after i and creating a new combination with it."""



#O(2^target ) time | O(t) space
def combinationSum(candidates, target):
    result = []
    comb = []
    total = 0
    dfs(0, candidates, target, comb, total, result)
    return result


def dfs(idx, candidates, target, comb, total, result):
    if total == target:  #True case should come first in case we have a valid total by the last index and we are out of bounds
        result.append(comb)
        return


    if idx == len(candidates) or total > target:
        return
    
    val = candidates[idx]

    #going left, choose current index value an unlimited number of times. idx stays same, comb and total is increased by current index value
    leftTotal = total + val                 #increase total by current index value
    leftComb = comb + [candidates[idx]]     #append current value to current combination
    leftIdx = idx                           #idx stays the same so that we choose idx an unlimited number of times

    dfs(leftIdx, candidates, target, leftComb, leftTotal, result)       #dfs call for left branch of current subtree


    #going right, we are not allowed to choose the current index value at all, comb and total stay same while idx is incremented 
    rightTotal = total                      #total stays the same, can't choose current number
    rightComb = comb                        #combination stays the same, can't choose current number
    rightIdx = idx + 1                      #increment idx so that current number is never chosen again down this path

    dfs(rightIdx, candidates, target, rightComb, rightTotal, result)    #dfs call for right branch of current subtree
    
    

"""We can skip creating multiple O(n) copies and concatenation each time. It doesnt improve the complexity per se but on average 
only doing an O(n) operation when appending a valid combination, while appending and then popping when backtracking is better since
array appending and popping is constant-time, compared to creating whole new arrays."""
#O(2^target ) time | O(t) space
def combinationSum(candidates, target):
    output = []
    dfs(0, candidates, target, [], 0, output)
    return output


def dfs(idx, candidates, target, current, total, output):
    if total == target:
        output.append(current[:])
        return
    
    if idx >= len(candidates) or total > target:
        return
    
    current.append(candidates[idx])
    dfs(idx, candidates, target, current, total+candidates[idx], output)
    current.pop()
    dfs(idx+1, candidates, target, current, total, output)


"""Same solution, but we opt for creating a new array when going left, O(n) but then we skip the copy operation when we find
a valid combination"""
#O(2^target ) time | O(t) space
def combinationSum(candidates, target):
    output = []
    helper(0, candidates, target, [], 0, output)
    return output


def helper(idx, candidates, target, current, total, output):
    if total == target:
        output.append(current)
        return
    
    if idx == len(candidates) or total > target:
        return
    
    newCurrent = current + [candidates[idx]] #choose the element at index i
    helper(idx, candidates, target, newCurrent, total+candidates[idx], output) #left branch, with newCurrent that includes element at i
    helper(idx+1, candidates, target, current, total, output) #go right by incrementing idx and passing in original current



candidates = [1,2,3]
target = 4
print(combinationSum(candidates, target))
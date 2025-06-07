"""Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
Only numbers 1 through 9 are used. Each number is used at most once. Return a list of all possible valid 
combinations. The list must not contain the same combination twice, and the combinations may be returned 
in any order.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

Constraints:

2 <= k <= 9
1 <= n <= 60

So this is an extension of combinationSum.py and combinationSumII.py and in this question we are not given a candidates input array, we
are just told that only numbers 1 through 9 are used, each number can be used at most once, so no duplicates and a valid combinatin must
sum up to a target number, n , and must contain exactly k elements. This means if a combination sums up to n but contains fewer or more
than k elements its not valid. Also, since we only have postive numbers to choose from we know that the total sum will either converge
or exceed target.

So I still use the method of restricting the choices made for the left subtree and right subtree. Since we can only choose each element
once, in both subtrees I increment the current index. I also keep track of the number of elements chosen thus far in the current path and
the total of the chosen elements in the current path. So the first thing I do is to generate my own candidates array, initialize the count
of elements in the current path as 0, and make the first dfs call.

So first the True base case. If the total equals our target, n,  and the count equals k, append the current combination and return. The
False case, if total exceeds target, or count exceeds k or we are out of bounds, just return. Otherwise, select the value in the candidates
at the current index.

In left branch, we choose the current value by adding it to our total, our combinationa and incrementing the count. We also advance the
current index so that we cant choose the current element again. Then we make our dfs call with these left branch variables.

In the right branch, we don't choose the current value, so our total, combination and count remain the same. We also advance the current 
index so that we never choose the current element. Then we make our dfs call wit these right branch variables.
"""

def combinationSum3(k , n):


    def dfs(start, total, comb, k, n, output):
        if total == n and len(comb) == k:
            output.append(comb[:])
            return 
        
        if total > n or len(comb) > k or start > 9:
            return 
        
        total += start
        comb.append(start)
        dfs(start+1, total, comb, k, n, output)

        total -= start
        comb.pop()
        dfs(start+1, total, comb, k, n, output)

    output = []
    dfs(1, 0, [], k, n, output)
    return output


def combinationSum3(k , n) :
        result = []
        comb = []
        count = 0
        array = [i for i in range(1,10)]
        dfs(0, array, n, k, count, 0, comb, result)
        return result

def dfs(idx, array, target, k, count, total, comb, result):
    if total == target and count == k:
        result.append(comb)
        return
    if count >= k or idx == len(array) or total > target:
        return
    
    val = array[idx]
    
    leftTotal = total + val
    leftComb = comb + [val]
    leftIdx = idx + 1
    leftCount = count + 1
    
    dfs(leftIdx, array, target, k, leftCount, leftTotal, leftComb, result)
    
    
    rightTotal = total
    rightComb = comb
    rightIdx = idx + 1
    rightCount = count
    dfs(rightIdx, array, target, k, rightCount, rightTotal, rightComb , result)
        
    
        
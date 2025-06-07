"""Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does 
not appear in nums. If there are multiple answers, you may return any of them. 

Example 1:
Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:
Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.

Example 3:
Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
 
So my first solution is to actually build all binary strings of length n, one index at a time. I am using a binary recursive tree structure 
such that in the left subtree, I choose '0' for the current index  and on the right subtree I choose '1' for the current index. Once the 
full string is built, the index will equal n so I check if the built string is in the input. Now before hand I put all the input strings 
in a set, and when building a string I store in an array, and join into a string at the end. So if the built string is in the set of strings
I return None, if its not I return the string. This means after branch of the string is traversed and the returned value is either None if
the string we built already existed in the input, otherwise it will be a valid binary strin that wasnt in the input. As such when we return
from the left branch, we check if the returned value is not None. If its not we return that value up the tree. If it is, we go down the 
right branch, again checking if the returned value is not None, and if its not we return that value up the tree. Otherwise after both calls,
we return None. This way, the first time, we find a valid string not in the input, we just return it up the tree and don't make any dfs calls.
Our initial call is to return the result of the recursive call for an empty current array and index 0. Since we are assured that there will be
some valid binary string of length n not in the input,  we expect to find some string and the moment we do, we will return that. That is we
only need find one such string that is why we use the if statements. This solution could als be rigged differently to find all valid binary
strings not in the input.

So there are 2^n binary strings of length n. Since our input contains n of these strings and we stop the moment we find a string not in the
set, we will have to generate at least n+1 strings ie n+1 dfs calls. Inside each dfs call we have a couple of O(n) operations meaning the
actual time complexity isnt 2^n, but rather n^2. That is because we only need 1 answer our solutin is more efficient than if we needed to 
find all answers. Now an optimization that doesnt necessarily improve the time complexity is to not start with an empty array but an array
of n '0's and then we just update the string at current index to '1' if that what we are choosing, which is constant time compared to O(n) 
of concatenating the current array with ['0'] or ['1]. Since we still need to join the array to form a string which is O(n), our time
complexity is still O(n^2) but at least we do a single O(n) operation at the end of the current branch instead of at each level of the tree.
"""

#2^n time | O(n) space
def findDifferentBinaryString(nums) :
    n = len(nums[0])

    words = set()
    for num in nums:
        words.add(num)

    current = []   # could also use 
    return dfs(0,current,n, words)


def dfs(idx, current, n, words):
    if idx == n:
        word = "".join(current)
        if word not in words:
            return word
        return None
    
    left = current + ['0']
    leftIdx = idx + 1
    value = dfs(leftIdx, left, n, words)
    if value:
        return value

    #backtrack and go right
    right = current + ['1']
    rightIdx = idx + 1
    value = dfs(rightIdx, right, n, words)
    if value:
        return value
    
    return None


"""Tiny optimization hmm"""
def findDifferentBinaryString(nums) :
        n = len(nums[0])

        words = set()
        for num in nums:
            words.add(num)

        current = ['0']*n
        return dfs(0,current,n, words)


def dfs(idx, current, n, words):
    if idx == n:
        word = "".join(current)
        return word if word not in words else None
    
    
    value = dfs(idx + 1, current, n, words)
    if value:
        return value

    current[idx] = '1'
    value = dfs(idx + 1, current, n, words)
    if value:
        return value
    
    return None
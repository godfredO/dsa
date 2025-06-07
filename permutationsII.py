"""Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output: [[1,1,2], [1,2,1], [2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

So this question is a backtracking question extending from permutations.py and the difference is of course the fact that there are 
duplicates means that swapping duplicate values with one another doesnt yield a new permutation. So how do we use backtracking to 
obtain unique permutations when our input has duplicates. The first thing is realising that utilizing the regular decision tree with 
n spots is not going to work because it will lead to duplicate permutations. So how do we model our problem to avoid that?

For this particular case, as we have duplicates in input, we can track the count of each number.We can also create a hashmap of the 
counts of each element in the input array ie for [1,1,2] we get {element:count} = {1:2, 2: 1}. Python provides a built-in lib Counter 
which can be using for this problem. As the order of output results doesn't matter, we can use this Counter variable to track visited 
elements in the exploration path. . Now we can use this hashmap instead of the input to create a valid decision tree. The first layer 
of this new decision tree has two choices (ie the unique value ) ie append 1 and decrement 1's count in this path or append a 2 and 
decrement 2's count in this path. At each point in any path, we have as many choices as there are keys whose count is greater than 0. 
Then when the result we are building reaches the length of the input array, we know that we have reached the end of a valid permutation 
and we append the result and return. So when we return up the counter decision tree, what does the backtracking step look like? You 
guessed it, we increment the count of the previously chosen element by 1 to restore it. Because we are building our permutation down 
each path, when we make a choice we create a new array, by concatenating a list of the choice with the current state of the permutation 
of this current path. We really cant use indices to avoid this additional operation. This question introduces using counts to generate
unique possiblities when there are duplicates in the input.
https://leetcode.com/problems/permutations-ii/discuss/2030416/Python-Simple-Backtrack-Beats-~90

I would say that if there are unique elements, then there would be n! perms so n! rec calls and in each call, we do an n*n operation 
and the max height of the rec stack is n, giving a time complexity of O(n^2*n!) and space of O(n*n!) (rec *output size)


"""
#O(n^2*n!) time | O(n*n!) space
def permuteUnique(nums):
    perms = []
    result = []

    counts = {n:0 for n in nums}
    for num in nums:
        counts[num] += 1
    
    explore(counts, result, perms, nums)
    return perms

def explore(counts, result, perms, nums):
    if len(result) == len(nums):
        perms.append(result)
        return
    
    for unique in counts:
        if counts[unique]:
            newArray = result + [unique] # decrement visited key
            counts[unique] -= 1
            explore(counts, newArray, perms, nums)
            counts[unique] += 1   # restore the state of visited key to find the next path, backtracking step



"""Solution using in-built Counter"""
from collections import Counter
def permuteUnique(nums):
        
        permutations = []
        counter = Counter(nums)

        def findAllPermutations(res):
            if len(res) == len(nums):
                permutations.append(res)
                return 
            
            for key in counter:
                if counter[key]:
                    counter[key]-=1 # decrement visited key
                    findAllPermutations(res + [key])    
                    counter[key]+=1 # restore the state of visited key to find the next path
                
        findAllPermutations([])
        return permutations
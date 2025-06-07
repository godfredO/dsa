"""You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks 
to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time. Return true 
if you can make this square and false otherwise.

Example 1:
Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

Example 2:
Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.


Hide Hint 1
Treat the matchsticks as an array. Can we split the array into 4 equal parts?

Hide Hint 2
Every matchstick can belong to either of the 4 sides. We don't know which one. Maybe try out all options!

Hide Hint 3
For every matchstick, we have to try out each of the 4 options i.e. which side it can belong to. We can make use of recursion for this.

Hide Hint 4
We don't really need to keep track of which matchsticks belong to a particular side during recursion. We just need to keep track of the 
length of each of the 4 sides.

Hide Hint 5
When all matchsticks have been used we simply need to see the length of all 4 sides. If they're equal, we have a square on our hands!



So this is an application of partitionToKEqualSumSubsets.py. We can only build a square if the sum(nums) % 4  == 0 and the length of a
side of this square is sum(nums) / 4. Since we are dealing with lengths the elements have to be positive. So we are basically going to 
reaply the partititionToKEqualSumSubsets.py solution here, and that is exactly what the first solution here does. That is we implement
a O(2^4*n) ie O(2^n) solution. In this approach we know that there are 4 sides and we know the length of these sides, so we build the
sides, one by one, and for each side, we decide, which numbers can go into it together. For a richer explanation of this binary decision
tree solution and the next n-ary decision tree solution, read partitionToKEqualSumSubsets.py.

In the 2^n approach, we used a visited array to determine the fork between include and dont include current value. Here, since we are
going to build four sides, we declare a sides array of length 4 and we initialize each side to be of length 0. So we can say index 0
represents the top side, index 1 the bottom side, index 2 the left side, index 3 the right side. What does the backtracking do here,
we are going to place each matchstick length into one of the four sides, so we will have a loop of range(4) to go through the sides
array and try placing the current matchstick. We place a matchstick by adding its length to the current length of the side, if it 
doing so doesnt give a value that exceeds the target length. If we find a side for the current matchstick, we make a recursive call 
to place the next matchstick. Of course, if a path doesnt eventually yield a successful placement of all matchsticks, we backtrack by
removing the placed matchstick's length from the current side by decrementing the length of the current side by the length of the 
current matchstick before trying a different side for the current matchstick. If we can't find a side for the current matchstick we
return False up the recursive tree, so that we can backtrack from a previously placed matchstick. So what is our True case? When we
make a recursive call with an index that is out of bounds, then it means we were able to place all matchsticks down the current path
so we return True. And of course, the instant we find True, we want to return that up the tree, so we clad our next matchstick 
recursive calls in an if statement to return True, if the recursive call returns True. We can add a small optimization that if we
backtrack to the first element we added to a side, ie we return a side to length 0, we break and return False.


"""
"""For this solution read partitionToKEqualSumSubsets.py"""
#O(2^4*n) time | O(4*n) space
def makesquare(matchsticks) :
        if sum(matchsticks) % 4 :   
            return False     
        matchsticks.sort(reverse=True)
        target = sum(matchsticks)/ 4
        visited= [False]*len(matchsticks)   #this visited array is the difference between choosing and not choosing a value
        return backtracking(0, 4, 0, target, visited, matchsticks)


def backtracking(i, subsets, subsetSum, target, visited, nums):
    if subsets == 0: #if we built all subsets
        return True
    
    if subsetSum == target:
        return backtracking(0, subsets - 1, 0, target, visited, nums)
    

    for j in range(i, len(nums)):
        if j > 0 and not visited[j -1] and nums[j] == nums[j-1]:
            continue
        if visited[j] or subsetSum + nums[j] > target:
            continue
        visited[j] = True   #choose current element

        if backtracking(j+1, subsets, subsetSum + nums[j], target, visited, nums):  #path containing
            return True

        visited[j] = False
        
    return False



#O(4^n) time | O(n) space
def makesquare(matchsticks) :
    if sum(matchsticks) % 4 :   
        return False   

    length = sum(matchsticks) / 4   #target length
    sides = [0]*4                   #initially all sides have length 0
    matchsticks.sort(reverse=True)    #this optimizes, if target length is 2 and matchsticks[0] is 3, then we quickly return False
    return backtracking(0, length, sides, matchsticks)


def backtracking(i, length, sides, matchsticks):
    if i == len(matchsticks):
        return True

    for j in range(4): #we can put currentMatchstick in one of four sides
        
        if sides[j] + matchsticks[i] <= length:  #if we can add the current matchstick to the current side
            sides[j] += matchsticks[i]    #add the current match stick to the stored value for the current side
            if backtracking(i + 1, length, sides, matchsticks):  #try placing next matchstick
                return True
            sides[j] -= matchsticks[i]

            if not sides[j]:  #optimizatioon
                break
    return False

            




        
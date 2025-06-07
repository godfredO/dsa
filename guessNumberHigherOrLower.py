"""We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
You call a pre-defined API int guess(int num), which returns three possible results:
-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

Example 1:
Input: n = 10, pick = 6
Output: 6

Example 2:
Input: n = 1, pick = 1
Output: 1

Example 3:
Input: n = 2, pick = 1
Output: 1
 

Constraints:

1 <= n <= 231 - 1
1 <= pick <= n


This is effectively the foundational question as far as using binary search to search over a linear search 
space; using the generalized steps in binarySearchII.py where the answer is the minimal value for which the 
condition function return True ; as well as re-writing the solution using the standard binary search algorithm 
in binarySearch.py where we separate the check for the answer from the situtaion where we move the right pointer.
Finally there is a solution for when the problem is best posed as the maximum value for which the condition 
function returns True. These three approaches are useful to know depending on the question criteria.

Note that the standard algorithm uses the value and checks each of them and also has while left <= right as the 
loop condition. The generalized algorithm for finding the minimum value for which the condition is true, bundles
the return value for gues() for right guess and when the guess is higher together, and sets right to mid, and 
then returns left outside the while loop ,and the loop condition is while left <= right. Finally there is the
solution where the question is best posed as the maximum value for which
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


"""Standard algorithm"""
class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1 , n
        
        while left <= right:
            mid = left + (right - left) // 2   #mid is my guess
            value = guess(mid)
            if value == 0:
                return mid
            elif value == -1:
                right = mid - 1
            elif value == 1:
                left = mid + 1
        
               
"""Minimum value for which condition function returns True"""
class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1 , n
        
        while left < right:
            mid = left + (right - left) // 2   #mid is my guess
            value = guess(mid)
            if value <= 0:
                right = mid
            else:
                left = mid + 1
        return left



"""Maximum value for which condition function returns True"""
class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1 , n
        pick = 1
        while left <= right:
            mid = left + (right - left) // 2   #mid is my guess
            value = guess(mid)
            if value >= 0:
                pick = mid
                left = mid + 1
            else :
                right = mid - 1
        return  pick
        
   
                     

def guess(val):
    pass
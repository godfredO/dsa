"""Given a positive integer num, write a function which returns True if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt.

Example 1:
Input: num = 16
Output: true

Example 2:
Input: num = 14
Output: false
 

Constraints:

1 <= num <= 2^31 - 1

So for a perfect explanation of the bounds of this solution, read sqrtX.py, since this is a direct extension of that question.
Here we are assured the input is a positive number (instead of non-negative). As such we can use a left, right = 1, n and our
condition will be mid*mid >= n ( instead of mid*mid > n) and our final answer will be to check if left*left == num instead of
using (left - 1 * left - 1) == num. With that said we could just use the solution from sqrtX.py 

"""

#O(n^0.5) time | O(1) space - Brute force approach
def isPerfectSquare(num):
    for i in range(1, num + 1):
        if i*i == num:
            return True
        elif i*i > num:
            return False

#O(log(n)) time | O(1) space
def isPerfectSquare(num) :
    left , right = 1, num 
        
    while left < right:
        mid = left + (right - left) // 2

        if condition(mid,num):
            right = mid
        else:
            left = mid + 1
    return (left)*(left) == num                    # `left` is the minimum k value, `k - 1` is the answer

def condition(mid,x):
    return mid*mid >= x



def isPerfectSquare(num) :
    left , right = 0, num + 1
        
    while left < right:
        mid = left + (right - left) // 2

        if condition(mid,num):
            right = mid
        else:
            left = mid + 1
    return (left - 1)*(left - 1) == num                    # `left` is the minimum k value, `k - 1` is the answer

def condition(mid,x):
    return mid*mid > x
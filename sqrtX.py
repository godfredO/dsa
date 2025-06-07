"""Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer 
should be non-negative as well. You must not use any built-in exponent function or operator. For example, do not use 
pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


So this also follows the generalized binarySearchII.py algorithm. first off, we are told that our input is a non-negative
integer and to handle edge cases of 1 or 0, we define our search space as the set of integers (in ascending order) between
0 and x+1. Now lets say that x=16, we can try a brute force approach starting from 0 and ask is 0*0 equal to 16, is 1*1 
equal to 16 etc. So the minimum of the search space is 0. What is the maximum value. For most numbers, the square root is
significantly less but for 0,1 the square root is equal to the number itself. But in the algorithm itself, we return 
left - 1, so our actual maximum is x + 1. The reason for this is because we are not assured that the input x is a perfect
square. So for example if x= 10, we are to return 3, and the only way we can do that is by getting to 3^2=9, then 4^2 = 16,
at this point we know that all values after 4 will only get bigger than 10 so we stop and return 4-1=3. As such, for the
case where x = 1, we don't want our algorithm to return 2 - 1 = 1.. So the idea in this case is to use the binary search 
algorithm to find the smallest value whose square is greater than 8 ie 3 and return 3-1=2. If given x= 0, we would start 
with left=0, right = 0+1 = 1, then the first mid = 0 which doesnt satisfy mid*mid > x  so we move the left to mid+1 = 0+1 
and then we break out of the loop and return left - 1 = 1 - 1 = 0. The brute force approach is also below.


"""

def mySqrt(self, x: int) -> int:
    for i in range(x+1):  #range is from 0 to x + 1, so range(x+2) though range(x+1) still works x=1 range(2)= 0,1 , 1*1=1
        if i*i == x:  #if we find a perfect square
            return i
        elif i*i > x:   #if we go pass a perfect square the previous value is the rounded down square root
            return i- 1

#O(log(n)) time | O(1) space
def mySqrt(x) :
    left , right = 0, x +1
        
    while left < right:                             #O(log(n))
        mid = left + (right - left) // 2
            
        if condition(mid,x):
            right = mid
        else:
            left = mid + 1
    return left - 1         # `left` is the minimum k value, `k - 1` is the answer

def condition(mid,x):   #O(1)
    return mid*mid > x



x = 16
print(mySqrt(x))
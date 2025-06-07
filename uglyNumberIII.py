"""An ugly number is a positive integer that is divisible by a, b, or c. Given four integers n, a, b, and c, return 
the nth ugly number.

Example 1:
Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.

Example 2:
Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.

Example 3:
Input: n = 5, a = 2, b = 11, c = 13
Output: 10
Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
 

Constraints:
1 <= n, a, b, c <= 10^9 ; 1 <= a * b * c <= 10^18 ; It is guaranteed that the result will be in range [1, 2 * 109].

So we are told that given three integers a,b,c, an ugly number is a positive integer divisible by a,b, or c. We are
also provided a integer n, and we are to return the nth ugly number. First off, whenever you see the nth, 1st or kth
something, we are talking about some sorted search space and the nth element in this sorted search space. So if we
can determine the linear search space in question, we can use binary search. The search space in this question is 
actually the bounds given in the constraints. We are told that a,b,c will be at least 1 and a*b*c will be at most
10^18. So now we take a guess for the nth ugly number, we have to find the number of ugly numbers that are less than
or equal to it. This is because the nth ugly number will have exactly n ugly numbers less than or equal to it; all 
numbers greater than the nth ugly number will have more than n ugly numbers less than or equal. In otherwords, the
nth ugly number is the minimum value which has n or more values less than or equal to it. To count we first count
the multiples of a that are less than the guess, then the multiples of b, then the multiples of c and we can add up
all those numbers. We get these counts by floor dividing the guess by a,b,c. So say our guess is 20, and a=2, b=3,
c=5/\ there are 10 multiples of 2 less than or equal to 20 ie 20 // 2, there are 6 multiples of 3 less than or equal
to 20 ie 20//3 and there are 4 multiples of 5 that are less than or equal to 20 ie 20//4. I
However, we know that we will double count, and triple count some multiples that are common to the numbers. That is
we will double count 6 (2&3),15(3&5), 10(2&5) etc. In otherwords we have to subtract the number of values that are
multiples a*b // math.gcd(a,b), a*c//math.gcd(a,c), b*c//math.gcd(b,c). We also have to add back multiples of
a*(bc)//math.gcd(a,bc), which would be removed by the other subtractions. And that is it. Since the condition function
here will be constant time, the algorithm as a whole is constant space. 
"""

import math
def nthUglyNumber(n,a,b,c):
    left , right = 1, 10**18
    res = 0
    while left <= right:
        mid = left + (right - left) // 2
        
        if condition(mid,n,a,b,c):
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res


def condition(mid,n,a,b,c):
    ab = a*b // math.gcd(a,b)
    ac = a*c // math.gcd(a,c)
    bc = b*c // math.gcd(b,c)
    abc = a*bc // math.gcd(a,bc)

    total = mid//a + mid//b + mid//c - mid//ab - mid//ac - mid//bc + mid//abc
    return total >= n
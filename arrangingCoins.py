"""

Tags: Binary search ; Monotonicity ; Greedy ; Medium

You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has
exactly i coins. The last row of the staircase may be incomplete. Given the integer n, return the number of complete rows of
the staircase you will build.  1 <= n <= 231 - 1 .

Example 1:
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

Example 2:
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.


So the brute force approach would be to build the rows one by one. So say n=10, then for the first row we put 1 coin and have
10 - 1 = 9. The second row 9 - 2 = 7, the third row 7 - 3 = 4, the fourth row 4 - 4 = 0. Oh we are out of coins and built 4
complete rows. Say n = 7, first row 7 - 1 = 6, second row 6 - 2 = 4, third row = 4 - 3 = 1, fourth row will not be complete
sice 1 - 4 = -3. So we use a while loop, and starting from row 1, we fill up the rows and by subtracting the number of coins
we need to fill the row and to check if we were able to complete that row we check if the remaining coins is greater than or
equal to 0 in which case we increment a complete variable by 1.

Now how do we use binary search here, what is our maximum and minimum values for number of completely filled rows, and what
is the  monotonicity condition pattern (ie the pattern where if one value is valid, all values less than it are valid or
all values greater than it are also valid is monotonicity).

So the question is asking for the number of completely filled rows. What is the minimum number of completely filled rows? Its
1, since n's minimum value is 1, not 0 (check the constraints). What is the maximum number of completely filled rows. For most
n, the number of completely filled rows will be significantly less than n, but if n = 1, then the maximum number of completely
filled rows is also n (like in sqrtX.py and validPerfectSquare.py). So we know that 1 <= completely filled rows <= n. Now what
is our monotonicity and how do we write the condition function. First off, we know that if row 2 is completely filled, then
row 1 is completely filled. If row 6 is completely filled then rows 5,4,3,2,1 are all completely filled (look at the brute
force approach). So we can say that if a row is said to be completely filled then all rows below it are completely filled.
Also we can use monotonicity and binary search because the search space is ordered in that as the rows increase, the number
of rows also increase.

So given the number of completely filled rows, we can determine the number of coins needed to completely fill all the rows
from row 1 to the number of completely filled rows. If completedRows = 1, we need 1 coin; if completedRows = 2, we need 3
coins (1 for row 1, 2 for row 2). If completedRows = 4, we need 1 + 2 + 3 + 4 = 10 coins. So our answer will be the maximum
value for which the needed number of coins is less than or equal to n, the availabe number of coins. Now that's interesting
because usually, the search space and our threshold are in reverse ( eg in kokoEatingBananas.py, speed and hours are
inversely related) so we minimize the space for which our condition is True, but here it will be easier to maximize the
space for which the condition is True. And the code is also a little different as a result. In the code, we use a completed
variable and set it to mid when the condition returns True, then we move the left to mid + 1 otherwise we move right to
mid - 1 when the needed number of coins exceeds available coins. The while loop condition is while left <= right (instead)
of while left < right. In otherwords, we store our mid values in completed variable and maximize the search for possible
complete rows left = mid + 1 if our last value returned True otherwise we minimize the search for possible complete rows.


So we know our binary search will be log(n) time but what about our condition. If we take mid rows as the possible answer,
and add all the needed coin values from 1 to mid rows, we will be doing an O(n) operation, for an overall time complexity
of O(nlog(n)) which is worse than the brute force approach. Can we reduce the condition function to O(1) (like in sqrtX.py
and validPerfectSquare.py). The answer lies in something called the Gauss Summation. But basically to calculate the sum
of a range from 1 to n in O(1) time, the equation is n* ((n+1)/2) . So for completedRows = 1, 1*((1+1)/2) = 1*1 = 1. If
completedRows is 4 ; 4 * ((4+1)/2) = 10. Using Gauss Summation, we are able to reduce the binary search approach to
O(log(n)) an improvement over the brute force solution. Gauss Summation is also used in the optimal and final soluton of
allKindsOfNodeDepths.py.

So why not try to find K (complete rows) from the Gauss summation equation, instead of using possible K values to get
to the max value?
		(K * ( K + 1)) // 2 <= n
		K^2 + K <= 2*N
K is the number of complete rows, n is the available number of coins. So after completing the square, we take the half
the coefficient of K ie 1/2 and square it and add to both sides and factorize

		K^2 + K + 0.25 <= 2*N + 0.25
		(K + 0.5)^2 <= 2*N + 0.25

		K <= sqrt(2N + 0.25) - 0.5

So what is the maximum possible valid value of K? Of course it is that value which is equal to sqrt(2N + 0.25) - 0.5 because a
valid K value cannot be greater than  sqrt(2N + 0.25) - 0.5. We thus simply round the value of sqrt(2N + 0.25) - 0.5.
And that's all we need to return. This is a constant time solution.


"""


"""Brute Force Approach"""
# O(n) time | O(1) space




import math
def arrangeCoins(n) :
    coins = n
    complete = 0
    row = 1					# we start from 1st row, where we will need 1 coin
    while coins >= 0:		# we check the remaining coins
        coins -= row		# take the rows for the current row
        if coins >= 0:		# if remaining coins is zero or greater, current row is complete
            complete += 1  	# variable for tracking number of complete rows
        row += 1			# increment row variable

    return complete			# number of complete rows


# O(log(n)) time | O(1) space
def arrangeCoins(n):
    left, right = 1, n   	# minimum and maximum number of coins needed for filling rows
    complete = 0
    while left <= right:  # while the pointers havent crossed one another
        mid = left + (right - left) // 2  # calculate the midpoint
        if condition(mid, n):  	# if the condition is true
            complete = mid  	# store maximum seen
            left = mid + 1  	# maximize search for possible complete rows by moving the left pointer
        else:					# if needed coins is greater than available coins
            right = mid - 1		# minimize search for possible complete rows by moving right pointer
    return complete


def condition(mid, n):			# needed coins needed less than or equal to available coins
    return (mid * (mid + 1)) // 2 <= n   # O(1) determination instead of O(N) adding from 1 to mid


# O(1) approach
def arrangeCoins(n):  # n is the availabe number of coins
    return int(math.sqrt(2 * n + 0.25) - 0.50)


n = 5
print(arrangeCoins(n))

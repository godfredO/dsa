"""There are several cards arranged in a row, and each card has an associated number of points. The points are given in the 
integer array cardPoints. In one step, you can take one card from the beginning or from the end of the row. You have to take 
exactly k cards. Your score is the sum of the points of the cards you have taken. Given the integer array cardPoints and the 
integer k, return the maximum score you can obtain. 1 <= cardPoints[i] <= 10^4. 1 <= k <= cardPoints.length.

Example 1:
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your 
total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

Example 2:
Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.

Example 3:
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.


This question is a good example where simply finding a way to reword it would make your life a lot easier. The question is asking us 
to find the maximum sum of values at the left and right edges of the array. More specifically, it's asking us to find the max sum of k 
values at the edges. If we were to reword the question, we're essentially asked to find the minimum subarray sum of length n - k. Once 
we find this, we simply subtract this from the total sum and this would be our answer.

Example:
We'll use the example cardPoints = [5,2,2,4,1], k = 3 to illustrate this point.
The answer is 5 + 4 + 1 = 10. The first thing to realize that there are four possiblities of k cards from the end. We can have [5,2,2],
[5,2,1], [5,1,4], [1,4,2]. Another thing to realize is that if we had used a two pointer method where the left pointer starts at 5 and
the right pointer starts 1 and at each iteration we just choose the maximum value and advance the appropriate pointer, we would actually
get the wrong value because we would choose 5,2,2 which gives 9 instead of the correct answer of 10. And the reason is that because of 
the 1, we would have never gone past and chosen 4. We have no way of knowing when we are at 1 that there is a greater value next to it.

Thus by cleverly using reverse thinking to realize that if we found the minimum subarray of width len(cardPoints) -k and we subtract this 
from sum(cardPoints), we would actually be getting the sum of k cards from the end. Think about it, since n= 5, k = 3 by finding the 
minimum subarray of size 5-3=2, subtracting the sum of size 2 subarrays from the array sum gives the sum of some 3 cards from the end. 
If we subtract [5,2], we get the sum of [2,4,1]; if we subtract [2,2] we get the sum of [5,4,1] ; if we subtract [2,4] we get the sum of
[5,2,1]; if we subtract [4,1] we get the sum of [5,2,2].

The reason this works is because the numbers that aren't included in the minimum subarray sum are the card points that are obtained in 
the actual question. This is why we need to subtract from the total sum.

Now in the code this follows a common pattern of coding up fixed width sliding window problems. Here we sum up our first n-k numbers and
initialize our min subarray sum as equal to that. Then we loop through the remainder of the array, adding the current right pointer value
and removing the current left pointer value before advancing the left pointer. I have a solution where we calculate the total separately
and one where we calculate the total of the whole array inside the loop. Note that the way its coded up, if k == n, the first for loop
doesnt run at all, and minSum = currentSum  = 0, and so when we calculate currentSum in the second loop, whatever value we get will always
be more than 0. This way when we do total - minSum = total - 0 = total which makes sense if we are looking for k elements from the end and
k == n, then we just sum up all the elements in the array as is. If k < n, then the first for loop will run, and we will have some minSum
value to compare with when we update currentSum, which is the general case.
"""

def maxScore(cardPoints, k):
    n = len(cardPoints)
    total = sum(cardPoints)

    width = n - k
    currentSum = 0
    for i in range(width):
        currentSum += cardPoints[i]
    
    left = 0
    minSum = currentSum
    for right in range(width, n):
        currentSum += cardPoints[right]
        currentSum -= cardPoints[left]
        left += 1

        minSum = min(minSum, currentSum)
    return total - minSum


def maxScore(cardPoints, k) :
        n = len(cardPoints)
        width = n - k

        currentSum = 0
        for i in range(width):
            currentSum += cardPoints[i]

        left = 0
        minSum = currentSum
        total = currentSum
        for right in range(width, n):
            total += cardPoints[right]
            currentSum += cardPoints[right]
            currentSum -= cardPoints[left]
            left += 1

            minSum = min(minSum, currentSum)
        return total - minSum

cardPoints =[9,7,7,9,7,7,9]
k = 7
print(maxScore(cardPoints, k))
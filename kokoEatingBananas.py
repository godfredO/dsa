"""Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and 
will come back in h hours. Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of 
bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not 
eat any more bananas during this hour. Koko likes to eat slowly but still wants to finish eating all the bananas before 
the guards return. Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23
 
Constraints:
1 <= piles.length <= 10^4 ; piles.length <= h <= 10^9 ; 1 <= piles[i] <= 109;

So this is an interesting binary search question. The are asked to find the minimum speed at which Koko can eat the bananas 
in h hours. We are told that Koko can eat from one pile per hour, and if Koko finishes the bananas in a pile before the hour is 
over, Koko still stays at that pile till the start of the next hour when she can go to the next pile. If a certain pile[i] = 3 
and speed is 2, koko will spend roundUp(3/2) = roundUp(1.5) = 2 at that pile. On the otherhand if a certain pile[i] = 6 and 
speed is 2, koko will spend 3 hours at that pile. So since Koko chooses some pile of it eat from, the minimum number of bananas 
Koko can eat per hour is 1/hr. That is the minimum speed of Koko is 1. This way if a pile[i] has exactly 1 banana, Koko will 
spend exactly 1 hour at that pile; If a pile[i] has more than 1 banana, Koko will spend more than 1 hour at the same pile. What
about Koko's maximum speed. Take [3,5], if the speed is 5 bananas/hr, Koko will eat the first 3 bananas in 45 minutes but will
still spend the full hour at pile[1], then when she gets to pile[2], she eats all 5 bananas in 1 hour. Meaning if we want Koko
to move to a new pile every hour, the maximum speed is the max(piles). So now that we know the min and max of the search space,
what condition do we use to intelligently move about the search space. For each mid value speed, we will calculate the number
of hours that Koko will take to eat all piles. If Koko spends more than h hours at a particular mid speed, we have to increase
our speed by moving the left pointer to mid + 1. If Koko spends less than or equal to h hours, we need to decrease the speed
by moving the right pointer to mid, since mid could also still be the answer here. We also have to remember to round up the
number of hours Koko spends at a pile after dividing by the speed. For this we can either use hours= math.ceil(piles[i]/speed) 
or we could say , hours = 1 + (pile[i]) // speed. For example, if pile[i] = 3, math.ceil(3/2) = 2 or 1 + (3-1) // 2 = 2. And
finally we are able to write this solution because we know from the constraints that h is at least equal to the number of
piles ie piles.length <= h <= 10^4. If speed = max(piles), Koko will speed exactly piles.length hours eating all bananas.


"""

#O(nlog(n)) time | O(1) space
def minEatingSpeed(piles, h) :
    left, right = 1 , max(piles)    #bounds of speed space since KoKo can only eat one 
        
    while left < right:
        mid = left + (right - left) // 2   #mid speed for current bounds
        if condition(piles, mid, h):
            right = mid             #decrease speed
        else:
            left = mid + 1          #increase speed
    return left             #


def condition(piles, speed, h):
    hours = 0
    for pile in piles:
        hours += 1 + (pile - 1)//speed
    return hours <= h                    
        

import math
def condition(piles, speed, h):
    hours = 0
    for pile in piles:
        hours += math.ceil(pile //speed)
    return hours <= h        
        
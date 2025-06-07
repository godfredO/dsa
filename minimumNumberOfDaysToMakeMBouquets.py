"""You are given an integer array bloomDay, an integer m and an integer k. You want to make m bouquets. To make a bouquet, 
you need to use k adjacent flowers from the garden. The garden consists of n flowers, the ith flower will bloom in the 
bloomDay[i] and then can be used in exactly one bouquet. Return the minimum number of days you need to wait to be able to 
make m bouquets from the garden. If it is impossible to make m bouquets return -1.

Example 1:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in 
the garden. We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

Example 2:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible 
to get the needed bouquets and we return -1.

Example 3:
Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here is the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers 
that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.
 
Constraints:
bloomDay.length == n
1 <= n <= 105
1 <= bloomDay[i] <= 109
1 <= m <= 106
1 <= k <= n


So we have an array, bloomDays,  of n flowers (n = len(bloomDays)) where bloomDays[i] , and we want to group the flowers into m 
bouquets and each bouquet requires k flowers. Each value in the array, bloomDays[i] represents the number of days needed for 
the flower at i to bloom ie to be ready to be harvested. In otherwords we need a total of m*k flowers, so first off if n < m*k, 
we dont have enough floewers. If we have enough flowers, the next question is how many days do we need to wait in order for m*k
flowers to be available for the bouquets. The way we go about it is to realize that if we wait max(bloomDays), all the flowers 
would be in bloom and we can harvest a maximum of n flowers. On the otherhand, since bloomDay[i] has a minimim (constraints) of
1, we can say that the absolute minimum number of days is 1,although we can also use a minimum number of days of min(bloomDays).
Then we determine the mid number of days, and we count all the flowers that are in bloom after mid number of days. This will be
all the flowers whose bloomDay[i] <= mid. As soon as flowers ==k, we can have a new bouquets so we add 1 to a bouquets variable,
and we can re-initialize the flowers variable to 0 since we just used it for a new bouquet. Now the question tells us that the
a bouquet can only be made with adjacent flowers, so say that we need 3 flowers for a bouquets and the flowers at index 0, 1
will both bloom by mid number of days, but the flower at index 2 takes more than mid number of days, it means that we cant use
the flowers at 0,1 for any bouquets due to the restriction to use only adjacent flowers. So if bloomDay[i] > mid, we also 
re-initialize flowers to be 0, since the preceding flowers cant be used in a bouquet for the current mid number of days. At the 
end of the loop we check if the number of bouquets is greater than or equal m. Thus the answer will be the minimum mid days such 
that this condition is True. In otherwords, we are using a greedy algorithm for the condition function (binarSearchII.py).
"""
def minDays(bloomDay, m, k) :
        if len(bloomDay) < m*k:
            return -1
        left, right = 1, max(bloomDay)
        
        
        while left < right:
            mid = left + (right - left) // 2
            if condition(bloomDay, mid, m, k):
                right = mid 
            else:
                left = mid + 1
        return left

def condition(bloomDay, mid, m, k):
    flowers = 0
    bouquets = 0
    for daysNeeded in bloomDay:
        if daysNeeded <= mid:
            flowers += 1
        else:
            flowers = 0
            
        if flowers == k:
            bouquets += 1
            flowers = 0
    return bouquets >= m
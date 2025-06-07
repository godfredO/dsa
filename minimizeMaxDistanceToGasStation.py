"""On a horizontal number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1], 
where N = stations.length. Now, we add K more gas stations so that D, the maximum distance between adjacent gas 
stations, is minimized. Return the smallest possible value of D.

Example:
Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
Output: 0.500000

Note:
stations.length will be an integer in range [10, 2000] ; stations[i] will be an integer in range [0, 10^8] ; K 
will be an integer in range [1, 10^6] ; Answers within 10^-6 of the true value will be accepted as correct.


So here we have a binary search question in the form of minimizing the maximum distance between stations which
follows closely with splitArrayLargestSum.py. Now, it is implied that the input array is sorted due the fact 
that we are told that the gas stations are on a horizontal number line. You can however, sort it if that works
for you. We are also told that any answer within 1e-6 of the true value will be accepeted. In otherwords, when
we apply binary search instead of seeking the true value with while left < right, we can stop if right - left
> 1e-6. So with that said, we will be using  binary search to guess the optimal max distance between gas 
stations. Lets say there are no additional gas stations added, what will be the max distance. Taking into 
consideration that the input is sorted,  the max distance with no additional gas stations will be the distance
from the first gas station to the last gas station. What about if we had a large number of gas stations added
so that gas stations are right next to one another. The max distance between gas stations would be 0. Now this
last points demonstrates an interesting thing about this question. Betwen any two gas stations there are an 
infinite number of places on the horizontal number line to place gas stations (lets pretend gas stations were
just a dot on a line). So if we have one gas station at point 1 and another at point 2, the original max 
distance will be a distance of 1 ie 2-1=1. If we decided to add 1 additional gas station, we could place it at 
1.1 so that the distances are 0.1 and 0.9 respectively (distance from the new station to the stations at point 
1 and point 2), so that the max distance between stations is 0.9. However the optimal position for the new 
station is at point 0.5 so that the distances are 0.5 and 0.5 (to stations at point 1 and 2 respectively). Any 
other positon will have a greater maximum distance. So the minimal max distance is 0.5. This also demonstrates
why the question asks us to find a value within 1e-6 of the true value, since we dont want to keep repeating 
binary search on infinitesmally small spaces. So we know that the left pointer is initialized at 0 and the right 
pointer, at stations[-1] - stations[0]. Since we are not just guess, whole number indices, but rather distance 
values that can be decimals, our guesses will be (left - right) / 2.0 so that Python does float division instead 
of the usual integer (floor) division.

We know that we are taking guesses of max distances and we want to return the minimized max distances after 
placing k stations. So as 0 < maxDistance < stations[-1] - stations[0], +inf > k > 0. That is our answer divides 
our search space into [0,maxDistance], [maxDistance, stations[-1] - stations[0]] and the corresponding number of
stations needed is [k, +inf], [0,k]. So which distance subarray do we minimize? Since maxDistance, our imaginary
answer is the minimum value in [maxDistance, stations[-1]-stations[0]] if we guess a maxDistance that falls 
within these bounds, we can ahead and minimize it in search of a better answer, and this subarray corresponds to
the stations subarray of [0,k]. In otherwords, if we guess a maxDistance that requires stations <= k, we can
go ahead and minimize it, by shortening our window in the direction of smaller max distance guesses. Otherwise, 
if for our current guess requires stations > k, the we know that the maxDistance guess falls within [0, maxDistance] 
which corresponds to +inf > k, so we need to maximize our distance guess so that we can reduce the number of stations 
needed to get closer to the k stations we have. In otherwise if we need too many stations, we need to maximize our 
distance guess, if we need too few stations, we need to minimize our distance guess. Another thing to keep in mind 
here is that because our left and right pointer can be as close as 1e-6, when we minimize our guess, we move right to 
mid and when we maximize our guess we also move left to mid (instead of the typical mid + 1).

So how do we actually determine the number of stations needed for a particular distance guess. First of all, this
is related to splitArrayLargestSum.py since in both cases, our guess represents some sort of upper threshold value.
Next we have to realize that depending on the distance between adjacent gas stations and our guess, we may need
to place more than 1 additional station between two existing stations. So  we iterate through the stations up to 
the penultimate value, to choose our current station, and the next station will be our station[currentIdx + 1]. 
Alternatively we can loop from the second station to the last for our current and choose our previous station to 
currentIdx - 1. For each pair of stations, we ask ourselves, how many additional stations do we need to place in 
between the existing stations such that the maximum distance between stations does not exceed our guess. If 
stations = [1,2] with an intial distance of 1, if our max distance guess is 0.5,  we will 1 station placed halfway 
between the existing stations. How do we do do this. Welp, the formula is distance = stations[current + 1] - current
then math.ceil(distance/guess) - 1. So in the example here math.ceil(1/0.5) - 1 = 2 - 1 = 1. Finally usually we 
return left when we break out of the loop, here you can do that or you can return right since they both will be
within 1e-6 of the answer.
"""
import math

def minmaxGasDist(stations, k):
    left, right = 0, stations[-1] - stations[0]
    while right - left > 1e-6:
        mid = (left + right) / 2
        if count(stations, mid, k):
            right = mid
        else:
            left = mid
    return left


def count(stations, mid, k):
    stationsToAdd = 0
    for i in range(len(stations) -1):
        initial = stations[i+1] - stations[i]
        stationsToAdd += math.ceil( initial/mid) - 1
    return stationsToAdd <= k

    

stations = [1, 2] 
K = 2
print(minmaxGasDist(stations,K))
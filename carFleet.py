"""There are n cars going to the same destination along a one-lane road. The destination is target miles away. You are given 
two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the 
speed of the ith car (in miles per hour). A car can never pass another car ahead of it, but it can catch up to it and drive 
bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these 
two cars is ignored (i.e., they are assumed to have the same position). A car fleet is some non-empty set of cars driving at 
the same position and same speed. Note that a single car is also a car fleet. If a car catches up to a car fleet right at the 
destination point, it will still be considered as one car fleet. Return the number of car fleets that will arrive at the 
destination.


Example 1:
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it 
reaches target. Note that no other cars meet these fleets before the destination, so the answer is 3.

Example 2:
Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation: There is only one car, hence there is only one fleet.

Example 3:
Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
Explanation:
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at 
speed 1 until it reaches target.
 
Constraints:
n == position.length == speed.length  ;  1 <= n <= 105  ; 0 < target <= 106  ;  0 <= position[i] < target  ; 
All the values of position are unique.;  0 < speed[i] <= 106 ;


One thing the question says is that since there is only one lane, a car cant pass another car thats in front of it. So if
we have a front car travelling at 10 miles/hr and a back car travelling at 20 miles/hr, then when the back car catches up
to the front car, they will become a fleet. So take the first example above, target = 12, position = [10,8,0,5,3], speed = 
[2,4,1,1,3]. For each car, we can calculate its distance from the target as distanceToTarget = target - position[i] hence 
distanceToTarget = [2, 4, 12, 7, 9]. Then for each car, we calculate the time it will take to reach the target by dividing 
the distance to target, by the speed ie TimeToTarget[i] = distanceToTarget[i] / speed[i] and this will give TimeToTarget = 
[1, 1, 12 , 7, 3]. Then we can say that for any pair of adjacent cars, if the back car's time is less than or equal to the 
front car's time, then they will meet and form a fleet, and when that happens, the speed of the fleet is the speed of the 
front car. This is because if the back car needs a shorter amount of car to reach the destination than the front car, it
will catch up to the front car at some point to form a fleet before or at the destination.

Now realize that the position of a car on number line, is in terms of proximity to the target and not in terms index position. 
So we would have to sort the position array in terms of proximity to the target. This means the position array will be sorted 
in descending order (so that the distance array is be sorted in ascending order), so that the car which starts off closest to 
the target will be at index 0, and the car that starts off farthest from the target will be at index len(n) - 1. So 
sortedPosition = [10,8,5,3,0], matchingSpeed = [2,4,1,3,1], matchingDistance = [2,4,7,9,12], matchingTime = [1,1,7,3,12]. Now 
we can iterate over the time array, and using an ascending stack type, count the number of fleets. We sort the position array 
in descending order, and modify the speed to match the sorted position array, and we iterate over both arrays (using zip()) 
and for each position, we calculate the distance and time. For the current time, we pop all times on the stack if the current 
time cannot be in the same fleet, ie if the current time is greater than the peek time. Thus if after this step the stack is 
empty, we are starting a new fleet, (think of numberOfConnectedComponents.py),so we increment the fleet variable by 1 before 
we append the current time. At the end we return the fleets variable.
"""

#O(nlog(n)) time | O(n) space
def carFleet(target, position, speed) :
    stack = []
    fleets = 0
    for i,v in sorted(zip(position,speed), reverse=True): # default sorts based on x[0]; descending ie closest to target
        dist = target - i                   # distance to target
        time = dist/v                       # time to target
            
        while stack and stack[-1] < time:   # pop if current stack top reaches target before a possible crash
            stack.pop()
            
        if not stack:   # if there no item
            fleets += 1
            
        stack.append(time)
    return fleets


def carFleet(target, position, speed):
    stack = []

    for i,v in sorted(zip(position,speed), reverse=True): # default sorts by tuple[0] ie position
        distance = target - i
        time = distance / v

        while stack and time <= stack[-1]:  # if the incoming car catches up to the car on top of stack
            stack.pop()

        stack.append(time) 
    return len(stack)
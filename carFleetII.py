"""There are n cars traveling at different speeds in the same direction along a one-lane road. You are given an array 
cars of length n, where cars[i] = [positioni, speedi] represents:
positioni is the distance between the ith car and the beginning of the road in meters. It is guaranteed that positioni < positioni+1.
speedi is the initial speed of the ith car in meters per second.
For simplicity, cars can be considered as points moving along the number line. Two cars collide when they occupy the same position. 
Once a car collides with another car, they unite and form a single car fleet. The cars in the formed fleet will have the same position 
and the same speed, which is the initial speed of the slowest car in the fleet. Return an array answer, where answer[i] is the time, 
in seconds, at which the ith car collides with the next car, or -1 if the car does not collide with the next car. Answers within 10-5 
of the actual answers are accepted.

 

Example 1:

Input: cars = [[1,2],[2,1],[4,3],[7,2]]
Output: [1.00000,-1.00000,3.00000,-1.00000]
Explanation: After exactly one second, the first car will collide with the second car, and form a car fleet with speed 1 m/s. After 
exactly 3 seconds, the third car will collide with the fourth car, and form a car fleet with speed 2 m/s.
Example 2:

Input: cars = [[3,4],[5,4],[6,3],[9,1]]
Output: [2.00000,1.00000,1.50000,-1.00000]

This question is an extension of carFleet.py, so read that first. So the one difference between this question and carFleet.py is that
in that question whiles the cars in carFleet.py are going to a destination, here the cars are on an inifinte stretch of road. So
take two cars A,B in that order. These cars will collide and form a fleet if and only if the speed of A is greater than the speed of B. 
We are told that when two cars when two cars collide, the speed of the fleet is the speed of the slowest car. Luckily in this question 
we are assured that the positions will be sorted and unique since we are told that position[i] < position[i+1]. Now if we wrote a 
solution based on this observation alone, the solution would be incomplete. Consider three cars A,B,C. with speed spd(A)>spd(B)>spd(C). 
In this situation, there are two possibilities. Either B collides with C first, form a fleet and A collides into BC, or A collides into
B first,and fleet AB collides into C. 

So first off, for a pair of cars A,B once we have established that spd(A) > spd(B), how do we determine the collision time. Well lets
say that the initial positions are 2, 6, meaning that there is a gap of 4. In other for car A to collide with car B, car A will have to
cover the gap with its faster speed. So lets say that the speed of A,B is 2 miles/sec, 1 mile/sec. Then after 1 second, the positions are
4,7. After 2 seconds, the positions are 6,8; after 3 seconds the positions are 8,9; after 4 seconds the positions are 10,10. So it takes
4 seconds for A to catch up to B, and fully cover the gap between the two cars. How do we calculate this? We say time = gap/relativeSpeed
where gap = initialPosition[B] - initialPosition[A] and relativeSpeed = spd(A) - spd(B) ie (6-2)/(2-1) = 4/1= 4.

So back to the collisions. If we have A,B,C, we can say that in order for A to collide into B, A must be faster than B and its collision
time to B must be less than B's collision time to C. In otherwords, A must be fast enough to catch up to B and before B catches up to C.
Since we need information about B's collision with C before we make a decision about whether A collides into B or BC, we have to iterate
from the back to the front. So we will add the last car to the stack first, and for the preceding cars, we pop from the stack if the
current car cannot collide into the car on top of the stack. This happens if the current car's speed is less than or equal to the stack
peek car or the stack peek car has a collided with the car that comes before it, and the collision car of the current car to the stack
peek car is greater than or equal to the collision time of the stack peek car.  If after popping off all cars that cant collide with the
current car as is, we use the relative speed formula to calculate the time till the car collides with the car on top of the stack. If 
this algorithm is used to on array [[3,4],[5,4],[6,3],[9,1]], say cars A,B,C,D, we find that B collides with C to form BC (with a speed
of C), then BC collides with D to form BCD (with a speed of D), then A collides with BCD, hence when we get to A, the top of the stack 
is actually D, meaning the speed and distance we use for the relative speed calculation of A is that of D. In otherwords, in other to 
make a decision about A, here we needed collision information of B,C,D to first be resolved first.


"""

def getCollisionTime(cars):
    n = len(cars)
    res = [-1]*n

    stack = []
    for i in reversed(range(n)):  # first step is to iterate back to front
        pos, spd = cars[i]

        while (stack and ( spd <= cars[stack[-1]][1] or (
                res[stack[-1]] > 0 and ((cars[stack[-1]][0] - pos) / (spd - cars[stack[-1]][1])) >= res[stack[-1]]
            ))): # current car won't crash into stack top car or crashes into it after its already crashed
            stack.pop()  
        
        if stack: # if there is something on the stack, then the stack can crash into stack top
            res[i] = (cars[stack[-1]][0] - pos) / (spd - cars[stack[-1]][1])
        
        stack.append(i)
    
    return res
"""There are n cars on an infinitely long road. The cars are numbered from 0 to n - 1 from left to right and each car is 
present at a unique point. You are given a 0-indexed string directions of length n. directions[i] can be either 'L', 'R', 
or 'S' denoting whether the ith car is moving towards the left, towards the right, or staying at its current point 
respectively. Each moving car has the same speed. The number of collisions can be calculated as follows:
When two cars moving in opposite directions collide with each other, the number of collisions increases by 2.
When a moving car collides with a stationary car, the number of collisions increases by 1.
After a collision, the cars involved can no longer move and will stay at the point where they collided. Other than that, cars 
cannot change their state or direction of motion. Return the total number of collisions that will happen on the road.

Example 1:
Input: directions = "RLRSLL"
Output: 5
Explanation:
The collisions that will happen on the road are:
- Cars 0 and 1 will collide with each other. Since they are moving in opposite directions, the number of collisions becomes 
0 + 2 = 2.
- Cars 2 and 3 will collide with each other. Since car 3 is stationary, the number of collisions becomes 2 + 1 = 3.
- Cars 3 and 4 will collide with each other. Since car 3 is stationary, the number of collisions becomes 3 + 1 = 4.
- Cars 4 and 5 will collide with each other. After car 4 collides with car 3, it will stay at the point of collision and get 
hit by car 5. The number of collisions becomes 4 + 1 = 5. Thus, the total number of collisions that will happen on the road is 5. 

Example 2:
Input: directions = "LLRR"
Output: 0
Explanation:
No cars will collide with each other. Thus, the total number of collisions that will happen on the road is 0.
 
Constraints:
1 <= directions.length <= 10^5   ; directions[i] is either 'L', 'R', or 'S'.


So this question is similar to asteroidCollision.py. In that question, we discovered that a collision only occurred if the 
asteroid on top of stack is going right when the current asteroid is going left. Here there are three scenarios under which a
collision occurs, and in each case, both cars are stationary after a collision.

We have 9 possible combinations : 
Collison happens in 3 scenarios
Top of Stack        Curr direction
R                   L               increment collision by 2, pop from stack, set direction to S
S                   L               increment collision by 1, set direction to S
R                   S               increment collisoin by 1, pop from stack, set direction to S

In all other cases, just append the direction to stack.

Now the interesting thing about this question is really about what happens when there is a pile up. Lets take the first scenario. 
If we have 'RRRS', our stack will contain ['R','R','R'] and when we get to the stationary car, the top car will collide with the 
stationary car, becoming stationary itself. Due to the collision so we pop it off the stack, to get ['R','R]. The new peek car 
will also collide into the previous peek and the stationary car (both are stationary at this point due to the previous collision), 
becoming stationary itself, so again we pop off the stack to give ['R']. Finally the new peek car on the stack will also collide 
into the pile up and become stationary itself. In otherwords, a single stationary car, will cause collisions while the peek is 
right-moving. In all these cases, we need not explicitly set the current car's direction to stationary since its already that; it 
suffices to just pop the right-moving peek off the stack and count the collisions. In otherwords, in a R-S collisioin we need to
use a while loop, so that the current statiionary car can cause collisions with all previous right-moving cars.

Lets take the second pile-up situation ie left-moving cars after a stationary car. If we have 'SLLL', the stack will contain
['S], then the left moving car at index 1, will collide into this stationary car, becoming stationary itself. Here because the
current car was originally moving left, we have to explicitly set its new direction to 'S' before appending. And since there was
a collison, we also have to pop off the stack before counting collisions. So after popping, setting directions and appending, the
stack will be ['S'] > [] > direction = 'S' > ['S']. The car at index 2 will collide into the newly stationary index 1 car, and again
we have ['S'] > [] > direction = 'S' > ['S']. The same thing with the last left moving car. In otherwords, in a 'SL' collision, we
need to use an if statement, and set the direction explicitly before appending the new stationary car onto the stack.

The final and most interesting situation is a mash-up of the previous two situations. If we have 'RRRL', the stack will be ['R','R','R']
and when the left moving car collides with the peek, stack becomes ['R','R']] and direction also becomes 'S' so that we have an RS
situation on our hands which will pop off the remaining two collisons. In otherwords, the first collision is RL, the next two collisons
are RS. The main thing here then is to ensure that the RL situation comes before the RS while loop in the code. This way we can handle
the case where a newly stationary car causes collisions with previous right moving cars.

As such in the code, we handle RL collisions with an if statement first (making sure to set direction), then we handle RS collisions
next second so that a newly set direction from the first if statement can also trigger this while loop. Finally we handle the SL 
situation making sure to set the new direction for the previous left moving car. In fact as long as we handle the RL situation before
the RS while loop we will be fine. Hence we can set both if statements before the while statement, or RL first RS while loop second and
SL last. The key is to ensure that an RL collision will also set of RS collisions.
"""
def countCollisions(self, directions: str) -> int:
    collisions = 0
    stack = []

    for i in range(len(directions)):
        direction = directions[i]
            
        if stack and stack[-1] =='R' and direction == 'L':
            stack.pop()
            collisions += 2
            direction = 'S'
                
        while stack and stack[-1] == 'R' and direction == 'S': 
            collisions += 1
            stack.pop() 
                
        if stack and stack[-1] == 'S' and direction == 'L':
            collisions += 1
            stack.pop()
            direction = 'S'
            
        stack.append(direction)

    return collisions
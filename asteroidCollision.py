"""
Tags: Stack; Previous Greater; Medium


We are given an array of integers representing asteroids in a row. For each asteroid, the absolute integer value
represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid
moves at the same speed. Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one
will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.


Constraints:
2 <= asteroids.length <= 104  ;  -1000 <= asteroids[i] <= 1000  ; asteroids[i] != 0

Intersting question here. So we are told that asteroids moving in the same direction will never meet since all asteroids are
moving in the same direction. This means if asteroids = [2,5] or asteroids = [-2,-5], the answer will be the same as the
input array since no collisions will occur. Now lets consider the case of two asteroids of different directions. If we have
asteroids = [-2,5], the first asteroid is going left and the second asteroid is going right so they will never meet. If we
have asteroids = [2,-5], the first asteroid is going right, the second asteroid is going left and since the first asteroid is
to the left of the second asterod (and second asteroid is to the right of the first asteroid), the two asteroids will actually
meet. This means as we iterate from left to right,  for two adjacent asteroids, collisions will only occur if the left asteroid
is going right and the right asteroid is going left. So we can use a stack to solve this question. Before we add a new asteroid
to the stack, we first check if a collision will occur ie if the current asteroid is going left and the peek asteroid on the
stack is going right, ie stack[-1] > 0 and current < 0. If this is the case, we go ahead and handle the result of the collision.
If both asteroids have the same magnitude, the collision will destroy both asteroids, so we pop the peek asteroid off the stack
and we do not append the current asteroid to the stack. If the peek asteroid is greater in magnitude, the current asteroid will
explode after the collision, so the peek asteroid will still stay on the stack but we will not append the current asteroid to the
stack. In otherwords, if the peek asteroid is greater in magnitude, we do nothing. If the current asteroid is greater in magnitude,
the peek asteroid will explode after the collision, so we pop the peek asteroid off the stack and then append the current asteroid
to the stack. Note that after we pop the current peek asteroid, we will compare the current asteroid to the new peek asteroid. If
both asteroids have equal magnitude, then both will explode after the collision, so we pop the peek asteroid of the stack and we do
not append the current asteroid to the stack. In otherwords, if of equal magnitude, since the current asteroid is also destroyed we
don't need to compare to the new peek asteroid.

So usually in stack problems we always append the current element. However in this case we don't. How then do we code this up. Well
we could use a while else block in Python (yep it exists). We put the append step in the else statement and that will run if and
only if the while loop isnt exited prematurely due to a break statement. Thus if equal magnitude  we pop and break out of the while
loop or if stack peek asteroid greater, we just break out of while loop, meaning in both cases, we don't append. If however the
current asteroid is greater in magnitude, after we pop, we continue to the top of the while loop to compare the current asteroid with
the new pop (I add an unnecessary continue statement to demonstrate this point, since the while loop will keep running until it
terminates). At the end of the operation, the stack will contain the state of the asteroids after all collisions.

"""


def asteroidCollision(asteroids):
    stack = []

    for current in asteroids:

        # crash only if top is going right + and incoming going left -
        while stack and stack[-1] > 0 and current < 0:  # collision occurs
            if abs(stack[-1]) == abs(current):  # collision of equal sizes
                stack.pop()      # asteroid at stack top explode due to equal size
                break            # incoming asteroid also explodes so no append
            elif abs(stack[-1]) < abs(current):  # incoming is bigger asteroid
                stack.pop()      # asteroid at stack top explode due to smaller size
                continue  # incoming not exploded yet, so check new peek
            elif abs(stack[-1]) > abs(current):  # stack top is bigger asteroid
                break  # ncoming is the one that explodes so no append
        else:  # if we exit while loop without encountering break statement
            stack.append(current)   # append only if did not explode or stack empty

    return stack

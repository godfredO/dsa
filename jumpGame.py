"""Given an array of non-negative integers nums, you are initially positioned at the first index of the array. Each element in the array
represents your maximum jump length at that position. Determine if you are able to reach the last index. Eg [2,3,1,1,4] is True. The key
word here is maximum jump length, meaning you can jump to the maximum but you can also jump less that. For example in the array above, 
from index 0 we can only do a max jump of 2 ie we can do a jump of 0, 1, 2 ie we can stay at index 0, go to index 1 or go to index 2.
Thus this question is giving climbing stairs, number of ways to traverse graph vibes ie dynamic programming vibes.

So in the example [2,3,1,1,4], there are several ways in which we can get to the last position. We can start from the first position and
take the max jumps each time ie from index 0, 2 jumps to index 2, then 1 jump to index 3, the 1 jump to index 4 which is the last position.
We can also take a single jump from index 0 to index 1, then 2 jumps from index 1 to index 3 the 1 jump from index 3 to the last position.
So here, we took less than the max jumps from index 0 and index 1 and still ended up in the last position.

So the brute force approach will be to test out every single path and if any path leads us to the destination, we return True. So we start
from the first position and draw a recursive tree where we take 1 jump to index 1, 2 jumps to index 2, 3 jumps to index 3. Then we go down
each path until we get to the last position or not. There will be a lot of repeated calls leading to an overall complexity of O(n^n). Now
we can cache intermediate solutions and improve the time complexity to O(n^2). If we ever get to position which has a 0 max jump, we cant
jump anywhere ie we would be in a dead end. So if we used a cache we would store a False at any oposition whose only option is to go to the 
dead end. So for example if we the array was [3,2,1,0,4], then we would know that any path that leads to index 2 will return a False because
from index 2 we go to a dead end of index 3. ie if we took 1 jump from index 0 to index 1 and 1 jump from index 1 to index 2 we know thats
a False. If we took 2 jumps from index 0 to index 2 thats also a False. And of course if we took three jumps from index 0 it is False.
In this way we store the result for each positon and eventually we return cache[0] because if cache[0] is True then we can get to the last
position from index 0. So like before this recursive solution with memoization is O(n^2) time, but there is a better greedy linear solution.

The greedy solution is actually quite simply sort of. We first initialize a data structure goal, which starts off as the last position in
the array. Then we loop backward through the array, and at each index we add the index to the max jumps stored at that index and check if
it is equal to or greater to the goal. If it is, we set the goal equal to that index. Outside the for loop we ask if goal is equal to the
starting position ie 0. Thus instead of asking if we can get to end from the start, we go from the end  to the start. 
So we first check if the position before end position can get to the end position. If it does, we shift the goal variable to it. Then we
ask if the position before that can get to the penultimate postion if it does we can shift, if not, we still go on in the loop and check
the position before that can get to the penultimate postiion, and on and on. So if we are able to shift the goal to the start position,
it is the same as saying that we can get to the end position from the start position. We are effectively asking if any position can get
to an updated end position without getting stuck in a dead end.

"""


def jumpGame(array):

    goal = len(array) - 1
    
    for idx in reversed(range(len(array))):
        if idx + array[idx] >= goal:
            goal = idx
    return goal == 0
         



array = [3,2,1,0,4]
print(jumpGame(array))
"""The fibonacci sequence is defined as follows: the first number of the sequence is 0, the second number is 1, and the nth number is the 
sum of the (n-1)th and (n-2)th numbers. The question is to write a function that returns the nth fibonacci number. This question has 
recursion / dynamic programming approaches. The dynamic approach uses the observation that we can store intermediary results in an array 
of length n, meaning our final answer will be the last element in this array when this is updated ie at index n-1 in this array of length n. 
Then we update the value at index 0 ie the 1st fibonacci number to 0 and the 2nd fibonacci number ie at index 1 to 1. Then with a for loop 
that starts at index 2 to index n-1 ie for idx in range(2,len(n)) or conversely with a while loop that uses a counter equal to the ith 
fibonacci number ie start from the 3rd fibonacci number to the nth fibonacci number, remembering to increment the counter every time, we add 
the fibonacci number in the array[i] = array[i-1] + array[i-2]. We have to handle the edge cases of n <=1 before the loop. Now since we 
realize that we only ever use the two preceding numbers we only need to store two values therefore instead of initializing an array of length 
n, we initialize an array that contains two numbers, fib(1)=0 and fib(2)=1. Then using the for loop or while loop above, we start calculating 
from fib(3), update fib(0) = fib(1) and fib(1) = current. At the end we return the second value in the array if n>1 else the first value in
the array. The recursive approach extends from drawing the recursion tree. So the base is as before and the recursive case is 
fib(n) = rec(n-1) + rec(n-2). This will make a pair of calls at each stage and it take up to n pair of calls to reach a base case at most,
therefore the time is 2^n and space is O(n) for the max calls on the recursive stack. This solution can be improved with memoization which
is first seeded with memoize[1] = 0, memoize[2] = 1, here with a default value in the recursive function. Then the base case is to check if
memoize[n] is in the hashtable. If it is, we return memoize[n]. Otherwise we get and store memoize[n-1] = rec(n-1] and memoize[n-2] = rec(n-2),
then memoize[n] is stored as memoize[n] = memoize[n-1] + memoize[n-2] before returning memoize[n]. Since there are n unique calls, there will
be at most n calls on the call stack leading to a linear time and space complexity."""

"""The "brute" force or naive approach. Define the base cases for first
and second fibonacci numbers which are zero and one and after that the nth
fibonacci number is the sum of the previous two fibonacci numbers"""
#O(2^n) time | O(n) space
def getNthFib(n):
    if n == 1: #first fibonnaci number, base case
        return 0
    elif n == 2: #second fibonacci number, base case
        return 1
    else: #recursive case, n > 2
        return getNthFib(n-1) + getNthFib(n-2)



"""Memoization recursive solution, which stores the result of function calls an
and allows constant time access when needed elsewhere"""
#O(n) time | O(n) space
def getNthFibI(n,memoize = {1:0,2:1}):
    
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFibI(n-1,memoize) + getNthFibI(n-2,memoize)
        return memoize[n]



"""Iterative solution, where we store the last fibonacci numbers in an array"""
#O(n) time | O(1) space
def getNthFibII(n):

    lastTwo = [0,1]
    counter=2
    
    while counter < n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    
    return lastTwo[1] if n > 1 else lastTwo[0]  #take care of edge case



print(getNthFibII(2))
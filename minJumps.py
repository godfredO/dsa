"""Naive dynamic programming solution where we iterate through the array. At each step, we iterate from the start of array
to our current position. We ask can we get here from there, by adding the index of there to the jumps stored there. If this
sum is greater than the index here, we can get here from there. If we can, then the jumps to get here is the minimum between
the jumps stored there plus one or the current jump stored here. Thus the last value in jumps array will be the minimum jumps
between start of array to end of array"""
#O(n^2) time | O(1) space
def minNumberOfJumps(array):
    jumps = [float("inf") for x in array] #store minimum number of jumps from start of array to current index
    jumps[0] = 0 #0 jumps from start of array to start of array

    for i in range(1, len(array)): #start from second value
        for j in range(0,i): #from start of array to current index, exclusive
            if array[j] + j >= i: #if we can get to i from j ie by taking array[j] jumps starting from j
                jumps[i] = min(jumps[j]+ 1, jumps[i])
    return jumps[-1]

"""Optimal solution. The idea behind this solution is that at each point, in our array, with the maximum number of jumps at an 
index, we can reach a number of possible destinations. To minimize the number of jumps from the start of array to the end of the
array, we need to choose the destination that has the greatest jump stored there. To do this we start from the first value, initialize
maxReach and steps variables as the first value in the array. We take our steps and maximize the max reach and decrement the steps variabel
When steps reaches zero, we know we must have chosen the destination with the greatest jumps stored there and so we increase our jumps 
variable by 1. Also we need to know how many steps we would have remaining from having chosen the destination with the greatest jump, which
will be equal to the maxReach variable minus our current index and then we continue, chosing the maxreach possible  and decrementing the steps
and when steps reaches zero, we increse our number of jumps taken and reset the steps as the number of steps remaining had we started from
the destination that gave the maxreach"""
#O(n) time | O(1) space
def minNumberOfJumps(array):
    if len(array) == 1: #edge case, if there is only one element in array
        return 0        #no step needed to go from start to end 
    maxReach = array[0]
    steps = array[0]
    jumps = 0
    for i in range(1, len(array) - 1):#second to penultima positon, from penultimate position, we need one more jump to reach end of array
        maxReach = max(maxReach, array[i] + i)
        steps -= 1 #used up one of the steps stored at previous point
        if steps == 0:
            jumps += 1 #chosen the best jump from previous jumps' destinations
            steps = maxReach - i #reset steps to be steps remaining at current index had we taken best jump from the previous jumps' destinations
    return jumps + 1 #from the penultimate position we need one more jump to end







array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
print(minNumberOfJumps(array))
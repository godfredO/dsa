"""The input is two positive integers representing the height of a staircase and the maximum number of steps that you can advance up the
the staircase at a time. The question asks to write a function that returns the number of ways in which one can climb the staircase. eg
if height = 3 and maxSteps = 2, you could climb the staircase in 3 ways. You could take 1,1,1 steps,  2,1 steps , or 1,2 steps. 
This question's structure reminds me of the 'Number Of Ways To Traverse A Graph' question. In that question we could only move right or
down. Here we can only take up to k steps. This means if we find ourselves at step height - k, we can directly take k steps to the top
of the stairs. So if height= 3 and maxSteps= 2 then if we get to height (3-2) ie 1 or height (3-1) ie 2 we can take take 2steps or 1 step
to get to the height. 
So the number of ways of going to height by taking k steps is the sum of the number of ways of getting to (height-1)+
(height-2) + ... + (height - k) steps becausee if we get there we just take 1 or 2 or,...,k steps and we are at the top of the stairs.
So that is what the recursive solution does we call the recursive function for each of these (height-s) wherre 1<= s<= k and sum them up.
But what is the base case? Well recursion/dynamic programming always start with the buffer choice, so to speak. So how many ways to get
to a height of 0, 1 way ie do nothing. Similarly if how many ways can we get to height of 1, 1 way ie taking one step. Note that we are
always able to take 1 step. So the base case is if height== 0 or height == 1, return 1. We are also assured that maxSteps oor k will 
always be less than or equal to height. So if height is 4, and we can only take 1 step, we will call rec(3) which will call rec(2) which
will call rec(1) which will return 1, and that will bubble up. So the key is realizing that we can continuously divide till we reach the
base case solve the answer for a particular height-step call and use it in other calculations. So the first solution, is pure fibonacci
numbers-esque recursion. This solution is improved by realizing that memoization reduces the repeated calls.

The initial dynamic array solution is an iterative version of the memoization step. We initialize a data structure for every height 
including 0 height ie len(height) + 1, and update the value at index 0 and index 1 to 1, since index will represent the height. The first
dynamic array solution then starts filling out the data structure from height 2 up to the height, that is currentHeight = range(2,height+1).
The for each current height we initialize the first step to be one and use a while loop to add up all values up to currentHeight - maxSteps.
Since maxSteps will be greater than some current height ie if current height is 2 and maxSteps = 3, the while loop's condition is while
step <= maxSteps and step <= currentHeight. Thus we update the values from current height of 2 to current height = height. After each update
we increment step by 1 to go to the next step up to maxSteps. The second re-write of this solution uses a for loop instead of a while loop.
In that case step varies from  1 to the min(maxSteps, currentHeight) ie for step in range(1, min(currentHeight, maxSteps)+1). And as always
the +1 in the range function is due to the end-exclusivity.

The final and optimal solution is realizing that say maxSteps is 3 and we are calculating the number of ways of reaching height 5, then
ways[5] = ways[4] + ways[3] + ways[2]. Similarly for height=6, ways[6] = ways[5] + ways[4] + ways[3]. Thus comparing the addends of ways[6]
and ways[5], ways[6] = ways[5] - ways[2] + ways[5] ie since ways[4]+ ways[3] = ways[5] - ways[2] and there is the ways[5]. 
So we can say that ways[6] = 2* ways[5] - ways[2] , and here ways[2] is the value that is just out of the window and ways[5] is the value
that is just in the window when we get to ways[6]. So we can calculate a variable, endOfWindow = currentHeight - maxSteps - 1 and if this
value is greater than or equal to 0, we subtract it from 2*ways[currentHeight-1] - ways[endOfWindow] otherwise we just use 
2*ways[currentHeight - 1]. That is as step varies from 1..maxSteps, insted of summing up ways[height- 1] + ... + ways[height-maxSteps] and 
that is on O(k) solution ie sum up values in a window of currentHeight - 1 to currentHeight - maxSteps, what we do is when we go to the next 
higher height we keep every addend from the previous height calculation except currentHeight - maxSteps - 1 and add the previous height
which will be the new currentHeight - 1. So if we can just increment the currentHeight's value by adding currentHeight - 1  which we just 
calculated and remove currentHeight - maxSteps -1, we will improve the O(k) operation, and make it O(1), thus improving the overall time
complexity.
"""

# O(k^n) time | O(n) time
def staircaseTraversal(height, maxSteps):
    return numberOfWaysToTop(height,maxSteps)


def numberOfWaysToTop(height,maxSteps):
    if height <= 1:
        return 1  #since height,maxSteps >= 1 
    
    numberOfWays = 0
    #as we loop we decrease the height considered but maxSteps stays the same so
    #we need the min function to ensure that when recursive call has a height less than step, we go down height step
    #max steps we height-min(height,maxsteps) = 0 eg if height = 1 and maxStep = 2 we can do rec(1-1) but not rec(1-2)
    for step in range(1, min(maxSteps,height)+1): #the + 1 is so that we include the given height, steps we can take 1<=s<=maxSteps
        numberOfWays += numberOfWaysToTop(height - step, maxSteps) #answer is the sum of ways of getting to these steps
    
    return numberOfWays



# O(k*n) time | O(n) time
def staircaseTraversalII(height, maxSteps):
    return numberOfWaysToTop(height,maxSteps, {0:1,1:1})


def numberOfWaysToTop(height,maxSteps, memoize):
    if height in memoize:
        return memoize[height]
    
    numberOfWays = 0
    #as we loop we decrease the height considered but maxSteps stays the same so
    #we need the min function
    for step in range(1, min(maxSteps,height)+1):
        numberOfWays += numberOfWaysToTop(height - step, maxSteps,memoize)
    
    memoize[height] = numberOfWays

    return numberOfWays

#O(k*n) time | O(n) space
def staircaseTraversalIII(height, maxSteps):
    waysToTop = [0 for _ in range(height + 1)]
    waysToTop[0] = 1
    waysToTop[1] = 1

    for currentHeight in range(2, height + 1):
        step = 1  #this is our iterator to keep calculating number of ways and updating waysToTop
        while step <= maxSteps and step <= currentHeight: #go up to height - maxstep without going negative 
            waysToTop[currentHeight] = waysToTop[currentHeight] + waysToTop[currentHeight - step]
            step += 1

    return waysToTop[height]

#O(k*n) | O(n) this uses a for loop to keep step between maxSteps and currentHeight
def staircaseTraversalIV(height,maxSteps):
	numberOfWays = [0 for _ in range(height+1) ]
	numberOfWays[0] = 1
	numberOfWays[1] = 1
	
	for currentHeight in range(2,height+1):
		waysToCurrentHeight = 0
		for step in range(1,min(maxSteps,currentHeight)+1):
			waysToCurrentHeight += numberOfWays[currentHeight-step]
		numberOfWays[currentHeight] = waysToCurrentHeight
	return numberOfWays[-1]

#O(n) time | O(n) space - we convert the O(k) step to constant time
def staircaseTraversalV(height, maxSteps):
    currentNumberOfWays = 0   #value to be used in loop
    waysToTop = [1]  #initialize ways to traverse list with number of ways when height is zero

    for currentHeight in range(1,height + 1):
        #for subtracting value removed by shifting window so more precisely called justoutofstartofwindow
        startOfWindow = currentHeight - maxSteps -1  
        #actual end of window
        endOfWindow = currentHeight - 1  

        #start subtracting when a valid justoutofstartwindow value is found
        if startOfWindow >= 0:
            currentNumberOfWays -= waysToTop[startOfWindow]
        
        #keep adding last value in window
        currentNumberOfWays += waysToTop[endOfWindow]
        #update ways to traverse
        waysToTop.append(currentNumberOfWays)
    
    return waysToTop[height]

#O(n) time | O(n) space - same as solution above and below
def staircaseTraversal(height, maxSteps):
    ways = [0]*(height+1)
    ways[0] = 1
    ways[1] = 1
    for currentHeight in range(2, height + 1):
        endOfWindow = currentHeight - maxSteps - 1
        if endOfWindow >= 0:
            ways[currentHeight] -= ways[endOfWindow]
        ways[currentHeight] += 2* ways[currentHeight - 1]
    return ways[-1]

#O(n) time | O(n) space - same as the the two solutions above
def staircaseTraversal(height, maxSteps):
	ways = [1]
	currentNumWays = 0
	
	for currentHeight in range(1, height + 1):
		endWindow = currentHeight - 1
		currentNumWays += ways[endWindow]
		
		startWindow = currentHeight - maxSteps - 1
		if startWindow >= 0:
			currentNumWays -= ways[startWindow]
		
		ways.append(currentNumWays)
	return currentNumWays


height=4
maxSteps = 2
print(staircaseTraversalIV(height,maxSteps))
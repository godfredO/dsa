"""The question gives an array of points ie 2-d arrray and asks to write a function that returns the maximum number of points that fall
on any single line. The input array will never contain duplicate points and will always contain at least one point. So the solution 
uses a double nested for loop to choose p1 and p2, calculates the slope between the two points and stores the slope in a dictionary after
hashing. The main helper function here is the calculation of the slope. We unpack the two points and initialize a slope to store for when
our slope is vertical. Since we initialize a hashtable with each choice of p1, a vertical line here will represent the vertical line that
goes through the x-coordinate of p1. Also to ensure consistency, we reduce the delta x and delta y of each slope to the smallest possible 
form. This is done with a very clever helper function that swictches two pointers and does a modulo of one pointers value at each switch
until one of the pointed values points to 0 at which point we know that the other remaining value which was the denominatior of the last
swich modulo operation is the greatest divisors of the input number. It is important that when passing deltaX and deltaY into the divisor
helper functions, we pass their absolute values so that we get positive divisors. After reducing the delta x and delta y, we also ensure 
that we move any negative to the top value ie. if delta x is negative, we want to make that positive and  make delta y negative. If both 
are negative we  want to make both positive. The slope here is going to be represented as a hashed key of delta y, delta x, after reducing 
to lowest numbers, handling negatives or if a vertical line through p1. We increment the slope in the hashtable of the current p1. Every
slope has two points so in the general case we increment by 1 for the current p2 since we would have already counted p1 the very first time 
the slope was added to the current p1's hashtable. Thus in the case where case where a slope is added for the first time, we first add 1
for p1 and then increment to 2 for p2, afterward, we only add 1 for the current p2. We then loop through all the values of slope keys for 
the current p1, choose the maximum value as this represents the maximum number of points that lie on any line with the current p1 and then 
update global maximumPointsOneLine with the maximum we ever find. We initialize this global value at 1 because we know that each point will 
at least form a line with every other point, with the exception of where we are passed a 2-d array with only 1 point, in which case wee
return 1. Also, because the inner for loop starts after the current idx of the first for loop, when idx1=len(points) -1 ie last point, 
slopes will be empty since idx2 inner loop wont run thus we need a default of 0 to handle that edge case."""


"""The optimal solution for this problem is to loop through the array of points. At each step, we choose a point one ,initialize a hashtable 
to store slopes and loop through the array again for p2. With p1 and p2 we calculate slope and count the number of points that give a specific 
slope as p2 when p1 is fixed. That is for every p1 we initialize a new hashtable. At the end of each step, we calculate the maximum number of 
points that lie on any slope with p1 fixed. Then we move p1 and repeat this step. The main complication of this question is in hashing our 
slopes due to floating point precision."""


#O(n^2) time | O(n) space
def lineThroughPoints(points):
    maxNumberOfPointsOnLine = 1 #we know we will be given at least 1 point so initialize as such

    for idx1, p1 in enumerate(points): #pick point1
        slopes = {} #initialize a new slopes hashtable with each pick of point1
        for idx2 in range(idx1+1,len(points)): #to avoid repeatition
            p2 = points[idx2]
            rise,run = getSlopeOfLineBetweenPoints(p1,p2) #get numer, denom of slope
            slopeKey = createHashableKeyForRational(rise,run) #create a hashable rational
            if slopeKey not in slopes: #add slope to slopes hashtable
                slopes[slopeKey] = 1 #add 1 point for the point1 pick, ie a slope always has 2 points, p1 and p2
            slopes[slopeKey] += 1 #update value stored in slopes for specific slope
        #when idx1=len(points) -1 ie last point, slopes will be empty since idx2 inner loop wont run
        #thus we need a default of 0 to handle that edge case
        maxNumberOfPointsOnLine = max(maxNumberOfPointsOnLine, max(slopes.values(), default=0))
    return maxNumberOfPointsOnLine

def getSlopeOfLineBetweenPoints(p1,p2):
    p1x, p1y = p1
    p2x, p2y = p2
    slope = [1,0] #a vertical line has no slope so we would hash this for a vertical line
    if p1x != p2x: #if x value are the same, its a vertical line otherwise its not
        xDiff = p1x - p2x
        yDiff = p1y - p2y
        gcd = getGreatestCommonDivisor(abs(xDiff), abs(yDiff)) #to have a reduced rational slope
        xDiff = xDiff // gcd #reduce denominator,floor division to avoid .0 at end
        yDiff = yDiff // gcd #reduce numerator,floor division to avoid .0 at end
        if xDiff < 0: #if denominator xDiff is neg move neg to top. If both neg, make both positive
            xDiff *= -1
            yDiff *= -1
        slope = [yDiff,xDiff] #[numerator,denominator]
    return slope

def getGreatestCommonDivisor(num1, num2): #gcd formula
    a = num1
    b = num2
    while True:
        if a == 0:
            return b
        if b == 0:
            return a
        a,b = b, a % b

def createHashableKeyForRational(numerator,denominator):
    return str(numerator) + ":" + str(denominator)
    



points = [
    [1, 1],
    [2, 2],
    [3, 3],
    [0, 4],
    [-2, 6],
    [4, 0],
    [2, 1]
  ]
print(lineThroughPoints(points))
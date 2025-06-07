"""The input is two integers, width and height, representing the width and height f a grid-shaped rectangular graph. The question asks 
to write a function that returns the number of ways to reach the bottom right corner of the graph starting at the top left corner. Each
move must either go down or right. In other words, you can never move up or left in the graph. eg if width =2 and height = 3 
the number of ways is 3 ie right, down, down ; down, right, down ; down,down, right. Note that you may assume that width * height >= 2.
In other words, the graph will never be a 1x1 grid. """




"""Recursive solution based on the idea that since we can only movedown and right we can only reach the ending position by movig downward
from the square above or moving right from the square on the left and recursively repeating this thought process on smaller grids until 
a base case are reached which is all squares with height / width = 1 have only one way to reach their endiing position. Because we can
only move downward and rightward, the only way to reach the ending position is by moving downward from the grid above or moving rightward
from the grid to the left of the ending position. Thus if we are able to figure out how many ways to reach the squares above and to the 
left of the ending position from our starting position, we will know how many ways to reach the ending position from the starting position
which will be the sum of the number of ways to reach those squares from the starting position. Now the way the question is setup, we model
the graph or grid as having a top left corner coordinate of (width,height) and the right corner coordinate of (1,1). Moving rightward 
involves decrementing the width by 1; moving leftward involves decrementing the height by 1. All squares to the left of the ending position
will have the same height as the ending position ie 1. All squares above the ending position will have the same width as the ending position
ie 1. Thus in the recursive solution the base case is when we call the recursive function with width/height = 1 in which case we return 1
for 1 way to reach the ending position (ie going straight down or right). The recursive case is summing up the returned values from 
decrementing height and width at each step until the base case is reached. Since from each recursive call we make two additional calls there
will be up to n+m pairs of recursive calls until base case is reached. This can be verified by drawing the recursive tree from a root with
coordinates (width, height) and having the left child have a coordinate of (width -1, height) and the right child have a coordinate of
(width, height - 1) until the base case where either width or height = 1. For example if we start a starting position of (3,3) we have a
total of 5 pairs of calls until we reach the base cases where width or height = 1 ie 2^5 where 2 is represents a pair of recursive calls
repeated 5 times which is in the order of 2^6 or O(2^(n+m)) time, and we reach the base case after at most (n+m)/2 calls so the space 
complexity so space complexity is O(n+m). By summing up all the 1's returned by reaching a base case, we get the total number of ways to
reach the ending position from the starting position."""

#O(2^(n+m)) time | O(n+m) space, n = width, m = height
def numberOfWaysToTraverseGraph(width,height):
    if width == 1 or height ==1: #base case when we reach destination
        return 1
    return numberOfWaysToTraverseGraph(width -1, height) + numberOfWaysToTraverseGraph(width, height -1) #go right, go down


"""Recursive solution with memoization. """
#O(n*m) time / O(n+m) time  | O(n*m) time / O(n+m) space - not sure, I added memoization
def numberOfWaysToTraverseGraph(width, height):
	memoize = {}
	return helper(width, height, memoize)

def helper(width, height, memoize):

	key = getHashableKey(width, height)
	if key in memoize:
		return memoize[key]

	if width == 1 or height == 1:
		return 1

	rightKey = getHashableKey(width - 1, height)
	downKey = getHashableKey(width, height - 1)

	memoize[rightKey] = helper(width - 1, height, memoize)
	memoize[downKey] = helper(width, height - 1, memoize)
	
	memoize[key] = memoize[rightKey] + memoize[downKey]
	return memoize[key]
	

def getHashableKey(width, height):
	return str(width) + ":" + str(height)


"""Dynamic programming solution where we use a two dimensional array to store the intermediate results. Dyanamic programming solution have
a inverse sort of relationship with recursive solutions to problems. That is in recursion, we start from the recursive case and work our
way down to the base case. In dynamic programming solutions we start from the base case and work our way up to the recursive case. Thus
in this dynamic programming approach, we use a 2d array of a matrix of size width * height, and thus the widthIdx will range from 0-width
and the heightIdx will range from 0-height. The choice of a matrix as the data structure is obvious since we are dealing with a grid.
In the code we do this by initializing the matrix with matrix = [[0 for _ in range(width+1)] for _ in range(height+1)]. Note that we fill 
the entire matrix initially with 0's and there is a co-ordinate (0,0) which is typical of dynamic programming solutions where we start from 
0 or empty string or some sort of none value. In fact the entire first column is a buffer column though typically we have a buffer row.
Now in the double nested for loop we actually go down column by column instead of the typical row by row. In other words for each column
we fill out all the rows in that column from top to down, starting from the second column to the last column, thus skipping the buffer
column each time. Then we say that if either the widthIdx == 1 or heightIdx == 1, we update the matrix value at that position to be 1 ie
matrix[heightIdx][widthIdx] = 1. Since this "2D array" is a list of lists so you have to select the row first then the column. In the else
case we look above for the numberOfWays above and we look to the left for the numberOfWays to the left and add up to give the numberOfWays
at the current position. Now, it is standard practice to have a buffer row and buffer column in dynamic programming solutions so row with
index 0 and column with index 0 will always have value 0 and is used here to simplify the code for two reasons; one we 
start looping from colIdx=1 and rowIdx=1 ( colIdx = widthIdx, rowIdx = heightIdx) and two rowIdx=1 or colIdx=1 is actually our base case.
So instead of filling up the rowIdx=1 with 1's and colIdx= 1 with 1's, the buffer row actually allows us to add these as part of the loop.
That is to say, we could have had a code that doesn't have this buffer row/column and we would have had to fill them with 1's initially
instead of the 0's for the base case row but then we would have needed a separate loop to fill out the base case case columns. Here we are
able to simplify the code and utilize the same base case conditions because of the use of a buffer row and column. Anyway at the end we 
return the number of ways at height and width. """
#O(n*m) time | O(n*m) space
#Add one row/colum of 0's to simplify indexing (Python's zero index)
def numberOfWaysToTraverseGraphI(width,height):
    numberOfWays = [[0 for _ in range(width+1)] for _ in range(height+1)]
    
    #loop through column by column and in each column , go down the rows
    for widthIdx in range(1,width +1): #make sure to skip the buffer column
        for heightIdx in range(1,height + 1): #make sure to skip the buffer row
            if widthIdx ==1 or heightIdx == 1: #base case, this also includes when rowIdx == 1 and colIdx == 1
                numberOfWays[heightIdx][widthIdx] = 1 #select the list first then the index in the list
            else:
                #note that this "2D array" is a list of lists so you have to select the
                #correct list using height and then index into it using width
                waysLeft = numberOfWays[heightIdx][widthIdx-1] #square left of current
                waysAbove = numberOfWays[heightIdx-1][widthIdx] #square above current
                numberOfWays[heightIdx][widthIdx] = waysLeft + waysAbove

    #select the last array and the last value in that array            
    return numberOfWays[height][width]


""""Dynamic programming solution without the use a buffer row/column. Remember it is essential to always start from the base case in
order to see what can be removed or optimized in order to maintain the same logic. In this solution we also go row by row instead of
column by column in the previous solution. Personally row by row is preferred. Also a solution with a buffer row and buffer column
is personally preferred. """
#O(n*m) time | O(n*m) space
def numberOfWaysToTraverseGraph(width, height):
	matrix = [[1 for _ in range(width)] for _ in range(height)]
	
	for rowIdx in range(1, height):
		matrix[rowIdx][0] = 1
	
	for row in range(1,height):
		for col in range(1,width):
			waysAbove = matrix[row - 1][col]
			waysLeft = matrix[row][col -1]
			matrix[row][col] = waysAbove + waysLeft
	return matrix[height - 1][width - 1]

"""Dynamic programmig solution with the use of a buffer row/column in order to use the same base case conditions, but instead of 
storing a width*height matrix, we store two rows of length, width."""
#O(n*m) time | O(n) space - where n is the width of the graph and m is the height 
def numberOfWaysToTraverseGraph(width, height):
	evenEdits = [0 for _ in range(width + 1)]
	oddEdits = [0 for _ in range(width + 1)]
	
	for rowIdx in range(1, height+1):

		if rowIdx % 2 == 1:
			currentEdits = oddEdits
			previousEdits = evenEdits
		else:
			currentEdits = evenEdits
			previousEdits = oddEdits

		for colIdx in range(1, width + 1):

			if rowIdx == 1 or colIdx == 1: #this also includes when rowIdx == 1 and colIdx == 1
				currentEdits[colIdx] = 1
			else:
				waysAbove = previousEdits[colIdx]
				waysLeft = currentEdits[colIdx - 1]
				currentEdits[colIdx] = waysAbove + waysLeft

	return evenEdits[-1] if height % 2 == 0 else oddEdits[-1]


"""Dynamic programming solution with the use of a buffer row / column in order to use the same base case conditions, but instead of
storing a width*height matrix, we store two rows of length min(width,height)."""
#O(n*m) time | O(min(n,m)) space - where n is the width of the graph and m is the height 
def numberOfWaysToTraverseGraph(width, height):

	small = width if width < height else height
	big = width if width >= height else height

	evenEdits = [0 for _ in range(small + 1)]
	oddEdits = [0 for _ in range(small + 1)]
	
	for rowIdx in range(1, big+1):

		if rowIdx % 2 == 1:
			currentEdits = oddEdits
			previousEdits = evenEdits
		else:
			currentEdits = evenEdits
			previousEdits = oddEdits

		for colIdx in range(1, small + 1):

			if rowIdx == 1 or colIdx == 1: #this also includes when rowIdx == 1 and colIdx == 1
				currentEdits[colIdx] = 1
			else:
				waysAbove = previousEdits[colIdx]
				waysLeft = currentEdits[colIdx - 1]
				currentEdits[colIdx] = waysAbove + waysLeft

	return evenEdits[-1] if big % 2 == 0 else oddEdits[-1]
	


"""Mathematical solution based on the idea that each way of traversing the graph is some permutation of width-1 rightward movements and 
height-1 downward movements. Thus if total movements = width -1 + height -1, then problem becomes the number of ways of permuting 
"total movements" objects with "width -1" repetitions and "height -1" repetitions. Eg if width is 5 ie starting point has a width of 4, 
if we keep moving right and thus keep decrementing width by 1, we go width = 4, width = 3, width = 2, width = 1 and at this point we 
go straight down to the ending position. Thus we make a total of 4 (width -1) rightward movements and this is always the case. Every way 
from the starting point to the ending point will include width - 1 rightward movements. If the height of the starting point is 4, we
will keep moving down and thus keep decrementing width by 1 , we would go height = 3, height = 2, height = 1 and at this point we go
straight right to the ending position. Thus we make a toal of 3 (height - 1) downward movements and this alwys the case. Every way from
the starting point to the ending point will include height - 1 downward movements. Thus totalMovements = totalRightWard + totalDownward
where totalRightWard = width - 1  and totalDownward = height - 1. So in the example where the starting position has a coordinate of
(width=5, height=4) a valid way will look something like  [R,R,R,R,D,D,D] or [D,D,D,R,R,R,R] or  [D,R,D,R,D,R,R] or [D,R,R,R,D,R,D].

This observation thus reduces the question to the number of ways of permuting totalMovements number of objects that includes
totalRightWard repeated objects and totalDownward repeated objects. Calculating any of these variables involves simple subtraction and
addition. The crux of this mathematical approach thus becomes how to implement a factorial function in order to evaluate the permutation
ie numberOfWays = (totalMovements)! / ( (totalRightward)! * (totalDownward)! ). To write a factorial function we initialize the product
as 1 then use a loop to generate multipliers between 1 and num. To generate these numbers we use Python's end-exclusive range function so
for multiplier in range(1, num+1) where the +1 is due to the end-exclusivity of the range function. Then inside the loop we update the
product by multiplying it with the mulitplier. At the end of the loop we return the updated product. The factorial function is called 
on totalMovements, totalRightWard and totalDownWard in order to yield (totalMovements)! , (totalRightward)! and (totalDownward)!.
This loop runs n+m times for totalMovements, n times for totalRightWard, m time for totalDownward. With the factorial values we then use
a simple division to return the answer. As a result the time complexity is O(n+m) time and O(1) space since we only store a couple
of variables. """

#O(n+m) time | O(1) space
def numberOfWaysToTraverseGraphII(width,height):
    #number of possible rightward movements along width, from starting position to corner
    numOfRightMoves = width -1  
    #number of possible downward movements along height, from starting position to corner
    numOfDownMoves = height -1 
    totalMoves = numOfRightMoves + numOfDownMoves #can only move down and right
    num, denom1, denom2 = factorial(totalMoves), factorial(numOfRightMoves), factorial(numOfDownMoves)
    #floor division just a precaution, if input is valid we should get an integer answer
    answer = (num) // (denom1*denom2)
    return answer

def factorial(num): #this loop runs n+m times for totalMoves, n times for numRightMoves, m time for numDownMoves
    fact = 1  #initialize at 1
    for i in range(1,num+1): #n+1 to include n in loop (Python's zero index)
        fact *= i
    return fact



width = 4
height = 3
print(numberOfWaysToTraverseGraphII(width,height))

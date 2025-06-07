"""This is another application of binary search where we move intelligently based on sorted order. The values in a row are sorted in 
ascending order and the values down a column are also sorted in ascending order and all values are distinct. Now any value in the matrix 
divides the matrix (graph) into four quadrants, the upper left, upper right, lower left, lower right. Due to the sorted order we know 
that any given number is greater than all the numbers to its left in the same row and above it in the same column. In the same vein any 
number is is less than all the numbers to its right in the same row and below it in the same column. Another way of saying it is that any 
number is greater than all the values in the upper left quadrant (left and above) and less than all the values in the lower right quadrant 
(right and below). Thus while a single value can give as accurate information about the upper left and lower right quadrants, it doesnt 
give any information about the upper right qudrants and the lower left quadrants since these contain a mixture of greater than and less 
than. The reason for all this rant is to say that the starting point of our algorithm must be in the top right corner of the matrix or in 
the bottom left corner in the matrix since these give the most variability. Another way of explaining the starting position is as follows, 
we can start at the top left corner, the top right corner, the bottom left corner or the bottom right corner. In the top left corner the 
numbers are in ascending order as we go down the row and down the column. Similarly in the bottom left corner the values decrease as we go 
down the row on the left or up the column above. Thus if we compared the target to the bottom right corner and found it to be greater, we 
would have no where to go since the remaining values in the row to the left and the remaining values in the column above are all less than 
the bottom left corner. The same thing happens if we start at the top left corner and find that our target is less than the current value, 
we would have no way of moving since the remaining values in the same row and column as the current value are all greater than our current 
value. However if we start from the top right corner, values increase down the column and decrease up the row. Similarly if we start from 
the bottom left corner, the values decrease up the column and down the row. So the only valid starting points are the bottom left corner
or the top right corner.

With the starting point chosen, here as the top right corner of the matrix, we compare the number at the current position to the target. 
If the current number is bigger than the target number aka if the target is less than the current number, eliminate every number below 
and to the right of the number of the current postion. We do this by decrementing column by 1. If the current number is smaller than the 
target number aka the target is bigger than the current number, eliminate every number to the left of and above the chosen number. We do 
this by increasing the row and since our starting point is in the top right corner we know we will not go back. Thus at any point we can 
either adjust the row or the col but not both, we start from a position of great variability and we ask ourselves, which parameter, row, 
or col can we increment or decrement to give get us closer to finding the target value based on a comparison with the current value and
our knowledge of the sorted order of the rows and columns in the matrix."""


#O(n+m) time | O(1) space
def searchInSortedMatrix(matrix,target):
    row = 0 #top row
    col = len(matrix[0]) -1 #last value in the first row

    while row < len(matrix) and col >=0: #while we havent run out of array
        if matrix[row][col] > target: #eliminate all the numbers largest than current number
            col -=1
        elif matrix[row][col] < target: #eliminate all the numbers smaller than current number
            row += 1
        else:
            return [row,col]
    return [-1,-1]


"""Moving in the other starting point of greatest variability and moving one step at a time. When we start from the bottom left corner, 
we can only go up the rows or down right the columns. Thus in here we increment col, decrement row. In the previous solution we decrement
col and increment row. Also the loop conditions reverse. From this starting point we go in the direction that gets us closer to the target
and eliminates the direction that gets us farther away from the target."""

def searchInSortedMatrix(matrix, target):
    row = len(matrix) - 1
    col = 0

    while row >= 0 and col < len(matrix[0]):
        if matrix[row][col] < target:
            col += 1
        elif matrix[row][col] > target:
            row -= 1
        else:
            return [row,col]
    return [-1, -1]
            






matrix= [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
  ]
target= 44
"""First off, this question gives me spiralTraverse question but if someone just wanted it to be more complicated. Zigzag order starts
from the top left corner, goes down one element, and proceeds in a zigzag pattern all the way down to the bottom right corner. Zigzag
order includes four movements based on the current location, straight down, diagonal up, straight right, diagonal down. We keep making 
the appropriate movement for the current position as long as we are in bounds. So zigzag movements are going to described by 
row, col, height, width , in addition to a goingDown boolean as opposed to the startRow, endRow, startCol, endCol of spiral traverse.

Anyway, we start by appending the top left corner value. In fact, in this iteration, when passed (row, col, height, width), we append
the value at array[row][col], then decide on the next move. If we are going down, and we're not in the first column or the last row,
we must be going diagonally down, so we increment row and decrement column to to move diagonally down. If we are in the first column
or last row, we know that we will not keep going further diagonally down (after we have already appended the current value), so we
change goingDown boolean to False, then check which of these conditions we are actually in ie first column or last row. If in the last 
row, we move straight right by incrementing column. If in the first column we go straight down by incrementing row. Thus we in the 
general going down case, (not first column or last row), we keep going down diagonally, after appending current value. In the case of 
first row or last column, we change direction first and if in the first column we go straight down, if in the last row we go straight 
right. What happens if goingDown is False, ie when going up. When going up, the general case is when we are not in the first row or 
the last column, in which case we must be moving diagonally up, which means decrementing row and incrementing column. In the other
case where we are in the first row or last column, after appending the current element, we change directions by setting goingDown to
be True and then depending on the particular situation we make our next move. If in the first row, we go straight right by only
incrementing column; if we are in the last column, we go straight down by incrementing only row. Thus the height and width parameters
tell us when to change direction and the conditon depends on the current direction. If going down, we check if its time to go up next
by checking if col == 0 or row == height; if going up, we check if its time to go down next by checking if row == 0 or col == width.
This way we know that after the next value is appended, the direction will be changed. Also by height, we mean the last row, and by
width we mean the last column as these need to be defined outside the while loop and will be used to check if out of bounds. A 
particular position is in bounds if row is between 0 and last row and if col is betwen 0 and last column. It is essential to use 
row == height and col +=1 in the case when direction changes when going down instead of col == 0 and row+=1 , why? Because in the 
case where we are in the first column and last row we want to move straight right instead of straight down.  Similarly, it essential 
to use col == width and row +=1  in the case when direction changes when going up instead of row== 0 and col+=1 , why? 
Because in the case where we are in the first row and last column, we want to go straight down instead of straight right. """

#O(n) time | O(n) space
def zigzagTraverse(array):
    height = len(array) -1 #n of n x m 2-dimensional array
    width = len(array[0]) - 1 #m of n x m 2-dimensional array
    result = [] #output array
    row,col = 0, 0 #starting traversal position
    goingDown = True # initial direction boolean
    #while not out bounds, we continue zigzag traverse
    while not isOutOfBounds(row,col,height,width):
        result.append(array[row][col])
        if goingDown:
            #if direction is down, change direction if in first col or last row
            if col == 0 or row == height:#if in first col or last row
                goingDown = False #change direction to go up
                #essential to use row == height and col +=1 here instead of col == 0 and row+=1
                #why? when col == 0 and row == height we want col += 1
                if row == height: #if last row, go right after changing direction
                    col += 1 #go right
                else: #if first col, go down after changing direction
                    row += 1 #go down
            else: #if goind down, but not in first col or last row, move zigzag
                row += 1
                col -= 1
        else: #if going up, goingDown= False
            #if direction is up, change direction if in the last col or first row
            if col == width or row == 0: #if in last col or first row
                goingDown = True #change direction to go down
                #essential to use col == width and row +=1 here instead of row== 0 and col+=1
                #why? if col == width and row == 0 we want row += 1
                if col == width: #if last col, go down after changing direction
                    row += 1 #go down
                else: #if in first row, go right
                    col += 1 #go right
            else: #if going up, and somewhere in middle, move zigzag
                row -= 1
                col += 1
    return result
    
def isOutOfBounds(row,col,height,width):
    return row < 0 or row > height or col < 0 or col > width



array = [
    [1, 3, 4, 10],
    [2, 5, 9, 11],
    [6, 8, 12, 15],
    [7, 13, 14, 16]
  ]

print(zigzagTraverse(array))
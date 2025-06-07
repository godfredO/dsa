"""You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise). You have to rotate the image in-place, 
which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]                       Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[7,4,1],[8,5,2],[9,6,3]]                               Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

This is not a graph traversal problem; no dfs, bfs or union-find. This is an array traversal problem like spiralTraverse.py, zigzagTraverse.py
and builds on rotateArray.py, shiftLinkedList.py.

So we are assured that the matrix will be a square matrix so taking a 2x2 matrix you realize that the topLeft, topRight, bottomRight and 
bottomLeft all shift among themselves. bottomLeft goes to the topLeft, topLeft goes to the topRight, topRight goes to the bottomRight and
bottomRight goes to the bottomLeft. That is [[1,2][3,4]] becomes [[3,1][4,2]]. And this relationship between the corner values is always the
same no matter the size of the nxn matrix. Then after rotating the corner values of the outer perimeter of the matrix, we rotate the inner 
'rhomboid' of the outer perimeter as well. This will involve the middle values of the first row, first column, last row and last column.
This means in an nxn matrix, we have n-1 quartets for the outer perimeter. Then after rotating the outer perimeter, we can move inwards to
an inner perimeter. The inner perimeter of a 4x4 matrix is a 2x2 matrix and this will have 2-1 rotations ie the rotation that involves the
corner values as previously seen. That is we start with the outer perimeter of the nxn matrix, there will be n-1 quartets involving the values
in the outer perimeter, rotate the values for each of these quartets and then adjust the boundaries to move to an inner perimeter which will
be an (n-2)x(n-2) square and thus will involve (n-3) square quartets to be rotated and so forth and so on. So how do we determine which values
in a perimeter (startRow, endRow, startCol, endCol) belong to the same square quartet? The top row values will be going left to right starting
from the topLeft to the penultimate column in the first row, the endCol values will be going top to penultimate bottom row starting from the 
last column of the first row, the endRow values will be going right to left (ie reversed) starting from the last column to the second column 
of the last row and the startCol values will be going bottom to top (reversed) starting from the first column of the last row up to the first 
column of the second row. And we pick a value from each of these sets of n-1 values to form a quartet. So the corner values are on quartet. 
The second quartet will be the second values in each perimeter and so on and so forth. So this 90 degree clockwise rotation is startRow 
(left to right), endCol (top to bottom), bottomRow (right to left) then startCol (bottom to top). 

So just like spiralTraverse.py, we will be keeping track of the bounds of a perimeter with startRow, endRow, startCol, endCol, as the corners 
of the square or rhomboid represening the quartet of numbers we are swapping around. So we start with startRow = 0, endRow = lastRow, startCol 
= 0, endCol = lastCol. Note that this is a nxn matrix, so endCol = len(matrix) - 1 (equal to len(matrix[0]) - 1). Now this is going to be an 
O(n^2) time algorithm. We have one loop, a while loop,  to choose the boundaries of the perimeter and another loop to loop , a for loop, to 
generate indices for picking the values of any quartet. And after we finish handling all the quartet values that involve the outer perimeter 
of the matrix, we then incrementing / decrementing the boundaries, startRow, endRow, startCol, endCol, by one to move to the inner perimeter 
and swap all quartet of values in that perimeter. Also because this is a nxn matrix, the indices for startRow == startCol, endRow == endCol.
In the end I actually use left,right, top, bottom to store the indices for the corners of the perimeter and then we can use the (n-1) indices
generated in the for loop, as some sort of offset to pick out the values using these corners. This for loop is for index in range(right - left).
This is to reflect the proper boundaries of the perimeter we are considering after updating the boundaries. Also since startRow, endRow =
startCol, endCol due to nxn matrix, we only update on pair, here startCol (left) and endCol (right) and use these to initialize the top 
(startRow) and bottom (endRow).
The quartet values are matrix[top][left + index], matrix[top+index][right], matrix[bottom][right - index], matrix[bottom - index][left]. So for 
a 3x3 matrix where the outer perimeter has top = 0, bottom = 2, left = 0, right = 2, the indices used for the n-1 quartets are index ie 
range(right - left) = range(2)= 0,1. So when index= 0 this gives (matrix[0][0+0], matrix[2-0][0], matrix[2][2-0], matrix[0+0][2]) ie
matrix[0][0], matrix[2][0], matrix[2][2], matrix[0][2] and when index = 1 it gives (matrix[0][0+1], matrix[2-1][0], matrix[2][2-1], 
matrix[0+1][2]) ie matrix[0][1], matrix[1][0], matrix[2][1], matrix[1][2]. Then we increment left and decrement right to go to the inner 
perimeter.

When shifting any quartet, we will need temporary variables to store the value at a position before overwriting it, so that we can shift the 
temporary variable to a new location. Now, take a 2x2 matrix for example, if we first move the topLeft corner to the topRight, we will need 
a temporary variable for the topRight and before we move that to the bottomRight, we will need a temporary variable for the bottomRight and 
before we move that to the botomLeft we will need a temporary variable for the bottomLeft. So if we move in this order, we will need a
temporary variable for all except the topLeft corner making three temporary variables. But we can be clever and acutally use a single temporary
variable, by storing the topLeft value in a temporary varialbe, move the bottomLeft to the topLeft, then move the bottomRight to the bottomLeft,
then the topRight to the bottomLeft before finally setting the temporary variable to the topRight. So by starting from the last position and 
working our way backwards, we can write cleaner code.

"""



#O(n^2) time | O(1) space
def rotate(matrix):
    left , right = 0, len(matrix) - 1
    while left < right:
        top, bottom = left, right   #startRow == startCol, endRow == endCol for nxn perimeter
        for i in range(right - left): #generate indices for current perimeter , endCol - startCol
            topLeft = matrix[top][left + i]  #save the topLeft

            matrix[top][left + i] = matrix[bottom - i][left] #move bottom left into top left

            matrix[bottom - i][left] = matrix[bottom][right - i] #move bottom right into bottom left

            matrix[bottom][right - i] = matrix[top + i][right]  #move top right into bottom right

            matrix[top + i][right] = topLeft    #move top left into top right
        
        left += 1   #choose the bounds of next perimeter, by moving inwards
        right -= 1  #choose the bounds of next perimeter, by moving inwards
    
    return matrix   #delete this line on leetcode since the point is to modify in place







matrix = [[1,2,3],[4,5,6],[7,8,9]]                       
#Output = [[7,4,1],[8,5,2],[9,6,3]]      
print(rotate(matrix))                         


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
#Output = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
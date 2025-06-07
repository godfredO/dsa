"""Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the 
following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 
Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:
m == matrix.length ; n == matrix[i].length ; 1 <= m, n <= 100 ; -104 <= matrix[i][j], target <= 104.

So my first solution here is exactly the same as the solutioin in searchInSortedMatrix.py and uses the same logic that is 
we start in the bottom left corner, row = len(matrix) - 1, col = 0, we have maximum variability meaning that the values 
decrease as we go up the rows (decrement rows) and increase as we do down the columns (increment column). As such read
searchInSortedMatrix.py for a clear understanding of the underlying logic. The reason why this works is because we are
told that the values in each row are sorted in ascending order from left to right. We are also told that the first value
in each row, is greater than the last value in the previous row. Meaning if row 1 ends in 9, row 2 can only start from 10.
And since we know that the first value in row 1 is less than the last value in row 1, it means that the first value in 
row 1 is less than the first value in row 2. In other words, the values are sorted in ascending order in each row from left
to right, as well as sorted in ascending order in each column from top to bottom. That is why using the solution from
searchInSortedMatrix.py works. The key to this solution is finding the position of maximum variability which is the bottm
left corner or even the top right corner (values increase as we go down the column from top to bottom and decrease as we
go down the row from right to left). There are two solutions below that implement these different starting points.
"""


"""Using the bottom left corner as starting position"""
def searchMatrix(matrix, target) :
    row = len(matrix) - 1
    col = 0

    while row >= 0 and col < len(matrix[0]):
        if matrix[row][col] < target:
            col += 1
        elif matrix[row][col] > target:
            row -= 1
        else:
            return True
    return False


"""Using the top right corner as starting position"""
def searchMatrix(matrix, target) :
    row = 0 
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] < target:
            row += 1
        elif matrix[row][col] > target:
            col -= 1
        else:
            return True
    return False
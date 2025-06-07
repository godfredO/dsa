"""In this algorithm we have to place all n queens and ensure that it is a non-attacking formation using backtracking.
We know a formation is non-attacking if none of the n queens share the same row, column, upper diagonal and lower
diagonal with any of the remaining queens. This means that first of all each queen will be in a different row. So we
start with a for loop for the rows and inside this for loop we choose a column for the next queen. To ensure that the
column chosen doesnt fall in the diagonal path of existing queens we check a data structure that stores information about
the existing queens. If this datastructure is a list of existing queen positions, it results in an additional O(n) 
operation. However when we find a valid position for any queen and we add its column to a column hashtable, row + column to
a hashtable for the up diagoanal and row - column for the down diagonal. This is because all positions on the same up diagonal
have the same constant for row + column and all positions on the same down diagonal share a constant value for row - column. If
we find that there is no column in the current row for the next queen it means some of the existing queens need to be moved 
in order to place all n queens in a non-attacking formation. Thus we backtrack to the preceding queen, remove the preceding 
queen(s) r+c, col, r-c from the hashtables and find a new position for them and add the col, r+c, r-c of this new position. 
Thus a col in the current row is a valid position, if its col,r+c, r-c isnt in the hashtables and later on allows all n queens 
to be placed. """
#O(n*n!) time | O(n) space - solution where we use an array of column placements instead of three hashtables
# def nonAttackingQueens(n):
#     columnPlacements = [0]*n #ds for columns of placed queens. Initialized with col 0
#     return getNumberOfNonAttackingQueenPlacements(0, columnPlacements,n) #place n queens starting from row 0

# def getNumberOfNonAttackingQueenPlacements(row,columnPlacements,boardSize):
#     if row == boardSize: #if we call this recursive function with row == n, then we placed the last queen , and
#         return 1 # we have one non-attacking formation of n queens, so return 1 to add to our num of non-attacking placements
    
#     validPlacements = 0 #initializse number of non-attacking placements of n queens on a n x n board at 0
#     for col in range(boardSize): #find a valid column for current row, 
#         if isNonAttackingPlacement(row,col,columnPlacements): #if current col is a non-attacking placement for current row, O(n)
#             columnPlacements[row] = col #then add / update the chosen  column to / in the column placements array
#             #place next queen, by calling recursive function on next row, add return value from next queen's call
#             validPlacements += getNumberOfNonAttackingQueenPlacements(row+1,columnPlacements,boardSize) 
#     return validPlacements #If columns in for loop run out for current row ,0 is returned, without attempting to place next queen

# def isNonAttackingPlacement(row,col,columnPlacements):
#     for previousRow in range(row) : #loop up to current row, to look at previously placed queens
#         columnToCheck = columnPlacements[previousRow] #read column each previously placed queen
#         sameColumn = columnToCheck == col
#         onDiagonal = abs(columnToCheck - col) == row - previousRow #row comes after previousRow so can skip abs() for diag gradient 
#         if sameColumn or onDiagonal: #if the chosen col clashes with an existing queen or is in a previously placed queens diagonal
#             return False #return false because current col is an attacking placement for current row with existing queens
#     return True #if choosen col for current row is non-attacking position for all previously placed queens

"""Optimal solution we use hashtables to store the up diagonal (row + col), down diagonal (row - col) and column for each placed
queen and remove them if we need to backtrack. The functions for up diagonal and down diagonal are extensions of the gradient
argument used in determining the diagonal placements. It turns out that the all points on a position's up diagonal share a constant
value for row + col. All points on a positon's down diagonal share a constant value for row - col. This improves the time complexity"""
#O(n!) time | O(n) space
def nonAttackingQueens(n):
    blockedColumns = set()       #hashset for columns of placed queens
    blockedUpDiagonals = set()  #hashset for up diagonals of placed queens
    blockedDownDiagonals = set() #hashset for down diagonals of placed queens
    return getNumberOfNonAttackingQueenPlacements(0,blockedColumns,blockedUpDiagonals,blockedDownDiagonals,n) #place n queens starting from row 0

def getNumberOfNonAttackingQueenPlacements(row,blockedColumns,blockedUpDiagonals,blockedDownDiagonals,boardSize):
    if row == boardSize: #if we call this recursive function with row == n, then we placed the last queen , and
        return 1 # we have one non-attacking formation of n queens, so return 1 to add to our num of non-attacking placements
    
    validPlacements = 0 #initializse number of non-attacking placements of n queens on a n x n board at 0
    for col in range(boardSize): #find a valid column for current row, 
        if isNonAttackingPlacement(row,col,blockedColumns,blockedUpDiagonals,blockedDownDiagonals): #if col is a non-attacking placement, O(1)
            placeQueen(row,col,blockedColumns,blockedUpDiagonals,blockedDownDiagonals)
            #place next queen, by calling recursive function on next row, add return value from next queen's call
            validPlacements += getNumberOfNonAttackingQueenPlacements(row+1,blockedColumns,blockedUpDiagonals,blockedDownDiagonals,boardSize) 
            removeQueen(row,col,blockedColumns,blockedUpDiagonals,blockedDownDiagonals) #after next queen or all n queens placed remove col choice
    return validPlacements #If columns in for loop run out for current row ,0 is returned, without attempting to place next queen

def isNonAttackingPlacement(row,col,blockedColumns,blockedUpDiagonals,blockedDownDiagonals):
    if col in blockedColumns or row+col in blockedUpDiagonals or row - col in blockedDownDiagonals:
        return False
    return True

def placeQueen(row,col,blockedColumns,blockedUpDiagonals,blockedDownDiagonals):
    blockedColumns.add(col)    #hashset for columns of placed queens
    blockedUpDiagonals.add(row+col)  #hashset for up diagonals of placed queens
    blockedDownDiagonals.add(row - col)

def removeQueen(row,col,blockedColumns,blockedUpDiagonals,blockedDownDiagonals):
    blockedColumns.remove(col)    #hashset for columns of placed queens
    blockedUpDiagonals.remove(row+col)  #hashset for up diagonals of placed queens
    blockedDownDiagonals.remove(row - col)

n=4
print(nonAttackingQueens(n))
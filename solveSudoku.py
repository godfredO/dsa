#Permutation with specific criteria
"""You're given a two-dimensional array that represents a 9x9 partially filled Sudoku board and asked to write a function that returns the 
solved sudoku board. Sudoku is a famous number-placement puzzle in which you need to fill a 9x9 grid with integers in the range of 1-9.
Each 9x9 Sudoku board is split into 9 3x3 subgrids. The objective is to fill the grid such that each row, column and 3x3 subgrid contains
the numbers 1-9 exactly one. In other words, no row may contain the same digit more than once, no column may contain the same digit more
than once, and none of the 9 3x3 grids may contain the same digit more than once. A filled position will contain valid number placement
ie 1-9 and an unfilled position will contain 0. If a valid number is filled in, we are not to change it. Otherwise, if the number is
0 at any position we are supposed to

So in typical solutions for grid based questions we have an outer loop that cycles through the rows and for each row cycles through the
columns. This outer for loop thus handles the progression from row to row and we know that we wont go out of bounds. Here the existence
of the subgrids may make such a solution complex. Thus in this solution we dont have an outer for loop at all, we call the backtracking 
recursion function with the row, col of the first position and 'manually' handle going down the row and columns. This solution uses three 
helper functions to solve the partially filled Sudoku board.

The first function solvePartialSudoku() takes a row,col, and the board matrix is inputs. The first thing is to check if we are at the last
column of the current row. If the current column is out of bounds for the current row, then it means we need to go to the next row, so
we increment the current row variable by 1 and reset the current column variable to 0. Next we check if we have the incremented current
row variable is out of bounds for the whole board ie == len(board). If it is we return True because we completed the board.
Next thing we check if the value at the current position equals 0 ie unfilled position. If it is we call the helper function
tryDigitsAtPosition with the current row and column. If the current postion is filled with a valid number, we call the current recursive
function solvePartialSudoku() on the next column in the current row. This call will again check if the position needs updating, if the board 
has been completed or if the position is unfilled. If it unfilled then it will call tryDigitsAtPosition() on that position.

The second helper function tryDigitsAtPosition() obviously tries a number in the range of 1-9 in the row,col passed to it, checks if the
current number is valid for the row, col, and subgrid using a helper function. So we have a for loop for number in range(1,10), 10 due to
the end-exclusivity of range(). Inside the current number we call the third helper function isValidAtPosition() with the current number in
the loop, row, col, board and this function checks if the number is the only one of its kind in the row, col, and subgrid in the board.
The inner workings of this function will be discussed later but for now let's say the current number is found to be valid at the row,col
in the board. The we set the number at that position in the board ie board[row][col] = number. So we now we need to fill the next position,
and to do that we make a call to the first helper function, solvePartialSudoku() with an incremented value for column so that that function
will do its checks, update currentCol and currentRow if necessary and check if the updated row is out of bounds in which case it returns
True, meaning the board has been completed. Thus solvePartialSudoku() and tryDigitsAtPosition() are recursively calling one another and
we know that solvePartialSudoku() will return True when we complete the board and we need this True to bubble up the recursive stack so that
we clear up all the recursive calls on the stack and return the completed board. So when we make a call to solvePartialSudoku() from
tryDigitsAtPosition() we check if it returns True in which case we return True ie if solvePartialSudoku(row,col+1, board): return True.
By the way it is this increment of column that solvePartialSudoku checks for being out of bounds for the current row. If we try all digits
and all are found to be invalid, then outside the for loop we set the current value to 0 for unfilled and return False. So what does
False do? When we return False, to an earlier recursive call, it is a sign to that call, that some subsequent recursive call didnt find any 
valid numbers to fill some subsequent position meaning that the current number chosen even though it looks valid, makes it impossible to 
fill the board later on so we need to choose a different number for the current postion. As a result when we call tryDigitsAtPosition() 
from solvePartialSudoku, we precede the call with return so that when we return False, we bubble it up for some recursive call to make 
another choice. Of course if we return True, we bubble it up because the board is complete, all current choices are valid and we want to 
clear all the recursive calls off the stack. Also realize that from solvePartialSudoku(), we only call tryDigitsAtPosition() when we confirm
that the current position is unfilled ie contains 0, that why when we reset the value to 0 when we cant find a valid value.

Now to the isValidAtPostion(value, row, col, board). A value is valid if it is row valid, column valid, and sub-grid valid. A value is row
valid if it is the only such value in the row. Thus in the code, if value not in board[row], then it is row valid. Similarly to check if
it is column valid, we need to loop through the col column of every row. In the code this is done with a map() function, that cycles through
rows with a lambda function, reads the value at row[col] into the map object which is iterable, thus we check if the value is not in the 
iterable,  ie value not in map(lambda row: row[col], board). We have to use map here because we need to use a lambda function to map every
row to row[col]. At this point if the value is in the row or is in the column, no need to even check the sub-grid. So if not rowIsValid or
not colIsValid: return False. Then to check if a value is sub-grid valid, just like the case of the row and column, a value is subgrid valid
if it doesnt exist in the sub-grid yet. Remember, in tryDigitsInPostion(), we check for validity before we set the value at the position and
move on. So to loop throught the sub-grid we use a standard double nested for loop that chooses the rows first and for each chosen row, 
choses the columns in the row. We know that each subgrid contains 9 values, inside a mini-square matrix of 3 rows and 3 columns. So we know
that if we find the startRow and startCol. The way we find the startRow and startCol is by floor dividing the row and column of the postion
by three ie if row,col = 3,8 then the startRow is 3//3 = 1 and startCol = 8 // 3 = 2. Then since we know that the there are 3 rows and 
3 columns in each, we start a row for loop and col for loop ie for row in range(3): for col in range(3). So how do we use the startCol and
startCol to generate the position in the same sub-grid as row,col. In the example, for position 3,8, the nine values in the subgrid are
positions (3,6),(3,7),(3,8),(4,6),(4,7),(4,8), (5,6),(5,7),(5,8). To access these these postions the say that rowToCheck= startRow*3 + row
ie rowToCheck = 1*3+0 = 3, 1*3+1 = 4, 1*3+2 = 5 and colToCheck= startCol*3 + row ie 2*3+0 = 6, 2*3+1 = 7, 2*3+2=8. So when we generate a
specific rowToCheck, colToCheck, we access the existing value and if the existing value is equal to the passed value, we just return False
ie the value is not valid at the position. Otherwise if we look at all subgrid values and we dont find the passed value then outside the
nested for loop we return True.

This True / False backtracking in tryDigitAtPosition works as follows, if True we completed the Sudoku board. If False, try another option,
and proceed. If no more options, return False to previous recursive call. When previous recursive call receives False, it tries another
option and proceeds.

"""


def solveSudoku(board):
    solvePartialSudoku(0,0,board)
    return board

#this function jumps non-zero squares and calls the other helper function on empty squares
def solvePartialSudoku(row,col,board):
    currentRow = row
    currentCol = col

    #base case of recursive algorithm
    if currentCol == len(board[currentRow]): #if the current col is past the num of cols in our board
        currentRow += 1 #this is where we increase row, only when we are at the end of current row,
        currentCol = 0 #in the next row, start at the first value
        if currentRow == len(board): #if the current row is actually the last row
            return True #then it must mean we just completed our board so return True
    
    if board[currentRow][currentCol] == 0:#if current row is unfilled, 
        return tryDigitsAtPosition(currentRow,currentCol,board) #try digits at position
    #if row, col was already filled in the input, move to next column, this is the recursive step if the row, col passed was already filled in the input
    return solvePartialSudoku(currentRow,currentCol + 1, board) #this is where we increase column

def tryDigitsAtPosition(row,col,board): #this function recursively fills empty spaces
    for digit in range(1,10): #test values 1-9
        if isValidAtPosition(digit, row, col,board):#if current value is valid
            board[row][col] = digit #insert current value in board
            #thus in order for a recursive call to be resolved, the next call has to be resolved, and for that to be resolved, the next has
            if solvePartialSudoku(row,col+1,board):#this is the actual recursive step in this algorithm, after we successfully fill a value
                return True #if we can solve the board with value, return true
    board[row][col] = 0 #if digits 1-9 are all invalid for current position, reset value
    return False #return False

def isValidAtPosition(value,row,col,board):
    rowIsValid = value not in board[row]
    colIsValid = value not in map(lambda r: r[col],board) #map object is an iterator, so we can iterate over its elements, hence "in"
    if not rowIsValid or not colIsValid:
        return False

    subgridRowStart = row // 3
    subgridColStart = col // 3
    #this will loop through all the positions in the subgrid until it finds that the proposed value is in already in the subgrid
    for rowIdx in range(3):
        for colIdx in range(3):
            rowToCheck = subgridRowStart * 3 + rowIdx
            colToCheck = subgridColStart * 3 + colIdx
            existingValue = board[rowToCheck][colToCheck]
            if existingValue == value:
                return False
    return True #if after looping through all positions in the subgrid, the proposed value isn't already there, return True



board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
  ]

print(solveSudoku(board))
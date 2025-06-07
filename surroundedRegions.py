"""Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'. A region is captured 
by flipping all 'O's into 'X's in that surrounded region.

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Example 2:

Input: board = [["X"]]
Output: [["X"]]


So the first thing to realize is that the question talks about regions of O's and a region of O's is basically a group of connected O's. So
given a region of O's we need to determine if that region is also surrounded by X's in which case we can flip the O's in the region to X's.
Another important realization is that if a region of connected O's has one of the O's on the border of the matrix (first row, first column,
last row, last column), then that region is said to be connected to the border. And if a region is connected to the border, that region 
cannot be flipped because it cannot be surrounded by X's since the border 0 will not be flanked by an X on one side. In otherwords, regions 
that are not connected to the border can be flipped. Regions that are connected to the border cannot be flipped. Now the solution here will
involve what I call complement thinking or as some youtubers call it reverse thinking. How does thinking affect the solution? In the 
question we are told to capture all surrounded regions. That is the same as saying capture everything except the 'unsurrounded' regions. 
And we know that every region that is connected to the border will be 'unsurrounded' by X's.

So how do we get the unsurrounded regions? Just like removeIslands.py we start from the border regions, looking for O's and if we find one,
we start a dfs to mark the regions that contain these O's in our visited matrix and these will be the O's that belong to regions that are 
connected to the border and are unsurrounded as a result. Then we set everything except these visited positions as X's thus flipping all 
of the surrounded regions. Again like removeIslands.py , if we are allowed to modify the input matrix, we can set the border connected O's
as say 'T' and then during our second iteration through the matrix, if we find a 'T' we make it an 'O', else we make it an 'X'.
There are two coded solutions that differ in the way the outer loop is structured, the first solution loops through the entire matrix and
only starts a dfs from the border O's. The second solution is more efficient by first looping over the columns and starting a dfs for the
top border and bottom border before a second loop over the rows and starting a dfs for the rightmost column and leftmost column. In either
solution, we mark the border connected O's in a visited matrix and then loop throught the whole matrix again, this time, skipping over the
positions that are marked as border connected O's (and in a tiny optimization, skipping over exisiting X's) and then setting the unvisited
positions (in the tiny optimization, we unvisited O's) to X's. Another graph question that uses this complement or reverse thinking is
pacificAtlanticWaterFlow.py.

"""
#O(n*m) time | O(n*m) space
def solve(board):
    rows, cols = len(board), len(board[0])
    visited = [[False for col in range(cols)] for row in range(rows)]

    for row in range(rows):
        for col in range(cols):
            isBorder = row == 0 or row == rows - 1 or col == 0 or col == cols - 1
            if not isBorder:
                continue
            if board[row][col] != "O":
                continue
            explore(row, col, board, visited, rows, cols) #start dfs only from border O's


    for row in range(rows):
        for col in range(cols):
            if visited[row][col]:
                continue
            if board[row][col] == "X": #tiny optimization of skipping over existing X's
                continue
            board[row][col] = "X"
    
    return board

def explore(row, col, board, visited, rows, cols):
    if row < 0 or col < 0 or row >= rows or col >= cols or visited[row][col] or board[row][col] != "O":
        return
    
    visited[row][col] = True
    explore(row - 1, col, board, visited, rows, cols)
    explore(row + 1, col, board, visited, rows, cols)
    explore(row, col - 1, board, visited, rows, cols)
    explore(row, col + 1, board, visited, rows, cols)


#O(n*m) time | O(n*m) space
def solve(board):
    rows, cols = len(board), len(board[0])
    visited = [[False for col in range(cols)] for row in range(rows)]

   
    for col in range(cols):
        explore(0, col, board, visited, rows, cols)
        explore(rows - 1, col, board, visited, rows, cols)
    
    for row in range(rows):
        explore(row, 0, board, visited, rows, cols)
        explore(row, cols - 1, board, visited, rows, cols)
            
    for row in range(rows):
        for col in range(cols):
            if visited[row][col]:
                continue
            board[row][col] = "X"
    
    return board

def explore(row, col, board, visited, rows, cols):
    if row < 0 or col < 0 or row >= rows or col >= cols or visited[row][col] or board[row][col] != "O":
        return
    
    visited[row][col] = True
    explore(row - 1, col, board, visited, rows, cols)
    explore(row + 1, col, board, visited, rows, cols)
    explore(row, col - 1, board, visited, rows, cols)
    explore(row, col + 1, board, visited, rows, cols)
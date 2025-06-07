"""The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other. Given an 
integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order. Each solution contains a 
distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]
 
So this is the foundational problem for the nonAttackingQueens.py problem. In this question, we are asked to return a list of arrays 
of strings, where each array represents a non-atttacking formation, and each string in the array represents the empty spaces and the 
queen's placement in that row index of the board. So [".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]] represents the two 
distinct non-attacking formations, in a 4x4 board and in each formation, the string at index i represents the empty spaces and queen 
placement in that row of the board. Reading nonAttackingQueens.py in the algoexpert notes explains that a queen in chess can move up
or down (row), right or left (column), in the positive (upward) or the negative (downward) diagonal. So if any queen is in another 
queen's line of sight they are in an attacking formation.

So basically we know for a valid non-attacking formation, each queen must be in its own row and column. But for each row, which column 
do we choose? It is the column that doesnt clash with another queeen's column, diagonally up or diagonally down placement. We can keep
track of previously chosen columns by simply storing the chosen columns. All positions that are on the same upward diagonal have a 
constant (row + col) value and all positions that are on the same downward diagonal have a constant row - col value. So (0,0), (1,1), 
(2,2), (3,3) are all on the same downward diagonal as row-col is 0 for all of them. In the same way (0,3), (1,2), (2,1), (3,0) are on 
the same upward diagoanl as row + col is 3 for all of them. In the same way positions (0,1) (1,2), (2,3) are on the same downward 
diagonal because row - col is -1 for all of them. Finally, positions (0,1) and (1,0) are on the same upward diagonal because row + col 
is 1 for both of them.

So basically, we have to use backtracking to brute-force every single position, since we are trying to find all the valid formations 
for any nxn board. We can choose any column for row 0, we record the col, row+col and row-col for the chosen col and make a recursive 
call to choose a column for row 1 such at it doesnt clash with these. If we are able to find such a position, we will go to row 2 and 
so on and so forth. As we go we need to keep track of the string placement for each row in an array. When we make a recursive call with 
row == n we know that we have a valid formation, so append a copy of the string placements to a result array and return up the tree. 
As we return up the tree, we need to clean up the choices we made. If we made it to the end, we would have appended a copy of the string
placements to the result array, and we still need to clean up previous choices and make another non-clashing choice. If we didnt make it 
to the end, we still need to clean up the current choice and make another non-clashing choice. If we find ourselves at any row and there 
is no column that doesnt clash with a placed queens col, row+col or row-col, then we know that the current path, will not lead to a valid 
formation, so we won't even record anything for that row, we will just backtrack up the tree, clean up the previous choice we made, and 
make a new non-clashing choice and then go back down the tree. If there is no non-clashing choice, we clean up and go up the tree. The
point is if we find a non-clashing choice, we make a recursive call and when that call concludes, we clean up, whether that choice led
to a valid formation or not, so that we can look for another valid choice. In otherwords this is not a True/False backtracking but rather
a brute-force backtracking solution since there can be multiple valid formations for the samen board size.

"""


def solveNQueens(n) :
        result, current = [], []
        positive, negative, columns  = set(), set() , set()    #reci
    
        dfs(0, positive, negative, columns, current, result, n)
                
        return result

def dfs (row, positive, negative, columns, current, result,n):
    if row == n:
        result.append(current[:])
        return
        
    
    for col in range(n): #brute force all position formations starting from current col in row
        if row + col not in positive and row-col not in negative and  col not in columns: #if valid

            addChoice(row, col, positive, negative, columns, current, n) #record col, row+col, row-col

            dfs(row+1, positive, negative, columns, current, result, n) #recursive call for next row

            removeChoice(row, col, positive, negative, columns, current) #backtrack by removing current choice before making another choice
            
            
def addChoice(row, col, positive, negative, columns, current, n):
    positive.add(row+col)   
    negative.add(row-col)
    columns.add(col)
    current.append(getString(col,n))
            
def removeChoice(row, col, positive, negative, columns, current):
    positive.remove(row+col)   
    negative.remove(row-col)
    columns.remove(col)
    current.pop()


def getString(col, n):
    array = []
    for i in range(n):
        if i == col:
            array.append('Q')
        else:
            array.append('.')
    return "".join(array)


"""Another way of coding up the solution, we create the string at the end"""
def solveNQueens(n) :
        result = []
        current = [['.']*n for i in range(n)] #rows of [['.', '.', '.', '.'], ['.', '.', '.', '.']]
        positive = set()    #we need a visited set for the positive diagonal
        negative = set()    #we need a visited set for the negative diagonal
        columns = set()

        
        dfs(0, positive, negative, columns, current, result, n)
                
        return result

def dfs (row, positive, negative, columns, current, result,n):
    if row == n:
        copy = ["".join(row) for row in current]
        result.append(copy)
        return
        
    
    for col in range(n): #brute force all position formations starting from current col in row
        if row + col not in positive and row-col not in negative and  col not in columns: #if valid
            positive.add(row+col)   #record col, row+col, row-col
            negative.add(row-col)
            columns.add(col)
            current[row][col] = 'Q'
            
            dfs(row+1, positive, negative, columns, current, result, n) #recursive call for next row
            
            positive.remove(row+col)   #backtrack by removing current choice before making another choice
            negative.remove(row-col)
            columns.remove(col)
            current[row][col] = '.'
    

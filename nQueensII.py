"""The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other. Given an 
integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
Input: n = 1
Output: 1

So this is an extension of nQueens.py and is actually the same question as nonAttackingQueens.py. So review those two. Basically the
only difference between this question and nQueens.py is that instead of returning the non-attacking formations themselves we need to
return the number of non-attacking formations. So the first idea would be to use nQueens.py and return the length of the result array.

The approach I have used here is two fold. Since we dont need to the attacking formations themselves, when we make a call with a row
index that is out of bounds, we can increment a value object by 1 and at the end we return the value stored in this object. The
second approach is to initialize a count of 0 at each recursive call, increment this count by the value returned by the dfs call and
outside the for loop, we return this count. If we ever get to the end and make a recursive call with an out of bounds row index, then 
we return 1, otherwise we will be returning 0 if no non-crashing placement is found. This will have the effect of adding up all the 1's
up the tree to the original recursive call.
"""

"""I prefer to carry a value object aroud, just my style"""
class Num:
    def __init__(self, value):
        self.value = value

def totalNQueens(n) :
    current = Num(0)
    positive, negative, columns  = set(), set() , set()    #reci
    
    dfs(0, positive, negative, columns, current,  n)
                
    return current.value

def dfs (row, positive, negative, columns, current, n):
    if row == n:
        current.value += 1
        return
        
    
    for col in range(n): #brute force all position formations starting from current col in row
        if row + col not in positive and row-col not in negative and  col not in columns: #if valid

            addChoice(row, col, positive, negative, columns) #record col, row+col, row-col

            dfs(row+1, positive, negative, columns, current, n) #recursive call for next row

            removeChoice(row, col, positive, negative, columns) #backtrack 
            
            
def addChoice(row, col, positive, negative, columns):
    positive.add(row+col)   
    negative.add(row-col)
    columns.add(col)
    
            
def removeChoice(row, col, positive, negative, columns):
    positive.remove(row+col)   
    negative.remove(row-col)
    columns.remove(col)
    



"""You can also return value of 1 when you get to the end, and add it to all the previous 0's up to the 
original call and then add up all the 1's from the original call and return that."""

def totalNQueens(n) :
    positive, negative, columns  = set(), set() , set()    #reci
                
    return dfs(0, positive, negative, columns,  n)

def dfs (row, positive, negative, columns, n):
    if row == n:
        return 1
        
    current = 0
    for col in range(n): #brute force all position formations starting from current col in row
        if row + col not in positive and row-col not in negative and  col not in columns: #if valid

            addChoice(row, col, positive, negative, columns) #record col, row+col, row-col

            current += dfs(row+1, positive, negative, columns, n) #recursive call for next row

            removeChoice(row, col, positive, negative, columns) #backtrack 
    return current
            
            
def addChoice(row, col, positive, negative, columns):
    positive.add(row+col)   
    negative.add(row-col)
    columns.add(col)
    
            
def removeChoice(row, col, positive, negative, columns):
    positive.remove(row+col)   
    negative.remove(row-col)
    columns.remove(col)
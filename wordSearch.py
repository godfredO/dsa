"""Given an m x n grid of characters board and a string word, return true if word exists in the grid. The word can be constructed from 
letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not 
be used more than once.
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

This question demonstrates graph backtracking. We have an outer loop that goes through the board and chooses each position as a possible
starting point for the word, and makes a dfs search call with the current position ie index 0 and this dfs is clad in an if statement
such that if it returns True, then we know that we have found the word and we return True immediately. Otherwise we only return False 
after going through all starting positions and the dfs call from all starting positions yielded False. This is because we are effectively
asking, did we find the suffix of the word starting from the current index with the calls starting from the current board position. If we 
found it, no need to look further, just return True. If we didnt, unmark this position and go back up the recursive tree, ie backtrack.

Inside the dfs, we check first check if we found the word, which will happen if we make a dfs call with a current index equal to the length 
of the word ie we matched every letter at every index of the word. Next we check the False situations ie if the current position has been 
visited in the current path or if the word at the current position doesnt match the current index of the word. Otherwise we have an node 
whose letter matches the current letter in the word and has not been used in our current path. So we mark the current position as visited
as its is now in our path. Then we collect the neighbors of the current position and loop through the neighbors, and make dfs calls from 
each unvisited neighbor, incrementing the current letter index of the word and if an unvisited neighbor's dfs call returns True, we bubble 
it up immediately. In otherwords, we make the neighbor calls to match the next letter. Otherwise if we finish going through all the neighbors, 
we do the essential backtracking step of marking the current node as unvisited ie we set visited back to False before returning False. The 
reason is that its visited status is useful only in light of the previous choices made in the current path and if we bubble False we make 
other choices higher up the recursive stack, the current position may be an match for another index in word in the new path.

The solution which explicitly employs a getNeighbors function works only if the input matrix is at least 2x2 but is very useful in 
explaining the inner workings of the backtracking algorithm. But if the input matrix is 1x1, the only node will have no neighbors so when
we try to get its neighbors, we get an empty array and the function may erroneously return False. With that said the previous option allows
as the ability to return early if a True is found from an unvisited neigbbor's dfs call. To make sure this backtracking solution is able
to handle input matrices of 1x1, 1x2, 2x1, we just passe in the numberOfRows and numberOfColumns variables and after marking the current
positon as visited, we make all four possible neighbor calls which means we have to add to add the invalid calls checks to the False base
ie if row <0 or col < 0 or row >= numRows or col >= numCols in addition to returning if the current position has already been visited in
the current path or if the letter stored there doesnt match the current letter in the word.

So we have the outer loop choosing possible starting points for matching the first letter so n*m, and then if we find a match for the 
first letter, we make 4 calls from the current position , one for each neighbor to match the second letter and if we find a match for
the second letter from that position we make four neighbor calls again to match the third letter. So we have n*m starting points for the
first letter and after whenever we make a match we make four neighbor calls for each remaining letter in the word. So if the word has 
length of s, then we make at most O(n*m*4^s) calls and that is the time complexity. The space complexity is O(n*m) for visited set and the
recursive stack since we backtrack and remove calls off the stack if we hit False otherwise if we match we keep going down the recursive
stack and the height of the recursive tree will be at most O(n*m).

The final solution merges what is best about the two previous solutions. Again all solutions are equivalent its just that the way they are
each written has some implications on test case performance. The first solution uses getNeighbors function and search pruning and so will
only pass 2x2 input matrices because of the getNeighbors function which doesnt run for 1x1 matrices or for the last neighbor of 1x2 or 
2x1 matrices. The second solution fixes this by making all neighbor calls even for invalid neighbors and incorporates the invalid call 
checks into the False base case. However this solution does not apply search pruning (search pruning is adding an if statement to 
immediately return when a True statement is found ), instead opting to make the remaining neighbor calls which we don't need to make once
we have found our word. The last solution merges the best of both worlds by implementing search pruning and incorporating the check for
invalid neighbor calls. In addition to cladding each neighbor calls in if statement, we also search prune the outer loop, opting to only
start dfs from positions that match the first letter of the word, otherwise we just choose another starting point. Note that backtracking
is more than just regular recursion in that we are unvisiting neighbors for a current path once we find that path to be inviable, (it 
actually more of a visiting pattern), and as such we caching based on a single position makes no sense here although i suppose you could 
cache based on the sequences of positional choices made for a particular path but that would be an astronomical size cache idk n*m^n*m 
effectively. So search pruning is the only way to optimize performance here.
"""
#This option assumes at least a 2x2 matrix, because of getNeighbors a matrix of smaller dimensions will have no neighbors at the last
#position
def wordSearch(board, word):
    numRows = len(board)
    numCols = len(board[0])
    visited = [[False for i in range(numCols)] for j in range(numRows)]

   
    for row in range(numRows):
        for col in range(numCols):
            if board[row][col] != word[0]:
                continue
            if explore(row, col, board, word, visited, 0):
                return True
    return False


def explore(row, col, board, word, visited, currentIdx):
    if currentIdx == len(word):
        return True

    if visited[row][col] or board[row][col] != word[currentIdx]: # if current word has been used or doesnt match
        return False

    visited[row][col] = True #position matches current letter
    neighbors = getNeighbors(row, col, board)
    for neighbor in neighbors:
        nrow, ncol = neighbor
        if visited[nrow][ncol]:
            continue
        if explore(nrow, ncol, board, word, visited, currentIdx + 1):
            return True
    visited[row][col] = False #backtracking step
    return False

def getNeighbors(row, col, board):
    neighbors = []
    if row > 0:
        neighbors.append([row-1, col])
    if row < len(board) - 1:
        neighbors.append([row + 1, col])
    if col > 0:
        neighbors.append([row, col - 1])
    if col < len(board[0]) - 1:
        neighbors.append([row, col + 1])
    return neighbors

"""This solution removes the need for a getNeighbors function, by making all possible neighbor calls and then returning from invalid calls. 
Also this solution works for matrices that are not 2x2. The reason is that if the board is 1x1 or 1x2 or 2x1 , the last position will have 
no neighbors and so the last call's search for neighbors in the previous solution will yield an empty list and so will wrongly yield
False."""
def wordSearch(board, word):
    numRows = len(board)
    numCols = len(board[0])
    visited = [[False for i in range(numCols)] for j in range(numRows)]

   
    for row in range(numRows):
        for col in range(numCols):
            if explore(row, col, board, word, visited, 0, numRows, numCols):
                return True
    return False

def explore(row, col, board, word, visited, currentIdx, numRows, numCols):
    if currentIdx == len(word):
        return True

    if row < 0 or col < 0 or row >= numRows or col >= numCols or visited[row][col] or board[row][col] != word[currentIdx]:
        return False

    visited[row][col] = True
    result = (
        explore(row - 1, col, board, word, visited, currentIdx + 1, numRows, numCols) or
        explore(row + 1, col, board, word, visited, currentIdx + 1, numRows, numCols) or
        explore(row, col - 1, board, word, visited, currentIdx + 1, numRows, numCols) or
        explore(row, col + 1, board, word, visited, currentIdx + 1, numRows, numCols) 
    )
    visited[row][col] = False  #this is the backtracking step
    return result

"""This solution implements search pruning by making individual neighbor calls and returning the first time we encounter a True as the return
value. Also, we incorporate the getNeighbors function into the dfs calls and add the checks for invalid calls to the False case."""
def wordSearch(board, word):
    numRows = len(board)
    numCols = len(board[0])
    visited = [[False for i in range(numCols)] for j in range(numRows)]

   
    for row in range(numRows):
        for col in range(numCols):
            if board[row][col] != word[0]:
                continue
            if explore(row, col, board, word, visited, 0, numRows, numCols):
                return True
    return False

def explore(row, col, board, word, visited, currentIdx, numRows, numCols):
    if currentIdx == len(word):
        return True

    if row < 0 or col < 0 or row >= numRows or col >= numCols or visited[row][col] or board[row][col] != word[currentIdx]:
        return False

    visited[row][col] = True
    
    if explore(row - 1, col, board, word, visited, currentIdx + 1, numRows, numCols) : #up neighbor
        return True

    if explore(row + 1, col, board, word, visited, currentIdx + 1, numRows, numCols) : #down neighbor
        return True

    if explore(row, col - 1, board, word, visited, currentIdx + 1, numRows, numCols) : #left neighbor
        return True

    if explore(row, col + 1, board, word, visited, currentIdx + 1, numRows, numCols) : #right neighbor
        return True
    
    visited[row][col] = False  #this is the backtracking step
    return False  #return False since all neighbors returned False


"""This is the same solution as the one directly above, ie search pruning for optimized average time and we also use a set instead
of a matrix for the visited data structure for an optimized average space complexity."""
def exist(board, word):
        numRows = len(board)
        numCols = len(board[0])  
        visited = set()   # visited = [[False for i in range(numCols)] for j in range(numRows)]

   
        for row in range(numRows):
            for col in range(numCols):
                if board[row][col] != word[0]:
                    continue
                if explore(row, col, board, word, visited, 0, numRows, numCols):
                    return True
        return False

def explore(row, col, board, word, visited, currentIdx, numRows, numCols):
    if currentIdx == len(word):
        return True
    
    if row < 0 or col < 0 or row >= numRows or col >= numCols or (row,col) in visited or board[row][col] != word[currentIdx] :
        return False
    
    visited.add((row,col))   # replaces visited[row][col] = True
    
    if explore(row - 1, col, board, word, visited, currentIdx + 1, numRows, numCols) : #up neighbor
        return True

    if explore(row + 1, col, board, word, visited, currentIdx + 1, numRows, numCols) : #down neighbor
        return True

    if explore(row, col - 1, board, word, visited, currentIdx + 1, numRows, numCols) : #left neighbor
        return True

    if explore(row, col + 1, board, word, visited, currentIdx + 1, numRows, numCols) : #right neighbor
        return True
    
    visited.remove((row,col))   # replaces visited[row][col] = False  #this is the backtracking step
    return False
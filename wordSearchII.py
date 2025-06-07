"""Given an m x n board of characters and a list of strings words, return all words on the board. Each word must be constructed from 
letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not 
be used more than once in a word.

Input: board = [["o","a","a","n"],                                  Input: board = [["a","b"],
                ["e","t","a","e"],                                                  ["c","d"]
                ["i","h","k","r"],                                                  ]
                ["i","f","l","v"]                                   words = ["abcb"]
                ]                                                   Output: []     
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]


This question is essentially the same as boggleBoard.py except that we can only move in horizontal and vertical directiions, but not in
the diagonal direction, so the solution one is actually the same as boggleboard minus the diagonal directions in getNeighbors(). Solution
two incorporates the getNeighbors() function into the dfs calls and returns from invalid calls. Even though the two solutions have the
same time and space complexity, explicitly defining the getNeighbors function means that we don't have a bunch of invalid calls on the 
call stack even though such calls will be cleared immediately. We can also have a small optimization of first checking if the letter at
the starting point (outer loop) is in the root node of the trie. If its not, we choose another starting point without calling the
depth first search.

In comparison to wordSearch.py, the brute force approch would have been to call wordSearch.py for every single word and store each word
for which wordSearch.py returns True. And the time complexity would be something like m*n*4^m*n or something as ridiculous. However by
using the trie we can find all the words that start from a single starting position in a single dfs call, and backtracking to a point
where one word diverges from another. That is if a starting position has 'a' in the board, using a trie allows us to all words that have
'a' as a prefix, so we go down the trie, find one word, backtrack find another word and so on. This is because a general trie is a 
prefix trie, check out prefixTrie.py. 


"""
"""Solution one repurposes boggleBoard.py solution"""
class Trie: #trie class to store list of words for constant time lookup
    def __init__(self):
        self.root = {}
        self.endSymbol = "*" 
    
    def add(self,word):
        current = self.root #start at the root node
        for letter in word:
            if letter not in current:#if current letter is not in the current node,
                current[letter] = {} #then add it to the current node and
            current = current[letter] #move to current letter's node
        current[self.endSymbol] = word #map the end symbol key to word as value
    
def findWords(board,words):
    trie = Trie() #instantiate Trie class object
    for word in words:
        trie.add(word) #add each word to Trie class object
    finalWords = {} #to store unique word found, because a word can appear multiple times in board, or use set()
    #Boolean matrix to store visited status of each letter in current branch, same size as board
    visited = [[False for letter in row ] for row in board] #False bcos all letters unvisited at start 
    for i in range(len(board)): #traverse board, row by row and for each row, column by column
        for j in range(len(board[i])): #for each row, go column by column for current letter
            if board[i][j] not in trie.root:
                continue
            explore(i,j,board,trie.root,visited,finalWords) #explore current letter, pass in root node
    return list(finalWords.keys()) #return a list of the keys in finalWords hashtable, if set(), the list(finalWords)

def explore(i,j,board,trieNode,visited,finalWords): 
    if visited[i][j]: #if the current letter was visited as part of previous word
        return #no need to go further in current recursive call
    letter = board[i][j] #grab current letter
    if letter not in trieNode: #if the current letter is not in the current trie node
        return #no point exploring further because its not going to yield a valid word
    visited[i][j] = True #if the current letter is in the current trie node, mark as visited
    trieNode = trieNode[letter] #then change current node to be current letter's node
    if "*" in trieNode: #if we are at the end of a word, the end symbol will be in letter's trie node
        finalWords[trieNode["*"]] = True #add the stored valid word to the final words hashtable, if set(), finalWords.add(trieNode["*"])
    neighbors = getNeighbors(i,j,board) #then get the neighbors of current letter
    for neighbor in neighbors: #for each neighbor
        explore(neighbor[0],neighbor[1],board,trieNode,visited,finalWords)#explore neighbor in dfs style
    visited[i][j] = False #at end of current branch, change visited status of letter to False


def getNeighbors(i,j,board):
    """Each node has up to eight neighbors, horizontal right and left, vertical above and below,
    diagonal above left and right, diagonal below left and right"""
    neighbors = []
    
    if i > 0: # with the exception of the first row
        neighbors.append([i-1,j]) # add vertical above neighbor
    if i < len(board) - 1: # with the exception of the last row
        neighbors.append([i+1,j]) # add vertical below neighbor
    if j > 0: #with the exception of the first column
        neighbors.append([i,j-1]) # add horizontal left neighbor
    if j < len(board[0]) - 1: # with the exception of the last column
        neighbors.append([i,j+1])  # add horizontal right neighbor
    return neighbors #return a 2d array of neighbors' row, col indexes for input node




"""Solution two where I incorporate invalid calls to avoid writing a getNeighbors function"""
class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"
    
    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = word

def findWords(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    
    numRows, numCols = len(board), len(board[0])
    
    visited = [[False for i in range(numCols)] for j in range(numRows)]
    finalWords = set()
    for row in range(len(board)):
        for col in range(len(board[row])):
            explore(row, col, board, visited, finalWords,trie.root, numRows, numCols)
    return list(finalWords)


def explore(row, col,board, visited, finalWords, currentNode, numRows, numCols):
    if row < 0 or col < 0 or row >= numRows or col >= numCols or visited[row][col] or board[row][col] not in currentNode:
        return
    visited[row][col] = True
    currentNode = currentNode[board[row][col]]
    if "*" in currentNode:
        finalWords.add(currentNode["*"])
    explore(row - 1, col,board, visited, finalWords, currentNode, numRows, numCols)
    explore(row + 1, col,board, visited, finalWords, currentNode, numRows, numCols)
    explore(row, col-1,board, visited, finalWords, currentNode, numRows, numCols)
    explore(row, col+1,board, visited, finalWords, currentNode, numRows, numCols)
    visited[row][col] = False #backtracking step


board = [["o","a","a","n"],                                  
         ["e","t","a","e"],                                                  
         ["i","h","k","r"],                                                  
         ["i","f","l","v"]                                  
        ]                                                   
words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
print(findWords(board, words))






class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self,word):
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.isWord = True

def findWords(baord, words):
    root = Trie()
    for word in words:
        root.addWord(word)
    
    visited = set()
    found = set()
    rows, cols = len(board), len(board[0])
    for row in rows:
        for col in cols:
            dfs(row, col, board, found, root, visited, "", rows, cols)
    
    return list(found)

def dfs(row, col, board, found, node, visited, current, rows, cols):
    if row < 0 or row >= rows or col < 0 or col >= cols:
        return
    
    if (row,col) in visited or board[row][col] not in node.children:
        return

    visited.add((row,col))

    letter = board[row][col]
    node = node.children[letter]

    current  +=   board[row][col]

    if node.isWord:
        found.add(current)
    
    
    dfs(row - 1, col, board, found, node, visited, current, rows, cols)
    dfs(row + 1, col, board, found, node, visited, current, rows, cols)
    dfs(row, col - 1, board, found, node, visited, current, rows, cols)
    dfs(row, col + 1 , board, found, node, visited, current, rows, cols)

    visited.remove((row, col))
    


# board = [["a","b"],
#          ["c","d"]
#         ]
# words = ["abcb"]
# # Output: []    
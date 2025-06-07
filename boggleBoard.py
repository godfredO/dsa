"""
Tags: Graph Trie, Dfs, Hard
You are given a two-dimensinal array (a matrix) containing letters; this matrix represents a boggle board. You're also given a list of
words. The question asks to write a function that returns an array of all the words in the boggle board in no particular order. A word is
constructed in the boggle board by connecting adjacent (horizontally, vertically, diagonally) letters without using any single letter at
a given position more than once in the same word; while a word can of course have repeated letters, those repeated letters must come from
different positions in the boggle board in order for the word to be contained in the board; however two or more words are allowed to
overlap and use the same letters in the boggle board.

So this looks like most graph question but there are two changes here. First the getNeighbors() function will also have to include diagonal
neighbors, increasing the maximum number of neighbors from 4 to 8 ie diagonal up right, diagonal up left, diagonal down left, diagonal down
right. The second is that while we are not allowed to use the same letter more than once in a particular word, the letter can be used in
two separate words. Now usually in graph problems, we use a visited set or matrix to avoid visiting a position more than once to avoid doing
repeated work. Thus when doing a dfs to construct a word we need to track the positions and thus letters that have been visited as part of
the current word but as soon as we are done with the current word we need to make those same positions and letters available for the next
word. That is we will of course initialize visited to False for every position, then turn it to True for any position that is still on the
recursive stack for the current word we are trying to construct but as soon as we determine that we cant continue with the current word or
we find a word, we simply reverse visited at all the positions involved in just ended recursive calls to False. This technique or pattern is
usually used in finding cycles in graph.

It will be helpful to review Cycles In Graph question or Topological Sort question where we use this pattern with a secondary indicator
called visiting. While a particular node is still on the recursive stack, visiting is True, as soon as we complete all depth-first-search
calls involving or originating from that node, we turn visiting off and if we ever make a recursive call to a node that is still on the stack,
we know we have a cycle otherwise. In those questions we still use visited to avoid doing repeated work and specifically to return a known
result ie we started a dfs from a node and didnt find a cycle so we know if we ever encounter that node, we already know that we will wont
find a cycle starting from there. Thus the visited pattern works in a memoization sort of way, while the visiting pattern is specifically for
tracking nodes on the recursive stack. All that to say that even though in the code, the auxilliary data structure used is named visited, it
will be more appropriately named visitig. That is, we flip it from False to True when we start a dfs from a node, and flip it back to False
when all recusive calls originating directly or indirectly from said node all complete. Here we don't need to find cycles, we just use this
pattern to ensure that we dont use the same letter twice in the same word while still making it available for another word. In addition to
making positions availabe for new words, for a given word we are trying to construct there will be different possible paths so we visit all
the letters that are chosen for the current path and as soon as we find the current path inviable we have to unvisit those letter positions
to make them available for a new path for the same word. This pattern is called backtracking and we backtrack when we finish a word or deem
a path invalid.

So like any graph problem, we will have our outer loop that attempts to find a word starting from each positon. We get the neighbors,
turn visiting to True and when all calls are completed or we find a word, we turn visiting to False and if we indeed find a word, we add
the found word to a hashtable. The reason we use a hashtable instead of an array is because, we are not assured that words appear only
once in the boggle board. That is its possible to find the same word multiple times in the boggle board where each instance of the word
starts off from a different position. So by using a hashtable, we know we only store the unique words found and at the end we return
a list of the hashtable's keys.

So the final piece of this solution is that how do we know if we have found a word during our graph depth first search, and how do we know
if the current depth first search cannot yield a word in the list of words. Using some sort of array matching like the inoptimal solution
of Dijkstra's algorithm is not even feasible here because that would lead to a monstrous time complexity if a computer can even run such
an approach without running out of memory. Well the answer is to use a specialized data structure, again like we do in the optimal
solution of Dijkstra's algorithm. And the specialized dat structure we use, is the Trie. So we instantiate our trie, which will be empty
in the beginning, then we loop through our list of words and insert each word into the trie. The words are like the suffixes we generate
in the suffix trie question and the for loop is essentially acting like the populate method on the trie clas in the suffix trie question.
As such the trie class we use here doesnt need a populate() method, just an insert method and it inserts the given word, letter by letter.
One thing we do however is that after inserting all the letters in a letter, we add an endSymbol key to the last current node that points
to the word (instead of True in the suffix trie question), so that whenever we encounter the endSymbol, we know that we have matched a
word, and the word we matched is the endSymbol key's value ie endSymbol: word. So when we first start a depth first search, we pass in
a current node which will be the root node of the trie to match a first letter of a word but after matching a first letter, we update
the current node to be that letter's node in the current node of the trie and that new current node becomes what we use to match the second
letter and if that is found, its node in the currrent node becomes the new current node to match the third letter and so on and so forth.
At the beginning of each recursive call, we first check if we have the endSymbol if we do we read the value ie matched word and still
continue just in case we have two words where one word is a substring of the other eg able, ableness. Just a comment but since this is
backtracking for matching multiple words, we use a trie; if the purpose of backtracking was to match a single word, we would be passing in
the word and a current index so that we match it one letter at a time like in wordSearch.py.

Again we are allowed to use the same letters for different words but not the same letter repeatedly in the same word. So at the start of the
dfs we first check if visiting (in the code its called visited but really its the visiting pattern) is True meaning this is a letter already
used for the current word we are trying to match. So if visiting (in code called visited) is True, we return so that the point where that
call originated from will try another neighbor (if the call originated from another dfs), or another starting point (if the call originated
from the outer loop). Otherwise we select the letter at that node position and check if the letter is in the current node. If the letter is
not in the current node we return again to the point where the call originated so that anothher neighbor is chose or another starting point
is chosesn (if the call originated from anther dfs or from the outer loop respectively). If however the letter is in the current trie node,
we mark the node as visiting (in the code its called visited) and then we update the current trie node to the current letters node inside
the passed trie node. Then we check if the endSymbol is in the updated trie node. If it is we add its stored word to the final words
hashtable  (ie the hashtable is also an input to the dfs function) with a key of True but really we need to use a set instead since we don't
need the True value for anythng. At this point is essential to note the sequencing of steps. A node is considered visited only after we have
found its letter in the current node. So we mark visiting to be True after checking if the letter is in the current Node. Then we update
current Node to the found letter's node before checking for the endSymbol.
Then we get the neigbors of the current node and inside a for loop, call the dfs on each neighbor, passing in the neighbors coordinates,
the current node, and the rest of the inputs. Outside the for loop, which signifies the conclusion of all the neighbor dfs calls, we set
the visiting (in code called visited) to False so that it can be sued for another word. Note that neighbors can continue the current word
eg able, ableness as long as none of the previous letters are used twice. If we use a set instead of a hashtable for the found words, at
the end we just convert the set to a list and return that list.

The getNeighbors() function takes the standard four neighbors ie the two vertical neighbors (up, down) and the two horizontal neighbors
(left, right) and pairs them and as such their conditions eg diagonal up,left combines up and left and as such their loop conditions. That
is we can only have an up neighbor if row > 0, we can only have a left neighbor if col >0 so we can only have a diagonal up,left neighbor
if row > 0 and col > 0.
"""


# O(nm*8^s + ws) time | O(nm + ws) space, n,m-matrix dim, w= num of words, s= length of longest word
def boggleBoard(board, words):
    trie = Trie()  # instantiate Trie class object, root node
    for word in words:
        trie.add(word)  # add each word to Trie class object
    finalWords = {}  # to store unique word found, because a word can appear multiple times in board, or use set()
    # Boolean matrix to store visited status of each letter in current branch, same size as board
    visited = [[False for letter in row]
               for row in board]  # False bcos all letters unvisited at start
    for i in range(len(board)):  # traverse board, row by row and for each row, column by column
        for j in range(len(board[i])):  # for each row, go column by column for current letter
            # explore current letter, pass in root node
            explore(i, j, board, trie.root, visited, finalWords)
    # return a list of the keys in finalWords hashtable, if set(), the list(finalWords)
    return list(finalWords.keys())

# recursive function to find words that start with current letter


def explore(i, j, board, trieNode, visited, finalWords):
    if visited[i][j]:  # if the current letter was visited as part of previous word
        return  # no need to go further in current recursive call
    letter = board[i][j]  # grab current letter
    if letter not in trieNode:  # if the current letter is not in the current trie node
        return  # no point exploring further because its not going to yield a valid word
    visited[i][j] = True  # if the current letter is in the current trie node, mark as visited
    trieNode = trieNode[letter]  # then change current node to be current letter's node
    if "*" in trieNode:  # if we are at the end of a word, the end symbol will be in letter's trie node
        # add the stored valid word to the final words hashtable, if set(), finalWords.add(trieNode["*"])
        finalWords[trieNode["*"]] = True
    neighbors = getNeighbors(i, j, board)  # then get the neighbors of current letter
    for neighbor in neighbors:  # for each neighbor
        explore(neighbor[0], neighbor[1], board, trieNode, visited,
                finalWords)  # explore neighbor in dfs style
    visited[i][j] = False  # at end of current branch, change visited status of letter to False


def getNeighbors(i, j, board):
    """Each node has up to eight neighbors, horizontal right and left, vertical above and below,
    diagonal above left and right, diagonal below left and right"""
    neighbors = []
    if i > 0 and j > 0:  # with the exception of first row and first col
        neighbors.append([i-1, j-1])  # add diagonal above and left neighbor
    if i > 0 and j < len(board[0]) - 1:  # with the exception of first row and last column
        neighbors.append([i-1, j + 1])  # add diagonal above and right neighbor
    # with the exception of last row and last column
    if i < len(board) - 1 and j < len(board[0]) - 1:
        neighbors.append([i+1, j+1])  # add diagonal below and right neighbor
    if i < len(board) - 1 and j > 0:  # with the exception of last row and first column
        neighbors.append([i+1, j-1])  # add diagonal below and left neighbor
    if i > 0:  # with the exception of the first row
        neighbors.append([i-1, j])  # add vertical above neighbor
    if i < len(board) - 1:  # with the exception of the last row
        neighbors.append([i+1, j])  # add vertical below neighbor
    if j > 0:  # with the exception of the first column
        neighbors.append([i, j-1])  # add horizontal left neighbor
    if j < len(board[0]) - 1:  # with the exception of the last column
        neighbors.append([i, j+1])  # add horizontal right neighbor
    return neighbors  # return a 2d array of neighbors' row, col indexes for input node


class Trie:  # trie class to store list of words for constant time lookup
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def add(self, word):
        current = self.root  # start at the root node
        for letter in word:
            if letter not in current:  # if current letter is not in the current node,
                current[letter] = {}  # then add it to the current node and
            current = current[letter]  # move to current letter's node
        current[self.endSymbol] = word  # * key for word end; store word for output


board = [
    ["t", "h", "i", "s", "i", "s", "a"],
    ["s", "i", "m", "p", "l", "e", "x"],
    ["b", "x", "x", "x", "x", "e", "b"],
    ["x", "o", "g", "g", "l", "x", "o"],
    ["x", "x", "x", "D", "T", "r", "a"],
    ["R", "E", "P", "E", "A", "d", "x"],
    ["x", "x", "x", "x", "x", "x", "x"],
    ["N", "O", "T", "R", "E", "-", "P"],
    ["x", "x", "D", "E", "T", "A", "E"]
]
words = ["this", "is", "not", "a", "simple", "boggle", "board", "test", "REPEATED", "NOTRE-PEATED"]
print(boggleBoard(board, words))

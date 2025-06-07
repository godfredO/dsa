"""
Tag: Trie, Objects, Medium

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:
WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
word may contain dots '.' where dots can be matched with any letter.

word in addWord consists of lowercase English letters. word in search consist of '.' or lowercase English letters.
There will be at most 3 dots in word for search queries.

Example:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True


So the '.' here is a wildcard character, such that '.b' will match any first character followed  by 'b' such as 'ab', 'cb' etc. 'b.' will
match 'ba', 'bc', 'bd' etc. So the efficient solution will require a prefix Trie. Now the addWord() function is typical of prefix tries,
check the question prefixTrie.py. Now how do we handle search() method, when we have the wildcat character '.' eg search('ab...') ie how
do we verify that we have a 5 word letter that starts with ab. Note that search('ab...') is asking to search for an entire word, not just
a prefix. So in this particular example, we will need to go to node 'a' then node 'b' then afterwards go through all of the children of
node 'b' to check if we are able to find an end symbol in three steps for the three dots, and this will obviously involve some sort of
backtracking depth-first search. If search('.ad') means for every node in the root node, we will go one step forward, and check if we
find node 'a' followed by node 'd' with an end symbol and we will backtrack (dfs) until we find a match or we go through every single
possibility. So search() which handles the wildcard backtracking dfs is really the main crux of this question; otherwise every other
functionality is similar to a prefixTrie.py.

So addWord() is just like in prefixTrie.py. The search() method however will be recursive and has an if/else statement to handle when the
current letter we are matching is the wildcard '.' or a regular letter. For the else case, for regular lowercase English letters, the
search() function resembles the searchWord() function of prefixTrie.py, in that if the current letter is not a key node in the current
node, we return False. Otherwise if we finish matching the last letter we check if the end symbol is in the current node. In the if case,
ie if the current letter is a wildcard, we have to go through the value nodes of all the key nodes in our current character. So say our
root node has is has three keys root = {'a':{}, 'b':{}, 'c:{}}, if we call search('.a'), then for the first '.' we will go through all
the hashmaps that are values and in there check if we can find an 'a' with an endSymbol in its node. So whenever the current letter is a
'.', we call our backtracking dfs function, and if this function returns True, we return True up the recursive tree. Otherwise if we go
through all the possibilities and never return True then outside the for loop we return False. Because of the nature of the backtracking
solution, the structure of the trie is different here, using a TrieNode() object.

"""


class TrieNode:
    def __init__(self):
        self.children = {}                          # dictionary to store children of node
        self.word = False                           # to store the end of a word


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()                      # calling WordDictionary() will create root trie node

    def addWord(self, word: str) -> None:           # addWord() returns None
        currentNode = self.root                     # start from root node created in init
        for letter in word:                         # for every letter in word to be added
            if letter not in currentNode.children:  # childeren is a dictionary so do a key check, constant time
                currentNode.children[letter] = TrieNode()   # add letter as key to new node
            currentNode = currentNode.children[letter]      # move currentNode to child node
        currentNode.word = True              # at the end of word, set word flag to True on last letter node

    def search(self, word: str) -> bool:            # word will be global to dfs()

        def dfs(j, root):                           # dfs function defined before call
            currentNode = root                      # dfs starts from passed node, root
            for i in range(j, len(word)):           # is current letter (at index j) in node children
                letter = word[i]
                if letter == '.':                   # if its a wild card character
                    for child in currentNode.children.values():  # start dfs call for all children
                        if dfs(i+1, child):     # call dfs on next letter starting from current child node
                            return True         # if dfs return True , bubble it up
                    return False  # if no child dfs returns True, then return False, bubble it up
                else:  # if not wildcharacter but lowercase English
                    if letter not in currentNode.children:  # current letter not in current node children
                        return False   # word not in trie
                    currentNode = currentNode.children[letter]  # otherwise, update currentNode
            return currentNode.word   # return if last letter was end of the word or not

        return dfs(0, self.root)  # dfs call . dfs takes index and root to search word

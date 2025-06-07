"""A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of 
strings. There are various applications of this data structure, such as autocomplete and spellchecker. 

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

This question is similar to the question suffixTrie.py. The only difference is in the populateSuffixTrieFrom() method in suffixTrie.py and
startsWith() method here. The insert() methods and the search() / contains() methods are the same. The only difference here is that we have
to add an additional method, startsWith(), that takes in a word (prefix) and checks the trie to see if the word is indeed a prefix of the 
previously inserted words. So for the word 'apple', the prefixes are 'a', 'ap', 'app', 'appl', 'appple' , so if we insert apple in the Trie,
any of these prefixes should return True. 

The startsWith method actually resembles the search method, the only differnce is in the return statement. The only difference is that if we 
match every letter in the possible prefix (as we update the currentNode), then outside the for loop, we return True for prefix. For search() 
method on the other hand, we return the result of checking if the endSymbol is in the current node ie did we fully match the word. Thus while 
only the prefixes above will return True with startsWith(), only apple will return True for search().

In otherwords when you think prefix, think starts with. When you think suffix think ends with. The only difference with the prefix is that 
since we start matching from the root node the start of a possible prefix has to be in the root node and that is why we have a populateSuffix
method that generates all the prefixes and inserts in the trie. With a prefix trie we don't need to do that since the start of a possible
prefix has to be the starting letter of the inserted word.
"""

class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol ="*"
    
    def insert(self,word):
        currentNode = self.root
        for letter in word:
            if letter not in currentNode:
                currentNode[letter] = {}
            currentNode = currentNode[letter]
        currentNode[self.endSymbol] = True
    
    def search(self, word):
        currentNode = self.root
        for letter in word:
            if letter not in currentNode:
                return False
            currentNode = currentNode[letter]
        return self.endSymbol in currentNode
    

    def startsWith(self, word):
        currentNode = self.root
        for letter in word:
            if letter not in currentNode:
                return False
            currentNode = currentNode[letter]
        return True


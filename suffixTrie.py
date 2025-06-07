""""This question is about creating a suffix trie. A trie is generally used for string matching purposes, like in the Boggle Board game
question where a list of words are stored inside of a trie for easy verification. A suffix trie stores all possible suffixes for a word. So
that for the word babcock, the possible suffixes are babcock, abcock, bcock, cock, ock, ck, k. So to create a suffix trie, we have a method
populateSuffixTrieFrom(string), that generates all the possible suffixes for a particular string by shifing the first index of the suffix
down the string, and calls the insert method on the on the root node passing in the start index, and string. This populateSuffixTrieFrom()
method is called from the SuffixTrie class instantiation method right after the root node and endsymbol are instantiated. Inside the insert 
method, we do the same thing for string matching Tries, just that we loop from the passed index to the end of the string and insert the 
represented suffix in the trie. Also in string matching Tries we usually store the matched word as the value for the endSymbol key in the 
last current node. Here in the suffix trie , we simply store True. When matching a possible prefix, we start from the root node, check if
the current letter is in the current node. If it is, we update the current node to the letter's node. If its not, we know that the string
is not a prefix so we return False. If we match all letters in current nodes, it still doesnt mean that the word is a prefix. It may be 
that all its letters are found in the suffix trie but a suffix starts from some index in the original suffix trie string all the way to 
the end. In the earlier example, if the word is babcock, abcock is a suffix, but abcoc is not because it doesnt exten to the end of the 
original string. So to ensure that we reached the end of the original string after matching every letter, we return if the last currentNode 
doesnt has the endSymbol key in there. If it does it means we matched every letter right to the very end. If not then we didnt not find a 
suffix because even though every letter matched, the match did not extend to the end. In otherwords, we found a substring, not a suffix.

One last thing, I imagine that to convert this to a prefix trie, we will do the index generation in populatePrefixTrieFrom,  ie 
for i in range(len(array) and then inside the insert method instead of for j in range(i,len(string)) we will have for j in range(0,i) 
in order to insert the prefixes.  That is instead of loop from the passed index to the end we will be looping from the beginning to the
passed index. """

class SuffixTrie:
    def __init__(self,string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)
    
    #O(n^2) time | O(n^2) space
    def populateSuffixTrieFrom(self,string):
        for i in range(len(string)): #this is what makes this trie a suffix trie 
            self.insertSubstringStrargingAt(i,string) #generate all suffixes and inserts them in the trie
    
    def insertSubstringStrargingAt(self,i,string):
        node = self.root # current node, start at the root node, empty hashtable
        for j in range(i, len(string)): 
            letter = string[j] #iterate throgh substring starting from current letter
            if letter not in node: #if the letter is not a key stored in our current node
                node[letter] = {} #create a new node for the letter, essentially adding all unique letters as keys in root node dictionary
            node = node[letter] #otherwiseupdate current node to node of current letter, either existing or just created above
        node[self.endSymbol] = True   #add an asterisk to the node of the last letter, boolean used in contains logic

    #O(m) time | O(1) space
    def contains(self,string):
        node = self.root  #starting from the root node
        for letter in string: #traverse through the contains string
            if letter not in node: #if current letter is not a key in our current node
                return False #then contains string is not a valid subtring
            node = node[letter] #keep going down the substrings and their nodes
        return self.endSymbol in node #if a valid suffix, last letter node will contain the endSymbol as key
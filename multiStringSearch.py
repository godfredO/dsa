"""The question is to write a function that takes in a big string and an array of small strings, all of which are smaller in length than the
big string. The function should return an array of booleans, where each boolean represents whether the small string at that index in the 
array of small strings is contained in the big string. Note that you can't use language-built-in string matching methods. There are three
solutions discussed below with different complexities. """

""" If we were allowed to use language-built-in string matching methods
def multiStringSearch(bigString, smallStrings):
    array = []
    for smallString in smallStrings:
        nextIdx = bigString.find(smallString, 0)
        if nextIdx == -1:
            array.append(False)
        else:
            array.append(True)
    return array

"""

"""Naive solution where for each small string we iterate through the big string until we find it or dont. So the idea is to iterate through
the big string until we match the first letter of the small string, O(b), and once we match the first letter we match every letter in the
small string, O(s) and we repeat this for all of the strings O(n), giving a complexity of O(bns). The code implementation is broken up into
the O(n) step, the O(b) step, O(s) step. In the O(b) step we iterate through the bigString indices for a starting index and we break if 
we ever don't have enough letters left in the big string to match the small string. Also if the O(s) step returns True, for match found, we
return True from the O(b) step to be filled into the list comprehension for the O(n) step. In the O(s) step we actually match the first and 
last letters of the small string and move inward. Thus we intialize for the big string, a left pointer at the starting index passed from the 
O(b) step and a right index by adding the last index of the small string to this starting index. The left and right pointers of the small
string is always 0 and len(smallString) -1. If we match the entire small sting, we break out loop because our pointers for the big string
crossed and the return True. If however we ever are in a situation where the letters at the corresponding pointers for big and small string
don't match we return False. Also, the use of left and right indices is also the reason why we make sure to break out of the O(b) loop if
we dont have enough remaining letters in the big string for the entire small string.

PS Because map() maps the elements in an iterable to a function, its only useful for functions that take only one input, which map will
provide as each element of the iterable in turn. ie cant use map() for isInBigString() since that requires two inputs. FYI, i thought I
could use map() and learned this. Anyway the list comprehension used here is far more intuitive anyway. """


#O(bns) time | O(n) space
# def multiStringSearch(bigString,smallStrings):
#     return [isInBigString(bigString,smallString) for smallString in smallStrings] #O(n)

# def isInBigString(bigString,smallString): #O(b)
#     for i in range(len(bigString)):
#         #if we are at a point in the big string where the small string is too long
#         if i + len(smallString) > len(bigString): #if too few letters to match
#             break #break out of for loop
#         if isInBigStringHelper(bigString,smallString,i):#if we match small string
#             return True #return True because we found small string in big string
#     return False #if we break or reach end of big string without matching return False

# def isInBigStringHelper(bigString,smallString,startIdx):#actual character comparison #O(s)
#     leftBigIdx = startIdx #big string left pointer for comparing first characters
#     rightBigIdx = startIdx + len(smallString) - 1 # right pointer for last characters
#     leftSmallIdx = 0 #small string left pointer for comparing string first characters
#     rightSmallIdx = len(smallString) - 1 #small string right pointer for last characters

#     while leftBigIdx <= rightBigIdx:
#         if ( 
#             bigString[leftBigIdx] != smallString[leftSmallIdx] or
#             bigString[rightBigIdx] != smallString[rightSmallIdx]
#             ) : #if the first letters and last letters don't match
#             return False #no need to match inner letters
#         #if the current first and last characters for bigString and smallString match
#         leftBigIdx += 1 #increment left pointer to compare inner characters of bigString
#         rightBigIdx -= 1 #decrement right pointer to compare inner characters of bigString
#         leftSmallIdx +=1
#         rightSmallIdx -= 1
#     return True #if all inner characters match for current startingIdx, smallString matched


"""In approach two we build a modified suffix trie from the big string and then for each small string we search the modified suffix trie to see 
if the small string is contained in it. This is a modified suffix trie because we dont add an end symbol to denote the end of a suffix. After,
generating all suffixies of the big string and inserting the suffix in the trie letter by letter, we go through the smallstrings and check if
each small string is contained in the big string suffix trie. Because there is no end symbol, we just need to find all the letters of the small
string in the root contiguousluy starting from the root node and checking if the current letter is in the current node. If it is, we update the
current node to the current letter node and move on to the next letter checking if that is in the updated current node. If there is ever a point
where the current letter is not in the updated current node, we return False because the word is not contained in the big string. As long as we 
find all the letters in a particular string contiguously without hitting the False return statement, then we return True."""
class ModifiedSuffixTrie:

    def __init__(self,string):
        self.root = {}  #initialize the root node for the trie to be built
        self.populateModifiedSuffixTrieFrom(string) #then populate the modified trie with string

    def populateModifiedSuffixTrieFrom(self,string):
        for i in range(len(string)): #loop through string, for each index or letter in string
            self.insertSubstringStartingAt(i,string) #insert letter into the root node and build trie out
    
    def insertSubstringStartingAt(self,i,string):
        node = self.root #current node starts at root node
        for j in range(i,len(string)):#loop through string starting at the index passed
            letter = string[j] #pick out letter at current index
            if letter not in node: #if the current letter is not in the current node
                node[letter] = {} #add a new dict as the value for the current letter key in current node
            node= node[letter] #then or otherwise, change current node to be current letter node

    def contains(self,string):
        node = self.root #current node starts at root node which contains each letter in big string
        for letter in string: #loop through letters in small string, starting current node from root
            if letter not in node:#if current letter is not in the current node, either root or advanced node
                return False #then return False because small string can no longer be matched
            node = node[letter] #change into the key in current node that matches current letter
        return True #if we loop through each small string letter and never hit False then we fully matched 

#O(b^2+ns) time | O(b^2 + n) space
# def multiStringSearch(bigString,smallStrings):
#     modifiedSuffixTrie = ModifiedSuffixTrie(bigString) #create modified suffix trie of big string
#     return [modifiedSuffixTrie.contains(smallString) for smallString in smallStrings] #check each small string

"""Approach three creates a trie of the small strings and then matches the substrings in the big string to the trie. This is a general Trie
class so it doesnt take in a string. When instantiated, it only has the root node and the endSymbol. However it has an insert method that
works as expected ie last node has the end symbol mapped to the string that was inserted. Then we have loop through the indices of the big 
string for possible first letters of substring. In effect this is the populateSuffixTrie method from suffix tries question . For each index, 
we loop through the suffix/substring it represents and check if the first letter of the substring is in the root node of the trie of small 
strings. If it is not, we break out of this secondary loop and advance the index for the first letter. This secondary loop is also the
contains() method of a regular suffix trie class. If the first letter is in the root node, we update the current node to the current letter's 
node and then check if we found a word by checking if the current node has the end symbol in it. Because we store the small string as the value 
for the end symbol key in our trie, if there is an end symbol, we add its value, the small string, to a dictionary. This way we have one loop 
finding the possible first letter of a possible small string and a second loop using a trie to find a match. This is effectively like both s
olution one and solution two and improves the complexity because the first loop is O(b), the second loop is O(s) and the trie creation is O(ns), 
giving a total complexity of O(bs + ns). We store all found substrings in a dictionary so that this way we can return True if a small string is 
in this dict of found substrings, otherwise False ; dictionaries provide constant time lookup operations. In this approach it is necessary to 
use an end symbol to denote the end of a suffix. Also we store the small string as the value to the end symbol key. Since we are only adding
the found strings to the hashtable and we don't need to store any values, we can use a set() instead of a dictionary 
ie set.add(node[trie.endSymbol])

This solution improves on solution two by 'inverting' solution two, a technique used in the apartment hunting question to get an optimal 
solution. In solution two we build a suffixtrie with the big string which involves generating suffixes and inserting them into the trie, O(b^2) 
and then we match the smallStrings O(ns). In this solution we create a generic trie with the smallStrings O(ns) and then generate suffixes of 
the bigString and match these suffixes O(bs), storing found smallStrings in a dictionary which provides constant time lookup for the final 
list comprehension loop O(n) which doesnt worsen time complexity because we already have an O(ns) step ie O(ns + bs + n)  -> O(ns + bs)."""

#O(ns + bs) time | O(ns) space
class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"
    
    def insert(self,string):
        current = self.root
        for i in range(len(string)): #loop through string
            if string[i] not in current:
                current[string[i]] = {}
            current = current[string[i]]
        current[self.endSymbol] = string #add the end symbol pointing to the contained string

def multiStringSearch(bigString,smallStrings):
    trie = Trie() #create an instance of Trie
    for string in smallStrings: #loop through small strings array
        trie.insert(string)  #for each string, insert it in the trie
    #next, we create an object of substrings in the big string that are contained in trie
    containedStrings = {} #using a dict of found substrings allows constant time lookup of each small string
    for i in range(len(bigString)):#check if big string's substring at index i is a valid suffix of small strings' trie
        findSmallStringsIn(bigString,i, trie,containedStrings) #helper method matches substrings and updates dict 
    return [ string in containedStrings for string in smallStrings]

def findSmallStringsIn(string,startingIdx,trie,containedStrings):
    currentNode = trie.root #start at the root node of the trie of small strings
    for i in range(startingIdx,len(string)): #loop through each letter of the substring
        currentChar = string[i] #current letter of substring
        if currentChar not in currentNode: #the current letter is not in current Node, break out of for loop
            break   #break out of this loop and go back to for i in range(len(bigString)) for new first letter
        currentNode = currentNode[currentChar] #go one level deeper in trie, if letter is in 
        if trie.endSymbol in currentNode: #if we find the end symbol key in the current Node
            containedStrings[currentNode[trie.endSymbol]] = True #add the stored string to dict with True value



        



bigString = "this is a big string"
smallStrings = ["this", "yo", "is", "a", "bigger", "string", "kappa"]
print(multiStringSearch(bigString,smallStrings))



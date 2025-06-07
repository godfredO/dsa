"""The input is two non-empty strings: a big string and a small string. Write a function that returns the smallest substring in the big
string that contains all of the small string's characters. The substring can contain other character's not found in the small string.
The characters in the substring don't have to be in the same order as they appear in the small string. And if the small string has
duplicate characters, the substring has to contain those duplicate characters (it can also contain more, but not fewer). We are also
assured that there will be only one relevant smallest substring. eg if bigString = 'abcd$ef$axb$c$' and smallString = '$$abf', the
smallest substring is 'f$axb$' """

"""This optimal solution uses the sliding window technique. We start by adding the character counts of the small string to a hashtable and 
keeping track of the total unique character count also, which will be the number of keys in the hashtable. The use of a hashtable also 
allows us constant time access to unique characters and their counts. So to find the smallest substring of the big string that contains
the the small string, we need to first be able to generate substrings, verify that the contain all the characters in the small string and
have a way of keeping track of the lengths of any such substrings in order to find the answer, which is where the sliding window technique
and hashtable summaries of substrings come in. We initialize both the L and R pointers at the start of the big string. We keep moving the 
R pointer and if we find a character in the big string that is also in the small string, we add that to a separate hashtable to keep track 
of the small string characters that have been found in the big string. That is to say we use the right pointer and the new hashtable to find 
the end of any substring that contains the all the characters of the small string. That is if this bigString hashtable contains all the keys 
of the smallString hashtable and each key matches or exceeds their respective counts in the smallString hashtable, we know that the substring 
between L and R represents a viable answer to the question, so we can use these pointers to calculate the length of the substring and we also 
store the pointers for use as slice indices. Thus we employ the common string technique of using slice indices to track substring lengths. 
Then we need to possibly find a smaller substring that also answers the question. Whenever we find that this big string hashtable equals the 
smallString hashtable, we update the minimum length substring variable and move the L pointer until the two hashtable counts are no longer the 
same then we start moving the right pointer again. 

In the code to find viable substrings and the smallest viable substring, we use a helper function, that initializes the substringBounds at
[0, float("inf")], an empty bigString hashTable, a variable numUniqueChars, which is simply the number of keys in the smallString hashtable,
(len(hash.keys())) numUniqueCharsDone, which will be used to track keys in the bigString hashtable whose counts match or exceed their respective 
counts in the smallString hashtable and which is initialized at 0 and of course L, R pointers which both start at index 0. We also have three 
smaller helper functions that abstract repeated operations of the main helper function here namely, increaseCharCount(), that takes a character 
and a hashtable and adds/increments a found character's count in the hashtable, decraseCharCount() which also takes a character and a hashtable 
and decreases an existing character's count in the hashtable, and finally getCloserBounds, that takes the updates the stored slice indices by 
comparing its length to a new viable substrings slice indices. So in the main function we keep iterating through the bigString while right 
pointer is within bounds ie this while loop's condition is while rightIdx < len(bigString). So we access the current letter at rightidx, check 
if it is in the smallString hashtable. If its not we increment rightIdx and continue, meaning we go back to the top of the while loop without 
running the remaining lines of code inside the loop. If the current letter is in the smallString hashtable, we pass it to the incraseCharCount 
with the bigString hashtable to increment its count. Then we check if the updated count is equal to the corresponding count of the current 
letter in the smallString hashtable, in which case we increment numUniqueCharsDone by 1. We use the equal to comparison instead of the equal to 
and greater than to ensure that we count each found key only once. Then we have an inner while loop that only runs once we have found all the 
required characters. That is to say the outer while loop moves the right pointer until all the characters are found and the inner while loop 
moves the left pointer only when all the characters have been found. Since we move only one pointer at a time, even though these while loops 
are nested, they still represent a linear traversal of the bigString and at any point, we would have done an O(r+l) traversal instead of an 
O(r*l) traversal. Thus inner while loop's condition is while numUniqueCharsDone == numUniqueChars and leftIdx <= rightIdx. The first thing we 
do in this inner loop is to compare the current indices of leftIdx and rightIdx to the stored slice indices, updating it if the current indices 
are found to be shorter. To do this, we pass leftIdx, rightIdx, storedStartIdx, storedEndIdx to getCloserBounds(). This mini helper function 
computes the lengths of both pairs of indices and returns a list of the current indices if they are found to be shorter otherwise returns a list 
of the stored bounds. Whatever list this mini helper function returns becomes the new stored sliced indices, thus we update the slice indices to 
a new or the same array each time we find all the small string character in the substring between leftIdx and rightIdx. Now that we have updated 
the stored slice indices, its time to move leftIdx. Similar to how we move rightIdx, we access the current letter at leftIdx and check if it is 
in the smallString hashtable. If its not, we increment leftIdx and continue to the top of the inner while loop. If it is, we decrement the count 
of the current leftIdx letter in the bigString hashtable, using decreaseCharCount() and increment leftIdx to advance. However before we decrement 
the count, we first check if the current count is equal to the count of the leftIdx letter in the smallString hashtable because if it is, we know 
that after decrementing its count in bigString hashtable we will not have the required character numbers between leftIdx and rightIdx to match 
smallString, so we decrement the numUniqueCharsDone by 1 before decrementing the count and advancing leftIdx. Decrementing numUniuqeCharsDone 
will thus terminate the inner while loop at the next loop condition check and then outside the inner while loop but inside the outer while loop 
we increment rightIdx to find the try and find another valid substring.

Thus we advance rightIdx to find a valid substring and we advance leftIdx to minimize the length of a valid substring until we render the
current substring invalid which will prompt rightIdx to move until another valid substring is found. 
This technique of using two indices for string matching and storing slice indices as we go is a common technique in string questions, along
with using hashtables to summarize strings.

At the end when we have the bounds representing the smallest substring that answers thequestion, we simply slice it out of the string 
using string[start:end+1] if end is not float("inf) otherwise we return an empty string as the answer. This functionality is habndled in a
helper function that unpacks the bounds and checks the end bound to choose the answer to return. """

#O(b+s) time | O(b+s) space
def smallestSubstringContaining(bigString,smallString):
    targetCharCounts = getCharCounts(smallString) #summarize small string character counts into a hashtable
    substringBounds = getSubstringBounds(bigString,targetCharCounts) #bounds of shortest big substring containing small string
    return getStringFromBounds(bigString,substringBounds) #construct smallest substring from bounds and return

def getCharCounts(string): #function to summarize the character counts in a string
    charCounts = {}
    for char in string:
        increaseCharCount(char,charCounts) #helper function because this functionality is used elsewhere
    return charCounts

def increaseCharCount(char,charCounts): #helperfunction updates the hashtable passed to it, returns nothing
    if char not in charCounts:
        charCounts[char] = 0
    charCounts[char] += 1

def decreaseCharCount(char,charCounts): #helper function updates the hashtable passed to it, returns nothing
    charCounts[char] -= 1 #if we are decreasing char's count we assume char already in hashtable

def getSubstringBounds(string,targetCharCounts):
    substringBounds = [0,float("inf")] #return indices, intialized at 0, inf to identify if no substring found
    substringCharCounts = {} #hashtable to track big string char counts that are in targetCharCounts
    numUniqueChars = len(targetCharCounts.keys()) #to track fully found chars in big string whose counts == targetCharCounts
    numUniqueCharsDone = 0 #to track fully found chars in big string whose counts == targetCharCounts, ie == numUniqueChars
    leftIdx = 0
    rightIdx = 0
    while rightIdx < len(string): #keep moving rightIdx until its out of bounds
        rightChar = string[rightIdx] #read the bigstring char at rightIdx, if not in small string continue to next char
        if rightChar not in targetCharCounts: #if current char not in small string, keep moving by incrementing rightIdx
            rightIdx += 1 #keep moving rightIdx if current big string char not in small string
            continue #ie don't excecute next line, go back to check rightIdx not out of bounds and read the next big string char
        #if we don't hit continue statement its because we found a big string char that's in small string
        increaseCharCount(rightChar,substringCharCounts) #increase the count of the found big char thats also in smallstring
        if substringCharCounts[rightChar] == targetCharCounts[rightChar]: #if we just fully found rightChar in bigstring
            numUniqueCharsDone += 1 #then increment number of fully found big string chars thats also in small string
        while numUniqueCharsDone == numUniqueChars and leftIdx <= rightIdx:#while substring bounds valid and contains small string
            substringBounds = getCloserBounds(leftIdx,rightIdx,substringBounds[0], substringBounds[1]) #smallest substring bounds
            leftChar = string[leftIdx] #read big string char at leftIdx, to see if substring shortening wont remove needed chars
            if leftChar not in targetCharCounts:#if leftChar is not in small string we can shorten the smallest substring
                leftIdx += 1 #move leftIdx forward by incrementing it, to shorten substring without losing small string chars found
                continue #the go back to the current while loop, update bounds and check leftChar
            #if the leftChar is in small string, then moving it would lose a needed char
            if substringCharCounts[leftChar] == targetCharCounts[leftChar]:#if moving the leftIdx would remove a required char
                numUniqueCharsDone -= 1  #update the number of fully found chars, since moving leftIdx would remove a needed char
            decreaseCharCount(leftChar,substringCharCounts) #decrement the count for current leftChar
            leftIdx += 1 #then increment leftIdx possibly removing a needed char while we have all the chars we need
        rightIdx += 1 #rightChar in targetCharCounts, maybe count matched targetCharCounts[]
    return substringBounds

def getCloserBounds(idx1,idx2,idx3,idx4): #compare the new bounds found to the existing bounds, using inf helps easy comaparison
    return [idx1,idx2] if idx2 - idx1 < idx4 - idx3 else [idx3,idx4] #if new bounds is shorter, update the bounds

def getStringFromBounds(string,bounds):
    start, end = bounds #unpack bounds
    if end == float("inf") : #if we never updated the bounds
        return "" #return empty string because we didnt find a substring of big string that contains all small string chars
    #otherwise if we found a substring of big string that contains all small string's chars, then slice the substring out
    return string[start:end+1] #+1 due to python slice endIdx exclusivity
    


bigString = "abcd$ef$axb$c$"
smallString = "$$abf"
print(smallestSubstringContaining(bigString,smallString))

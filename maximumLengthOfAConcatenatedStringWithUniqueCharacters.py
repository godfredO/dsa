"""You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters. 
Return the maximum possible length of s. A subsequence is an array that can be derived from another array by deleting some or no elements 
without changing the order of the remaining elements.

Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

Example 2:
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").

Example 3:
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.
 

Constraints:
1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.


So this is a combination question, as we are seeking concatenation (think combination) of subsequences (thing indices) of the strings in
the input array. We can only concatenate a subsequence if the resulting string won't have duplicates. In otherwords, we could have
duplicates if we concatenate indiscriminately. So the first question to ask our selves is how do we represent the decison tree. Do we use 
a binary decision tree or a n-ary decision tree. And the answer is that we use a binary decision tree (think combinationSum.py and 
combinationSumII.py). This will give us the maximum control in what we choose. In general, combination questions can first be modeled with
a binary decision tree and improved to a n-ary decision tree if we find that we can do that and not risky uncontrolled duplicates.

So what are the two choices we can make? At each level for the element at the index passed, we can choose it or not choose it. That is for 
an array of length n and if the maximum string length is m, the time complexity is O(m*2^n). Once we are able to build and analyze the 
decision tree, the main thing will be how to code up the solution. Mainly we can create all possible concatenations, adding checks to our 
decision tree such that we make a decision to continue down a path if the current candidate contains unique characters when compared to the 
elements in the current concatenation of that path and we track the max length of concatenations with unique characters.

Obviously to check if thre are duplicates between a concatenation and a string, we will need to keep track of the counts of the characters 
in any concatenation with a set. That is down any path, we track the letters in the current concatenation with a set of letter counts and
we will be comparing any condidates string to this charSet of the current concatenation path. In other words, we dont actually need to store 
a string for the current concatenation, just a set of its letter counts. To compare the current candidate to the concatenation we write a 
function that compares the charSet of the current concatenation to a charSet of the curent candidate. In the code this function is overlap().

So we build our own function called overlap() which can use or own logic, or we can use the inbuilt Counter module of python. When Counter() 
is passed an iterable, it creates a hashmap where the keys are the unique elements in the iterable and the values are the counts of the 
unique elements. So if using the Counter module, we simply create a counter of our concatenation charSet, and union that with a concatenation 
of our candidate string, access the values of this union hashmap and return if the max value is greater than 1, which will return True if 
we have duplicates or False if there are no duplicates. Checking max value is a clever way of asking if any value is greater than 1. If using 
our own logic we can initialize a prev set, iterate through the candidate string and add each letter to our prev set but before we do that we 
check if the letter is already in the prev set (the candidate string already has duplicates as is) or if the letter is in the charSet of our 
current concatenation (ie we will have duplicates if we add the candidate string), in which case we instantly return True from our overlap()
otherwise we return False.

So to our backtracking itself. We initialize a charSet for current concatenation path as an empty set, then pass this with our initial 
current candidate string index of 0. Since we are using a binary decision tree to avoid duplicates, we go left, backtrack, then go right. As 
we go left we add the current candidates letters to our charset if they don't overlap, and make a recursive call with an incremented index for 
the next candidate string. As we go right, we don't add the current candidates letters but we still need to pass in the original concatenation 
charSet as is and an incremented index for the nex candidates string. As a result, in between the go left and go right steps, we back track by
removing the current candidate string's letters from the current concatenation charSet. We need to track the max unique concatenation length
somehow ie our backtracking algorithm should return the max length of unique concatenation of any path. Here for each recursive call, we 
initialize a result variable at 0 and update it to the max of going left and going right and then return that. The base case is that if we
ever call our function with an index that is out of bounds, we return the length of the charSet as is. By initializing length as 0, we know
that we can return that if the going left will lead to duplicates or

"""

def  maxLength(arr):
    charSet = set()   #initial concatenation path charSet
    return dfs(charSet, 0, arr)   #initial dfs backtracking call

def dfs(charSet, idx, arr):
    if idx == len(arr):  #if out of bounds
        return len(charSet)   #return the lenggh of the current charSEt
    
    length = 0   #max length for paths rooted at this subtree of the binary decision tree
    candidate = arr[idx]    #access current string in input
    if not overlap(charSet, candidate): #we only go left if current string wont overlap, if not
        for letter in candidate: #add current string to concatenation
            charSet.add(letter)

        left = dfs(charSet, idx + 1, arr)  #go left
        length = max(length, left)  #update the max length after going left

        #backtrack
        for letter in candidate:
            charSet.remove(letter)
        
    right = dfs(charSet, idx + 1, arr) #go right
    length = max(length, right)   #update max length after going right
    return length   #return max length rooted at current subtree


def overlap(charSet, candidate):
    prev = set()
    for letter in candidate:
        if letter in charSet or letter in prev :
            return True
        prev.add(letter)
    return False


"""An alternate version of overlap() using Counter module"""
from collections import Counter
def overlap(charSet, candidate):
    union  = Counter(charSet) + Counter(candidate)
    return max(union.values()) > 1
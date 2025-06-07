"""Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character 
in t (including duplicates) is included in the window. If there is no such substring, return the empty string "". The testcases will 
be generated such that the answer is unique. A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window. Since the largest window of s only has one 'a', return empty string.
 
Constraints:
m == s.length ; n == t.length ; 1 <= m, n <= 105  ; s and t consist of uppercase and lowercase English letters.


Hint 1:  Use two pointers to create a window of letters in s, which would have all the characters from t.
Hint 2:  Expand the right pointer until all the characters of t are covered.
Hint 3:  Once all the characters are covered, move the left pointer and ensure that all the characters are still covered to minimize 
the subarray size.
Hint 4:  Continue expanding the right and left pointers until you reach the end of s.


This question is the same as algoexpert's smallestSubstring.py. This question is an application of the sliding window technique. In 
this question the window is going to contain some substring of string s. So in sliding window, we move the right pointer while doing
some logic to widen the window, and when a particular condition is met, we move the left pointer to shrink the window. 

So in this question what logic will be doing while moving the right pointer. We will be keeping a count of the number of occurences of 
string t's letters inside our window. In addition we will be checking if we have enough of each of string t's letters inside the window. 
So if the current right pointer letter is in string t, we increase the count in hashtable and if we have enough of that letter we 
increment a found variable. How do we know that we have enough? Well we first create a map of string t's letter count so if the count 
of our current right pointer letter equals its count in string t's count, we know that we have enough and we increment found variable. 
Note that if its essential that we increment the count before checking if we have enough. Also afterwards, if we find more instances of 
the same letter, we increment its count in the string s map, but we dont increase found on account of that letter. When we have enough 
of each letter in string t inside our window, its time to shrink the window by moving the left pointer. How do we know that this is the
case? When found equals the number of keys in string t's letter count map, a number we will call required. That if found = 1 it means
we found enough instances of 1 key in map of string t inside our window. When found == required, it means we have enough instances for 
all of the keys in map of string t inside of our window.

So why do we shrink the window? Because, the question is asking us to return the minimum window substring, so as soon as we have a 
valid substring of s that contains enough instances of all the characters of t, we want to see if we can shrink the window and still
have enough instances of the characters of t inside the new window. But first we have to update our slice indices for our final return
statement. If right + 1 - left is less than the current stored slice indices we update the current slice indices first. Then we can
start shrink the current window. If the current letter pointer is not in strig t, we just increase the left pointer. If the current left 
pointer letter is in map of string T, we first check if the current count in map of string s is exactly equal to the count in map of 
string t. This means that if we advance the left pointer and decrease the count accordingly, found will no longer equal required. So if
that is the case, we decrease found before decreasing the letter count. Otherwise we just decrease the letter count in string s's map.

At the end if our slice index was unchanged, we return "" because we didnt find string t inside string s otherwise we use the updated
slice indices to to slice the relevant substring out of string s and return that substring as the answer. 
"""
#O(s+t) time | O(s+t) space
def minWindow(self, s: str, t: str) -> str:
        mapT = {}
        for letter in t:
            addCount(mapT, letter)
    

        found , required = 0, len(mapT)
        mapS, bounds = {}, [0,float("inf")]
        left = 0
        for right in range(len(s)):                             # widen window  
                                
            rightChar = s[right]
            if rightChar in mapT:                               # increase counts till substring is valid
                addCount(mapS, rightChar)                       
                if mapS[rightChar] == mapT[rightChar]:          # check if increasing letter count will increase found
                    found += 1                                  
     
            while found == required and left <= right:          # if substring is valid, start shrinking window
            
                if right + 1 - left < bounds[1] - bounds[0]:    # first check if min window bounds need update
                    bounds[0], bounds[1] = left, right + 1      

                leftChar = s[left]                              #the idea is to remove all the unnecessary left letters    
                if leftChar in mapT:                            #if the left char not in mapT, moving it wil not change found
                    if mapS[leftChar] == mapT[leftChar]:        # check if decreasing letter count will decrease found
                        found -= 1                              
                    decreaseCount(mapS,leftChar)                

                left += 1                                       # shrink window  
        
                                                  
        return s[bounds[0]: bounds[1]] if bounds[1] != float("inf") else ""    #return empty string if t not in s


def addCount(map, letter):
    if letter not in map:
        map[letter] = 0
    map[letter] += 1

def decreaseCount(map, letter):
    map[letter] -= 1
    



        
s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s,t))
"""The input is a string and the question is to write a function that returns the longest substring without duplicate characters. For the
string 'clementisacap', the answer is 'mentisac'. We are only interested in substring that contain non-duplicate characters, so the brute
force approach would be to find all substrings that contain no duplicates and return the longest substring with no duplicates. The first
thing here is to use a technique common in many array, string and dynammic programming questions where we re-formulate a question to
reflect 'ending at' instead of 'starting at'. That is to say instead of looking for non-duplicate substrings starting at the character
at each index, we look instead for non-duplicate substrings ending at the character at each index of the input string. This technique has 
the effect of changing a double nested for loop that chooses starting and ending points for a substring into a single for loop for choosing 
the ending point. This approach is used in the longest palindromic substring problem where instead of choosing the starting and ending
index of a palindrome, we instead choose the center of a palindrome and move from a nested loop to a single loop. Anyway we initialize a
startIdx = 0 outside our main for loop and use the for loop to choose the ending index for non-duplicate substrings. As a variable, starIdx
denotes the index at which the current longest non-duplicate starts. Thus at any ending index in the loop, the length of the current 
non-duplicate substring is endingIdx + 1 - startIdx. We also initialize an array, longest, to store the indices to be used to slice the 
longest non-duplcate substring out of the input string. We initilize this array ,longest = [0,1] ,which when used to slice the string 
string[0:1] will yield the first letter.  We also initialize an empty hashtable, called lastSeen, to help us detect duplicate letters.

So we iterate through the string, at each letter, we add the letter to a hashtable, with the letter as key and the index as value. 
But before we add to the hashtable, we do some checks. If we ever come to a letter in the loop that is already in this hashtable, it 
must be a duplicate so we need to update the starting index used for slicing for the longest non-duplicate substring ending at the current 
index to the max(startingIdx,lastSeen[letter] +1). That is to say, we update startingIdx to the index after the last occurence of the current 
letter if this is greater than startingIdx as it stands. First of all why do we add 1 to the last occurrence of the current character? It is
because to achieve non-duplicate substring, any substring that contains the current letter cannot contain the last occurrence of the current
character and as such any substring will have to start at the letter after the last occurrence in order to be a valid substring as well as a
non-duplicate substring. And why do we do a maximum comparison with the startIdx as it stands? We do that,just in case startingIdx was shifted 
by another letter whose last occurence occurs after the last occurence of the current letter Eg for the string 'acbabc', when at index 5, c, 
the last occurence of c is at index 2 so last occurrence + 1 would be 1+1 ie 2. But saying the longest non-duplicate substring ending at index 
5 starts at index 2 would be wrong because b at index 4 would have shifted startIdx to 2 after its last occurence ie 2+1 which is 3. So that 
substring endig at 5 but starting at 2 ie babc would contain a duplicate b, but one ending at index 5 but starting at index 3, abc would 
contain no duplicates. 

So after updating starting index, we know we have the startingIdx of the longest non-duplicate substring ending at the current index, 
but we need to track the longest such substring seen, with indices, so that we can return it via slicing. To do this we compare the length of 
the non-duplicate substring ending at the current loop index with the current longest indices for the longest non-duplicating substring. That 
is if i + 1 - startIdx > longest[1] -longest[0], we update longest to [startIdx, i + 1]. The +1 here is for Python's exclusivity in slicing and 
neatly yields the correct length count.  So after updating startIdx, and longest indices, we finally update the index in our lastSeen hashtable 
for the letter at the current index. At the end of the iteration, we use the longest indices to slice our longest non-duplicate substring. The 
hashtable will contain as many keys as there are unique letters in the string and this is either all the unique letters in the alphabet or the 
length of the string, for short strings, so O(min(n,a)) space where a= is the length of the alphabet. The reason for this is because a really 
really long string with all the letters of the alphabet in there will only have as many keys as there are in the alphabet. Even if the string 
is really long and doesnt contain all the letters of the alphabet, the max number of keys is the number of letters of the alphabet.  
The time complexity is linear time O(n).

This solution uses a clever application of the 'ending at' technique and the use of hashtables. In summary, we iterate through the string 
and at each index we store char:idx inside a hashtable, which is used to detect duplicates but before we update the hashtable, we first
use it to check if the current letter is a duplicate and if it is, we update startIdx, then we calculate the length of the non-duplicate
string ending at the current index and update a longest array which stores indices for string slicing. """


#O(n) time | O(min(n,a)) where n = number of letters in string, a= string alphabet or number of unique letters 
def longestSubstringWithoutDuplication(string):
    lastSeen = {} #indices of most recent appearances of each letter
    longest = [0,1] #indices for longest non-duplicate substring; initialize at first letter(Python zero index)
    startIdx = 0 #starting index for longest non-duplicate substring that ends with current letter

    for i, char in enumerate(string):
        #first is to check if current letter is a duplicate
        if char in lastSeen:#if current letter is a duplicate, 
            startIdx = max(startIdx, lastSeen[char] + 1) #update start index 

        #next is to update longest non-duplicate substring seen, if current non-duplicate substring is longer
        if longest[1] - longest[0] < i+ 1 - startIdx: #because of Python's zero index add + 1
            longest = [startIdx, i + 1] #because of Python's zero index add + 1
        
        #last is to update hashtable
        lastSeen[char] = i
    return string[longest[0]:longest[1]]

string = "clementisacap"
print(longestSubstringWithoutDuplication(string))
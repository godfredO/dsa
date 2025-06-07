"""You are given a string s and an array of strings words. All the strings of words are of the same length. A concatenated 
substring in s is a substring that contains all the strings of any permutation of words concatenated. For example, if 
words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. 
"acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words. Return the starting 
indices of all the concatenated substrings in s. You can return the answer in any order. s and words[i] consist of lowercase
English letters.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
The output order does not matter. Returning [9,0] is fine too.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation: Since words.length == 4 and words[i].length == 4, the concatenated substring has to be of length 16.
There is no substring of length 16 is s that is equal to the concatenation of any permutation of words.
We return an empty array.

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.

First we can create a dict to store the occurrence times for each word in words.

For example,
If s = "barfoofoobarthefoobarman" and words = ["bar","foo","the"],
the dict will be word_count = {'bar': 1, 'foo': 1, 'the': 1},

Since all the strings stored in words have the same length, the size of sliding window will be the word length of a single string. 
In the example above, the sliding window will be 3.

bar -> foo -> foo -> bar -> the -> foo -> bar -> man
ignore b -> arf -> oof -> oob -> art -> hef -> oob -> arm -> ignore an
ignore ba -> rfo -> ofo -> oba -> rth -> efo -> oba -> rma -> ignore n
Then, we can scan s in these 3 ways one by one

Let the word in sliding window be word. Also, we will create a queue to store the scan history.

So this hard question is based on findAllAnagramsInAString.py and permutationInString.py, so first read those. The key 
difference here is that we are finding anagrams of words and not anagrams of the letters in those words. So if our words 
are "ab","cd", the valid anagrams are "abcd", "cdab", that is each word is treated like an indivisible entity. We are also 
told that all the words are of the same length, and we are to find these valid anagrams of words in a string s and return 
the starting indices of these. So first off our count hashmap is actually going to have the words as key and since we are 
not assured of uniqueness, its possible our list of words could be like 'ab', 'ab', 'cd' in which the count hashmap is 
{'ab':2,'cd':1}. Since all words have the same length, the length of a valid anagram will be the length of 1 word * number of 
words ie len(words[0])*len(words). Now this is the first tricky situation. What is the size of our sliding window? It will be the 
length of a single word ie len(words[0]), How does the choice of this size of window help us solve the question.

The idea is that we are going to find the valid substrings one word at a time. Since we are told that all words are the 
same size, say 3, we check if the first 3 words are in our string, if it is, we decrement the count by 1 assuming the count 
of that word isnt 0, then we append the word we just found to a queue. Now suppose the words are 'ab', 'cd' so we find 'ab' 
first, then 'cd', after we find each word, we check if the sum of the values in our count hashtable is 0, that is we found
each word and decremented their indices. In that case, how do we determine the starting index of the valid substring. So 
lets say the valid substring was from index 0 to 3, we did our first slice of index 0,1 and the next slice is index 2,3
(the step of the range function is the window size ie 1 word length), we know that the current word, which is the last
found word in the current valid substring is extends from s[j:j+wordLen], and so if we subtracted the the full length of a
valid substring from the this value we get to the start of the current valid substring ie j + wordLen - allWordLen (try
looking at the length / index math and it checks out). Now each time we  start a new search for a valid substring we 
actually make a copy of our actual count hashtable and its this copy that we increment and decrement. The reason for this 
is that there is no true backtracking, so if we get to the end of a path and we made changes to our actual count hashtable, 
those changes would be permanent. As a result whenever we initialize a new deque, we make a copy of our hashmap.


Now how do we advance our left pointer, we popleft() from our deque, storing the word we popped in some variable so that, 
we can use it to increment the count of that word in our count hashtable.  Now that happens if the current slice of wordLen 
size is not in our count hashtable or we already used all of it ie its count is 0. In that case we know that the current 
path wont yield a valid substring. In that case, if the queue is non-empty, we popleft to remove the first element we added. 
Now in the general case, we increment the count of that word in the hashtable, as a way of restoring the count, this is 
equivalent to shifting the left pointer. Now we before handling this general case we need to handle the edge case where the 
word slice we are looking for is actually the word we just popped left, meaning that we had previously used that occurrence 
earlier but we realize that is better to shift the current start of the current substring and use that occurrence here by 
appending it to the top of the deque. In that case we append the popped word to the top of the deque and break. Now in 
popping left to shif the left pointer, so to speek, we keep popping and incrementing till the queue is empty unles we meet
the edge case where we moved the word we just popped to the top of the queue and break. In otherwords, we have our actual 
start pointer (see the code) and the left pointer is generated from that and the right pointer will be the end of the last 
word on top of our queue, here the queue represents the substring. 

For an example of a solution where we use a deque so that popping left from deque is our way of shifting the left boundary,
look at my first solution on RepeatedDNASequence.py. The kind of variable width sliding window technique used here is
reminiscent of minimumWindowSubstring.py in that we have a hashmap for our current path or substring, and we compare it
to some other hashmap.





"""
from collections import deque
def findSubstring(s, words):
    counts = {}
    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1
    
    wordLen = len(words[0])
    substringLen = wordLen * len(words)
    result = []
    for startIdx in range(wordLen):
        queue = deque()
        currentMap = counts.copy()
        for j in range(startIdx, len(s)-wordLen + 1, wordLen):
            current = s[j:j+wordLen]
            if current in currentMap and currentMap [current] != 0:
                currentMap[current] -= 1
                queue.append(current)

                if sum(currentMap.values()) == 0:
                    result.append(j+ wordLen - substringLen)
                    leftMost = queue.popleft()       #shift left boundary and keep going
                    currentMap[leftMost] += 1        #shifting left boundary also means restoring count
            else:
                while queue:
                    leftMost = queue.popleft()
                    if leftMost == current:      #if popped is current, append to queue and continue
                        queue.append(leftMost)
                        break
                    else:
                        currentMap[leftMost] += 1  #pop and restore
    
    return result


    
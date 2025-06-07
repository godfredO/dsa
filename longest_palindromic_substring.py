""" The input is a string and the question asks to return the longest palindromic substring of the input string. This question clearly builds
on top of the palindormic check question. It should be noted that a single letter (sub)string is a palindrome. The brute force approach is to 
generate all substrings using slicing, check if each substring is a palindrome and if it is compare its length to the length of the longest 
palindromic substring seen so far. We use two nested for loops to choose the indices for the start and end of each substring, and we slice 
using these indices to generate the substring. Then we use a helper function to check for palindromicity before comparing the length of the 
current palindromic substring to the longest seen so far. The longest palindromic substring is initialized with an empty string and the time 
complexity is O(n*n*(n+n)), where n+n represents the slice and the palindromicity check. We use a for loop to choose the start of the substring, 
initialize the end of the substring to just after the start and use a while to expand the end of the substing to just past the last index, due 
to Python's exclusivity when slicing. Inside this while loop we slice, check for palindromicity and increment the ending index for the next 
substring slice. Instead of using a while loop, we can also use two for loops so that the ending index of each substring is inside a for loop. 
As a result, when slicing, we add +1 to the ending index to Python's exclusivity when slicing, but this is still the brute force approach.

The optimal approach, is based on the technique common in dyanammic programming -esque questions, like Kadane's algorithm, where instead of
considering starting and ending indices, you only consider ending indices. That is instead of using two indices to describe a substring we 
use one index to describe a possible palindromic substring. So do we consider starting indices or ending indices? The answer is neither. We 
consider center indices. So in this approach how do we consider all possible palindromic substrings? Well, we start by realising that 
palindromes are symmetrical about the center; the center of a palindrome is an empty string if the palindrome has an even-number length  eg 
'abba'; the center of a palindrome is a single letter string if the palindrome has an odd-number length eg 'abcba'. So how do we use these 
observations to solve this problem in a better time complextiy. We traverse the string with indices, starting from the second index ie index 1, 
to the end of the string, and at each point we check if the letter at the current index is the center of an even-length palindrome or a 
odd-length palindrome. Thus, we use a helper function, that expands outward from the center of the possible palindrome. In an odd-length 
palindrome the leftIdx is i-1 and the rightIdx is i+1 for the first comparison and outward from there. That is the letter at i is center of a 
possible palindromic substring. In an even-length palindrome, the leftIdx is still i-1 but the rightIdx is i, meaning the center of the 
possible palindromic substrig is the empty string between i-1 and i. This outward expansion starts at index 1 so that we can expand leftward on 
the first left/right check and is able to go to the end of the array because, when i is len(string) -1, the odd-length rightIdx is len(string) 
and the helper function will not even run but still returns the right answer to calculate the length of this odd-length palindromic string. This 
techique of expanding outward from a center is a variation of the  left / right boundary technique seen in 1-d arrays, which is itself a 
simplification of getNeighbors() technique. Anyway, with the given the leftIdx and rightIdx, how do we check for a palindrome based on its 
symmetry. If the letters at both indices are the same we decrement and increment the leftIdx and rightIdx respectively as long as we are in 
bounds. If they are not the same, or we break out of the loop, we return [leftIdx + 1, rightIdx] which would represent the indices we would 
use to slice for the substring. If it turns out that no substring centered at the current letter in the original for loop is a palindrome, 
the returned indices of [leftIdx +1, rightIdx] would slice into a single-letter for an odd-length and an empty string for an even-length. 
We then use these returned indices to calculate the length of the longest palindromic substring found that is centered at the letter 
at index i, using the formla rightIdx - leftIdx since, when we break out the loop, we are just outside the actual palindrome indices. 
That is if the palindrome is centered at index 1 , extends from index 0 to index 2, the helper function will terminate at leftIdx = -1 and 
rightIdx = 3 and we retun [leftIdx + 1, rightIdx] ie [0,3] so subtracting returnedIndices[1] - returnedIndicds[0] = 3 - 0 which is the correct 
length. So for each current letter, we calculate which is the longer palindromic substring, even or odd and then compare that to the longest 
length seen, and we store, the returned indices of the longest palindromic substring. In the code we use a very neat lambda function as the 
key to the max() function and this lambda function calculates the length using the returned indices and max() chooses the input with the max 
length. The initialized longest indices is initialized at [0,1] and would slice to a length of 1 which is the smallest possible palindrome
length, but since we are assured that there would be one longest palindromic substring, we expect this to be updated at some point otherwise
a single element palindrome can be any of the letters in the string. At the end of the algorithm, we use these indices to slice for the 
longest palindromic substring. This solution is O(n*(n+n)) ie O(2n^2) which is in the order of O(n^2), where n+n is for even and odd
palindromic checks. Also when choosing center indices we go from index 1 to the last index because at the last index we will have an even
length possible palindrome but the call to the palindromicity function for the odd will not pass the while loop check and that returned 
indices will yield the single element palindrome anyway so we are covered there.



It is to be noted, that while the general two pointer method for palindromicity check starts from the ends and moves inward based on the fact 
that palindromes are written the same backward and forward in linear time, we could write a palindromicity check linear time function that 
expands outward from the center using two pointers and the position of those pointers will depend on whether the palindrome has an even
number length or an odd number length, that is a palindromicity check based on the symmetry of palindromes instead of the backward
forward nature of palindromes.
"""

"""
Generate all possible substrings and check for palindromicity
"""
# O(N^3) time
def longestPalindromicSubstring(string):
    longestPalindrome = "" #initialize longest palindromic substring as empty string
    # Generate all substrings O(N^2)
    for i in range(len(string)): #O(n) for start of substring
        j = i+1
        # <= ensures that single character strings are valid substrings of itself
        while j <= len(string): #O(n) loop, j is for slicing for end of substring, so goes to len(string) due to slice exclusivity
            sub = string[i:j] #O(n), slice of string
            if isPalindrome(sub) and len(sub) > len(longestPalindrome): #O(n), that is O(n) + O(n)
                longestPalindrome = sub
            j +=1      
    return longestPalindrome

# Check for palindromicity
def isPalindrome(sub):
    l=0
    r = len(sub) - 1
    #this while loop doesnt include the center of array
    #this while loop returns True for single character strings
    while l < r:
        if sub[l] != sub[r]:
            return False
        l += 1
        r -= 1
    return True

# Same solution as above using two for loops 
# note the way index j and subString is defined
def longestPalindromicSubstringII(string):
    longestPalindrome = ""
    for i in range(len(string)):
        for j in range(i,len(string)):
            substring = string[i:j+1]
            if isPalindrome(substring) and len(substring) > len(longestPalindrome):
                longestPalindrome = substring
    
    return longestPalindrome


# O(N^2) solution using odd / even palindromic center techique
def longestPalindromicSubstringIV(string):
    currentLongest = [0,1] #storing the indices for the start and end of palindromic substring ie for a single element string.
    
    for i in range(1,len(string)): #here we only choose center index, O(n), only considering sizes 2 since size 1 is currentLongest
        odd = getLongestPalindromeFrom(string, i-1, i+1) , #O(n), returns slice indices of longest centered odd-lengh palindrome 
        even = getLongestPalindromeFrom(string,i-1,i)  #O(n), returns slice indices of longest centered even-lengh palindrome 
        longest = max(odd,even,key=lambda x: x[1]-x[0]) #choose, longest centered palindrome using returned indices for length calc
        currentLongest = max(longest,currentLongest, key= lambda x: x[1]-x[0]) #compare to longest palindrome, using indices for calc
    return string[currentLongest[0]:currentLongest[1]] #O(n) slice for the longest palindromic substring, using indices for slice

def getLongestPalindromeFrom(string,leftIdx, rightIdx): #palindromicity check based on center symmetry and left/right outward expansion
    while leftIdx >=0 and rightIdx < len(string): #rightIdx is len(string) for odd length when i is len(string) - 1
        if string[leftIdx] != string[rightIdx]: #if the current letters about center are not same, we reached the end of longest palindrome
            break
        leftIdx -= 1 #if current letters about center are same, decrement leftIdx to continue outward expansion
        rightIdx += 1 #if current letters about center are same, increment rightIdx to continue outward expansion
    return [leftIdx+1, rightIdx] #return indices of longest centered palindromic substring for slice and length calculation


string = "abaxyzzyxf"
stringII = "a"
stringIII = "122216"
print(longestPalindromicSubstringIV(stringIII))
"""The input is a string and the question asks to return a boolean that represents whether the string is a palindrome or not. A palindrome is
a string that is written the same forward as it is backward eg abcdcba. The property that allows a palindrome to be written the same forward
as it is backward is that the first letter and the last letter are the same, the second and the penultimate letter are the same etc. That the
optimal solution, O(n), O(1) space iteratively uses two pointers from the left and right and compares the first and last letters, then 
increments the left pointer to the second letter, decrements the right pointer to the penultimate letter and repeats the comparison. The 
pointers keep getting adjusted until they cross. If we ever find that the left pointer letter is not the same as the right pointer letter,
then we return False. If we successfully compare all letters from the front and back , then we return True at the end of the while loop.
Thus the key to this solution is the use of two pointers to iterate through a string from opposite ends.

The second optimal solution is based on the observation that a palindrome is symmetric about the center. the center of a palindrome is an 
empty string if the palindrome has an even-number length  eg 'abba'; the center of a palindrome is a single letter string if the palindrome 
has an odd-number length eg 'abcba. We use a while loop, that expands outward from the center of the possible palindrome. In an odd-length 
palindrome the leftIdx is i-1 and the rightIdx is i+1 for the first comparison and outward from there. That is the letter at i is center of a 
possible palindromic substring. In an even-length palindrome, the leftIdx is still i-1 but the rightIdx is i, meaning the center of the 
possible palindromic substrig is the empty string between i-1 and i. Thus in this approach we first handle the edge case of a single length
string, which is a palindrome. We are assured that the string is non-empty so need to include an empty string here. Then we calculate the 
centerIdx and a boolean that stores whether the string is even-length or odd-length. We then initialize leftIdx and based on the isEven 
boolean, we initialize rightIdx . Then with leftIdx and rightIdx, we expand outward from the center of the string and compare the 
corresponding letters. If the corresponding letters are not the same, we return False. Otherwise we decrement leftIdx and increment rightIdx.
If we are able to match all corresponding letters, the string is a palindrome and so we return True.
'"""

# O(N^2) time, O(1) space - Brute Force Approach
"""
This solution is actually O(N^2) time because string concatenation is 
a O(N) operation not constant time
"""
def isPalindrome(string):
    new_string=""
    for i in reversed(range(len(string))):
        new_string += string[i]
    return new_string == string


"""
O(N) time and O(N) space by avoiding concatenation. Instead we store the 
characters by appending to an empty list, which is constant time and 
then we create a new string at the end.
"""
#O(n) time, O(n) space
def isPalindromeIII(string): 
    newlist = []

    for i in reversed(range(len(string))):
        newlist.append(string[i])
    newlist= "".join(newlist)
    return newlist == string #O(n)
    

#Recursive solution O(n) time O(n) space

def isPalindromeIV(string, i=0):
    j = len(string) - 1 -i
    return True if i>=j else string[i] == string[j] and isPalindromeIV(string,i+1)


# O(N) time, O(1) space, Optimal solutin I
"""
This solution uses pointers and the fact that palindrome characters are
effectively mirror images across the axis / center of the palindrome
"""
def isPalindromeII(string):
    l,r = 0, len(string)-1

    while l < r and l < len(string) and r >=0:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True


#O(n) time | O(1) space, Optimal solution II, based on palindromic symmetry
def isPalindrome(string):
	if len(string) == 1:
		return True
	
	isEven = len(string) % 2 == 0
	
	centerIdx = len(string) // 2
	
	leftIdx = centerIdx - 1
	rightIdx = centerIdx if isEven else centerIdx + 1
	
	while leftIdx >= 0 and rightIdx < len(string):
		if string[leftIdx] != string[rightIdx]:
			return False
		leftIdx -= 1
		rightIdx += 1

	return True




string = "abcdcba"
print(isPalindromeIV(string))
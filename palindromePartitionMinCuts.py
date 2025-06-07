"""The question gives us a string and we are asked to return the minimum number of cuts or slices that would yield substrings 
that are palindromes. A single letter is a palindrome so we know that the upper bound of slices or cuts is length(string) - 1 
because if we have two letters, we need one cut to make one letter palindrominc substrings. Okay so the way the solution works 
is to first build a 2d array that stores if the substring starting at row and ending at column is a palindrome. This means the 
entire diagonal will be True because at the diagonal we are considering single letters, ie a substring that starts and ends at 
the same index. Building this 2d array is actually an O(n^3) operation because in addition to the two for loops needed to fill 
the array, the palindromicity test is an O(n) operation. The most optimal solution reduces this to O(n^2) by recognizing that 
determining if a substring is a palindrome basically means testing if the first and last letters are the same plus the result 
of if the inner string is a palindrome which we can access from our the array. With the 2d array build we then build the cuts 
array that stores the minimum cuts needed to create palindromic substrings ending at an index. This 1d array will thus be the 
length of the string and uses the 2d array to answer some questions. Specifically at each index we ask if the substring ending 
at that index is a palindrome. If it is, we need 0 cuts. This is essential base case. If the substring ending at that index is 
not a palindrome, then the minimum cuts is the minimum of two values. Either we add one to the minimum cuts at the index before 
or we find our if the substring has a palindromic suffix contained within. If it does, we add one instead to the minimum cuts of 
the prefix. The minimum of these two values; add one to the preceding minimum cuts or add one to the prefix minimum cuts if a 
palindromic suffix is found within ; is the answer. Then we return the last value in the cuts array"""
#O(n^3) time | O(n^2) space - this solution calls isPalindrome every time in the 2d-array
def palindromePartitioningMinCuts(string):
    palindromes = [[False for i in string]for j in string] #Initialize to False, flipping to True where True, n x n array
    for i in range(len(string)):
        for j in range(i,len(string)):#j starts at i not i+1 for substring starting at i and ending at j,i==j for single chars 
            #test slice for palindromicity since slicing doesnt worsen complexity here, otherwise we can pass string, i, j
            palindromes[i][j] = isPalindrome(string[i:j+1]) #slice to include i, j. so Pythons exclusivity means j+1 needed
    cuts = [float("inf") for i in string] #initialize minimum cust dp array using inf to easy minimum comparison
    for i in range(len(string)):
        if palindromes[0][i]: # if the substring ending at i is a palindrome, which will be located in the first row of 2d array
            cuts[i] = 0 # then we need 0 cuts to yield a palindromic substring, this substring, ie a string is its own substring 
        else: #if the substring ending at i isn't a palindrome
            cuts[i] = cuts[i-1] + 1 #then put a cut right after the preceding substring, ie add a 1 to the preceding value
            for j in range(1,i): #check for any palindromic suffix, thus check for palindromicity starting from second letter
                if palindromes[j][i] and cuts[j-1]+1 < cuts[i]: #if a palindromic suffix exists, and leads to a lower total cuts
                    cuts[i] = cuts[j-1] + 1 #then update the tentative value with the lower cuts value
    return cuts[-1]

def isPalindrome(string):#instead of taking a sliced substring, this function can be re-written to take the original string, i,j
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True


"""Optimal solution where we realize that in builiding the palindromes 2d-array we don't have to actually implement an O(n)
isPalindrome function to tell if a substring starting at row and ending at column is a palindrome or not. We can simply ask
if the characters at those indices are the same, if they are and the inner substring is a palindrome then the entire substring
is a palindrome. Because we build one letter at a time we will always have access to whether the inner substring is a palindrome"""
def palindromePartitioningMinCuts(string):
    palindromes = [[False for i in string]for j in string] #Initialize to False, flipping to True where True, n x n array

    for i in range(len(string)) : #set the diagonal to True, for single chars, len(string) number of times
        palindromes[i][i] = True #digonal represent single character substring, which is always a palindrome
    
    for length in range(2,len(string)+1): #to look at substrings of length 2 to the length of the string
        for i in range(0,len(string) - length + 1): #for all lengths, all valid starting indices, i , +1 is for range's end excl
            j = i + length - 1 #if len(string) = 6, length = 2,  0<=i<=5 and 1<=j<=6 for exclusive slicing for len 2 substrings
            if length ==2:#if length is 2, we just compare the two letters
                palindromes[i][j] = string[i] == string[j]
            else: #if the length > 2,we check if the first and last characters are same and if inner substring a palindrome
                palindromes[i][j] = string[i] == string[j] and palindromes[i+1][j-1]

    cuts = [float("inf") for i in string] #initialize minimum cust dp array using inf to easy minimum comparison
    for i in range(len(string)):
        if palindromes[0][i]: # if the substring ending at i is a palindrome, which will be located in the first row of 2d array
            cuts[i] = 0 # then we need 0 cuts to yield a palindromic substring, this substring, ie a string is its own substring 
        else: #if the substring ending at i isn't a palindrome
            cuts[i] = cuts[i-1] + 1 #then put a cut right after the preceding substring, ie add a 1 to the preceding value
            for j in range(1,i): #check for any palindromic suffix, thus check for palindromicity starting from second letter
                if palindromes[j][i] and cuts[j-1]+1 < cuts[i]: #if a palindromic suffix exists, and leads to a lower total cuts
                    cuts[i] = cuts[j-1] + 1 #then update the tentative value with the lower cuts value
    return cuts[-1]

string = "noonabbad"
print(palindromePartitioningMinCuts(string))
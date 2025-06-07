
""" 
This is a classic dynamic programming problem, where you optimize something under constraints. We 
are given two strings and we are to find the longest common subsequence between the two strings. A 
subsequence of a string is a new string generated from the original string with some characters 
deleted without changing the relative order of the remaining characters. For example "ace" is a 
subsequence of "abcde". A common subsequence of two strings is a subsequence that is common to both 
strings. The longest subsequence differs from longest common substring in that unlike substrings, 
subsequences are not required to occupy consecutive positions within the original sequences.

We will need a grid to solve this problem. The positions of the grid will characters in the strings.
If the characters represented by a cell is different in both strings, then the maximum subsequence
is either above or to the left.  The reason is that if the characters are different, then we consider 
the longest subsequence for each of the different characters; so above will be considering string 1
and to the left will be considering the current character of string two. So if we have hik vs fish,
the since k and h are different we either look at the value stored for hik vs fis ie above or fish
vs hi ie the left.

If the characters are the same, then we take the value in the top left corner ie row -1, col -1 
and add 1 to it. The reason is because that top left represents the subsequence without either the
current character. So if we have his vs fis, then we look at hi vs fi and add 1 to the value stored
there.
"""

#O(nm*min(n,m)) time | O(nm*min(n,m)) space, where n= len(str1), m=len(str2)
def longestCommonSubsequence(str1,str2):
    #colums = str1 + 1, rows = str2 + 1, use empty array for empty string and later join, yel = matrix, red is row, blue is entry ie empty array
    lcs = [[[] for x in range(len(str1)+ 1)]for y in range(len(str2)+ 1)] #empty array repeated str1 + 1 times in an row repeated str2 + 1 times
    for i in range(1, len(str2)+ 1): #choose a row, skipping the first row, for empty string
        for j in range(1, len(str1)+ 1): #loop through the columns in current row, skipping the first column, for the empty string
            if str2[i-1] == str1[j-1]:#if the current last letter in both strings are the same, matrix idx is one ahead of strings idx cos of ""
                lcs[i][j] = lcs[i-1][j-1] + [str2[i-1]] #lcs is diagonal lcs plus current last letter and matrix idx is one ahead of strings idx
            else: #if current last letter is not the same in both strings, the look at lcs of strings with last letter from one of them
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1], key = len ) #choose longest lcs above or to right, ie depending on len
    return lcs[-1][-1]

"""Optimal Solution where instead of storing the actual lcs we store an array of length four"""
#O(nm) time | O(nm) space
def longestCommonSubsequence(str1,str2):
        #[current letter if being used,len(current_lcs)], row pointer to prev letter in lcs, col pointer to previous letter in lcs]
    lcs = [[[None,0,None,None]for x in range(len(str1)+ 1)] for y in range(len(str2)+1)]
    for i in range(1,len(str2)+1):#choose row, starting from second row, since first row is for empty string and the lcs for that is always empty
        for j in range(1, len(str1)+1): #choose column, starting from second column since first column is for empty string whose lcs is empty
            if str2[i-1] == str1[j-1]:#current last letter is same so current last letter will be used, and add 1 to len(diagonal_lcs)
                lcs[i][j] = [str2[i-1],lcs[i-1][j-1][1]+1, i-1, j-1]#[current letter, len(diagonal_lcs) + 1, prev row pointer, prev col pointer]
            else:#current last letter not same so will not be used
                if lcs[i-1][j][1] >  lcs[i][j-1][1]: #if above lcs is bigger than left lcs, choose above lcs above
                    lcs[i][j] = [None,lcs[i-1][j][1],i-1,j] #[cur letter not used, len(above lcs), row pointer above_lcs, col pointer above_lcs]
                else:#else, choose left lcs
                    lcs[i][j] = [None, lcs[i][j-1][1], i,j-1] #[cur letter not used, len(left lcs), row pointer left_lcs, col pointer left_lcs]
    return buildSequence(lcs)


def buildSequence(lcs):
    sequence = []  #at most len(min(n,m))
    i = len(lcs) - 1 #final row in lcs
    j = len(lcs[0]) - 1 #final column in lcs
    while i != 0 and j != 0: #backtrack until the first row and first col, ie empty string vs empty string
        currentEntry = lcs[i][j]
        if currentEntry[0] is not None: #if we use current letter
            sequence.append(currentEntry[0]) #append the current being used
        i = currentEntry[2] #backtrack row
        j = currentEntry[3] #backtrack column
    return list(reversed(sequence)) #reverse sequence because its backwards


str1 = "ZXVVYZW"
str2 = "XKYKZPW"
print(longestCommonSubsequence(str1,str2))
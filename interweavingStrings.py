""" The question is to write a function that takes in three strings and returns a boolean representing whether the third string can be
formed by interweaving the first two strings. To interweave strings mean to merge them by alternating their letters without a specific
pattern. For instance, the strings 'abc' and '123' can be interwoven as 'a1b2c3', 'abc123', 'ab1c23' etc. Letters within a string
must maintain their relative ordering in the interwoven string. 

So it is clear that the interwoven string will have a length equal to the length of the first string plus the length of the second string.
If not, we can return False, which is the first step in the coded algorithm. Otherwise we use a recursive helper function to attempt
building the interwoven string with the two strings.

So in building the interwoven string, we know we have to choose a letter from stringOne or a letter from stringTwo. Say stringOne is 
'abc' and stringTwo is 'def', and the interwoven string is 'abdecf', we start building the interwoven string from index 0 to index 5.
We also have two pointers i, j which point to the current letters being considered as we build the interwoven string, and these start
from index 0 for both strings. So in this example  0<=i<=2, 0<=j<=2 and k, the current index of the interwoven string is 0<=k<=5. At 
any point in the algorithm, the current choices for k are the current letter at i if the current letter at i is equal to the current
letter at k, and the current letter at j if the current letter at j is equal to the current letter at k. What i mean is that in this
example, since the current letter at k (interwoven string) is 'a', our only option is the current letter at i. If the current letters
in stringOne and stringTwo are both equal to the current letter in the interwoven string, we choose the current letter in stringOne, 
keep going down the recursive calls and if we determine that the current course of action cannot yield the interwoven string, then we 
backtrack up the recursive tree, choose the current letter in stringTwo and go down the recursive tree trying to build the interwoven
string and the answer returned by that call will be what we return up the tree. What I mean is this, if we make a recursive call with
a particular pair of i,j and neither letter at i in stringOne nor letter at j in stringTwo is equal to the current letter at k in
the interwoven string, then we return False for that recursive call. If the letter at i in stringOne, is equal to the current letter
at k in the interwoven string, we make that our choice and make a recursive call with i+1 ie rec(one,two, three, i+1, j). If this
call returns True, we found our answer and we return True up the tree up to the original call. If however this call returns False,
we check have to check if the current letter at j in stringTwo is equal to the current letter at k in the interwoven string aka
stringThree. if it is we make choose it and make a recursive call where the letter being considered from stringTwo is the next letter
ie rec(one, two, three, i, j+1). And whatever that call returns whether True/False that becomes the boolean we return for the current
recursive call. You may have noticed that we dont pass k, that is because k = i + j. And we return True if k == len(stringThree). Why
is this so. First we realize that when making a choice we first check if the current index is in bounds for that particular string 
before checking if the letter at the current index in the string equals the letter at the current index of the interwoven string.
So because of this check, when we are at say the last letter in stringOne ie index 2 and we choose it the next call will be made with
index 3 so, no more choices will be made from stringOne. Then when we place all the letters from stringTwo and we get to the last letter
the next index call index will also be 3 and 3+3 = len(stringThree) and throughout the recursive calls this holds. So that's the algorithm. 

This solution will be improved by realizing that there will be repeated calls. For example if we ever determine that 
rec(one, two, three, 1,1) leads to False (ie i=1, j = 1) and we go that by going down the path where when k=0 we choose i=0, and increment 
i to 1 and then when k=1, we choose j=0 and increment j to 1, then we got to k=2 and realized that neither letter at i or j matches k, we 
can store this result so that if we choose another path say when k=0 we choose j=0, and  increment j to 1 and then when k=1, we choose i=0 
and increment i to 1, we know we have attribed here before so no need to continue this path so we return False down the tree eg 'aba' , 
'aca', 'aaqdef'. 
To store intemediary results we use a dynammic programming technique of building a matrix where the columns represent one string and the 
columns the other. And since we are not actually doing dynammic programming we can skip the buffer zone so that the row/colum indices of 
this matrix directly match the indices in the strings. In the code we initialize this data structure with None for columns equal to 
range(len(stringTwo)+1) (+1 for end-exclusivity) so that we have one column for each letter in stringTwo and the column array is repeated
range(len(stingOne)+1) times for n*m matrix, so that we have one row for each letter in stringTwo and at position i,j ie row i, column j 
in this matrix we store the result for rec(one,two, three, i,j) ie current index for stringOne is i, currentIndex for stringTwo is j ie 
the stringOne index is the row and the stringTwo index is the column.
This way we improve the time complexity from a whopping 2^(n+m) to nm. The reason for 2^(n+m) is that each choice has at most two options 
which will be repeated n+m times. Caching takes n*m space which is slightly worse than the time taken by then recursive stack n+m but the 
time improvements of caching are worth it.  

The point to this question is making sure to return True as soon as True is received just like the Lowest Common Manger question where we 
make sure to return the orgInfo class returned the first time the lowestCommonManager attribute is not None. In fact, we can change the code 
to only check if True is returned from stringTwo because if it returns False, we can still return the False from outside the two if checks. 
If caching, we store the returned boolean before checking if the returned boolean is True. Outside both if statements we store the False 
before returning it.  """


"""Naive solution, where we try all possible interweaves of string one and two as we iterate through all three strings at the same time"""
#O(2^(n+m)) time | O(n+m) space
def interweavingStrings(one,two,three):

    if len(three) != len(one) + len(two):
        return False

    return areInterwoven(one,two,three,0,0)


def areInterwoven(one,two,three,i,j):
    k = i+ j #index we are at in string three
    if k == len(three):#if we are at the end of string three without breaking recursive call
        return True #we have found strings that are interwoven
    
    if i < len(one) and one[i] == three[k]:# if in bounds of string 1 and we choose current letter if same as current letter in string 3
        if areInterwoven(one,two,three,i+1, j): #advance to next letter of string 1 and explore possible interweaves down this path
            return True #if we found the correct interweave down this path, lets return true

    if j < len(two) and two[j] == three[k]:#if in bounds of string 2 and we choose current letter if same as current letter in string 3
        return areInterwoven(one,two,three,i,j+1) #advance to next letter of string 2 and explore possible interweaves down this path
    
    return False #if we never hit True by getting to the end of string three or the if statement inside string one's call

"""Caching or Memoization solution where we pass around a cache of booleans that tells us if a particular interweave path has returned"""
#O(nm) time | O(nm) space
def interweavingStrings(one,two,three):

    if len(three) != len(one) + len(two):
        return False
    
    cache = [[None for _ in range(len(two)+1)] for _ in range(len(one)+1)] #len(one) + 1 rows, len(two) + 1 columns, in case we reach both ends
    return areInterwoven(one,two,three,0,0,cache)


def areInterwoven(one,two,three,i,j,cache):
    if cache[i][j] is not None: #first check if value stored in the cache is False or True
        return cache[i][j]


    k = i+ j #index we are at in string three
    if k == len(three):#if we are at the end of string three without breaking recursive call
        return True #we have found strings that are interwoven
    
    if i < len(one) and one[i] == three[k]:# if in bounds of string 1 and we choose current letter if same as current letter in string 3
        cache[i][j] = areInterwoven(one,two,three,i+1, j,cache) #advance to next letter of string 1 and explore possible interweaves down this path
        if cache[i][j]:
            return True #if we found the correct interweave down this path, lets return true

    if j < len(two) and two[j] == three[k]:#if in bounds of string 2 and we choose current letter if same as current letter in string 3
        cache[i][j]= areInterwoven(one,two,three,i,j+1,cache) #advance to next letter of string 2 and explore possible interweaves down this path
        return cache[i][j]
    
    cache[i][j] = False #otherwise update cache to be false 
    
    return False #if we never hit True by getting to the end of string three or the if statement inside string one's call




one = "algoexpert"
two = "your-dream-job"
three = "your-algodream-expertjob"
print(interweavingStrings(one,two, three))
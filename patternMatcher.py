"""The input is two non-empty strings. The first one is a pattern consisting of 'x's and / or 'y's; the other one is a normal string of 
alphanumeric charactrs. The question asks to write a function that checks whether the normal string matches the pattern. A main string
is said to match a pattern if replacing all the 'x's of the pattern with some non-empty substring of the main string and all the 'y's 
of the pattern with some other non-empty substring of the main string yields the same string as the main string. Thus the question is
asking to return an array of these substrings that match x,y ie [x-substring, y-substring] in that order. If the input string doesnt 
match the input pattern, the function should returnn an empty array. We are also assured there will be only one pair of substrings that
match the pattern. So if the main string is 'gogopowerrangergogopowerranger' and the pattern is 'xxyxxy' the answer is 
['go', 'powerranger']. So how do we solve this question?

Well the first thing is to ensure that our code works no matter the ordering of x and y in the pattern. In the question statement we are 
told to return the substrings matching x and y in that order. This means for the example above, if the pattern had been 'yyxyyx', ie we 
replaced every x with a y and vice versa, then y = 'go' , x='powerranger' but we would still have to return the substrings for x and y in 
that order [x,y] ie ['powerranger', 'go']. Thus to avoid this confusion, we generate a new pattern, one in which the letters in the pattern 
are ordered in the same way we are expected to  return the results and then we store a boolean to know if we switched our pattern or not so 
that we know what order to return it in. By this I mean, if our original pattern is yyxyyx and we switch it to 'xxyxxy', and store a 
boolean didSwitch=True, then when our algorithm finds  'x'='go', 'y'=powerranger , we simply switch the returned strings ie we return [y,x] 
from our function. This allows us to ensure that our algorithm works in the same way, and returns the expected answer. There are examples of 
using booleans to update answers appropriately before returning, like the shorten path question. To generate the new pattern here, we use a 
helper function, that first converts the pattern string to a list, to avoid repeated O(n) operations, then checks if the first element of 
this list is 'x'. If it is, we return the pattern list to be the new pattern. If it's not, we use map() to map every element of this list to 
a lambda function, that returns an 'x' if the element is a 'y' and vice versa and we convert this to a list before returning as new pattern. 
Thus it is useful to note that we convert our original pattern to a list of pattern characters, with or without substitution. 

Then with the new pattern list, we count how many instances of 'x' and 'y' there are in the pattern as well as the first y position. We store 
the counts in a hashtable with 'x' and 'y' keys {'x':countOfX, 'y': countOfY}. In the code we obtain the counts and the first Y position using 
the same helper function. To do this, we iniitialize firstYPos to be None then enumerate over the newPattern list, we say if the element at the 
current index is 'y' and firstYPos is None, then we update firstYPos. Since after this update firstYPos will not be None again, we ensure this 
update is only done once for the first y postion. And after the new pattern list, we know that the first x position is always at index 0. So we 
summarized the pattern by generating a new pattern list to ensure that the first x position is always at index 0, we obtained the first y 
position, a counts hashtable, and a boolean indicating if we made x,y switches for new pattern list. 

With the summary of the pattern complete, we realize that lenOfString = countOfX * lenOfX + countOfY * lenOfY, so that means
lenOfY = (lenOfString - countOfX * lenOfX ) / lenOfY. This means that we can generate different possiblities for lenOfX and use it to calculate
lenOfY and check if the resultant lenOfY is valid, and if valid, try generating the string with the x-substring and y-substring represented by
lenOfX and lenOfY. This which will involve division by the count of y, so here there are two main divergent cases, when the count of 'y' is 
non-zero and when it is, so that we don't run into division by 0. 

Lets start with the case when the count of 'y' in the pattern is 0. Here we say that the length of 'x' is the lengthOfString / countOfX ie we
don't need a for loop to generate different possiblities for the length of X, we can simply calculate it. If this division leads to a decimal, 
ie lenOfX % 1 != 0 we do nothing because this means that the pattern doesnt match the string and we return an empty list outside the main 
function. However if the division is not a decimal, the if the modulo by 1 of the result will equal 0, ie lenOfX % 1 == 0. So if the division 
did not result in a decimal, then we convert it to a whole number for array slicing ie int(lenOfX). We need to do this because division in
Python will yield a float ie 2.0 and we cant use a float to slice strings, we can only use integers hence the need to do integer conversion.
So with lenOfX as an integer, we slice the string up to that index, calling the result of this slice, xSlice. We then use a map() function to 
map every letter in newPattern list (which at this point contains on 'x's) to xSlice, join the result of the map with an empty string,(since 
a map object is iterable so can be passed directly into str.join(iterable)) and if this result is a match to the the originial string 
ie string = "".join(map(lambda char:xSlice,newPattern)), we return [xSlice,""] if didSwitch is False, else ["", xSlice]. Thus we say that with 
'y' as an empty string and 'x' as xSlice, the pattern matches the string.

If the count of 'y' is not 0, there might be a range of possibilities for the length of x, so we use a for loop to generate lenOfX from
1 to len(string), effectively saying that the length of x and y each varies 1 <= lenOfX/lenOfY <= lenOfString - 1. That is if both x and y
exist (remeber we will always have x's after the substituition step), the if one is length 1 the other is length, lenOfString - 1 and vice 
versa. Thus we use a for loop from range(1 ,lenOfString) to generate the possibilities for length of x, due to end-exclusivity of range().
So with lenOfX from the loop, we calculate lenOfY. ie len(string) = lenOfX * countOfX + lenOfY*countOfY, and if countOfY is non-zero, then
lenOfY = (lenOfString - countOfX * lenOfX ) / lenOfY . If the lenOfY is less than or equal to 0 or a decimal ie lenOfY <= 0 or lenOfY % 1 != 0, 
we just continue because this pair of lenOfX and lenOfY cannot be valid. In fact we only need to check for the possibility of a decimal but
we add the non-zero, non-negativity as some catch all option. However if lenOfY is greater than 0 ( we handled lenOfY equal to 0 with the 
countOfY == 0 branch),  and lenOfY is not a decimal, we convert it from a float to an integer for slicing. A note here that since the for 
loop goes from range(1, len(string)), the last lenOfX will be len(string) - 1 and since we use this for slicing and Python's slicing is 
end-exclusive, the longest possible xSlice will leave one character for the lenOfY. So with the integer lenOfY, we get the y start y slice 
from  yIdx = firstYPos * lenOfX. Then xSlice is string[:lenOfX] and ySlice is string[yIdx:yIdx+lenOfY]. We then generate a potential match, 
by using map() to iterate through newPattern and using a lambda function, if the character in newPattern is 'x', map to xSlice and 'y', map  
to ySlice. We join the elements of the potential match with "".join() and if the result is equal to the original string, we return [x,y] if 
there were no x,y substitutions. If we don't find a match by the end of the for loop, then we return the empty array outside like earlier when 
countOfY is 0.

This solution thus depends on the use of a hashtable to summarize a string using character counts and the realization that 
len(string) = lenOfX* countOfX + lenOfY*countOfY as well as the realization, after any necessary x,y substitutions, that 
yIdx = lenOfX* firstYPos, since firstYPos encodes within it how many instances of 'x' occur before the first 'y'. Also by using 'x' and 'y'
as the key for counts hashtable, we are able to increment counts simply as counts[char] += 1. Neat!!. Another comment, but 'continue' and
'break' are only used for loops (for/while) and not conditionals (if), so to do the same thing use 'pass'. Eg we can say 
if lenOfX % 1 != 0:pass the way we would use continue in a loop. """

"""
-convert our pattern to a list switching x's with y's if necessary to make x the first letter
-getcounts of x and y and the first position of y
-generate possible lengths of x and their correspo=nding y length and compare with string
-handle edge case where pattern only has x's
"""


#O(n^2 + m) time | O(n+m) space
def patternMatcher(pattern,string):
    if len(pattern) > len(string):  #edge case where the string is too short to match the given pattern ie
        return [] #return an empty string, the pattern is longer than the string 
    newPattern = getNewPattern(pattern)
    didSwitch = newPattern[0] != pattern[0]
    counts = {"x":0, "y":0}
    firstYPos = getCountsAndFirstYPos(newPattern, counts) #this function modifies counts, returns firstYPos
    if counts["y"] != 0:#main logic of program
        #test every possible combination starting with a length of x = 1 
        for lenOfX in range(1,len(string)):
            lenOfY = (len(string) - lenOfX * counts["x"]) / counts["y"]
            if lenOfY <= 0 or lenOfY % 1 != 0: #either a negative number or a decimal
                continue #skip to next possible length of x
            lenOfY = int(lenOfY) #in Python the division above yields a float, convert to an integer
            yIdx = firstYPos* lenOfX
            x = string[:lenOfX]
            y = string[yIdx:yIdx+lenOfY]
            potentialMatch = map(lambda char: x if char == "x" else y, newPattern)
            if string == "".join(potentialMatch):
                return [x,y] if not didSwitch else [y,x]  #didSwitch determines the order to return found substrings
    else:#case where there is no y in our pattern
        lenOfX = len(string) / counts["x"]
        if lenOfX %1 == 0:#not a decimal
            lenOfX = int(lenOfX) #we convert from float resulting from division to integer for slicing
            x = string[:lenOfX]
            potentialMatch = map(lambda char: x, newPattern)
            if string == "".join(potentialMatch): # .join() takes in an iterable and map() objects are iterable
                return [x,""] if not didSwitch else ["", x]
    return [] #if not match is found

def getNewPattern(pattern): #this function returns a list of the pattern, with or without x,y switching.
    patternLetters = list(pattern) #turn string into list
    if pattern[0] == "x": #if "x" is the first in the pattern
        return patternLetters #return list convert of pattern string
    else: #otherwise if y is the first in pattern, switch x and y and return a list, x is hardcoded so
        return list(map(lambda char:"x" if char == "y" else "y", patternLetters)) #map returns a map object
        
def getCountsAndFirstYPos(pattern,counts):
    firstYPos = None
    for i, char in enumerate(pattern):
        counts[char] +=1
        if char == "y" and firstYPos is None: #firstYPos is None only once ie before its updated. So if
            firstYPos = i
    return firstYPos

pattern = "xxyxxy"
string = "gogopowerrangergogopowerranger"
print(patternMatcher(pattern,string))
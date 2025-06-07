"""The question gives a string and asks to return the run-length encoding of the string. So run-length encoding encodes runs of repeated 
characters with a number and a letter. So AAAAA becomes 5A. However since the string can contain all kinds of characters including numbers 
the string AAAAAAAAAAA must be encoded as 9A2A instead of 11A which can be decoded to the original string or 1A ie the first 1 in 11 is 
decoded as a number not the count of A. Thus the the count of any letter must be at most 9 and no double digit counts are allowed in 
run-length encoding in order to avoid confusion during decoding. The solution starts by initializing an empty array to store all intermediary 
results and an initial count of 1, which represents the count of the first letter in the string. The we iterate through the string, starting 
from the second letter and using two pointers, previous and current to compare the current letter to the previous letter. Because we are using 
pointers, this loop requires the use of indices. If the two are the same, we increment the count by 1. Thus if the second letter is the same 
as the first letter, we have a count of 2 after the first run. However before incrementing the count, we check if the current count is at most 
9. That is, we check if the current count is 9 or if the previous letter is not the same as the current letter. In either case, we append as 
stingfied count, then we append the previous letter since the current count, before incrementing actually represents the count of the previous 
letter, then finally we set the count to 0 so that when it is incremented outside this check, if now represents the current letter count. At 
the end of this loop, we append the last count then the last letter, since inside the loop we only append the count and previous letter, the 
last letter and its count will be not be added. Then we use the string join method to concatenate the contents of the array with an empty string.

Thus the crux of this solution is the clever use of two pointers that follow one another and keeping an eye out for loop conditions and 
remaining operations."""


# O(n) time O(n) space where n is length of input string
def runLineEncoding(string):
    countChars = []
    currentRunLength = 1  # 1 because we expect a non-empty string

    for i in range(1,len(string)): #we start the currentChar at the second character
        currentChar = string[i] #select current character
        previousChar = string[i-1] #select previous character

        if currentChar != previousChar or currentRunLength == 9: #if current run ended
            countChars.append(str(currentRunLength)) #append current count
            countChars.append(previousChar) #append previous char, whose count just ended
            currentRunLength = 0 #re-initialize count at zero
        
        currentRunLength += 1 #increment count
    
    countChars.append(str(currentRunLength)) #append last count
    countChars.append(string[len(string)-1]) #append last character


    return "".join(countChars)



string = "AaAa"
print(runLineEncoding(string))
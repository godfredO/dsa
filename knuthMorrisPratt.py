"""This algorithm uses a pattern matching technique to do string matching in linear time. The first step
is to build a pattern match array for the potential substring. Using two pointers compare letters so see
where is the string up to that point do we have a prefix which is also a suffix, storing the last index 
of the prefix at the suffix end location in the array. This helps us to not go to the beginning of the
algorithm each time."""
#O(n+m) time | O(m) space
def knuthMorrisPrattAlgorithm(string,substring):
    pattern = buildPattern(substring) #first build the pattern of the substring
    return doesMatch(string,substring,pattern) #then use pattern to match substring to string 

def buildPattern(substring):
    pattern = [-1]*len(substring)
    j = 0  #first pointer for pattern making, initialize at first char of substring
    i = 1  #second pattern for pattern making, initialize at second char of substring

    while i < len(substring): #loop condition
        if substring[i] == substring[j]: #if the characters at the two indices are the same
            pattern[i] = j  #we have a prefix ending at j which is also a suffix ending at i
            i+= 1 #increment second pointer, if characters match
            j += 1 #increment first pointer, if characters match
        elif j > 0: #else if the characters don't match and j > 0
            j = pattern[j-1] + 1 #read pattern stored at j - 1, then go to the character after that
        else: #if j is equal to zero, we just increment i till loop condition breaks
            i += 1 #if characters dont match and first pointer is 0, then just increment second pointer
    return pattern

def doesMatch(string,substring,pattern):
    i = 0   #string pointer
    j = 0   #substring pointer
    
    while i + len(substring) - j <= len(string):#when we don't enough chars in string to match substring
        if string[i] == substring[j]: #if the chars at both string pointer and substring pointers match
            if j == len(substring) - 1: #if we just matched the last character of the substring
                return True #the we successfully matched
            i += 1 #if not at the end of substring, increment both pointers, string pointer
            j += 1 #increment substring pointer
        elif j > 0: #else if chars dont match and j is not the beginning of substring
            j = pattern[j-1] + 1 #go back in substring to one letter after the preceding pattern
        else: #if chars don't match and we are at the start of the substring,
            i += 1 #then increment the string pointer
    return False #if we break, j didnt make it to the end of the substring










string = "huntykojomama"
substring = "kojo"
print(knuthMorrisPrattAlgorithm(string,substring))
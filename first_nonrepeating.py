"""This input is a string and the question asks to return the first non-repeating character in the string. That is if the string is 'abcdcaf',
the first non-repeating character is b, and this is because a and c both repeat and of the non-repeating characters, b,d,f, b occurs the 
earliest in the string. This reminds of the first duplicate value question. So the brute force operation will be to use two loops to find 
duplicates and use a boolean to store whether a duplicate is found for the current letter in the outer. Thus in the outer loop we choose a 
letter, and initialize our boolean to False. Then we loop a second time, through the entire string again , and if we find a letter that is the 
same as the current letter in the outer loop but the index of the letter is different from the outer loop, then it means we found a duplicate 
of the current outer loop letter and then we change the boolean to True for duplicate. If at the the end of the inner loop, the boolean is 
still false, then we return the current index of the outer loop. This approach uses no space and is O(n^2) time. The optimal approach is to 
loop through the string and store counts of each letter in a hashtable. Then in a second loop from left to right, if we find a letter whose 
count is 1, that is the first non-repeating letter. In either solution, we return a -1 if all characters in the string repeat. Thus the optimal 
solution to this problem involves the clever use of a hashtable.

In the brute force solution it is essential that the inner loop also start from the beginning because if a duplicate exists, it position 
does not matter eg 'aba', at index 0 in the outer loop we should find index 2 in the inner loop and at index 2 in the outer loop we should
find index 0 in the inner loop. To ensure that we don't say that the same element is its own duplicate that why we check that the outer
loop index is not the same as the inner loop index .

Also in the optimal solution where we replace the previous inner loop with a hashtable, we are able to find the first non-repeating 
character because we loop and check in sorted order from the left to the right """

# O(n^2) time | O(1) space
def firstNonRepeatingCharacter(string):
    for idx in range(len(string)):
        foundDuplicate = False

        for idx2 in range(len(string)): #in case the duplicate of idx2 occurs earlier in the string eg"aba" at idx2=
            if string[idx] == string[idx2] and idx != idx2: #in case the duplicate of idx2 occurs earlier in the string eg"aba" at idx2=
                foundDuplicate = True
    
        if not foundDuplicate:
            return idx
    return -1


# O(n) time | O(1) space because max number of keys is 26 for lowercase English letters
def firstNonRepeatingCharacterII(string):
    characterFrequencies = {}

    for character in string: #create map
        characterFrequencies[character] = characterFrequencies.get(character,0) + 1
    
    for idx in range(len(string)):
        character = string[idx]
        if characterFrequencies[character] == 1:
            return idx

    return -1



string = "abcdcaf"

print(firstNonRepeatingCharacterII(string))
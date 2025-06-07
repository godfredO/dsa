"""The input is a string of words separated by one or more whitespaces and the question asks to write a function that returns a string that
has these words in reverse order. Note that the input string can be empty, and all whitespaces have to also be reversed so to speak. We are 
not allowed to use split() or reverse() functions but we can use .join() string methods.

The intuitive method starts by splitting the string into a list of characters using a simple list comprehension loop instead of a string
split() method. This way whitespace will be a sting with 1 empty space within it. We then use a helper function to swap-reverse the characters 
in the string. This function takes the array of characters, a start index pointer and end index pointer and swaps the charachters at those 
positions before incrementing the start index pointer and decrementing the end index pointer as long as these pointers don't cross. This 
function is a standard two pointer traversal with a swap() function inside and will reverse the characters array by swapping pairs of opposite 
elements at a time. This helper function is really the crux of the intuitive solution. With the characters reversed, we then iterate with a 
while loop through the reversed characters array, to search for the start and end of words and re-reverse the letters of each word in other to 
reform the word because at this point the contents of each word is reversed too. So we initialize a startIdx at 0 and inside the outer while 
loop we initialize the endIdx at the same as the startIdx. The outer loop runs as long as startIdx < len(characters), where characters is the 
reversed array ie as long as startIdx is within bounds. The inner loop runs as long endIdx is within bounds and the element at endIdx is not 
a whitespace string which would be a string with 1 space inside. So with the startIdx poiting to the start of a word and endIdx pointing to the 
space after a word, we use the helper function to swap-reverse the letters of the word from startIdx to endIdx - 1. We then advance startIdx to 
endIdx + 1. If we have a series of whitespace strings, this line will advance the startIdx through the reversed characters array and the call to 
the helper function will do nothing because we will be calling the helper function with startIdx == endIdx instead of startIdx < endIdx. Whenever 
startIdx = endIdx+1 finds the first letter of a new word, the inner while loop, will find the end of that word by looping until it reaches the 
whitespace after the last letter, reverse(array, startIdx, endIdx-1) will swap-reverse the letters of the word in-place and so on and so forth. 
At the end of outer while loop when startIdx == len(characters), we would have an array representing the words in reverse while all whitespaces 
are reversed and we simply join all of these using the ''.join(characters) string method as the answer. """

# Solution 1. Create a list to store words and spaces
# O(N) time | O(N) space
def reverseWordsInString(string):
    words = []
    startOfWord = 0

    for idx in range(len(string)):
        character = string[idx]

        if character == " ":
            words.append(string[startOfWord:idx])
            startOfWord = idx
        elif string[startOfWord] == " ":
            words.append(" ")
            startOfWord = idx
    # append last word
    words.append(string[startOfWord:])
    
    reverseList(words)

    return "".join(words)

def reverseList(list):
    start, end = 0, len(list) - 1
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1


# O(N) time | O(N) space
def reverseWordsInStringII(string):
    #create a list of all characters and spaces in string
    characters = [char for char in string] #use a simple for loop to split the string, each white space is an empty string
    #reverse the order of spaces
    reverseListRange(characters, 0, len(characters) - 1) #swap function to reverse each characters place in array, with indices

    startOfWord = 0
    while startOfWord < len(characters):
        endOfWord = startOfWord
        while endOfWord < len(characters) and characters[endOfWord] != " ": #whitespace represented by string with 1 space inside
            endOfWord += 1

        # unreverse characters between startOfWord and endOfWord  
        reverseListRange(characters, startOfWord, endOfWord - 1) #when loop above breaks, actual endOfWord = endOfWord - 1
        startOfWord = endOfWord + 1 #start after this word
    
    return "".join(characters)

def reverseListRange(list,start,end): #a function reverse array elements by swapping first and last, second and penultimate etc
    while start < end:
        list[start] , list[end] = list[end], list[start] #swap current pointer elements
        start += 1 #increment start pointer
        end -= 1 #decrement end pointer

    

string = "AlgoExpert is the best!"
stringII = ""
print(reverseWordsInString(string))
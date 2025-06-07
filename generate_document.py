"""The input is two strings named characters and document and the question asks to return a boolean representing whether you can generate the 
document using the characters. You are only able to generate the document if the frequency of unique characters in the characters string is 
greater than or equal to the frequency of characters in the document. We will be needing to generate and check character counts and so the
optimal solution screams hashtable. A hashtable will allow us constant-time access to character counts. So we iterate through the characters
string, and store each letter and their counts in the hashtable. We then iterate through the documents and decrement the count of each
letter in the hashtable. Thus if we ever find a letter in the documents that isnt in the hashtable or we ever the counts of that letter is
0 (as a result of the decrements), then we don't have all the necessary unique characters or enough counts of the unique characters to 
generate the document with the characters string. So the crux of this solution is to cleverly use a hashtable. Know that we actually count 
the empty spaces in the characters array and those two must be equal to or more than in the document string. 

The key to this solution create the map by initializing to 0 and incrmenting and then check by decrementing until 0 in which case we know we
don't have enough characters."""

# O(m*(n+m)) time | O(1) space where c is unique characters in document string
# n is the characters in characters string m is characters in document string
def generateDocument(characters,document):
    
    for character in document:
        documentFrequency = countCharacterFrequency(character,document)
        charactersFrequency = countCharacterFrequency(character,characters)

        if documentFrequency > charactersFrequency:
            return False
    return True

def countCharacterFrequency(character,target):
    frequency = 0
    for char in target:
        if char == character:
            frequency += 1
    return frequency

# O(c*(n+m)) time | O(c) space where c is unique characters in characters string
# n is the characters in characters string m is characters in document string
def generateDocumentII(characters,document):
    alreadyCounted = set()

    for character in document:
        if character in alreadyCounted:
            continue
        
        documentFrequency = countCharacterFrequency(character,document)
        charactersFrequency = countCharacterFrequency(character,characters)

        if documentFrequency > charactersFrequency:
            return False

        alreadyCounted.add(character)
    return True

#O(n+m) time | O(c) space where c is unique characters in characters string
# n is the characters in characters string m is characters in document string
def generateDocumentIII(characters,document):
    characterCounts = {}

    for character in characters:
        if character not in characterCounts:
            characterCounts[character] = 0

        characterCounts[character] += 1

    for character in document:
        if character not in characterCounts or characterCounts[character] == 0:
            return False
        characterCounts[character] -= 1
    
    return True

characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"
print(generateDocumentIII(characters,document))
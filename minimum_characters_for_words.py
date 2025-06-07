"""The input is an array of words and the question asks to return the smallest array of characters, needed to form any of the words in the 
input array. So if the array of words is ['aba', 'bag'], the smallest array of characters would be ['a', 'a', 'b', 'g'] because we have two 
a's and a 'b' to form 'aba' and 1 'a', 1 'b', 1'g' to form bag. So first off it is clear that the output has to have all the unique characters 
in the array of words and the frequency of each unique characters must equal the maximum frequency of that character for any one word in the 
input array. This question is obviously screaming for a hashtable and we do indeed use a hashtable.

The difference between the brute force approach here vs the optimal approach is similar to the difference for the apartment hunting question.
In that to move from the brute force approach we decouple a nested loop from n^2 to 2n, and that improves the time complexity by one order.
In the brute force approach iterates through the array of words and for each word, we iterate through the letters and for each letter we
iterate through the word again for the frequency of the letter in the word. We then add the letter:frequency to the hashtable if the letter
isnt in there. If it is, we compare the existing frequency to the frequency of the same letter in the current word and update it to the 
maximum frequency. At the end of the nested arrays, we have another loop go through the hashtable, and appends each letter key, maxFrequency
number of times to the output array which is then returned after.

Instead of iterating through a word repeatedly to get the count for each letter, we could iterate through it once to get the frequencies of
all letters and create a hashtable for the letter frequency of each word. Then we update the maxFrequency hashtable with the frequencies of
the current word, adding letters that are not maxFrequency or updating the frequecy of a letter to the max frequency by comparing the 
frequency of each exisiting letter in maxFrequency to its frequency in the current word's frequency table. This is the crucial 
re-interpretation that decouples the l^2 loop to 2l operation. After updating maxFrequency hashtable for every word in the input array, 
we then use maxFrequecy to produce the output array by appending each letter key in maxFrequency, a maxFrequency[letter] number of times.
As we can see here and in other questions that use decouple and iterate, this technique uses additonal space, but since we are using space
anyway, it doesnt worsen complexity. The space complexity is explained by having words of unique letters only example 'abc', 'efg', here
the maxFrequency hashtable will contain a key for each of a,b,c,e,f,g ie 6 keys equal to n*l where n=2 and l=3. And the wordFrequency 
hashtable will be at most l keys anyway.
"""


# O(n*l^2) time | O(n*l) space, n= number of words in input, l = length of longest word
# Solution I same logic as solution II but we iterate through each word twice to get the counts, l^2 of each char and update to max frequency
def minimumCharactersForWords(words):
    maxFrequency = {}
    outputlist = []

    #update hashtable with unique characters and their maximum frequencies
    for word in words: #O(n)
        for char in word: #O(l)
            charFrequency = countCharFrequency(char,word) #count the frequency of current letter in current word, O(l)

            if char not in maxFrequency:
                maxFrequency[char] = charFrequency #initial addition to hashtable, O(1)

            maxFrequency[char] = max(maxFrequency[char],charFrequency) #update the frequency to maximum in any one word, O(1)
    
    #create output list of unique characters repeated their maximum frequency number of times
    for item in maxFrequency: #iterate through hashtable, O(l)
        repeatitions = maxFrequency[item]
        for _ in range(repeatitions):  #O(l)
            outputlist.append(item) #append to output max frequency num of times

    
    return outputlist

# helper function to count the occurence of a character in a word
def countCharFrequency(target,word):  #O(l)
    frequency = 0 #initialize frequency
    for character in word:
        if character == target:
            frequency += 1
    return frequency


# O(n*l) time | O(n*l) space, n= number of words in input, l = length of longest word
# Solution I same as solution II just different style
def minimumCharactersForWordsII(words):
    maximumCharacterFrequencies = {}

    #iterate through input list
    for word in words: #O(n)
        #create a dictionary of characters in a word and their counts 
        characterFrequencies = countCharacterFrequencies(word) #O(l)
        updateMaximumFrequencies(characterFrequencies, maximumCharacterFrequencies) #O(l)

    return makeArrayFromCharacterFrequencies(maximumCharacterFrequencies)


def countCharacterFrequencies(word):
    characterFrequencies = {}

    for character in word:
        if character not in characterFrequencies:
            characterFrequencies[character] = 0

        characterFrequencies[character] += 1
    
    return characterFrequencies


def updateMaximumFrequencies(frequencies, maximumFrequencies):
    for character in frequencies:
        frequency = frequencies[character]
        
        if character in maximumFrequencies:
            maximumFrequencies[character] = max(frequency,maximumFrequencies[character])
        else:
            maximumFrequencies[character] = frequency


def makeArrayFromCharacterFrequencies(maximumCharacterFrequencies):
    characters = []

    for character in maximumCharacterFrequencies:
        frequency = maximumCharacterFrequencies[character]

        for _ in range(frequency):
            characters.append(character)

    return characters



wordList = ["this",'that','did','deed','them!','a']
print(minimumCharactersForWordsII(wordList))

"""The input is an array of strings and the question asks to write a function that groups anagrams together. Anagrams are strings made up of
exactly the same letters, where order doesn't matter. Eg cinema and iceman are anagrams. Thus if we have a pair of anagrams and we sort both
of them alphabetically, we would have the same strings. Note that whiles arrays have the .sort() method for in-place sorting, strings don't 
have any such method in Python thus we have to use sorted() function which for both 'cinema' and 'iceman' will yield 
['a', 'c', 'e', 'i', 'm', 'n'] which can be joined using the string method "".join(array) method to yield 'aceimn'. So now that we can use
sorting to find anagrams, how do we group them together. We use a hashtable. Specifically, we iterate through the array, generate a sorted 
string for each word and add to a hashtable with the sorted string as the key and the value is an array of words that yeild the same 
sorted string. At the end we return a list of all the hashtable's values which will all be groups of anagrams. If n is the length of the
longest word, and there are w words then the complexity of this optimal approach is O(w*nlog(n)) time and O(wn) space, where w*n is the 
space taken up the hashtable and we sort (nlogn)  w words.

Thus the solution to this question uses sorting and hashtable techniques for optimal solution.
 """


# O(w*n*log(n) +  n*w*log(w)) time | O(wn) space
def groupAnagrams(words):
    if len(words) == 0:
        return []

    sortedWords = ["".join(sorted(w)) for w in words] #rearrange each word's letters alphabetically
    indices = [i for i in range(len(words))] # generate a list of indices for words list
    indices.sort(key=lambda x: sortedWords[x])  # sort indices by using the rearranged words in alphabetical order

    result = []
    currentAnagramGroup = []
    currentAnagram = sortedWords[indices[0]]

    for index in indices:

        word = words[index]
        sortedWord = sortedWords[index]

        if sortedWord == currentAnagram:
            currentAnagramGroup.append(word)
            continue

        result.append(currentAnagramGroup)
        currentAnagramGroup = [word]
        currentAnagram = sortedWord

    result.append(currentAnagramGroup)

    return result

# O(w*n*log(n))  | O(wn) space
def groupAnagramsII(words):
    anagrams = {}

    for word in words:
        sortedWord = "".join(sorted(word))

        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]

    return list(anagrams.values())



words = ['yo','act','flop','tac','foo','cat','oy','olfp']
print(groupAnagramsII(words))




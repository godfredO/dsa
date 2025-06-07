"""
Tags: Hashmap, Modulo, Medium


The input is a string and a key which is an integer and the question asks to return a new string where each letter in the original string
has been shifted by 'k' positions in the alphabet where k is the key in the input. The question also mentions that the letters should 'wrap'
around the alphabet. So xyz and a key of 2 becomes zab. So first thing, instead of writting a custom mapping of letters, we use the ord()
and chr() functions in Python. The ord() function takes in a letter and returns the Unicode code for that letter, the codes range from 97 for
'a' to '122'. The chr() takes in a valid Unicode code (97-122) and returns the letter it represents. So they main crux of this solution is to
ensure that the key can wrap around the alphabet by modulo dividing by 26. So we first start by getting a new key by modulo dividing the input
key by 26, the number of alphabets in the English language. The we loop through the string, and at each letter we add the newKey to the Unicode
representation of the letter. If the sum is valid ie less than 122 (we are assured that key is non-negative so we dont have to worry about a
value of less than 97), we can use this to get the new shifted letter which we append to an array. If the sum is above 122 we modulo divide the
sum by 122 and add this to 96 to yield the code for chr, and we append the shifted letter to the array. At the end, we use the string join
method with an empty string and with the array as input.

The second solution just converts a string of all alphabet letters to a list and indexes into this list for the shifted letters after modulo
division. That is we get the new key by modulo dividing by 26 to ensure the wrap around. Then we iterate through the string and for each
string, we get the index of the current string in the list of alphabet letters, add the new key for the new letter code. The before indexing
into the alphabet list again for the shifted letter we modulo the new letter code by 26 in case the sum was out of bounds. Again we append
the shifted letter to an empty array and at the end join the contents of this array with the string join method using a empty string as
separator.

This question demonstrates the use of the modulo operator for acheiving wrap around indexing using the length of an entity. It also
demonstrates the use of an array to hold intermediate results when dealing with strings, to avoid O(n) concatenations.  """


"""
Initialize an empty array to include the shifted alphabets
using Unicode values. To return a unicode value of an alphabet
in Python use ord() and chr() functions. This is O(N) time and O(N) space
"""


def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26

    for letter in string:

        newLetterCode = ord(letter) + newKey

        if newLetterCode <= 122:
            shiftedLetter = chr(newLetterCode)
            newLetters.append(shiftedLetter)
        else:
            shiftedLetter = chr(96 + newLetterCode % 122)
            newLetters.append(shiftedLetter)
    return "".join(newLetters)


"""
This solution uses an array of alpabet characters instead of Pythons
Unicode functions ord() and chr()
"""


def caesarCipherEncryptorII(string, key):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")  # constant memory / time
    newLetters = []  # to hold shifted letters
    newKey = key % 26  # to ensure the wrap around when shifted by key when key > 26

    for letter in string:
        newLetterCode = alphabet.index(letter) + newKey

        if newLetterCode <= 25:  # no wrap around needed for alphabet index 0(a)-25(z)
            shiftedLetter = alphabet[newLetterCode]
            newLetters.append(shiftedLetter)
        else:  # wrap around needed
            shiftedLetter = alphabet[newLetterCode % 26]  # modulo operation for wrap around overlap
            newLetters.append(shiftedLetter)
    return "".join(newLetters)


# Cleanest approach using alpahbet mapping
def caesarCipherEncryptor(string, key):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    newLetters = []
    newKey = key % 26

    for letter in string:
        newLetters.append(getNewLetter(letter, newKey, alphabet))
    return "".join(newLetters)


def getNewLetter(letter, newKey, alphabet):
    currentIdx = alphabet.index(letter)
    newIdx = (currentIdx + newKey) % 26   # even if sum < 25, modulo provides correct index
    return alphabet[newIdx]


string = "xyz"
key = 2
print(caesarCipherEncryptorII(string, key))

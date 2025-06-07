"""Given a stringified phone number of any non-zero length, the question asks to write a function that returns all mnemonics for this
phone number based on the phone number, in any order. The solution depends on creating a phone number map of digits (0-9) with their
associated alphabets, then starting from index 0, we go to this map, select the map letters, make a choice, then advance the starting
index, choose letter for that number's map letters, and so on. When the starting index equals the length of the array, we have a valid
mnemonic. Since we know that each mnemonic has the same length as the input stringified phonenumber, we pass around an array of same
size (initialized with 0's) and whenever we make a letter choice we update the element at the corresponding index in this array. Then
when the current index equals the length of the array, we join the elements of this array to create a stringified mnemonic. Since the
digits with the most alphabet letters mapped to them have 4 letters mapped, the are at most 4 options for each element so there are
an upperbound of 4^n mnemonics, and since we use an O(n) loop, the time complexity is O(4^n*n) and same space since each mnemonic 
has n letters"""

#4^n*n time 
def phoneNumberMnemonics(phoneNumber):
    currentMnemonic = ['0']*len(phoneNumber)
    mnemonicsFound = []

    #recursive function to pick characters for digits
    phoneNumberMnemonicsHelper(0,phoneNumber,currentMnemonic,mnemonicsFound)
    return mnemonicsFound

def phoneNumberMnemonicsHelper(idx,phoneNumber,currentMnemonic,mnemonicsFound):
    if idx == len(phoneNumber):
        mnemonic = "".join(currentMnemonic) #O(n)
        mnemonicsFound.append(mnemonic)
    else:
        digit = phoneNumber[idx]
        letters = DIGIT_LETTERS[digit]
        for letter in letters:
            currentMnemonic[idx] = letter
            phoneNumberMnemonicsHelper(idx+1,phoneNumber,currentMnemonic,mnemonicsFound)



DIGIT_LETTERS = {
    "0":["0"],
    "1":["1"],
    "2":["a","b","c"],
    "3":["d","e","f"],
    "4":["g","h","i"],
    "5":["j","k","l"],
    "6":["m","n","o"],
    "7":["p","q","r","s"],
    "8":["t","u","v"],
    "9":["w","x","y","z"],

}


phonenumber="1905"
print(phoneNumberMnemonics(phonenumber))
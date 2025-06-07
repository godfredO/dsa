"""Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order. A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 
does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

This question is the same as phonenumber_mnemonics.py, and uses backtracking . If s= '23' and '2 : abc, '3': def , '4': ghi. We
need a map of the characters. So index 0 '2' could map to a, b, c. And index 1 could map to d, e, f. So, we need to write a 
backtracking algorithm choose one letter fora current index and then go down the recursive tree, incrementing the index until we 
go outof bounds, then we backtrack up the recursive tree and make another choice for that index. Typically you should store the
intermediary results in an array but we could also build the string as we go. Also we should handle the edge case of an empty
digits string, and you could explicitly state that if the digit is of length 0, retun [] or you could neatly clad the backtracking
call in an if statement like below. The max digit-letter map is 4 letters (ie number 7,9) so time complexity is 4^n*n.
"""



def letterCombinations(digits) : 
        result = []
        if len(digits):
            comb = ""
            dfs(0, digits, comb, result, DIGIT_LETTERS)
        return result

def dfs(idx, digits, comb, result, map):
    if idx == len(digits):
        result.append(comb)
        return

    digit = digits[idx]
    letters = map[digit]
    for letter in letters:
        updated = comb + letter
        dfs(idx+1,digits, updated, result, map)

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
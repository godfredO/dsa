"""
Tags: Stack; Medium

The input is a string of different bracket types and optional characters and asks to return a boolean representing whether the string is
balanced with regards to brackets. A string of parentheses is balanced if for every opening parenthesies or bracket there is a matching
closing parentheses after it to balance it. A closing parentheses can only balance opening parentheses that come before it and both brackets
must also be matching types. Also, brackets cant overlap each other as in [(]) There are three types of brackest or parenthesis, the square
[], curved () and curly {}. So we use a stack here, only because we have different type and we need some space to store the parentheses. We
also need a way of verifying if a bracket is opening or closing so we store a string with all the opening and a string with all the closing
brackets. We ideally should use a set, since we would get constant time access but since we know that this string is always going to be three,
since there are only three bracket types not a variable bracket type, using a string instead of a set for verification will always be O(3) so
constant-time. Also in practice using a set() will be tricky to because of the function brackets, so a string is the easiest option, fyi. We
also have to initialize a hashtable that matches closingBracket:openingBracket so that we can verify if we found a matching pair. Anyway, we
use a stack to solve contiguity/ adjacency / position based problems ie problems where the meaning assigned to an element is based not on
sorted order per se but rather its relationship to the elements that are adjacent or close or in its proximity. When we don't necessarily
need to store stuff we can use the decouple and iterate method depending on the question eg min rewards question or optimal apartment hunting
question. Anyway, as we iterate through if the current character is an opening bracket (verified by checking if its in the opening bracket set
or string), we append it to the stack. If the current character is a closing bracket, we first check if the stack is empty. If it is, we
return False because a closing parentheses cannot balance an opening parentheses that comes after it only when ones that come before it.
If the stack is not empty, we check if the opening bracket at the top of the stack (peek) is a match to the current closing bracket. If it
is, we found a match for that opening bracket so we pop if off the stack. If the opening bracket on top of the stack is not a match to the
current closing bracket, then it means that different bracket types are interweaving or crossing and that is also inbalanced, so we return
False. At the end of our loop, we verify that we matched every opening bracket appropriately by returning len(stack) == 0. Finally even
though we are assured that the input strings if containing brackets will only contain the three types of brackets, we are not assured that
inside those bracket, there wont be letters eg (a) is balanced. As such the condtions are if current character is an opening bracket do xy,
if current character is a closing braket do efg instead of if current character is an opening bracket do xyz else do efg. The first stating
of the conditions ensures that the code skips over non-brackets, the second stating will treat letters, number etc as though they were
closing brackets which will lead to errors.

This solution uses a stack, a hashtable and a hashset."""

# O(N) time | O(N) space where N is length of string


def balancedBrackets(string):
    openingBrackets = "([{"  # for checking for opening brackets
    closingBrackets = ")]}"  # for checking for closed brackets
    # maps every closing bracket to matching opening brackets
    matchingBrackets = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in string:
        if char in openingBrackets:  # only add opening brackets to stack
            stack.append(char)
        elif char in closingBrackets:  # this runs only for closing brackets and skips over numbers, letters, optional characters
            if len(stack) == 0:  # if a closing brackets comes before an opening bracket
                return False
            # if the closing brackets balances the opening on top of stack ie matching brackets
            if stack[-1] == matchingBrackets[char]:
                stack.pop()  # pop because balanced
            else:  # if closing bracket is overlapping ie doesnt match previous opening bracket
                return False  # stack[-1] != matchngBrackets[char]
    return len(stack) == 0  # check that every opening bracket was matched

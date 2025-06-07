"""The input is a string made up of parentheses ( and ), and the question asks to write a function that returns an integer representing 
the length of the longest balanced substring with regards to parentheses. Eg if the string is '(()))(', then the longest substring that 
is balanced has a length of 4, from index 0 to index 3. There is a stack question to determine if a string of parentheses is balanced and 
the answer to that question is used here in the brute force solution, ijs. Anyway the first thing to realize is that if the entire string
is parentheses-balanced, then the answer is the length of the input string. The next observation is that the length of the shortest
possible parenthesis-balanced substring would be 2, representing '()' ie, opening parentheses and closing parenthesis next to each other. 
In fact for any substring to be parentheses-balanced, the length has to be even, the first parentheses has to be an open parentheses,
the last parentheses has to be a closing parenthesis and the inner substring has to be balanced too.

Now the brute force solution uses a double nested for loop to generate all possible leftIdx and rightIdx and for each pair of indices, 
calls the stack-based solution to return a boolean representing if the substring contained between those indices is balanced. Because the 
stack-based balanded parentheses solution takes a string as input, we need to slice the substring. And since we know that a balanced 
substring has to be even-length (eg '()') and also since Python's slicing is end-exclusive, rightIdx = leftIdx + 2 in order 
for string[leftIdx:rightIdx] to yield '()' the smallest possible balanced substring. As a result of this whiles leftIdx will be at the 
start of the substring, rightIdx is actually going to be the right slice index instead of the right ending index. All of this to stay that 
the inner for loop (rightIdx) is going to start two indices after the outer for loop (leftIdx) and is going to take a step of two indices
at a time, to only consider even-length substrings. In addition in order to be able to have an even-length substring that ends at the end
of the string, the inner loop has to end at range(len(string) + 1) and the outer loop has to go to range(len(string) -1) so that we when
leftIdx = len(string) - 2 and rightIdx = len(string) , when we use these for slicing, string[leftIdx:rightIdx], we get an even-length
substring starting at len(string) - 2 and ending at len(string) - 1. With our substring generated, we call the stack-based solution to
with the sliced substring as input and if it returns True, we calculate the length of the balanced substring using rightIdx - leftIdx
and compare with the existing stored length, updating to the maximum length. The stack-based solution is linear time and since it is
nested inside the double for loop for slice indices, this brute force solution of generating every possible even-length substring runs
in O(n^3) time and O(n) space, where O(n) space is the space used up by the stack.

The optimal solution is a decouple and iterate technique. This technique is used in questions where an element's meaning is based on
the other elements that are closest / adjancent or in its proximity. This technique is used in the min rewards question where the 
rewards a student gets is based on whether its greater or lower than the adjacent students and any change done affects the student in
its proximity. It also used in the optimal solution of the apartment hunting question, where the req distance for a block depends on
the closest block that has the required building and when one is found it becomes the closestReqIdx for all the other buildings. In
the decouple and iterate technique, we check one condition while iterating from left to right and we check another condition  while
iterating from right to left, allowing us to reduce a n^2 time to 2n time. Also the adjancency / closeness/ proximity requirment is
does not refer to sorted order per se. In the buildings question, we first calculate the req distance with the closestReqIdx to the 
left while iterating from left to right, the we iterate from right to left and calculate req distance with the closestReqIdx to the
right and choose the minimum of these a the block req idx.

We are able to use the decouple and iterate technique here because we, a parenthesis is deemed balanced based on the paranthesis that
is closest/ adjacent or in its proximity. This solution uses the simple fact that a closing parenthesis can only balance an opening 
parenthesis that comes before it when we are looping from left to right. If we are looping from right to left, then an opening 
parenthesis can only balance a closing parenthesis that comes before it. Thus we loop from left to right and then from right to left 
and each time we count the closing and opening parenthesis, knowing that if these counts are ever equal we have a balanced substring 
and we can then calculate the length of this balanced substring by adding the two counts or multiplying one count by 2. When looping 
from left to right, we expect opening parenthesis come before closing parenthesis so the opening parenthesis count can be larger than 
the closing parenthesis count. If while looping from left to right, the closing parenthesis count is ever larger than the opening 
parenthesis count, we know that the substring at that point cannot be balanced so we reset both counters. Similarly whilst looping 
from right to left, expect closing parenthesis to come before opening parenthesis so if we ever come to a point where the opening 
parenthesis count exceeds the closing parenthesis count we know the substring at that point cannot be balanced so we reset the counts 
and continue looping. At the end we return the length of the maximum balanced substring ever encountered. 

In the first versiion of this solution, we use a two for loops, left to right and reversed() right to left and the logic is pretty 
much simple after that, check the current loop character. If it is an opening bracket, increment the opening bracket count. If it is
a closing bracket, we increment the closing bracket count. Then we use a if/elif statement to compare the counts. In both loops, left
to right and right to left, the if statement is the same. If the counts are equal, we have a balanced string, and we calculate its even
length by adding the two counts together or by multiply one of them by 2 since they are equal. The two loops differ only
in the elif check. In the first loop, left to right, we check if the closing parentheses outnumber the opening parentheses, such as if
the first element is a closing parentheses, in which case we reset both counter since we cannot have a balanced string with the string
ending there, so both counters become 0. In the right to left loop, we check if the opening parentheses outnumber the closing 
parentheses, we reset the couunters to 0 because we can no longer have a balanced string ending there. Other things of note is that 
since we are tracking the same maxLength variable in both cases, we initilize this once at the top. Otherwise we initialize an opening
and closing count for each for loop. At the end, we return the updated maxLength found.

The second version of the optimal solution removes the repeated code by putting the necessary functionality in a helper function. We 
make two calls to the helper function with the string and a boolean leftToRight, which if True refers to the first loop, left to right
and if false, refers to the second loop, right to left. The helper function returns the maximum length balanced substring2 In the helper 
function, based on the boolean, we declare openingParens to be an opening bracket if leftToRight else closing bracket. We only need to 
track an opening parentheses if leftToRight and a closing parentheses when leftToRight is False, because we have only two choices since
our string is assured to only contain parentheses. Since we will be using a while loop we need (an) iterator variable(s). The first 
iterator variable is startIdx which is 0 if leftToRight is True else len(string) - 1. The second iterator variable is step, which 
determines how we move progressively through the string, and is +1 if leftToRight is True, and -1 if leftToRight is False. With 
openingParens, startidx, step initialized based on leftToRight, we initialize openingCount, closingCount, maxLength all to 0 and
enter the while loop which is going to iterate through the array from 0 to len(string) - 1 so the loop condition is that initialize a
generic iteator idx= startIdx and the loop condition is that idx >= 0 and idx < len(string). The we choose the string character at idx,
and if its equal to the openingParens for our current direction, we increment the openingCount, else we increment closingCount, again
due to the binary choice we have. Then we use the if of an if/elif statement to check if  the two counts are the same in which case we 
compare and update maxLength after a max() comparison with the length of the current balanced string (either count * 2) , followed by
an elif which checks if the closing count is greater than the openingCount in which case we reset both counters to 0. Outside these
if/else and if/elif statements but inside the while loop, we advance idx by adding step to it (which is chosen based on leftToRignt).
At the end of the while loop we return maxLength to the original function that is receive the maxLength when leftToRight is True and
for when leftToRight is False, and retuns the maximum of these as the final answer.

In the stack based question about balanced parentheses, there are multiple different parentheses,hence we needed the space to check
which type of opening parentheses a closing parentheses balances. Otherwise if we are assured that a string of parentheses contains
a single type like in here, we can use one pass of this algorithm of counting opening and closing parentheses, returning False if
closingCount exceeds openingCount and at the end we return openingCount == closingCount ie True if equal, False if not equal.

The mid-optimal approach, improves on the brute force approach by using a stack directly instead of generating even-length substrings
to be passed to the stack-based balanced parenthesis function. In that solution, we add opening parentheses to a stack and when we
find a closing parenthesis we check if the stack is empty. If it is, it means a closing parentheses is coming before an opening
parentheses and therefore the string is unbalanced. Here, we modify this approach so that we can use the stack to directly calculate
the lengths of balanced substrings. The first modification is to append the indices of opening parenthesis. Since we are iterating
in order we know that all the indices underneath the peak value of the stack are indices that come before the peak index. We could
just go ahead and pop the peak value and use that for our calculation by we run into a problem, when two balanced substrings are
back to back and thus together form a longer substring eg '())()(()())'. The substring at index 3-4 is balanced with a length of 2.
The substring at index 6-7 and 8-9 are also back to back balanced substrings of length 2 that are both enclosed in the substring 5-10
giving the longest substring a length of 6. So if we just append the indices of only the opening indices and at a closing index, we
pop from the stack and use the these to calculate the length (closingIdx-popIdx+1), we will find all the balanced strings of length 2,
we will miss the back to back balanced substring 6-9 of length 4 , we will find the balanced string of length 6 at index 5-10. Thus
if the only modification we do to the stack-based solution is to append indices, we will find every balanced string where the closing
parentheses comes after the opening parentheses, since that is what you are testing when determining if a string of parentheses is
balanced, but we will not find longer substrings composed on smaller balanced back to back substrings. To ensure that we find the 
max length substrings, we first no longer use the popIdx for calculating length, instead using the new peak value of the stack after
popping since in the general case would be the index right before the popped value ie in '(())' when we get to closingIdx = 2, we pop
index 1 of the stack and use index 0 , the new peek value after popping, for the calculation ie 2 - 0 which gives us the correct
answer. What about the string '()('? We will run into a problem, because when we reach closingidx = 1, the stack would be empty after
popping index 0 from it. So to handle this case we initialize the stack with -1 so that after popping index 0 we can still say 1 - -1
= 2 for the length of the balanced substring 0-1. But the final case is '())()', after using up the initialized -1, how do we avoid
using the wrong idx= -1, for length calculation when closingIdx =4 and we pop index 3? The answer is that when we get to closingIdx=2 
we still pop of the stack anyway ie pop -1 and since the stack will empty after that we append index 2, so index 2 will become like -1 
in the previous sitution, helping us calculate length. So that is exactly what the mid-optimal solution does, we first initialize a stack 
and add -1 to it. Then we iterate through the array with indices, and if the current character is an opening parentheses we add its index. 
If its a closing a parenthesis, we pop of the top of the stack. Then we check if the stack is empty after popping, if it is, we add the 
closingIdx to the stack for future calculations and popping operations. If after after popping off the stack, the stack is still not empty, 
then we use the peek value to calculate the length of the substring that the current closing parentheses balances and compare to the 
maxLength. Even though the this solution runs in the same time complexity of the optimal solution, it uses linear space for the stack. 
However it is an excellent example of making necessary modifications in order to use an existing implementation to solve a new problem. 
In any way, it vastly improves upon the brute force solution by negating the need for generating substrings.
"""


"""In the brute force approach we generate every even-length substring of the input, check if these 
substrings are balanced using a stack and return the length of the longest balanced substring"""
#O(n^3) time | O(n) space
# def longestBalancedSubstring(string):
#     maxLength = 0 #initialize the length of the longest balanced substring
#     for i in range(len(string)): #loop to generate even-length substrings, j starts two paces after i
#         for j in range(i+2,len(string)+1, 2): #j step=2, len(string) + 1 to include last index if even
#             if isBalanced(string[i:j]): #if the generated substring is balanced, O(n) slice + O(n) check
#                 currentLength = j - i
#                 maxLength = max(maxLength, currentLength)
#     return maxLength

# def isBalanced(string):
#     openParensStack = []
#     for char in string:
#         if char == "(": #if current character is an open parenthesis
#             openParensStack.append("(") #append to stack
#         elif len(openParensStack) >0: #if current character is a closed parenthesis and stack is not empty
#             openParensStack.pop() #pop opening parenthesis off top, to balance current closing parenthesis
#         else: #if current character is a closed parenthesis and stack is empty
#             return False #bcos we don't have an opening parenthesis on stack to balance current closing parenthesis
#     return len(openParensStack) == 0 #if able to balance every closing /open parenthesis by end then balanced=True

"""Mid-optimal solution here. In this solution, we use a stack differently. Instead of adding opening parenthesis
to the stack we add the indices of opening parenthesis.The stack is initially seeded with a -1 to simplify calculation 
of the length of balanced parenthesis strings. As we iterate through the string, if we come to a closing parenthesis,
we pop off the top of the stack and read the new top of stack and subtract that value from the current iterator index
to calculate the length of the substring that was just balaced. If the stack is empty after popping, we append the
closing parenthesis index to the stack because any future balanced substrings will use that to calculate length. The
initial -1 stack seed also ensures that we can pop if the first character is a closing parenthesis"""
#O(n) time | O(n) space
# def longestBalancedSubstring(string):
#     maxLength = 0 #initialize maxLength for the length of longest balanced substring
#     idxStack = [] #stack
#     idxStack.append(-1) #stack iniitially seeded with -1 for calculating substring length starting from first character

#     for i in range(len(string)): #loop through string
#         if string[i] == "(": #if char at current iterator index is an opening parenthesis
#             idxStack.append(i) #append the index of the opening parenthesis to the stack
#         else: #if the char at the current iterator index is a closing parenthesis
#             idxStack.pop() #pop the index at the top of stack. If first char is a closing parenthesis, pop -1 seed
#             if len(idxStack) == 0: #if the stack is empty after popping off top
#                 idxStack.append(i) #append the index of closing parenthesis, for substring length calculation and popping
#             else: #if the after popping,the stack is not empty
#                 balancedSubstringStartIdx = idxStack[-1] #balanced substring starts after the index at peek value of stack
#                 currentLength = i  - balancedSubstringStartIdx
#                 maxLength = max(maxLength,currentLength)
#     return maxLength

"""Optimal solution. This solution uses the simple fact that a closing parenthesis can only balance an opening parenthesis
that comes before it when we are looping from left to right. If we are looping from right to left, then an opening parenthesis
can only balance a closing parenthesis that comes before it. Thus we loop from left to right and then from right to left and 
each time we count the closing and opening parenthesis, knowing that if these counts are ever equal we have a balanced substring 
and we can then calculate the length of this balanced substring by adding the two counts or multiplying one count by 2. When looping 
from left to right, we expect opening parenthesis come before closing parenthesis so the opening parenthesis count can be larger than 
the closing parenthesis count. If while looping from left to right, the closing parenthesis count is ever larger than the opening 
parenthesis count, we know that the substring at that point cannot be balanced so we reset both counters. Similarly whilst looping 
from right to left, expect closing parenthesis to come before opening parenthesis so if we ever come to a point where the opening 
parenthesis count exceeds the closing parenthesis count we know the substring at that point cannot be balanced so we reset the counts 
and continue looping. At the end we return the length of the maximum balanced substring ever encountered"""
#O(n) time | O(1) space
# def longestBalancedSubstring(string):
#     maxLength = 0

#     openingCount = 0    #initialize count of opening parentheses at 0 for left to right iteration
#     closingCount = 0    #initialize count of closing parentheses at 0 for left to right iteration
#     for char in string: #left to right iteration
#         if char == "(":
#             openingCount += 1
#         else: #if char == ")"
#             closingCount += 1
        
#         if openingCount == closingCount:
#             maxLength = max(maxLength, closingCount*2)
#         elif closingCount > openingCount: #from left to right, in this case we cant balance this substring
#             openingCount = 0 #reset count of opening parentheses
#             closingCount = 0 #reset count of closing parentheses
    
    # openingCount = 0    #initialize count of opening parentheses at 0 for right to left iteration
    # closingCount = 0    #initialize count of closing parentheses at 0 for right to left iteration
    # for i in reversed(range(len(string))): #right to left iteration
    #     char = string[i]
    #     if char == "(":
    #         openingCount += 1
    #     else: #if char == ")"
    #         closingCount += 1
        
    #     if openingCount == closingCount:
    #         maxLength = max(maxLength, openingCount*2)
    #     elif openingCount > closingCount: #from right to left , in this case we cant balance this substring
    #         openingCount = 0 #reset count of opening parentheses
    #         closingCount = 0 #rest count of closing parentheses
    # return maxLength


"""Optimal solution. This is the exact same algorithm as solution three, but written in a cleaner, non-
repetitive manner"""
#O(n) time | O(1) space
def longestBalancedSubstring(string):
    return max(getLongestBalancedInDirection(string,True), getLongestBalancedInDirection(string,False))

def getLongestBalancedInDirection(string,leftToRight):
    openingParens = "(" if leftToRight else ")"
    startIdx = 0 if leftToRight else len(string) - 1
    step = 1 if leftToRight else -1

    maxLength = 0

    openingCount = 0 #openingCount here refers to whatever we expect to see first in the direction of iteration
    closingCount = 0 #if leftToRight openingCount is count of opening parenthesis in right to left its closing parenthesis

    idx = startIdx
    while idx >=0 and idx < len(string): #both conditions for left to right and left to right
        char = string[idx]
        if char == openingParens:
            openingCount += 1 #openingCount tracks opening parentheses on left to right and closinng parenthesies on right to left
        else: 
            closingCount += 1
        
        if openingCount == closingCount:
            maxLength = max(maxLength, closingCount*2)
        elif closingCount > openingCount: #closingCount here will be what we dont expect to see more of based on direction
            openingCount = 0 #reset count 
            closingCount = 0 #rest count 
        
        idx += step #increment idx by step amount

    return maxLength

string = "(()))("
print(longestBalancedSubstring(string))

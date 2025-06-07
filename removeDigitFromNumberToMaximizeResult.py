"""You are given a string number representing a positive integer and a character digit. Return the resulting string 
after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal 
form is maximized. The test cases are generated such that digit occurs at least once in number.

Example 1:
Input: number = "123", digit = "3"
Output: "12"
Explanation: There is only one '3' in "123". After removing '3', the result is "12".

Example 2:
Input: number = "1231", digit = "1"
Output: "231"
Explanation: We can remove the first '1' to get "231" or remove the second '1' to get "123".
Since 231 > 123, we return "231".

Example 3:
Input: number = "551", digit = "5"
Output: "51"
Explanation: We can remove either the first or second '5' from "551".
Both result in the string "51".
 

Constraints:
2 <= number.length <= 100 ; number consists of digits from '1' to '9'. ; digit is a digit from '1' to '9'.  ;  
digit occurs at least once in number.

This question is related to removeKDigits. Anyway the algorithm for removing a single instance of digit such that the
remaining value is maximized is as follows:
If we want to maximize the number after remove the target digit :
from left to right, we find the first target digit such that char(i) == digit && char(i+1) > char(i) 
otherwise we remove the first occurance of digit from right to left. 
The rationalization is that in general we remove the least significant instance of digit, unless there are instances
of digit where the next value is greater than digit, in which case we remove the first such instance. The reason is
that if the nextt value is greater than digit, then it will take the place of the removed instance of digit and in
that case, we want to replace the most significant instance for which the next value is greater.


"""

def removeDigit(number, digit) :
    firstLargerIdx = -1
    lastTargetIdx  = -1
    n = len(number)
        
    for i in range(n):
            
        if int(number[i]) != int(digit):
            continue
        
        lastTargetIdx = i
        if i+1 < n and int(number[i+1]) > int(digit):
            firstLargerIdx = i
            break
        

    if firstLargerIdx != -1:
        removeIdx = firstLargerIdx
    else:
        removeIdx = lastTargetIdx

    output = []
    for i in range(len(number)):
        if i != removeIdx:
            output.append(number[i])
        
    return "".join(output)


number = "1212122"
digit = "2"
print(removeDigit(number, digit))
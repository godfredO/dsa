

# def pascalsTriangle(numbers):
#     finalTwo = getFinalTwoNumbers(numbers)
#     a, b = str(finalTwo[0]), str(finalTwo[1])
#     return "".join([a,b])


# def getFinalTwoNumbers(numbers):
#     if len(numbers) == 2:
#         return numbers
    
#     startIdx = len(numbers) - 1
#     array = []
#     while startIdx > 0:
#         val = numbers[startIdx - 1] + numbers[startIdx]
#         entry = val % 10
#         array.append(entry)
#         startIdx -= 1
    
#     return getFinalTwoNumbers(array)
        

def pascalsTriangle(numbers):

    array = numbers
    while len(array) > 2:
        output = []
        startIdx = len(array) - 1
        while startIdx > 0:
            val = array[startIdx - 1] + array[startIdx]
            entry = val % 10
            output.append(entry)
            startIdx -= 1
        array = output
    a, b = str(array[0]), str(array[1])
    return "".join([a,b])



numbers = [4,5,6,7]
print(pascalsTriangle(numbers))
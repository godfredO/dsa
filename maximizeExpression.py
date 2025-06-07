"""Brute force solution where we test every possibility for the expression and store the maximum value of the 
expression"""
#O(n^4) time | O(1) space
# def maximizeExpression(array):
#     if len(array) < 4: #if there are less than four elements then there is no possibility for the expression
#         return 0  #question prompt asks us to return this

#     maximumValueFound = float("-inf")  #initialize max expression value at -infinity for easy comparison

#     for a in range(len(array)): #pick an index for a
#         aValue = array[a]   #choose a value for a

#         for b in range(a+1,len(array)): #pick b index greater than the current a index
#             bValue = array[b]  #choose b value

#             for c in range(b+1,len(array)): #pick c index greater than the current b index
#                 cValue = array[c]

#                 for d in range(c+1, len(array)):#pick d index greater than the current c index
#                     dValue = array[d]

#                     expressionValue = evaluateExpression(aValue,bValue,cValue,dValue)
#                     maximumValueFound = max(maximumValueFound,expressionValue)
#     return maximumValueFound

# def evaluateExpression(a,b,c,d): #abstracting this expression allows to change the expression in future 
#     return a - b + c - d


"""Optimal approach where we use dynammic programming to maximize successive sub-expressions for subarrays ending
at each index of the input array ,storing the answers for each sub-expression in a data structure to be used to
build solutions for successive sub-expressions until the full expression has been maximized for the full input array."""
#O(n) time | O(n) space
def maximizeExpression(array):
    if len(array) < 4: #if there are less than four elements then there is no possibility for the expression
        return 0  #question prompt asks us to return this

    maxOfA = [array[0]]                 #max for subarray ending at first element is first element; simplifies loop logic
    maxOfAMinusB = [float("-inf")]      #-infinity simplifies later comparisons; a-b will have no value for first entry
    maxOfAMinusBPlusC = [float("-inf")] * 2    # a - b + c will have no values for first two entries
    maxOfAMinusBPlusCMinusD = [float("-inf")] * 3 #a - b +c -d will have no values for first three entries

    for idx in range(1,len(array)): #start at second element since first value for maxOfA has already been added to simplify logic
        currentMax = max(maxOfA[idx -1], array[idx]) #choose a max for a, for subarray ending at each index
        maxOfA.append(currentMax) #append max of first subexpression, a, for subarray ending at idx
    
    for idx in range(1,len(array)):#start at second element since we cannot index 0  for b in a - b
        currentMax = max(maxOfA[idx-1] - array[idx],maxOfAMinusB[idx - 1]) #first value is -inf for easy comparison
        maxOfAMinusB.append(currentMax) #append max for a - b , for subarray ending at each index
    
    for idx in range(2, len(array)): #start at third element since we cannot choose index 0, 1 for c in a - b + c
        currentMax = max(maxOfAMinusB[idx -1] + array[idx], maxOfAMinusBPlusC[idx - 1]) #first two values are -inf for easy comparison
        maxOfAMinusBPlusC.append(currentMax) #append max for a - b + c , for subarray ending at each index
    
    for idx in range(3, len(array)): #start at fourth element since we cannot choose index 0, 1,3 for d in a - b + c - d
        currentMax = max(maxOfAMinusBPlusCMinusD[idx -1], maxOfAMinusBPlusC[idx -1] - array[idx])
        maxOfAMinusBPlusCMinusD.append(currentMax)
    
    return maxOfAMinusBPlusCMinusD[-1]




array = [3, 6, 1, -3, 2, 7]
print(maximizeExpression(array))
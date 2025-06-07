"""The question gives two non-empty arrays of integers and asks to find the pair of numbers, one from each array, whose absolute difference
is closest to zero. Now the absolute difference of any two numbers is always a non-negative number, and equals 0 when the two numbers are 
equal otherwise it is greater than 0. So we know that if we find the same number in the two arrays, that is our answer , since we are 
assured that there will be only one pair of numbers with the  smallest difference. The naive approach is to generate all pairs, compute
the absolute difference and track the smallest absolute difference seen and the pair that created that. This solution is O(n*m) where n
and m are the lengths of the two input arrays. Anyway, this approach would be naive because it doesnt make use of the facts that we
are assured one answer and we know that the smallest possible absolute difference is 0. The optimal approach sorts both arrays so that
we can move in an intelligent manner. Then using two pointers, one for each array, we iterate through the arrays, compute the absolute
difference for the current pointer values in each array and then move one pointer based on a comparison of the values. First off,
we compare the current absolute difference with the last smallest absolute difference and if the current is smaller we update the last
seen smallest absolute difference and store the new pair. Then we check if the two values (one from each array) are the same. If they are
equal, then we know that the absolute difference is 0 and thus we can just return the current pair of values. However if they are not
equal, since we are looping from left to right, we know that all the remaining numbers are greater for each array. As a result we cannot
get the smaller of the pair any closer to 0 but we might be able to still get the larger of the pair closer to the minimum value of 0.
Thus we compare the two values and whichever one is smaller, we increment the pointer for that array. That way if the larger value also
occurs in the other array we could find it. Even if the larger value is not in the other array, we know that we are more likely to find
a number that possibly generates a smaller absolute difference. The loop itself in this approach take O(n+m) and even with the sorting,
it still has a better complexity than the naive solution."""

"""
First solution generates all possible pairs and keeps track of the smallest
difference seen and pair that yielded this difference.
O(n*m) quadratic time complexity, where n,m are the lengths of arrayOne,arrayTwo
O(1) constant space complexity, since we are assured there will only be one solution 
so auxilliary memory needed doesnt change with input size
"""

def smallestDifference(arrayOne,arrayTwo):
    smallest = float('inf')
    current = float('inf')
    smallestPair = []

    #we effectively generate all pairs for each first number in arrayOne, compute every absolute difference for current number in arrayOne
    #store the smallest difference for current number in arrayOne, and then change the currentNumber for arrayOne. Then repeat by choosing
    #the next number in arrayOne as first number.
    for i in range(len(arrayOne)): #choose first number
        for j in range(len(arrayTwo)):
            firstNum = arrayOne[i]
            secondNum = arrayTwo[j]
            current = abs(firstNum - secondNum)
            if current == 0:
                return [firstNum,secondNum]
            if current < smallest:
                smallest = current
                smallestPair = [firstNum,secondNum]
    return smallestPair

"""
Second solution sorts the two arrays to avoid generating every pair. Instead we set pointers
for each array and move the pointer in the direction that could yield a smaller difference 
than previously seen. This is done by comparing the current numbers from each array and moving the pointer
of the lower one. Note that it is important to access the current numbers before this comparison. 
Then compare the current absolute difference to the smallest previously seen and update the tracked
pair if its a smaller difference than the previous.
"""

def smallestDifferenceII(arrayOne,arrayTwo):
    arrayOne.sort()  # O(nlogn)
    arrayTwo.sort() # O(mlogm)

    i = 0  # arrayOne pointer 
    j = 0  # arrayTwo poiinter

    smallest = float("inf") 
    current = float("inf") # current absolute difference
    smallestPair = []

    while i < len(arrayOne) and j < len(arrayTwo):
        firstNum = arrayOne[i]
        secondNum = arrayTwo[j]

        if firstNum < secondNum:
            current = secondNum - firstNum
            i += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            j += 1
        else:
            return [firstNum,secondNum]
        if current < smallest :
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair

        


#O(nlog(n) + mlog(m)) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	difference = float("inf")
	output = []
	
	i, j = 0, 0
	while i < len(arrayOne) and j < len(arrayTwo):#O(n+m)
		current = abs(arrayOne[i] - arrayTwo[j])
		if current < difference:
			difference = current
			output = [arrayOne[i], arrayTwo[j]]
		
		if arrayOne[i] < arrayTwo[j]:
			i += 1
		elif arrayTwo[j] < arrayOne[i]:
			j += 1
		else:
			return [arrayOne[i], arrayTwo[j]]
	return output


        






arrayOne = [-1, 5,10,20,28,3]
arrayTwo = [26,134,135,15,17]

print(smallestDifference(arrayOne,arrayTwo))
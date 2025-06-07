""""This rather simple looking question requires some clever manipulation. Since we know we are looking for the three largest numbers we
initialize a three element array of None values. This is because this output array is to be in sorted order at all times, and a None 
indicates that we havent filled that position yet. I say this because my initial reaction was to initialize the output array with the 
first three numbers of the array, but there is no assurance that the first three numbers are sorted. So the output array contains sorted
numbers or None. Next thing is that we loop through our array and compare each value with the elements in the output array but it is
essential that this comparison is that from the back to the front. This is because if we find that the current loop element is larger 
than the last output element, we shift the last output element to the second position and replace the last element with the current loop
value. Thus we starting from index 2, then index 1, then index 0, if the element in the output array is None or the current loop value 
of the array is larger we call a helper function to shift the current output element forward and update it with the current array value.
Finally to shift and update elements, we actually loop from the from, and copy the next element into the current position except when 
we get to the passed idx, where we update with the current array value. Thus remember to compare from the back to the front to maintain
sorted order of the output array. And for a particular update idx, shift from the front so that we have access to the shift value and 
when the shift idx matches the update idx, set the current array value. This backward compare and forward shifting are both generalizations
of the clever movement of binary search based on known or expected sorted order. In binary search we start comparing from the middle,
here we start comparing from the back , but its the same underlying principle of intelligent movement based on sorted order."""


#O(n) time | O(1) space
def findThreeLargestNumbers(array):
    threeLargest = [None,None,None]

    for num in array: #find the three larget values
        updateLargest(threeLargest,num)
    return threeLargest

def updateLargest(threeLargest,num): #compare current loop value to current output array back to front
    if threeLargest[2] is None or num > threeLargest[2]: #if number is less than or equal to output[2] we will check output[1]
        shiftAndUpdate(threeLargest,num,2)
    elif threeLargest[1] is None or num > threeLargest[1]:#if number is less than or equal to output[1] we will check outuput[0]
        shiftAndUpdate(threeLargest,num,1)
    elif threeLargest[0] is None or num > threeLargest[0]:#if number is less than or equal to output[0] then its not part of threeLargest
        shiftAndUpdate(threeLargest,num,0)

def shiftAndUpdate(array,num, idx): #if adding current loop value to output, shift front to back
    #use a for loop to updte and shift
    for i in range(idx+1): #we will doing up to idx shift and update steps, +1 for range() end-exclusivity from index 0 to idx
        if i == idx:  #update step
            array[i] = num
        else:    #shift step, shift from front so that we have access to shift value
            array[i] = array[i+1]


array = [99, -23, 899, 3 , 67,3, 900, 1, 5]
print(findThreeLargestNumbers(array))

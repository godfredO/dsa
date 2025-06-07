
""" The question asks to write a function that takes in an array of integers and returns a new array containing, at each index the next
element in the input array that's greater than the element in the input array. That is outputArray[i] is the next element greater than
inputArray[i]. If there is no such next greater element for a particular index, the value at that index in the output array should be
-1. eg [1,2] should return [2,-1]. The function should treat the input array as a circular array ie wrap around its self as if 
connected end-to-end. Thus for [0,4,3], the next greater element after 3 is 4. 

The brute force solution is to use two for loops, the inner for loop finding the next greater element for the element in the outer for
loop ie O(n^2). The inner loop will use the circular index method from outer loop index, to 2*length of array and mod the obtained index
by the length of the array. See below. In both the brute and optimal solution we initialize an output array with -1 at each index.

The optimal solution uses a stack. Stacks are great for when we need to use space to solve proximity / contiguity / closest to type of
questions. Now the solution works is that we iterate through the array in (sorted) circular order ie from index 0 to index len(array) -1
and back to index 0 and at each point we add the index to the stack. So at index 0, we add 0 to the stack. However before we add the
current index to the stack, since we are iterating in (sorted) circular order ie the current index comes after the last index added to
the stack, it is possible that the current index could be the next greater element for the index on top of the stack. That is after adding 
index 0 (since the stack is empty at this point), when we get to index 1, we first check if the value at index 1 is greater than the value 
at index 0. If it is, we found the next greater element for the index on top of the stack, so we pop from the top of the stack and set the 
value at that index in the output to be the current value, so if the value at index 1 is greate than the value at index 0, we pop 0 off the 
top of the stack and at index 0 in the output we store the value at index 1. Now in this example, the stack would be empty after a single 
pop operation, so we would append index 1 to the stack. But what if we were at index 3 in [2,1,0,4,5] and the stack = [0,1,2] we would find 
that the value at index 3 is the next greater element for index 0,1,2 and so we would pop update the output, pop, update the output and keep 
going until we the stack is empty or we reach a point where the current element is equal to or less than peek value. Since we initialize the 
output array, with -1, if we don't find a next greater element, we would be covered. And as always to generate circular indices we multiply
the length by 2, as though to get indices for an array twice the length and modulo divide by that index by the length of the array to get
the circular index for accessing values in the array."""


#O(n^2) time | O(n) space
def nextGreaterElement(array):
    output = [-1 for _ in array]
    for i in range(len(array)):
        for k in range(i,2*len(array)): #generate circular array indices
            j = k % len(array)
            current_num = array[i]
            current_test = array[j]
            if current_test > current_num:
                output[i] = current_test  # next greater element for ith array value found
                break  #break out of while loop since next greater element for ith array value has been found
    return output


#O(n^2) time | O(n) space
def nextGreaterElement(array):
	output = [-1 for _ in array]
	
	for i in range(len(array)):
		w = list(range(i+1,len(array)))  #generate circular array indices for test
		w.extend(list(range(0,i)))       #generate circular array indices for test
		for j in w:
			current_num = array[i]
			current_test = array[j]
			if current_test > current_num:
				output[i] = current_test  # next greater element for ith array value found
				break  #break out of while loop since next greater element for ith array value has been found
	return output


# O(n) time
def nextGreaterElementI(array):
    output = [-1 for _ in array]
    stack = []
    
    #loop through array using circular indices
    for j in range(2*len(array)): # generate circular array index
        i = j % len(array)        # generate circular array index

        # loop through stack
        while len(stack) != 0 and array[i] > array[stack[-1]]:
            output[stack[-1]] = array[i]
            stack.pop()
        
        #update stack
        stack.append(i)
    
    
    return output



"""
This solution loops through the array in reversed fashion from right to left
"""
#O(n) time | O(n) space
def nextGreaterElementII(array):
    output = [-1] * len(array)
    stack = []

    for j in reversed(range(2*len(array))):
        i = j % len(array)

        while len(stack) > 0 :
            if array[stack[-1]] <= array[i] : # stack peek not the next greater element for ith array value
                stack.pop()
            else:
                output[i] = array[stack[-1]] # found next greater element for ith array value
                break  #break out of while loop since next greater element for ith array value has been found
            
        stack.append(i)
    return output


array = [2,5,-3,-4,6,7,2]
print(nextGreaterElementII(array))
"""This question gives two non-empty arrays of integers and asks to return a Boolean representing whether the second array is a subsequence
of the first array. A subsequence of an array is a set of numbers that aren't necessarily adjacent but that are in the same order as they
appear in the array. The solution to this problem has similarities in terms of logic to both the complement solution and the sorting solution
of the twoSum question. Like the sorting solution we use two pointers, but this time one pointer for each array. Like the complement solution,
we iterate through the first array using its pointer, but before we move the first array pointer we make a constant time check and if True we 
do something to the second pointer. So the solution is as follows, iterate through the first array with its pointer, but before we move the
pointer we check if the current element in the first array is equal to the second pointer in the second array. If it is, we increment the 
second pointer. If the second array is a valid subsequence, by the time we break out of our while loop, the second pointer will just be
out of bounds ie equal to the length of the second array, meaning we found each element of the second solution inside the first array and in
the same order as it appears in the second solution. So we know the second array is a valid subsequence if the second pointer is equal to the
length of the second array. Since we know that we are going to iterate through the first array anyway, instead of using a while loop and 
always checking that neither pointer is out of bounds, we use a for loop to iterate through the first array and pointer for the second array, 
compare the current first array element to the element at the second array pointer and if it is we increment the second array pointer. To
handle the situation where we find the second array before we reach the end of the first array in the for loop, we need to add a break
statement for when the second array pointer is already out of bounds so that we don't throw errors. At the end, we still check if we are just 
out of bounds for the second array, meaning we found every second array element in the first array and in the same order as they appear in the 
second array. Clearly the while loop solution is more intuitive."""


def isValidSubsequence(array,sequence):
    a, s = 0,0 # pointer for array and sequence

    while a < len(array) and s < len(sequence):
        if sequence[s] == array[a]:
            s += 1 #move to next in sequence
        a += 1 #at least go through array
    return s == len(sequence)

array = [5,1,22,25,6,-1,8,10]
sequence = [1,6,-1,10]

"""
Since you have to go through the array at least once, use a for loop for array for array and a pointer for the second array. At each stage 
check if the second array pointer is out of bounds at which point we break out of the for loop. If not, we check if the current for loop
element is equal to current second array (sequence) element. If equal move to next number in the second array (sequence) by incrementing the 
second array (sequence) pointer.
"""
def isValidSubsequenceII(array,sequence):
    s = 0

    for aval in array:
        if s == len(sequence):
            break
        if aval == sequence[s]:
            s += 1
    return s == len(sequence)



print(isValidSubsequenceII(array,sequence))
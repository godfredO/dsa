"""Mid-optimal solution where we use two arrays to keep track of increaasing subsequences and their lengths. The first
array is called lengths and the second is sequences. Lengths will have the same length as the input array and at  each 
index of this array, we store the length of the longest increasing subsequence that ends with the value at that index in 
the input array. In the sequences array at each index we store the index of the preceding value in that longest increasing 
subsequence. Thus as we loop through array at each point, we loop again from the start to that point looking for values that 
are less that the current value. The idea is that we are looking for the penultimate value in the increasing subsequence and 
so whenever we find a lesser value, we read the length stored in the lengths array and add one to it as the value to be stored 
at the current index of lengths array and the lesser value's index in the sequences array since it is the penultimate value. At 
the end of the double for loop we reconstruct the longest subsequence using the sequences array and the longest length found"""
#O(n^2) time | O(n) space
def longestIncreasingSubsequence(array):
    sequences = [None for x in array] #initialize to None to be updated later
    lengths = [1 for x in array] #we initialize to 1 bcos each element on its owwn is a subsequence so length is at least 1
    maxLengthIdx = 0 #index to keep track of location of longest length seen, initialize at index 0 since array is non-empty
    for i in range(len(array)): #choose index of last element in subsequence
        currentNum = array[i] #access current value for last element in subsequence
        for j in range(0,i): #choose the index of the penultimate element in subsequence
            otherNum = array[j] #choose penultimate value in subsequence
            if otherNum < currentNum and lengths[j] + 1 >= lengths[i]: #if subsequence is strictly increasing and longer length
                lengths[i]  = lengths[j] + 1 #update the length at current ending index
                sequences[i] = j 
        if lengths[i] >= lengths[maxLengthIdx]:
            maxLengthIdx = i
    return buildSequence(array,sequences,maxLengthIdx)

def buildSequence(array,sequences,currentIdx):
    sequence = []
    while currentIdx is not None: #if value in sequences is None, it means no number comes before it in subsequence
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence)) #reverse before returning

"""In the optimal solution we use two arrays, indices and sequences. The purpose of the sequences array is the same as before
However the indices array stores the index of the last element of an increasing subsequence whose length is the same as index.
Thus at index 1 we store the index of the increasing subsequence of length 1. Same at index 5 we store the index of the last
element of an increasing subsequence of length 5. The sequences array still stores the index of the penultimate element in an
increasing subsequence that ends at the value stored at that the same index in the input array. Anyway as we iterate through 
the array, we use binary search instead of linear search to search for the penultimate element, calculate the length and update
some variable that tracks the max length seen. Since the indices array represents the lengths, and we want the longest increasing
subsequence we choose the middle element in the indices array, compare it to the current value in the array for loop. And if the 
value in the array stored at them middle index of indices array, is less than the current value we have an increasing subsequence
and since the indexes in the indices array represent lengths and we want to maximize this length we ignore everything to the left
of middle index and move the left pointer of binary search to middle index and keep searching. When we come to a value that is
greater than the current value, we stop our search and form an increasing subsequence with the previous value."""
#O(nlog(n)) time | O(n) space
def longestIncreasingSubsequence(array):
    sequences = [None for x in array] #initialize to None to be updated later
    indices = [None for x in range(len(array) +1)] #longest possible subsequence is len(array) so +1 for exclusivity
    length = 0
    for i, num in enumerate(array): #keep track of current index and current value
        #start at index 1 since index 0 of indices(for 0 length subseq)is always None, endIdx is length since that last updated
        newLength = binarySearch(1,length,indices,array,num) #the last updated value in indices was at length index hence endIdx
        sequences[i] = indices[newLength - 1] #store the index of the penultimate element in the subsequence
        indices[newLength] = i #add the last element i, at newLength index of indices
        length = max(length,newLength)
    return buildSequence(array,sequences,indices[length])

def binarySearch(startIdx,endIdx,indices,array,num): #we are using recursion instead of a while loop for binary search here
    if startIdx > endIdx: #binary search base case
        return startIdx
    middleIdx = (startIdx + endIdx) // 2
    if array[indices[middleIdx]] < num: #if the number in array with index equal to middle index is less than current value
        startIdx = middleIdx + 1 #move the left pointer to after middleIdx
    else: #if value in array at index stored in indices array at middle index is greaterthan or equal to current value
        endIdx = middleIdx - 1 #then ignore everything to the right by moving endIdx to just before middleIdx
    return binarySearch(startIdx,endIdx,indices,array,num) #recursive step

def buildSequence(array,sequences,currentIdx):
    sequence = []
    while currentIdx is not None: #if value in sequences is None, it means no number comes before it in subsequence
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence)) #reverse before returning

array = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
print(longestIncreasingSubsequence(array))
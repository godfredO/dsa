"""The input is an array of positive integers and the question is to write a function that returns the maximum sum of non-adjacent elements
in the array. We first have to handle the edge cases of an empty input or a single element array. If the array is empty we return 0, since we 
expected positive integers anyway, so 0 is the lowest sum possible. If the array has a single element we return that element. Thus you have to 
identify these edge cases first. Then like all dynammic programming questions. we start by initializing a data structure the same size as the 
input and then use the classic technique of solving the problem, for the sub-array ending at each index. So we start by initializing an array 
of length(n) because the  input is an array of length n. The at index 0 of this data structure, we ask what is the max non-adjacent sum for the 
sub-array ending at index 0. At index 0 we have only one valid addend, ie array[0] so in the data structure (array) we add this value at index 
0. Then at index 1 of the data structure, we ask, what is the max non-adjacent sum for the sub-array ending at index 1. Again, at index 1, we 
can only have 1 valid addend since the subarray ending at index 1 has two adjacent values, array[0] and array[1], we can't add these for our
answer, but we can choose one of them for the answer. Which one do we choose? We choose max(array[0], array[1]), so this is the value that 
goes into the data structure at index 1. Then at index 2, we ask the same question and this time we have choices in the addends. We can add 
array[0] + array[2] since these are non-adjacent, or we can choose the non-adjacent sum at index 1 if this is greater than the sum. So at
index 2, we choose max(array[2] + array[0], maxNonAdjacentSum[1]). And there in lies the pattern.
maxNonAdjacentSum[i] = max(array[i] + maxNonAdjacentSum[i-2], maxNonAdjacentSum[i-1]). Dyanammic programming questions often have a single
solution that employs dyanammic programming thinking and so the only optimization is often whether we can improve the space complexity by
only storing the data structure size that we need instead of the data structure size which is equal to the input structure size. In this 
question we recogninze that at any point we need two values maxNonAdjacent[i-1] and maxNonAdjacent[i-2]. So the optimal initializes thes
two values and updates them as we go. If we do this our final answer will be the final maxNonAdjacent[i-1]. So in the code below, we use a
for loop starting from index 2 after initializing the answers for index 0,1. Then inside the for loop we access the required values and 
plug into the formula and we return the last value in the data structure. In the optimal solution, after initializing only the answers
for index 0, 1 using either an array of length 2 or two variables, we update these by recognizing inside the loop that the current answer
calculated with the formula becomes maxAdjacent[i-1] and the previous maxAdjacent[i-1] becomes the updated maxAdjacent[i-2] and we first
update maxAdjancent[i-2] = maxAdjacent[i-1] and then we can update maxAdjacent[i-1] = maxAdjacent[i]. This we know that when i = 
len(array) - 1, that final answer would have been updaated to maxAdjacent[i-1], inside the loop, so we return the the variable for this,
if we used variables, or the updateArray[1] if we use an array to store the two values. Using an array or even a custom data structure is
is the right thingg compared to using passed-around variables when in a recursion, and in dynammic programming makes for cleaner code. 

The key to this solution is realizing that the maxNonAdjacentSum[i] need not include array[i] in the addends, if maxNonAdjacentSum[i-1]
is greater than any sum that includes array[i]."""

"""The input array will be empty or contain only positive integers, ask interviewer about other edge 
cases. Otherwise, base case of i= 0 and i= 1 after which use formula to generate each maxSum at i"""
#O(n) time | O(n) space
def maxSubsetSumNoAdjacent(array):
    #edge cases, empty array and single element array
    if not len(array): #if array empty
        return 0
    elif len(array) == 1:
        return array[0]

    #initialize maxSums as the array and update second value
    maxSums = array[:] 
    maxSums[1] = max(array[0],array[1])

    #iterate through array and update maxSums
    for i in range(2,len(array)):
        maxSums[i] = max(maxSums[i-1], maxSums[i-2]+array[i])

    return maxSums[-1]


"""Same solution as earlier, only storing maxSums[i-1], maxSums[i-2]
and the greatest maxSums seen at each step of the iteration in order to improve space complexity"""
#O(n) time | O(1) space
def maxSubsetSumNoAdjacentI(array):
    #edge cases, empty array and single element array
    if not len(array): #if array empty
        return 0
    elif len(array) == 1:
        return array[0]

    second = array[0]     #maxSums[i-2] initialized at array[0]
    first = max(array[0],array[1]) #maxSums[i-1]

    for i in range(2,len(array)):
        current = max(first, second + array[i])
        second = first
        first = current

    return first


array = [75, 105, 120, 75, 90, 135]
print(maxSubsetSumNoAdjacentI(array))
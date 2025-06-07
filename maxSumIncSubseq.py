#O(n^2) time | O(n) space
def maxSumIncreasingSubsequence(array):
    sequences = [None for x in array]
    sums = array[:] #initialize sums as a copy of array, which is the least sum at any index
    maxSumIdx = 0 #initialize max sum as first element index, 0

    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0,i): 
            otherNum = array[j]

            #strictly increasing subsequence and greater sum
            if otherNum < currentNum and sums[j] + currentNum >= sums[i]:  #if two subsequences have the same max sum, we will keep the last
                sums[i] = sums[j] + currentNum
                sequences[i] = j
        if sums[i] >= sums[maxSumIdx]:#if two subsequences have the same max sum, we will keep the last
            maxSumIdx = i

    return [sums[maxSumIdx],buildSequence(array, sequences, maxSumIdx)]

def buildSequence(array, sequences, currentIdx):
    subsequence = []
    while currentIdx is not None:
        subsequence.append(array[currentIdx]) #first index appended is maxSumIdx then we look up previous index stored at maxSumIdx in sequences
        currentIdx = sequences[currentIdx] #in sequences, we stored the index of the previous number in the subsequence
    return subsequence[::-1] #return sequences before returning


array = [10, 70, 20, 30, 50, 11, 30]
print(maxSumIncreasingSubsequence(array))
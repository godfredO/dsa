"""Given an array, processes,  representing the memory used by processes on a virtual private server on AWS cloud. It is recommended that 
processes that consume a lot of main memory should be deleted. You can only delete processes that from a single contiguous segment of a 
given fixed size, m. The size of a contiguous segment is the number of contiguous processes in main memory. The question is to find the 
minimum amount of main memory used by all of the processes after you delete a contiguous segment of processes."""

"""The main idea behind the solutions below is that the totalMemory = RemainingMemory + DeletedMemory. As such RemainingMemory =
totalMemory - DeletedMemory. So, since totalMemory is a constant for any input memory array, we can minimimze RemainingMemory, by
maximizing DeletedMemory. As such the solutions below, find the maximum sum of a contiguous segement of memory of size m, and with the
maximized DeletedMemory value, we return totalMemory - DeletedMemory."""

"""So we start with the brute force approach. In this approach we loop over the numbers using indices, and at each index, we slice out an
array of size m. Because of this slice, the for loop goes up to range(len(processes) - (m-1)). This ensures that the last index in this 
loop will sum up to the last element in the processes array. With the slice done, we sum up the sliced sub-array, and keep track of the
maximum subarray sum. At the end we return the sum of the processes array minus the maximum subarray sum. The outer loop is O(n), the 
slice is O(n), the subarray sum is O(m) and the final sum is O(n), giving a overall time complexity of O(n*(n+m) + n) which is in the 
order of O(n^2). 

To optimize the brute force approach to a mid-optimal approach we realize that there is no need to slice the subarray before summing. So
insde the for loop (up to range(len(processes) - (m-1))), we start a while loop to add up m elements. So inside the for loop, we initialize
an index j which starts out equal to i, the outer loop current index, we initialize deleted variable, this will be the sum of m elements,
and addeds, which will count the number of elements we have added. So the while loop goes as long as addends is less than m. So we increment
the deleted variable with the value at j, then we increment addend, and we increment j. Outside the while loop, deleted will represent
the sum of an m-element sub-array starting with the outer loop index variable. So we keep track of the max subarray sum (of size m) by 
doing a maximum comparison with a variable maxContiguousMemory, which is initialized as 0 before the 0. At the end of the loop, this variable
will store the max subarray suum of size m, and we return sum(processes) - maxContiguousMemory, representing the amount of main memory used
by all of the processes after you delete a contiguous segment of processes. The outer loop is O(n) and the inner while loop that computes
sums of m elements without slicing is O(m), the final sum of the processes is O(n), giving O(n*(m) + n) which is in the order of O(nm).

The optimal solution takes care of the removes the sum of m elements by first calculating a baseMemorySum of the first m elements in the array,
using a while loop of range(m). Then, we initialize a runningMemorySum and a maxContiguousMemorySum as equal to this basemmorySum. So we loop
through the array starting at index m ie the value after the first m elements that were summed to yield baseMemorySum. Then at each index in 
the for loop we calculate an index to subtract as j -m, subtract the value at this index from the runningSum ie runningSum-= array[j-m]. After
this we add the element at the current loop index ie array[j] to the runningSum. This represents the amount of sum of contiguous m elements,
ending at index j. Then we track the maxContiguousSum by do a maximum comparison  of runningSum with maxContiguousSum. At the end we return
the maxContiguousSum. 

Assuming that m <= len(processes), we only need handle the edge cases of m = 0 and the edge case of len(processes) = 0. In the first case we
just return the sum of processes array since m=0 means we cant delete any processes. In the second case, we return 0."""

#O(n^2) time | O(1) space
# def minimizeMemory(processes, m):
#         if m == 0:
#             return sum(processes)
        
#         if not processes:
#             return 0

        
#         maxContiguousMemory = 0
#         for i in range(len(processes)-(m-1)): #O(n)
#             slice = processes[i:i+m]          #O(n)
#             maxContiguousMemory = max(maxContiguousMemory, sum(slice)) #O(m)
#         return sum(processes) - maxContiguousMemory
        

#O(nm) time | O(1) space
# def minimizeMemory(processes, m):
#         if m == 0:
#             return sum(processes)
#         if len(processes) == 0:
#             return 0

#         maxContiguousMemory = 0
#         for i in range(len(processes) - (m - 1)):
#             j = i
#             deleted = 0
#             addends = 0
#             while addends < m:
#                 deleted += processes[j]
#                 j += 1
#                 addends += 1
#             maxContiguousMemory = max(maxContiguousMemory, deleted)
#         return sum(processes) - maxContiguousMemory


#O(n) time | O(1) space
def minimizeMemory(processes, m):
    if m == 0:
        return sum(processes)
    if len(processes) == 0:
        return 0

    baseMemorySum = 0
    for i in range(m): #O(m)
        baseMemorySum += processes[i]

    runningMemorySum = baseMemorySum
    maxContiguousMemory = baseMemorySum
    for j in range(m, len(processes)): #O(n)
        idxToDelete = j - m 
        runningMemorySum -= processes[idxToDelete]
        runningMemorySum += processes[j]
        maxContiguousMemory = max(maxContiguousMemory, runningMemorySum)
    return sum(processes) - maxContiguousMemory #O(n)




#processes = [10,4,8,13,20]
#processes = [10,4,8,1]
processes = [4,6,10,8,2,1]
m = 3
print(minimizeMemory(processes,m))
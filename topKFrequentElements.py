"""Given an array nums and an integer k, return the k most frequent elements. You may return the answer in any order. k is in the range
of 1 to len(nums). It is also guaranted that the answer is unique.

Obviously we are going to have to count the elements so we will need a counts hashtable. Then after that we can generate a list of lists
[num:counts[num]] and this is also going to take linear time and linear space. Now the possible solutions differ in the next step. We can
sort all the lists in descending order according to the counts leading to O(nlog(n)). We could also use a heapSort algorithm (and therefore
a maxheap) to sort the intervals according to counts, and pop exactly k times leading to O(klog(n)). The optimal solution would be use a 
modified version of bucket sort to achieve linear time complexity. The way we would go about it, is to have the positions in the bucket sort 
array be the frequencies and at each position we store a list of the nums that have that frequency. Because the max frequency possible is 
equal to the length of the nums array, this bucket sort array will have the same length as the nums array. Then we loop from the back of the 
bucket sort array and add the elements in there to a final output array until we have added exactly k elements to the final output array."""



"""In-optimal solution"""
#O(nlog(n)) time | O(n) space
def topKFrequent( nums, k) :
    counts = {}
        
    for i in range(len(nums)):
        if nums[i] not in counts:
            counts[nums[i]] = 0
        counts[nums[i]] += 1

    #array = list(counts.items())   
    array = []
    for key in counts:
        array.append([key,counts[key]])
        
        array.sort(reverse=True,key=lambda x:x[1])
        
        output = array[:k]
        
        final = [interval[0] for interval in output]
        return final
            


"""Optimal solution"""
#O(nlog(n)) time | O(n) space
def topKFrequent( nums, k) :
    counts = {}
        
    for i in range(len(nums)):
        if nums[i] not in counts:
            counts[nums[i]] = 0
        counts[nums[i]] += 1

    #+1 because we have a buffer of 0 frequency, so that we freq 1 = index 1
    buckets = [[]for i in range(len(nums)+ 1)] 
    #in python dict.items() gives a dict object of (value,key)
    for num, freq in counts.items(): 
        buckets[freq].append(num)
    
    output = []
    for i in reversed(range(len(buckets))):
        for num in buckets[i]:
            output.append(num)
            if len(output) == k:
                return output


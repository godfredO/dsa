"""You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array 
to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return 
the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints: 1 <= nums.length <= 105 ; -104 <= nums[i] <= 104  ; 1 <= k <= nums.length

Hint 1 : How about using a data structure such as deque (double-ended queue)?
Hint 2 : The queue size need not be the same as the window's size.
Hint 3 : Remove redundant elements and the queue should store only elements that need to be considered.

So the brute force approach is to use left and right pointers to demarcate the first k elements, loop through them to find the maximum,
append to the result array, then shift the left and right pointers one step to the right and repeat the process. That is as we do an O(n)
iteration through the input, we perform an O(k) operation, leading to O(nk) time. The first thing to realize is that whenever we shift 
the window and do a new comparison, we are repeating a lot of work since we only remove one number and add a new number and the remaining
numbers were already compared in the previous window. Secondly this approach gets a Time Limit Exceeded on leetcode for very large inputs.

So could we improve our sliding window to better improve the time complexity?. We could use a max heap to obtain the maximum of k elements 
in logarithmic time instead of implementing a linear search algorithm ie we improve O(k) portion to O(log(k)). Now there are a couple of 
considerations. We will first initialize the heap with the first k elements of the input, obtain the maximum value by peeking, not popping. 
Why? Because to advance the window we will need to pop the value at the index just outside our new window (index 0, first time), which may 
or may not be the maximum of the first k elements. Then we add the element at the new ending index of our current window (index k first 
time). So to get the max value we just peek. Now the main crux of this approach. How do we pop based on index. Remember popping here is how 
we advance our left pointer. Well the answer is a little bit tricky. Say to advance our left pointer we need to remove the value at index 0,
then that value is only a problem if its also the max value, but if its not the max value, we can keep it for the moment. The work around
is to have a start index and if the identifying value of the heap's root node is less than or equal to the start index, we call heappop and 
remove the unnecessary nodes from our heap. This allows us to achieve logarithmic time. Now I will use the heapq module and an actual class 
implementation of a maxHeap. The implementation with the maxHeap class is basically re-engineering minHeapConstruction.py to get a maxHeap, 
you will see below. To use the in-built heapq module, the first question to ask is, how do we use heapq module to implement a max heap since 
its default is to implement a min heap. Well by negating the values. ie instead of supplying [value, index] of [1,0],[2,1] we supply [-1,0],
[-2,1] so that the minimum is -2 and then we re-negate to get the max value of 2. And how do we peek the root node of the max heap? Well we 
just look at the value at index 0 of the max heap  ie maxHeap[0][0] ( peeking the value and not the identifying index).

Now can we still do better? Instead of O(nk) or O(nlog(k)), can we get a linear O(n) time complexity? The surprising answer is yes!!!. To
do this we use a double ended queue ie deque. In python we actually use a deque when we need a queue. So how does a double ended queue help
us solve the question in linear time. A deque allows us to append / insert and pop from either end in constant time, so we can use this 
property to keep the elements on our deque in decreasing order. This way, the max value is always at the front of the deque.  

So we will be iterating through our input and adding the values to our deque, but before we compare with the element at the end of the 
deque to the new value. If the new value is equal or less than the element at the end of the deque, we append the new value to the end of 
the deque. If the new value is greater than the element at the end of the deque, we pop from the end of the queue before appending the new 
value, and we do this in a while loop to keep popping from the end of the deque as long as the new value is greater. Then we append the new 
value to our deque. Now in the actual implementation, we store indices instead of value on the deque, so what we append is the new value's 
index to thedeque. Before we go ahead and select the first element as the max value, we have to check if its inside our current window, so 
we say that if the left pointer index of our current window is greater than the index at the first position of our deque, we popleft() to 
remove that element from our deque since its not in our current window. We can use an if here, because if you go through the example you 
realize that we only ever remove one element, but you could also use a while loop which will run only once. 
Now since we will be adding values one at a time, we want to only add the first output value once we have 'added' (and maybe popped), the 
first k values. So say that if the right pointer of our window is greater than or equal to k-1, we can go ahead and add the leftmost value 
on the deque to our output and then increase the left pointer. This is because, since we are adding indices the first k elements will have 
indices 0,1,2, so we only add to our output when our right pointer is at least 3-1 ie index 2. And when we append, we know the deque contains 
indices, so we use the index to access the value. Whenever we update our output we increment the left pointer (which is essential when we are 
removing values not in our current window), meaning that left will be at 0 when we 'add' (and maybe pop) indices 0,1 and only when we get to 
index 2, do increment left after appending the leftmost value. When we get to index 3, we will make sure to pop all values less than than it
on the deque, then we check if the first index on our deque is even in the current window, if its not we pop from the front until it is. At
this point we know the first indeex on our deque represents the max value in our current window, so we append its value and increment the 
left pointer. Since each element in the input can only be pushed onto and popped out of the deque only once, the time complexity is O(n). 
And just like the heap solution we only ever remove the front value if its outside our current window.


This is a fixed width sliding window problem.
"""

"""Brute-force approach of using linear search to find max of k elements"""
#O(nk)- time | O(n) space - Brute force approach
def maxSlidingWindow(nums,k):
    result = []
    
    for endIdx in range(k-1, len(nums)):
        result.append(getWindowMax(nums, endIdx, k))
    return result

def getWindowMax(nums, right, k):
    left = right - (k-1)
    windowMax = nums[left]

    for i in range(left, right+1):
        if nums[i] > windowMax:
            windowMax = nums[i]
    return windowMax


"""Solution using a deque"""
from collections import deque
def maxSlidingWindow(nums, k):
	output = []
	left = 0
	queue = deque()

	for right in range(len(nums)):
		while queue and nums[right] > nums[queue[-1]]: #add values in montonically decreasing order
			queue.pop()
		queue.append(right)

		while left > queue[0]:   #check that current max value is actually in the current window
			queue.popleft()
		
		if right >= k - 1:      #handle the edge case of not adding to output unless we've gone through first k elements
			output.append(nums[queue[0]])
			left += 1


"""Solution using a maxHeap both heapq and class implementation"""
#O(nlog(k)) - time | O(n) space - Using heapq module
from collections import heapq
def maxSlidingWindow(nums, k):
	output = []
	maxHeap = []

	for i in range(k):
		maxHeap.append([-nums[i],i])    #negate values before adding to heap to achieve maxHeap with heapq

	heapq.heapify(maxHeap)
	output.append(-maxHeap[0][0])  		#negate before appending to get original values

	startIdx = 0
	for endIdx in range(k, len(nums)):
		while maxHeap and maxHeap[0][1] <= startIdx: #if current root is not in our current window
			heapq.heappop(maxHeap)

		heapq.heappush(maxHeap, [-nums[endIdx], endIdx] )     	#negate values before adding to heap 
		output.append(-maxHeap[0][0])							#negate before appending to get original values

		startIdx += 1
	return output

#O(nlog(k)) - time | O(n) space - Using my own heap class below
def maxSlidingWindow(nums, k):
	output = []
	firstK = []
	for i in range(k):
		firstK.append([nums[i],i])

	maxHeap = MaxHeap(firstK)
	output.append(maxHeap.peek()[0])
	
	startIdx = 0
	for endIdx in range(k, len(nums)):
		while not maxHeap.isEmpty() and maxHeap.peek()[1] <= startIdx: #make sure that root is in the current window
			maxHeap.remove()

		
		maxHeap.insert([nums[endIdx], endIdx])
		output.append(maxHeap.peek()[0])

		startIdx += 1 #increment the start or left Idx
	return output



class MaxHeap:
	def __init__(self,array):		
		self.heap = self.buildHeap(array)
	
	def isEmpty(self):
		return len(self.heap) == 0
	
	def buildHeap(self,array):
		lastParentIdx = (len(array) - 2 ) // 2
		for currentIdx in reversed(range(lastParentIdx + 1)):
			self.siftDown(currentIdx, len(array) - 1, array)
		return array

	def siftDown(self, currentIdx, endIdx, heap):
		childOneIdx = currentIdx * 2 + 1
		while childOneIdx <= endIdx:
			childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
			if childTwoIdx != -1 and heap[childTwoIdx][0] > heap[childOneIdx][0]:
				idxToSwap = childTwoIdx
			else:
				idxToSwap = childOneIdx
			if heap[idxToSwap][0] > heap[currentIdx][0]:
				self.swap(idxToSwap, currentIdx, heap)
				currentIdx = idxToSwap
				childOneIdx = currentIdx * 2 + 1
			else:
				return
	
	def siftUp(self,currentIdx, heap):
		parentIdx = (currentIdx - 1) // 2
		while parentIdx >= 0 and heap[currentIdx][0] > heap[parentIdx][0]:
			self.swap(parentIdx, currentIdx, heap)
			currentIdx = parentIdx
			parentIdx = (currentIdx  -1) // 2
	
	def remove(self):
		self.swap(0,len(self.heap) -1, self.heap)
		valueToRemove = self.heap.pop()
		self.siftDown(0, len(self.heap) - 1, self.heap)
		return valueToRemove
	
	def insert(self,value):
		self.heap.append(value)
		self.siftUp(len(self.heap) - 1, self.heap)

	def peek(self):
		return self.heap[0]

	def swap(self,i,j, array):
		array[i], array[j] = array[j], array[i]




nums = [1,-1]
k = 1
print(maxSlidingWindow(nums,k))
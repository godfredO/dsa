"""You're given a list of time intervals during which students need a laptop. These time intervals are represented by pairs of integers
[start, end], where 0<= start < end. No two students can use a laptop at the same time, but immediately after a student is done using a
laptop, another student can rent the same laptop. Eg if one student rents a laptop during time interval [0,2], another student can rent
the same laptop during any time interval starting with 2. The question is to write a function that returns the minimum number of laptops
that the school needs to rent such that all students will always have access to a laptop when they need one."""


class MinHeap:
    def __init__(self,array):
        self.heap = self.buildHeap(array)
    
    def buildHeap(self,array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx,len(array)-1, array)
        return array
    
    def siftDown(self,currentIdx,endIdx,heap):
        childOneIdx = currentIdx *2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx *2 + 2 <= endIdx else -1
            #sift based on ending times of intervals
            if childTwoIdx != -1 and heap[childTwoIdx][1] < heap[childOneIdx][1]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            
            if heap[idxToSwap][1] < heap[currentIdx][1]:
                self.swap(idxToSwap,currentIdx,heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return

    def siftUp(self,currentIdx,heap):
        parentIdx = (currentIdx - 1) // 2
        #sift based on ending times of intervals
        while currentIdx > 0 and heap[currentIdx][1] < heap[parentIdx][1]:
            self.swap(currentIdx,parentIdx,heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self):
        return self.heap[0]
    
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0,len(self.heap)-1, self.heap)
        return valueToRemove
    
    def insert(self,value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1 , self.heap)
    
    def swap(self,i,j,array): #swap positions
        array[i], array[j] = array[j] , array[i]

"""Optimal approach I. 
This approach is pretty similar to the Sort K-Sorted Array question in that we have a minHeap, and we have a for loop, and inside the for loop
whenever we remove the root node from the minHeap, we insert the element at the current loop index into the minHeap. The details of how the
two questions differ though. 

In this solution we first start by sorting the times array (list of lists) by the start times. This simulates taking reservations starting with 
the earliest reservation. The reason is that we unless we can re-use an existing laptop, we will need a new laptop for each reservations, so
we need to compare the start times of the reservations from the earliest start time to the end times of the reservations to see if the just 
ended reservation is ending at a time equal or less than the current start time in which case we can repurpose the laptop. To have access to the
earliest end times, we use a minHeap. Thus we have a for loop for our start times, and a minHeap for our endTimes and so we can compare.

We initialize the a minHeap starting with an array that contains only first interval in the sorted times array ie the interval at index 0. It
is important to have the first interval in an array to avoid errors ie [times[0]], minHeap([times[0]]). Since our minHeap starts with interval 
at index 0, just like the Sort K-Sorted Array question, the for loop index will start at index 1 ie just after the index of the last interval on 
the minHeap. Remember the for loop is looping over intervals sorted according to their start times.So In this solution we create a minHeap based 
on ending times of intervals ie we always want to know which of these rental reservations will end the earliest. This means that our heap gives 
us constant-time access to the interval with the lowest ending times which will be the peek value (root node). This way we can always know if the 
laptop being used by the peek value interval can be repurposed if it is ending before the next reservation.

Thus we iterate through the sorted times array, starting from the second interval and compare the starting time of the current interval in the 
for loop with the ending time of the peek value of the minHeap. If the current rental is starting before the peek value rental has ended it means 
we need one more laptop so,we insert the current interval into the minHeap. Again this is exactly like the Sort K-Sorted Array question where
we knew the correct value for any index in the sorted array was the minimum of the next k+1 elements, so whenever we removed from the array we
inserted the current loop index element into the array to maintain the k+1 elements for the next position. Here the are doing something similar
but the logic is different. In this solution we know we will need at least 1 element so we initialize our minHeap with the earliest start
reservation in terms of start time. So we can say here that the minHeap represents the laptops in use or the reservations that are currently
using laptops. Then we check if the next reservation in-line (based on start-time) needs a new laptop or can use the same laptop being used
by the minHeap root value (earliest aka minimum ending time). So if the start time of the current interval in the loop is less than the endtime
of the root of the minHeap, we know we need another laptop, so we append the current interval to the minHeap. If however the current start time
in the loop is greater than or equal to the endtime, then we can re-use that laptop, so we pop the root value before adding the current interval
from the loop to the minHeap. 

Now in the Sort K-Sorted Array, at the end of the for loop, we had a secondary loop to pop the remaining values of the minHeap and insert them
in sorted order into the  array. So when our for loop terminates, what do we do? We return the length of the minHeap. This is because since the
minHeap is holding all the reservations that are currently using laptops and we removed any reservation whose laptop could be re-purposed, it 
means that at the end of the algorithm the number of laptops needed is the len(minHeap) since this matches the maximum number of laptops ever in 
circulation. As such we return len(minHeap.heap), again it is essential to point to the heap array stored as an attribute on the minHeap class
instead of the class itself, otherwise len() will throw an error. """

#O(nlog(n)) time | O(n) space
def laptopRentals(times):
    if len(times) == 0:#edge case, if times array has no rental intervals
        return 0 #return 0 because no laptop is needed if no rentals exist
    
    times.sort(key=lambda x: x[0] ) #sort based on start times

    timesWhenLaptopIsUsed = [times[0]] #seed minHeap with first interval
    heap = MinHeap(timesWhenLaptopIsUsed)

    for idx in range(1,len(times)): #start looping from second interval
        currentInterval = times[idx]
        if currentInterval[0] >= heap.peek()[1] :#if rental start same/after peek end
            heap.remove() #remove peek interval to free up a laptop
        heap.insert(currentInterval) #in anycase, insert the current interval
    return len(timesWhenLaptopIsUsed) #use array since heap doesnt have len method



"""Approach Two. Solution two uses the observation that we only ever compare startimes and endtimes to figure out if we can free up an existing 
laptop or if we need to add another laptop, if our intervals are in sorted order. Specifically in solution one we first sorted the intervals 
based on their starting times and used a minHeap to allow constant time access to the lowest ending time for comparison. Thus in solution two we 
create a sorted list of startimes and endtimes and use these for our comparisons using the same logic as before. There are two versions of this 
algorithm . In the first version, after sorting through the start times and end times, we loop through both arrays using pointers but move the
pointers under different circumstances. The start times pointer represents an incoming reservation, the end times pointer represents an existing
reservation. So if the incoming reservation is starting before the current one has ended, we increment the number of laptops and advance only the 
start times pointer, to compare the next incoming reservation startime to the current reservation end time. If however, the incoming start time
starts same time as or after the current end time we advance both pointers. The intuition behind this is that, if all startimes are before the
end of the earliest end time, we would need as many laptops as there are starttimes. In the very least, for the earlest end time, we would need
as many laptops as startimes that start before it. If we encounter a starts time that starts after the earliest end time, we know that since the
start times array is sorted all the remaining start times will start after the earliest end time. So we are re-phrasing the question into this,
for a particular end time, how many startimes start before that end time has ended because that is how many laptops we will need to have in
circulation while the appointment with that particular end time is ongoing. If the current startime starts before the current end time has 
come to an end we add one more laptop in circulation and move the start time pointer to find the next starttime that also starts while the current 
end time is ongoing. As soon as we encounter a startime that starts at or after the current endtime, we know that we have all the laptops 
we need while that current end times appointment is ongoing, so we advance both pointers, to compare the next start time to the next end time. 
This solution also works in the same time and space complexity."""
#O(nlog(n)) time | O(n) space
def laptopRentalsI(times):
    if len(times) == 0:
        return 0

    startTimes = sorted([interval[0] for interval in times])
    endTimes = sorted([interval[1] for interval in times])

    laptops = 0 #initial number of laptops in circulation
    i, j = 0, 0 #startTimes iterator, endTimes iterator
    while i < len(startTimes):
        if startTimes[i] < endTimes[j]: #if a rental is starting before a rental has ended
            laptops += 1 #increase laptops in circulation
            i += 1 #then advance startTimes iterator
        else:#if a rental is starting at the same time as or after a rental has ended
            i += 1 #just advance startTimes iterator 
            j += 1 #free up a laptop in circulation by advancing the endTimes iterator to next
    return laptops #return the laptops in circulation

"""Second version of approach two where we decrease and increase numbrer of laptops in circulation based on the endtimes. In this solution, as 
we iterate through the start times array we increment the start times pointer and the used Laptops counter meaning that if there are no laptop 
re-use, we would have as many laptops as there are start times. However if we find that the current start time is equal to or greater than the 
current endtime, we decrement the laptops and move the end times pointer followed by the increase in laptop count and start times pointer 
which happens anyway. This way at the end, we have maximum number of laptops - the number of re-purposed laptops remaining as the minimum number 
needed."""    
#O(nlog(n)) time | O(n) space
def laptopRentalsII(times):
    if len(times) == 0:
        return 0
    
    startTimes = sorted([interval[0] for interval in times])
    endTimes = sorted([interval[1] for interval in times])

    usedLaptops = 0
    startIterator, endIterator = 0, 0

    while startIterator < len(times):
        if startTimes[startIterator] >= endTimes[endIterator]:
            usedLaptops -= 1
            endIterator += 1
        usedLaptops += 1
        startIterator += 1
    return usedLaptops


times = [
    [0, 2],
    [1, 4],
    [4, 6],
    [0, 4],
    [7, 8],
    [9, 11],
    [3, 10]
  ]

print(laptopRentalsI(times))

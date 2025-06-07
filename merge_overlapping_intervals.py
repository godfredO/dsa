"""The question give a list of interval where each interval is of form [start, end] and wants to return an array where overlapping 
intervals have been merged. In order to simplify the search for overlapping intervals we sort the array according to the start values
of the intervals. This way, all overalapping intervals will be adjacent to each other, and the start of the merged interval will appear
first in the sorted array, thus we only need worry about the end of the merged array. Then with the sorted interval array, we iterate
and compare if the next interval's start is equal to or less than the current interval's end ie do they overalap. If they do, we merge
them by updating the end of the current interval to maximum of the two ends of the overlapping intervals. If not, we add the current 
interval to the final output array. Thus we are using two pointers to iterate through the sorted array, the currentInterval pointer
and the nextInterval pointer and based on a comparison of the ends of these two intervals, we decide if they overalap or not. Since
we are assuming that we are not allowed to mutate the input array, we use sorted() to yield an sorted array and a output array. Also,
we initialize the currentInterval array outsside of the for loop, update it inside the for loop and use the for loop to choose 
the interval for the nextInterval pointer. This solution uses a coding technique of initializing a reference before adding the
reference to a data structure, here its an array but in the tournament question it is a dict, to allow update of the referred value."""
def mergeOverlappingIntervals(intervals):
    sortedIntervals = sorted(intervals, key=lambda x: x[0]) #first step is to sort according to start times

    mergedIntervals = []
    currentInterval = sortedIntervals[0]  #initialize currentInterval pointer first interval in sortedIntervals
    mergedIntervals.append(currentInterval) #proactively append current interval to output

    for nextInterval in sortedIntervals: #we could use ranges and loop from second interval to choose interval for next pointer
        _,currentIntervalEnd = currentInterval #unpack interval pointed to by currentInterval pointer to start, end
        nextIntervalStart, nextIntervalEnd = nextInterval #unpack interval pointed to by next poiner to start, end

        #at first run, we update the initialized current end to the same value but that's okay, simplifies code
        if currentIntervalEnd >= nextIntervalStart: #compare next start to current end , sorting allows us to this meaningfully
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd) #update current's end, current pointer stays put
        else:
            currentInterval = nextInterval #if not overlapping, advance current pointer since that interval already in output
            mergedIntervals.append(currentInterval) #then proactively append the new current interval to output, this why above line works

    return mergedIntervals #return the merged 

#Same algorithm, cleaner code
#O(n) time | O(n) space
def mergeOverlappingIntervals(intervals):
	sortedIntervals = sorted(intervals, key=lambda x:x[0])
	merged = [sortedIntervals[0]]
	
	
	for nextIdx in range(1, len(sortedIntervals)):
		prevStart, prevEnd = merged[-1]
		nextStart, nextEnd = sortedIntervals[nextIdx]
		
		if nextStart <= prevEnd:
			end = max(nextEnd, prevEnd)
			merged[-1][1] = end
		else:
			merged.append(sortedIntervals[nextIdx])
	return merged


intervals = [[1,2],[3,5],[4,7],[6,8],[9,10]]
intervalsII = [[1,2],[2,3],[1,5]]
print(mergeOverlappingIntervals(intervalsII))
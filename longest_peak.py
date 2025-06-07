"""
A peak is three numbers x,y,z in an array that follow one another in the array and for which x < y > z. This algorithm first finds a 
peak and then the index of the ends of the peak. The ends of the peak are not part of the peak itself. On the left its the point where 
the numbers stop being strictly increasing. For the right is the point where the numbers stop being strictly decrasing. After the ends 
are found, we compute the length of the peak and store it if its the longest peak length. Because of how Pythons zero index work to get 
the first member of the peak we add 1 to the left end index. To get the last member of a peak we use the right end to index into our array. 
This solution thus uses the left boundary, right boundary (which is a derivation of get neighbors from graphs) technique which is also used 
in some stack problems. So first find the tip of a peak, find the left boundary of the peak, find the right boundary of the peaak, then
calculate the length with the boundaries. Remember to test and use examples to verify logic. Note the loop conditions for the left / right
boundary while loops. Whenver you use a while loop you may need boundary conditions in addition to the progress conditions.
"""
def longestPeak(array):
    longestPeakLength = 0
    i=1  #tip from second to penultimate value, to left edge, right edge of peak tip
    longestPeak = []

    while i < len(array) - 1: #i finds a possible tip of the peak, from second to penultimate value, to left edge, right edge of peak tip
        isPeak = array[i-1] < array[i] and array[i] > array[i+1] #check if current index is the tip of the peak
        if not isPeak:
            i += 1 #advance in array
            continue #if not a peak, don't run the rest of the code inside loop, go back to top
        #if a peak is found, find the left boundary    
        leftIdx = i-2 #start from just outside of left value of peak tip
        while leftIdx >=0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -=1
        
        rightIdx = i+2
        while rightIdx <len(array) and array[rightIdx] < array[rightIdx-1]:
            rightIdx += 1
        
        currentPeakLength = rightIdx -leftIdx - 1 #calculate the peak length ie num of points in peak not the distance
        if currentPeakLength > longestPeakLength: #check for longest peak
            longestPeakLength = currentPeakLength #update the value reference by longestPeakLength variable
            longestPeak = array[leftIdx+1:rightIdx] #update the peek values, inclusive:exclusive
        i = rightIdx # after the length move forward in the list for a new peak

    return longestPeakLength, longestPeak


#Same solution, different coding
def longestPeak(array):
	longest = float("-inf")  #I used -inf out of habit, replace with 0
	
	for peakIdx in range(1,len(array) - 1): #use for loop to choose peak idx from index = 1 to index = len(array) - 2
		isPeak = array[peakIdx] > array[peakIdx - 1] and array[peakIdx] > array[peakIdx+1] #the peak is higher than both adjacents
		
		if not isPeak: #if current idx not a peak, continue in for loop
			continue
		
		leftIdx = peakIdx #initialize left boundary at current peak idx, 
		while leftIdx > 0 and array[leftIdx-1] < array[leftIdx]: #strictly decreasing as you go down and left from peak
			leftIdx -= 1
		
		rightIdx = peakIdx #initialize left boundary at current peak idx, 
		while rightIdx < len(array) - 1 and array[rightIdx + 1] < array[rightIdx]: #strictly decreasing as you go down and right from peak
			rightIdx += 1
	
		length = rightIdx - leftIdx + 1
		if length > longest:
			longest = length

	return longest if longest != float("-inf") else 0 #if longest initialized to 0 we dont need comparison
	

    


array = [1,2,3,3,4,0,10,6,5,-1,-3,2,3]
print(longestPeak(array))


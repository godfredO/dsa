#O(n^2) time | O(n) space
def diskStacking(disks):
    disks.sort(key=lambda disk:disk[2]) #sort by height, in-place
    heights = [disk[2] for disk in disks] #max height with disk at index at the bottom, initialized to height at index
    sequences =  [None for disk in disks] #list to store the last disk at the top of tower
    maxHeightIdx = 0 #index of maximum tower seen so far, to aid in buildSequence

    for i in range(1,len(disks)): #start at second desk because for first disk in sorted input, there is no other on top
        currentDisk = disks[i]  #bottom of current tower
        for j in range(0,i): #loop in sorted disks array for other disks that can go on top of current tower
            otherDisk = disks[j] #other disk that could go on top of current tower
            if areValidDimensions(otherDisk,currentDisk): #check if otherdisk can go on top of current disk
                if heights[i] <= currentDisk[2] + heights[j]: #if adding other disk max height ie heights[j] to current disk height is worth it
                    heights[i] = currentDisk[2] + heights[j] #we use an if statement instead of max(heights[i], currentDisk[2] + heights[j])
                    sequences[i] = j #we use if statement so that we can store index j at position i
        if heights[i] >= heights[maxHeightIdx]:
            maxHeightIdx = i

    return buildSequence(disks,sequences,maxHeightIdx)

def areValidDimensions(o, c):
    return o[0] < c[0] and o[1] < c[1] and o[2] < c[2] #all otherdisk dimensions are smaller than current disk dimensions

def buildSequence(array,sequences,currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])  #append disk stored at currentIdx
        currentIdx =  sequences[currentIdx] # update currentIdx to the index stored at currentIdx
    return list(reversed(sequence)) #reverse so disks are arranged top to bottm




disks = [
    [2, 1, 2],
    [3, 2, 3],
    [2, 2, 8],
    [2, 3, 4],
    [1, 3, 1],
    [4, 4, 5]
  ]

print(diskStacking(disks))
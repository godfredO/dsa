"""
Tags: Sliding Window ; Two Pass ; Medium

In this question, you are given a list of contiguous blocks on a street and a list of required buildings. The list of blocks contains
information on which buildings are present on each block. Each block is represented by a dictionary where the required buildings are keys
and the values are True/False for present at the block or not present at the block. The list of required buildings or reqs is simply a
list of names like gym, school, bank, which are also the keys in the block dictionaries. The question asks to write a function that returns
the block which optimizes the farthest distance one would have to walk to reach any of the required buildings. Thus for each block we need
to know the minimum distance to reach each required building and then choose the maximum distance out of these to represent the farthest one
would have to walk to reach all of the required buildings. The block with the lowest representative distance is the optimal one. The brute
force approach and the optimal approach look like the result of inverting matrices. In the brute force approach we iterate through the
blocks, and at each block we calculate the min req distance for each req and store the max distance for all reqs for the current block.
Calculating the nearest distance to a required building also requires iterating through the array giving a b*r*b time or O(b^2*r) time and a
O(b) space for the representative distance for the blocks.

In the optimal solution, we create create an array for each required building that stores the minimum distance for each block. Thus we will
have r arrays of b length. Then we simply loop through the req distances for each block, since each block will be at the same index, and
store the maximum distance to any req for that block. Finally, we choose the building with the minimum req distance. Thus to fill out the
b-length array for each req, we take O(br) time and O(br) space. In defining r arrays of length b, we actually use a matrix by mapping the
reqs to a lambda function whose expression is actually a user-defined function for calculating the req distances for each block. We can also
use a loop, initialize an array for each req, fill it up with the minimum distance to the req from each block and append the filled up array
to some array initialized outside the loop, so that at the end we have the matrix. Inside the user-defined function, we split the distance
calculation into 2*O(b) calculations first loop from left to right and then from right to left. Thus we use the decouple and repeat technique
to make the time better. The way it works is that we find the closestReqIdx for the current req and this value is initialized at infinity.
So we go from left to right in the list of blocks and if we find the current req in the current block then the current block idx becomes the
closest req idxx and will be used for the calculations for all the following buildings until the req is found at another block which will
become the new closestReqIdx. This means if the first block doesnt have the current req, then after the first pass its distance, which is
calculated with the initialized closestReqIdx , will be infinity until the second pass. Then in the second pass, we go from right to left,
doing the same thing and this time we store the minimum of the distance from closestReqIdx to current block and the value stored from the
first pass. This technique is also used in the minimum rewards question, where we change a n^2 to 2*n by looping from left to right then
right to left and update some stored value in the second pass. Once we have our matrix, the maximum required building distance, by looping
through the columns of the matrix, ie list of lists, where each column represents the req distance for the same block but for different reqs,
and returning an array which contains the maximum req distance for each block. Then with indices inside a loop, here we also use the map
function to map each list of in the matrix to a lambda function, and the expression of the lambda function is simply the value at distance i
for the block and we select this value and add to an array. Then we compute, still inside the loop, the maximum distance for all reqs for
block i. All these maxDistances are put into a list for the representative distance for each block. Finally with the representative req
distances for all blocks, we then get the idx of the block with the optimal or minimum distance.

To use map() to map an iterable's elements to a function that takes more than one input (and one input is the iterable element), the way
you do that is to define a lambda function that takes the iterable's element as input but the lambda function's expression is a function
(pre-defined) that takes the iterable element as input in addition to any other inputs.
"""

"""
The two-pass method is used to improve sliding window method in array_of_products.py also. In array_of_products
the sliding window leftRunningProduct and rightRunningProduct from each index was tracked and this was replaced
by two pass left pass and a reverse right pass through the array. In this question, the left right sliding
window to find the minimum req distance for a block can be replaced by right and left req distances for each
block.



"""

"""Brute-force approach. In this approach we iterate through the blocks array and at each block
iterate through the required buildings and for each required building we iterate through the blocks
array again to see the distance fromthe current building in the outer loop to the next instance of
said required building. The maximum distance to reach all required buildings is associated
with each block and the minimum of these max block distances is the answer."""
# O(b^2*r) time | O(b) space


def apartmentHunting(blocks, reqs):
    # to keep track of the max distance to required buildings at each block
    maxDistancesAtBlocks = [float("-inf") for block in blocks]  # for max comparsion

    # for every block, go through every requirement and for all of them, go back through all the blocks
    # and keep track, whenever you do find those requirment,if its the closest one to index i
    for i in range(len(blocks)):  # use indices to be able to calc distances
        for req in reqs:  # at each block loop through the required buildings
            closestReqDistance = float("inf")  # for min comparison, for each req initialize
            for j in range(len(blocks)):  # calculate distances to req buildings
                if blocks[j][req]:  # check if req is True at block in second loop
                    # for each req, we want the shortest distance from block i
                    closestReqDistance = min(closestReqDistance, distanceBetween(i, j))
            # for each block i , store the maximum closestReqDistance of all the reqs
            maxDistancesAtBlocks[i] = max(maxDistancesAtBlocks[i],
                                          closestReqDistance)  # update after each req
    return getIdxAtMinValue(maxDistancesAtBlocks)


def getIdxAtMinValue(array):  # helper method to return the index with the min value in array
    idxAtMinValue = 0
    minValue = float("inf")     # for currentValue < minValue and idxAtMinValue
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:  # want the index of the min distance value
            minValue = currentValue
            idxAtMinValue = i       # this is the actual return value
    return idxAtMinValue


def distanceBetween(a, b):
    return abs(a-b)  # the distance between two points is the absolute difference between them


"""Optimal solution. In this solution we do a r repeations of 2*O(b) traversals. That is for each req we calculate
the closest req distance for each block by doing two sweeps through the blocks array and store the answers in an array.
Thus we will have r arrays of length b, leading to br space. Then for each block index i we go through the distances array
for each req to find the max req distance for block i and store these block req distances in an array of length b. Finally
we find the minimum req distance and the index at which it occurs using the block req distances array and return the index
as the block that minimum req distance occurs. Thus precomputing the closestdistance for each req improves time complexity
while using more auxilliary memory"""
# O(br) time | O(br) space


def apartmentHunting(blocks, reqs):
    # matrix of req block closest distances
    minDistancesFromBlocks = list(map(lambda req: getMinDistances(blocks, req), reqs))  # [[],[],..]
    maxDistancesAtBlocks = getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks)
    return getIdxAtMinValue(maxDistancesAtBlocks)


def getMinDistances(blocks, req):  # for req, calcuate closest distances to nearest instance of req for each block
    # the least possible min distance is 0, when req occurs at blocks[i]
    minDistances = [0 for block in blocks]  # data structure to store intermediate result
    # needs to be +infinity in case req doesnt exist at block we get +infinity as req distance
    closestReqIdx = float("inf")

    # splitting the distance calculation into opposite directions reduces the O(b^2) repeated loop to 2*O(b) which is O(b)
    for i in range(len(blocks)):  # traverse from left to right, rightside req distance for block i
        if blocks[i][req]:  # if req is present at block i
            closestReqIdx = i  # then set the closest index at which req is found to i
        # calculate distance from closest req idx to block i
        minDistances[i] = distanceBetween(i, closestReqIdx)  # update min distances

    for i in reversed(range(len(blocks))):  # traverse from right to left, leftside req distance for block i
        if blocks[i][req]:  # if
            closestReqIdx = i  # set closest index at which req is found to i
        # calculate and compare to distances from previous loop to get the closest req distance for block i
        minDistances[i] = min(minDistances[i], distanceBetween(i, closestReqIdx))

    return minDistances


def getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks):  # O(br)
    # initialize the max block req distances for each block
    maxDistancesAtBlocks = [0 for blocks in blocks]

    for i in range(len(blocks)):  # select all req distances of block i, the find max
        # select closest req distances from matrix for each block i, length = len(reqs) for each column i
        minDistancesAtBlock = list(map(lambda distances: distances[i], minDistancesFromBlocks))
        # then compute and update the max distance from block i to the best req distances for each req
        maxDistancesAtBlocks[i] = max(minDistancesAtBlock)  # re-organize and find max

    return maxDistancesAtBlocks  # return array of max distances from each block to any of the best req distances


def getIdxAtMinValue(array):  # helper method to return the index with the min value in array
    idxAtMinValue = 0
    minValue = float("inf")
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            minValue = currentValue
            idxAtMinValue = i
    return idxAtMinValue


def distanceBetween(a, b):  # helper function of
    return abs(a-b)  # the distance between two points is the absolute difference between them


blocks = [   # list index is the location of the block; dict at index is block amenities
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": True,
        "school": False,
        "store": False
    },
    {
        "gym": True,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": True
    }
]
reqs = ["gym", "school", "store"]
print(apartmentHunting(blocks, reqs))

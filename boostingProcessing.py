"""
Tags: Sliding Window; Two Pass ; Medium

AWS data centers have multiple processors that perform computations, and the processors are placed in a sequence with their IDs denoted
by 1,2,..n. Each processor consumes a certain amount of power to boot up, denoted by bootingPower[i]. After booting, a processor uses
processingPower[i] of power to run the processes. For maximum utilization, the data center wishes to group these processors into clusters.
Clusters can only be formed of processors located adjacent to each other. Eg processors 2,3,4,5 can form a cluster, but 1,3,4 cannot.
The net power consumption of a cluster of k processors (i,i+1,.., i+k-1) is defined as:
net power consumption = maximum booting power among the k processors + (sum of processing power of processors) * k. A cluster of processors
is said to be sustainable if its net power consumption does not exceed a given threshold value powerMax. Given the booting power consumption
and the processing power consumption of n processors, denoted by bootingPower and processingPower respectively and the threshold value
powerMax, find the maximum possible number of processors which can be grouped together to form a sustainable cluster. If no such cluster
can be formed, return 0. Thus we are looking for the largest k, such that some adjacent cluster of k processors is sustainable. """

"""The only solution i have so far is the brute force approach, where we go through every cluster, determine the cluster's size and consumption
and if the consumption is less than or equal to the threshold, we compare the clusterSize to the maxNumber stored. And we return in the end,
maxNumber. So we have two for loops to choose the processorIdx for each cluster, the outer loop is for i in range(numProcessors) and the inner
loop is for j in range(i, numOfProcessors). We calculate the cluster size as j - i + 1.

Its giving permutation or backtracking where consumption is less than max power threshold. Maybe the beginning double for loop
can be decoupled into a two pass technique.

"""

# O(n^3) time


def findMaximumSustainableClusterSize(processingPower, bootingPower, powerMax):
    numOfProcessors = len(bootingPower)

    maxNumber = 0
    for i in range(numOfProcessors):  # consider all clusters
        for j in range(i, numOfProcessors):

            clusterSize = j - i + 1

            maxBoost = 0
            k = i
            while k <= j:  # for k in range(i,j+1)
                maxBoost = max(maxBoost, bootingPower[k])
                k += 1

            # for l in range(i,j+1) ; a single for loop for maxBoost and processingSum
            processingSum = 0
            l = i
            while l <= j:
                processingSum += processingPower[l]
                l += 1

            consumption = maxBoost + (processingSum * clusterSize)
            if consumption <= powerMax:
                maxNumber = max(maxNumber, clusterSize)

    return maxNumber


# bootingPower = [3,6,1,3,4]
# processingPower = [2,1,3,4,5]
# powerMax = 25

# bootingPower = [8,8,10,9,12]
# processingPower = [4,1,4,5,3]
# powerMax = 33

processingPower = [10, 8, 7]
bootingPower = [11, 12, 19]
powerMax = 6
print(findMaximumSustainableClusterSize(processingPower, bootingPower, powerMax))

"""The question gives an array of integers representing student scores in an exam and the teacher wants to give rewards out with the following
rules. Each student must receive at least 1 reward and if a student has a higher score than an adjacent student, the higher scoring student has
to receive more rewards than the lower scoring adjacent student and vice versa. It is important to note that there is no requirement for when
adjacent students have the same score, we only care about adjacent students' scores being greater than or less than the other.

In the naive approach, we initialize rewards array with 1 reward for each student, since this is the base case given by the teacher, then we 
start iterating starting from the second student, and comparing the current student's score to the previous student's score, thus for each 
student we only compare to the preceding neighbor hence why we start from the second student. If the current student has a higher score, we 
update their reward to previous student reward + 1. Thus as we iterate from left to right, if the current score > previous sccore, 
rewards[current] = rewards[previous] + 1. If this is not the case, the current score is less than or equal to the previous score. We don't
care if they are equal. So if the current score is not greater than the previous score, we only need to check if the current score is less
than the previous score or in other words if the previous score is greater than the current score. Now since this turn of event will affect
the number of all previously awarded rewards, we use an inner while loop to adjust the rewards assigned to the previous student. Because of
this, it is essential that when we use choose the index for the current student in a for loop, we store an index to the (first) previous 
student. This reference will be used for the backward iteration to adjust scores whenever we find that current score is not greater than 
previous. So in that case, we iterate backwards ie going left and check if the previous student has a greater score, in which case we update 
the previous students score to current student score + 1, if this update is greater than the previous student's current  score, that is
rewards[previous] = max(rewards[previous] , rewards[current] + 1). The reason for this is a follows. Suppose our array is [1,2,3,4,1],
the at index 3 our rewards array will look like [1,2,3,4]. When we get to index 5, the score of 1 is less than the previous score so we have
to adjust the previous score to max(4,2) ie the exisiting vs current + 1. If we choose current + 1 we would have undone all the good work we
did, hence the need to update only if the update gives a maximum rewards to the previous student. Also since we keep going backward to fix
rewards, we use a while loop and keep going as long as j, previous student index reference stored earlier, while j >= 0 and scores[j] >
scores[j+1]. Also make sure you remember to decrement j inside this while loop. This is effectively 1-d dynammic programming of sorts.

This is O(n^2) solution because for each student we potentially have to loop backwards, in a left boundary technique manner. However in 
questions where we have exponential time, we can usually improve complexity by using space. In fact in this question, we are using space 
anyway to store the rewards of the students, so the optimal solution decouples the forward iteration for current>previous from the backward
iteration for previous > current and use the rewards array to store the intermediate rewards.

The optimal solution is to actually decouple these two loops. To start, we still initialize 1 reward from each student. In the first loop, 
we go from left to right, starting from the second score and we compare the current score to the previous score. If the current score is 
greater than the previous score, we update the reward[current] = reward[previous] + 1. In the second loop we go from right to left, starting 
from the penultimate score and we compare the current score to the next score. If the current score is greater than the next score, we update 
rewards[current] = max(rewards[current], rewards[next] + 1). At the end of either we sum up all the rewards as the minimum number of rewards."""

# """Naive Solution
# Iterate forward through array and increment rewards if current score is 
# greater than previous score.if current is less than previous, iterate backwards
# to fix previous rewards as long as the previous is greater than current and the new
# reward update is greater than existing reward"""
# #O(n^2) time | O(n) space
# def minRewards(scores):
#     rewards = [1 for _ in scores] #initialize

#     #loop to compare current score to previous score
#     #so start loop from second score in scores array
#     for i in range(1,len(scores)): 
#         j = i-1 # store a referecne to the previous score index
#         if scores [i] > scores[j]: #if current score is greater than previous
#             rewards[i] = rewards[j] + 1 #current reward is previous reward plus 1
#         else: # current is less than previous, scores[j] > scores[i] ie scores[j] > scores[j+1] or equal we just do nothing if equal
#             #iterate backwards and fix all previous rewards
#             #keep going back as long as previous value j is greater than current value j+1
#             # i will at this point be a local min with a reward of 1
#             while j >=0 and scores[j] > scores[j+1]:#this condition is why we needed j defined
#                 rewards[j] = max(rewards[j], rewards[j+1] + 1)
#                 j -= 1 #decrement j to keep going backwards
#     return sum(rewards)

# """Optimal Solution I
# First, find local mins and then starting from them, expand outwards"""
# #O(n) time | O(n) space
# def minRewards(scores):
#     rewards = [1 for _ in scores] #initialize rewards array with minimum reward, 1
#     localMinIdxs = getLocalMinIdxs(scores) #get local mins using helper function
#     for localMinIdx in localMinIdxs: #for each local minimum
#         expandFromLocalMinIdx(localMinIdx,scores,rewards) #expand outwards using helper function
#     return sum(rewards)

# def getLocalMinIdxs(array):
#     if len(array) <= 1:
#         return [0] #if only one item, return index 0
#     localMinIdxs = []
#     for i in range(len(array)):
#         if i == 0 and array[i] < array[i+1]:
#             localMinIdxs.append(i)
#         elif i == len(array) - 1 and array[i] < array[i-1]:
#             localMinIdxs.append(i)
#         elif array[i] < array[i-1] and array[i] < array[i+1]:
#             localMinIdxs.append(i)
#     return localMinIdxs

# def expandFromLocalMinIdx(localMinIdx,scores,rewards):
#     leftIdx = localMinIdx -1 #starting point of leftward expansion, look at Largest Range question
#     while leftIdx >= 0 and scores[leftIdx] > scores[leftIdx + 1]: #stop if out of bounds or just past a peak
#         rewards[leftIdx] = max(rewards[leftIdx], rewards[leftIdx + 1] + 1)
#         leftIdx -= 1
#     rightIdx = localMinIdx + 1 #starting point of rightward expansion,from localMinIdx expand rightward, comparing new to previous
#     while rightIdx < len(scores) and scores[rightIdx] > scores[rightIdx - 1] : #if in bounds or just past a peak
#         rewards[rightIdx] = rewards[rightIdx -1] + 1 #no need for max check since going rightwarsd rewards will be assigned for first time
#         rightIdx += 1

"""Optimal Solution II, do two expansions, left to right and right to left. Onleft to right traversal, 
compare current to previous. On right to left traversal compare current to next score. Update if current is 
greater than previous or currentis greater than next. Since left to right is one first, no need for max check 
since its first assignnment. max check required for right to left traversal"""
#O(n) time | O(n) space
def minRewards(scores):
    rewards = [1 for _ in scores]
    #left to right expansion,compare current to previous score
    for i in range(1,len(scores)):
        if scores[i] > scores[i-1]: #if current is greater than previous
            rewards[i] = rewards[i-1] + 1 #this is the first time assigning, so we dont need a max check
    #right to left expansion, comparing current to next score
    for i in reversed(range(len(scores)-1)): #exclude last value in array, starting at penultimaate score
        if scores[i] > scores[i+1]: #if current is greater than next
            rewards[i] =max(rewards[i], rewards[i+1]+1)
    return sum(rewards)


scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
print(minRewards(scores))
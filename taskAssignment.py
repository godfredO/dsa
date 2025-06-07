"""The input to this question is an integer k, representing a number of works and an array of positive integers representing durations
of tasks that must be completed by the workers. Each worker is to complete two tasks and the array length is 2k. All workers work in 
parallel meaning the total time to complete all tasks is determined by the last worker to finish their pair of tasks.  The question asks
to write a function that returns the optimal assignment of tasks to each worker such that the tasks are completed as fast as possible.

The rationale for this solution is that, each worker's performance is mostly affected by the duration of the longest task assigned to them. 
Thus to optimize assignements, the worker assigned the longest task should also be assigned the shortest task. To do this we will need to 
sort the task durations in ascending order and pair up the last duration with the first duration in the sorted array. This is staightforward 
enough, and can be accomplished using a left and right pointer technique as long left < right. However the question asks to return pairs 
of indices of the taks durations instead of pairs of the durations themselves. Thus the crux of the question is how to sort the indices 
based on durations at each inde and return a pair of the indices that represent the pair of durations. Solution one and solution three use 
in-built Python functions sorted() and sort() and supply key=lambda k: tasks[k], to sort generated indices according to the task duration at 
those indices. Solution two explicitly writes functions to do handle to demonstrate the steps in this algorithm. This is because while solution 
I, II ask how can we sort indices according to the duration at those indices, solution II just stores the original indices before sorting them 
and then iterates through the sorted array and accesses the original indices from the hashmap, kind of like the nodes k distance away question, 
bfs solution. The first function maps durations to a list their indices that have that duration. Then uses sorted() to generate a list of sorted 
tasks and finally pairs the task indices in another function. This function works as by iterating through the sorted array a total of k times 
(left pointer), selects the indices list of that duration, pops one index off, calculates the right pointer index, access this duration from the 
sorted array, uses this duration to access its indices list from the map and pairs the two indices before appending to the output array. 
Because we calculate the right pointer, we only need run the for loop k number of times for the left pointer and since we know that the array 
length will always be 2k, we know we will pair up the correct indices in a O(k) loop. """


#O(nlog(n)) time | O(n) space
def taskAssignment(k, tasks):
	#sort the indices of tasks by the duration of tasks
	sortedTasks = sorted(range(len(tasks)), key=lambda k : tasks[k])
	pairedTasks = []
	
	l , r = 0, len(sortedTasks) - 1
	
	#use two pointers to pair up the longest task with the shortest task by theiir indices
	while l < r: #we are assured that tasks, is exactly 2k hence there its even and l should never equal r
		firstTask = sortedTasks[l]
		secondTask = sortedTasks[r]
		
		pairedTasks.append([firstTask,secondTask])
		
		l += 1
		r -= 1
		
	return pairedTasks


"""Same algorithm thinking wise, just a different way of going about the coding solution. This is the only solution if in a coding
interview one is not allowed to use in-built functions."""
#O(nlog(n)) time | O(n) space
def taskAssignmentI(k,tasks):
    pairedTasks = []
    taskDurationsToIndices = getTaskDurationsToIndices(tasks)
    sortedTasks = sorted(tasks) 
    

    for idx in range(k): #generate left index, for each worker
        task1Duration = sortedTasks[idx] #From sorted tasks, select first task duration of current pair, left index 
        indicesWithTask1Duration = taskDurationsToIndices[task1Duration] #choose index list of first task duration
        task1Index = indicesWithTask1Duration.pop() #pop one index from current task duration index list
        task2SortedIndex = len(tasks) - 1 - idx #calculate right index location in sorted task list, index of second task in pair
        task2Duration = sortedTasks[task2SortedIndex] #select second task duration of pair with calculated index
        indicesWithTask2Duration = taskDurationsToIndices[task2Duration] #choose index list of second task duration
        task2Index = indicesWithTask2Duration.pop() #pop one index from current task duration index list
        pairedTasks.append([task1Index,task2Index]) #pair them up and append to output array
    return pairedTasks


def getTaskDurationsToIndices(tasks):
    taskDurationsToIndices = {}

    for idx,taskDuration in enumerate(tasks):
        if taskDuration in taskDurationsToIndices:
            taskDurationsToIndices[taskDuration].append(idx)
        else:
            taskDurationsToIndices[taskDuration] = [idx]
    return taskDurationsToIndices


def taskAssignment(k, tasks):
	indices = list(range(len(tasks)))
	indices.sort(key= lambda k : tasks[k])
	
	l , r = 0, len(indices) - 1
	output = []

	while l < r:
		task = [indices[l], indices[r]]
		output.append(task)
		l += 1
		r -= 1
	return output

k= 3
tasks= [1, 3, 5, 3, 1, 4]
print(taskAssignmentI(k,tasks))
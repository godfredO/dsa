"""A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID. Each 
employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID]
= -1. Also, it is guaranteed that the subordination relationships have a tree structure. The head of the company wants to inform all the 
company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on 
until all employees know about the urgent news. The i-th employee needs informTime[i] minutes to inform all of his direct subordinates 
(i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news). Return the number of minutes needed to 
inform all the employees about the urgent news.

Example 1:
Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.

Example 2:
Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform 
them all.

Hint 1
The company can be represented as a tree, headID is always the root.
Hint 2
Store for each node the time needed to be informed of the news.
Hint 3
Answer is the max time a leaf node needs to be informed.

This is an application of the maxDepthOfBinaryTree.py. Here the edge from each supervisor to their direct subordinates is equally weighted 
by informTime[supervisor]. Also each employees direct manager is in the manager array. The root of tree is headID who has a manager[headID] 
of -1. So the question is asking what is the weighted depth of this organization tree. So the naive solution is to use breadth-first search
aka level order traversal to ask what is the time it takes for the news to reach every manager's's subordinates, starting from the headID
and we track the maximum time it takes for the news to reach a manager's subordinates. In this case, the answer is to return the maximum
time it takes for any manager to inform their subordianates. So we create a graph (tree) of our organization structure where each manager is 
mapped to a list of their direct subordiantes. Then to start bfs, we initialize the queue with (headID, informTime[headID]). Whenever we pop, 
a manager we first do a max comparison of the time it takes for the manager to inform his direct subordiantes from the time the news is 
became available. Then we go through the direct subordinates of the manager and to those sub-managers we say that the time for the news to
reach their subordinates is currentTime of their manager + their informTime to inform their subordiantes. At the end we return the max time
of any manager to inform their direct subordinates. 

Note that the lowest ranked employees have no direct subordinates. So, we could also use bfs search and re-phrase the question as the amount
of time it takes for the news to reach any employee. That in this approach we initialize the queue with (headID, 0) and when we add to the
queue, we add currentTime of their manager + informTime of their manager. This still yields the maximum weighted depth of the deepest leaf
node and thus the correct answer.

Now of course, since the question is based on maxDepthOfBinaryTree.py, we have can have a depth-first search version (pre-order) based on
the first / second bfs solution that improves space complexity. For the dfs based on bfs solution I, we ask each manager, what time takes
to inform all their direct subordinates, and we track the maximum time. In the dfs based on bfs solution II, we ask each employee, what is 
the time it took for the employee to receive the news after news break, and we track the maximum time. We start the preorder dfs from headID. 

"""
"""Bfs solution I - asking the max time for any manager to inform their direct subordinatees"""
#O(n) time | O(n) space
from collections import deque

def numOfMinutes(n, headID, manager , informTime ) :
    
    adj = {i:[] for i in range(n)}
        
    for sub, sup in enumerate(manager): #enumerate of manager array for direct subordinate, manager values
        if sup == -1: #don't add the headID's -1 manager, this is just a placeholder
            continue
        adj[sup].append(sub) #append the current direct subordinate to manager's adjacency list
        
    queue = deque()
    queue.append([headID, informTime[headID]]) #initialize queue with headID and time it takes to inform their direct subordinates
        
    maxTime = 0     #time it takes for any manager to inform their direct subordinates after news break
    while queue:
        sup, curTime = queue.popleft()
            
        maxTime = max(maxTime, curTime) #max time it takes current manager to inform their direct subordiantes after news break
            
        for sub in adj[sup]: #add current manager's subordinates and time it takes them to inform their subordiantes after news break
            queue.append([sub, curTime + informTime[sub]]) #time for their manager to inform them + time to inform their subordiantes
               
    return maxTime #max time it takes any manager to inform their direct subordinates from news break


"""Bfs solution II - asking the max time for any subordinate to receive information after initial news break"""
#O(n) time | O(n) space

def numOfMinutes( n, headID, manager, informTime) :

    adj = {i:[] for i in range(n)}  #initialize graph
        
    for sub, sup in enumerate(manager): #populate graph
        if sup == -1:
            continue
        adj[sup].append(sub)
        
    queue = deque() #initialize queue for bfs
    queue.append([headID, 0]) #initialize queue with headID and time it takes to receive information after news break
        
    maxTime = 0 #max time it takes for any manager/employee to receive the news
    while queue:
        sup, curTime = queue.popleft()
            
        maxTime = max(maxTime, curTime)  #max time it takes current manager employee to receive information after news break
            
        for sub in adj[sup]:#add current employee's direct subordinates and the time for them to receive the news 
            queue.append([sub, curTime + informTime[sup]]) #time for their manager to receive + time to inform their them
                
    return maxTime #max time it takes any manager / employee to receive the news from initial news break





"""Preorder Dfs solution I, at each manager we ask what is the time to inform all direct subordinates after news break. """
class Time:
    def __init__(self, value):
        self.value = value
    
def numOfMinutes( n, headID, manager, informTime) :

    adj = {i:[] for i in range(n)}  #initialize graph
        
    for sub, sup in enumerate(manager): #populate graph
        if sup == -1:
            continue
        adj[sup].append(sub)
    
    maxTime = Time(0)
    preorderDfs(headID, informTime[headID], maxTime, adj , informTime)
    return maxTime.value

def preorderDfs(employee, time, maxTime, adj, informTime):

    maxTime.value = max(maxTime.value, time)

    for directReport in adj[employee]:
        preorderDfs(directReport, time + informTime[directReport], maxTime, adj, informTime )


"""Preorder Dfs solution II, at each node we ask what is the time it took for the news to reach the employee. """
class Time:
    def __init__(self, value):
        self.value = value
    
def numOfMinutes( n, headID, manager, informTime) :

    adj = {i:[] for i in range(n)}  #initialize graph
        
    for sub, sup in enumerate(manager): #populate graph
        if sup == -1:
            continue
        adj[sup].append(sub)
    
    maxTime = Time(0)
    preorderDfs(headID, 0, maxTime, adj , informTime)
    return maxTime.value

def preorderDfs(employee, time, maxTime, adj, informTime):

    maxTime.value = max(maxTime.value, time)

    for directReport in adj[employee]:
        preorderDfs(directReport, time + informTime[employee], maxTime, adj, informTime )
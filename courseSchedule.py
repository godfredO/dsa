"""There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where 
prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai. For example, the pair [0, 1],
indicates that to take course 0 you have to first take course 1. Return true if you can finish all courses. Otherwise, return false.

This is a topological sort question ie if a cycle exists you can't finish ie if you have to finish course 0 before course 1 and you have to
finish course 1 before course 0 then which one do you complete first? So the first step is to create a graph here using a hashmap of 
{course: [prerequisites] }. Since we know the courses are from 0 to numCourses -1, we first fill our graph with courseIdx:[] for courseIdx in
range(numCourses). The reason is because in order for a valid topological sort to exist, there has to be no cycle, meaning there must be some
courses that don't have prerequisites, so we have to initialize the graph with all the courses otherwise if we used the prerequisites array,
there will be some courses that will never have prerequsiites and thus will not be added to the graph if we only use the prerequisites array.
We use this same logic in the outer loop of the dfs. So after initializing the graph with an empty array for each course, we loop through the 
prerequisites array and fill up the empty arrays by appending the prerequisites to each courseIdx key in the graph.


Now its time for the depth first search to detect a cycle. For this we need a visited set, a visiting set, and the graph. So we have our
outer loop in case the graph is disconnected. So we first check if the current courseIdx is in the visited set, meaning we already started
and completed a depth first search from it without ever finding a cycle, if so no need to start again. If not we call a dfs from it and it 
this dfs detects a cycle we return False for no we cant finish the courses. When this outer loop concludes without finding a cycle from any 
courseIdx, then we retutn True, for we can finish the courses.

So how do we detect a cycle. First we check that if the course is in the visited set then we return False. This base case actually prevents
getting stuck in a cycle due to later on calling dfs on a course's prerequisites. So if we call dfs on a visited node, we need to return
False immedaiately. If not , we add the current course to the visiting graph. Then we loop over its prerequisites. First we check the
cycle detection situation ie if the prerequisite is currently in the visiting set ie its currently on the recursive stack, then we detected
a back edge from a node to its ancestor hence a cycle, so we return True for a cycle. If not we start dfs from the prerequisite and if this
dfs detects a cycle it will return True so we need to return True to the ancestor dfs or to the outer loop. If the ancestor dfs receives 
True, it will bubble this up to the outer loop which will return False for no we cant finish the courses. When we complete the dfs for all 
prequisites, we remove the current courseIdx from visiting set and add it to the visited set and return False to the outer loop. """

def canFinish(numCourses, prerequisites):
    graph = {i:[]for i in range(numCourses)}

    for course, prereq in prerequisites:
        graph[course].append(prereq)
    
    visited = set()
    visiting = set()
    for courseIdx in range(numCourses):
        if courseIdx in visited:
            continue
        if containsCycle(courseIdx, visited, visiting, graph):
            return False
    return True

def containsCycle(nodeIdx,visited, visiting, graph):
    if nodeIdx in visited:
        return False
    visiting.add(nodeIdx)
    for prereq in graph[nodeIdx]:
        if prereq in visiting:
            return True
        if containsCycle(prereq, visited, visiting, graph):
            return True
    visited.add(nodeIdx)
    visiting.remove(nodeIdx)
    return False
    
        


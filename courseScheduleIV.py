"""There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where 
prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi. For example, the pair [0, 1] 
indicates that you have to take course 0 before you can take course 1. Prerequisites can also be indirect. If course a is a prerequisite of 
course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c. You are also given an array queries where 
queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not. Return a boolean array 
answer, where answer[j] is the answer to the jth query. We are assured that there will be no cycles.

Example 1
Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.

Example 2:
Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites, and each course is independent.

So the answer stated here is pretty simple and derives from both the courseSchedule.py and topological sort question in general. Basically, 
we create a graph of the courses and prerequisites ie graph[course] = [prerequisite1, prerequisite2, etc]. This step derives from
the courseSchedule.py question. Then we have an outer loop go through the queries, unpacks each query into possiblePrerequisite, course and 
starts a dfs from course to collect all of its prerequisites direct and indirect into a set, and then checks if possiblePrerequisite is in the 
set of prerequisites for course. If True, it means possiblePrerequisite is in the set ie its a direct or indirect prerequisite of course. If 
False, it means its neither a direct nor indirect prerequisite of course. Either way we store the corresponding boolean in the output array. 
Now in order not to collect prerequisites for the same course whenever we are trying to verify a new possiblePrerequisite, we initialize a
hashtable collected that stores the prerequisites set the first time we meet a course, after that we just use this stored set to verify other
possiblePrerequisites. 
In order to collect all the prerequisites for a course we use a simple dfs. We initialize a visited set, since we know that we will visit 
every prerequisite in the dfs. Then in the dfs function, we first check if the course has already been visited in which case we return ie to 
avoid calling dfs on the same prerequisite over and over again. Otherwise, we go through all the prerequisites of the current course, using 
the graph and call the dfs function on each prerequisite. At the end of the for loop, we add the current course to the 
visited set. This will have the effect of adding the prerequisites that have no prerequisites themselves first and afterwards, we add a 
course after we have gone through and satisfied all of its prerequisites. And since we are assured that there will be no cycles we don't
need to use a visiting set to track the courses that are currently on the call stack. The pattern of going through all prerequisites before
adding a course to the visited set is one of the two basic topological sort pattern parts and that is what we use here. So if we had cycles
we would also use the visiting set as part of the topological sort pattern but we don't need that here. 

So in this simplified version, the difference between the topological sort pattern and the numberOfConnectedComponents.py pattern is when we 
add a node to visited. When trying to count the number of groups, we add a node to visited before going throug its edges as a way of avoiding 
repeated work or getting stuck in a cycle, both of which lead to interminable loops. When trying to get the topological ordering, and there
is no cycle, we only use the visited set pattern, and we add a node to the visited set after we have gone through its edges. If there is a 
cycle, then we need to detect the cycle using the visiting set as a way to tracking whats on the recursive stack. So at this point, there are
three primary patterns for dfs, numberOfConnectedComponents, cycleInGraph, topologicalSort patterns.
"""


def checkIfPrerequisite(numCourses, prerequisites, queries) :
    graph = { course:[] for course in range(numCourses)}
        
    for prereq, job in prerequisites:
        graph[job].append(prereq)
        
    connected = {}
    output = []
    for pair in queries:
        u, v = pair
        if v not in connected:
            visited = set()
            getConnected(v, visited, graph)
            connected[v] = visited
        output.append(u in connected[v])
    return output

    
def getConnected(course, visited, graph):
    if course in visited:
        return
    for prereq in graph[course]:
        getConnected(prereq, visited, graph)
    visited.add(course)
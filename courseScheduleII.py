"""There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where 
prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai. For example, the pair [0, 1], 
indicates that to take course 0 you have to first take course 1. Return true if you can finish all courses. Otherwise, return false.
Example 1: Input: numCourses = 2, prerequisites = [[1,0]] Output: true Explanation: There are a total of 2 courses to take. To take course 1 
you should have finished course 0. So it is possible.
Example 2: Input: numCourses = 2, prerequisites = [[1,0],[0,1]] Output: false Explanation: There are a total of 2 courses to take. To take 
course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
Example 3: Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]] Output: [0,2,1,3] Explanation: There are a total of 4 courses to 
take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:Input: numCourses = 1, prerequisites = [] Output: [0]

So this is the similar question to courseSchedule.py and follows the exact same logic, so first review courseSchedule.py. The only difference 
is that you have to return an actual topological sort ordering of the course. So the only additions we make to couseSchedule.py is that we have 
a topological sort array initialized to an empty array outside the outer loop, and we pass this array into the containsCycle() dfs function. 
Then inside the dfs containsCycle(), after we remove the course from the visiting set, we append it to the topological sort array before we
add the course to the visited set, then we return False, either to a recursive dfs call or the outer loop. In the outer array, if we receive 
true from containsCycle() we immediately return an empty array for the ordering, otherwise upon completion of the outer for loop, we return the 
filled topological sort array. In otherwords, this question is exactly like topologicalSort.py (and topologicalSortII.py), meaning a valid 
topological ordering exists if there are jobs or courses that dont have prerequisites, and the topological sort should start with those. 
Otherwise if there is a cycle, there is no valid topological ordering. So for the jobs/courses with no prerequisites, containsCycle() will try 
to access graph[course] which will go no where since its an empty array, so those courses are added first. topologicalSort.py and 
topologicaSortII.py create nodes, but here we just use an adjacency graph. """

#O(v+e) time | O(v) space
def findOrder(numCourses, prerequisites):   
    graph = {course:[] for course in range(numCourses)}
    for course, prereq in prerequisites:
        graph[course].append(prereq)
        
    topologicalSort = []
    visited = set()
    visiting = set()
    for course in range(numCourses):
        if course in visited:
            continue
        if containsCycle(course, visited, visiting, graph, topologicalSort):
            return []
    return topologicalSort

       
def containsCycle(course, visited, visiting, graph, topologicalSort):
    if course in visited:
        return False
    if course in visiting:
        return True
    visiting.add(course)
    for prereq in graph[course]:
        if containsCycle(prereq, visited, visiting, graph, topologicalSort):
            return True
    visiting.remove(course)
    topologicalSort.append(course)
    visited.add(course)
    return False


numCourses = 4 
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(findOrder(numCourses, prerequisites))
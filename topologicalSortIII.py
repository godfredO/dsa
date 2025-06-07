"""This is a rewriting of the topological sort quesion on algosexpert.io, using dfs just like in 
topologicalSortII.py but in a much simpler way using the style in learned in courseScheduleII.py and 
courseSchedule.py. In this rewriting I just use a an adjacency hashmap for my graph instead of the 
verbose method used in topologicalSortII.py. One day try search the Topological Sort tag on leetcode 
(via google) and solve the medium questions then the hard questions. Leetcode provides description of
solutions so that you can read them and note the essential points and how the topological sort algorithm, 
based on depth-first search, is used in solving those questions."""

def topologicalSort(jobs, deps):
    graph = {}
    for job in jobs:
        graph[job]= []

    for prereq, job in deps:  # in a topological sort, the edge goes from the job to the prerequisite
        graph[job].append(prereq)

    validOrdering = []
    visited = set()
    visiting = set()
    for job in jobs:
        if job in visited:
            continue
        if containsCycle(job, visited, visiting, validOrdering, graph):
            return []
    return validOrdering


def containsCycle(job, visited, visiting, validOrdering, graph):
    if job in visited:
        return False
    visiting.add(job)
    for prereq in graph[job]:
        if prereq in visiting:
            return True
        if containsCycle(prereq, visited, visiting, validOrdering, graph):
            return True
    visiting.remove(job)
    validOrdering.append(job)
    visited.add(job)
    

jobs = [1,2,3,4]
deps = [[1,2], [1,3],[3,2],[4,2],[4,3]]
print(topologicalSort(jobs, deps))
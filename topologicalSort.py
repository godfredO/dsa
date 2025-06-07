""" You're given a list of arbitrary jobs that need to completed; these jobs are represented by distinct integers. You are also given a list
of dependencies. A dependency is represented as a pair of jobs where the first job is a prerequisite of the second [prerequisite, dependency]. 
In other words, the second job depends on the first one and can only be completed once the first job is completed. The question asks to write 
a function that takes in a list of jobs and a list of dependencies and returns a list containing a valid order in which the given jobs can be 
completed. If no such order exists, the function should return an empty array. Now this question can be asked in other ways, instead of jobs it 
can be college classes that have prerequisites or computer programs that have prerequisites and dependencies. Whatever the flavor the question 
is asking if there is some order in which we can complete the tasks or classes such that all prerequisites of any task or class is completed
before the task or class itself is done? 

A couple observations first is that a task or job can have multiple prerequisites and a job can have multiple dependencies. Eg in the 
dependencies array = [[1,2], [2,3], [1,3]], task 1 has two dependencies ie 2 and 3. Similarly task 3 has two prerequisites ie 1,2. This means 
we can only do task 3 only after doing task 1 and task 2. Since task 2 has only one dependency ie task 1, we can only do task 2 after 
completing task 1. So the only valid ordering is [1,2,3], since both of task 3's prerequisites occur before it, task 2's singular prerequisite 
comes it, and task 1 has no prerequisites so we can do it right away. So this example shows a couple of key observations which is that, we have 
to have tasks that have no prerequisites and we have to start with those. So under what conditions can we not complete the tasks? When all jobs
have prerequisites ie there is a cycle. Eg [[1,2], [2,3], [3,1]]. In this dependencies array, task 2 depends on task 1, task 3 depends on task
2, task 1 depends on task 3. So what do we start with? We cant start with task 1 until we are done with task 3, we cant start task 3 until we
are done with task 2 and we cant start task 2 until we are done with task 1. That is if we represented the dependencies array as a graph,
the existence of a cycle would denote no valid topological ordering or sorting.

Now there are two different approaches to this question, the zero- prerequisite approach and the cycle approach. Each approach starts off by 
creating a graph out of the dependencies array but the way the graph is structured differs. The coded solution here is the cycle approach were 
we create the graph is such a way as to detect cycles. It is advisable to look at the other solution first since that is simpler to understand. 
It is also advisable to review the Cycle In Graph question since this is an application of detecting cycles in graphs.

So clearly we will need to create a graph of jobNodes. This is actually the first step of the solution ie calling createJobGraph(jobs,
dependencies) before the main function described above. This method createJobGraph(jobs, dependencies), first creates a graph by calling
the initialization method fof the JobGraph class. The JobNode node object contains attributes, job, prereqs, visited and visiting. These 
attributes store the job name or number, job's prerequisites, a boolean for the node has been visited in a dfs, and a boolean for if the node 
is still on the recursive stack during dfs. The JobGraph class itself is similar to the other solution's Job Graph class. The initialization 
method of the JobGraph class takes in a list of jobs which is an input to the question in addition to the dependencies array. This 
initialization method's attributes includes a self.nodes attribute which is an array, a self.graph attribute which is a hashtable, and then a 
loop which goes through the list of jobs and calls the addNode() method with each job as input ie self.addNode(job). Now the purpose of the 
graph hashtable is to map a job's name (number) to the node object ie {1:JobNode(1)}. So when addNode() receives a job, this is the first 
thing it does, creates a node and map it to its name (number) in the graph hashtable ie self.graph[job] = JobNode(job). Next it appends the 
node object created to the self.nodes array using the mapping that was just added ie self.nodes.append(self.graph[job]). So this is all what 
the initialization method does with a list of jobs ie create a hashtable map {job:JobNode(job)} and adds to a nodes array.

Next in createJobGraph() we add prerequisites to the nodes in the graph. At this point we would have an instance of the JobGraph class, with 
jobNodes in the nodes array and graph hashtable. So in the next step we go through the dependencies array, unpack each subarray ie 
[prereq, job] and for each prereq,job we call graph.addPrereq(job, prereq) on the JobGraph instance, graph. This addPrereq() method on the 
JobGraph class, takes in a job and prereq, accesses the jobNode and prereqNode using the graph hashtable, and appends the prereqNode to the 
jobNode's prereq attribute array. To avoid errors, we have a separate method fetch the nodes from the graph hashtable, first checking if 
the nodes even exists, it not it calls addNode() before returning the node. That is we have another method getNode(job) which is used by 
addPrereq to fetch the jobNode and depNode. This method first checks if the passed job's key is in the graph hashtable. If it is, we return 
the node by accessing the graph hashtable.

The main logic of this solution (checking for cycles), is called getOrderedJobs(). This function takes the graph as the only input. We first 
initialize the output, the access all the nodes in the graph using the nodes attribute array ie nodes = graph.nodes. The reason is that we
are going to do a depth first search for cycles (review the Cycles In Graph question) and as such we need an outer for loop to ensure that
we visit every node in the case of a disconnected graph. So while the nodes array is non-empty, we will keep running the depth first search.
So inside of the while loop we pop a node and call a dfs helper function on this node and store the returned boolean in a variable
called ie containsCycle =  depthFirstSearch(node, output). This is because depthFirstSearch wil return True if it finds a cycle in the cause 
of traversal, otherwise False. As such if we pop all nodes of the nodes array, start a dfs for each of them and no dfs returns True, then
when the while loop terminates (due to nodes being empty), we return the output array. However, the first time the dfs returns True ie a 
cycle has been found, getOrderedJobs() returns an empty array. depthFirstSearch also populates the output array.

Inside depthFirstSearch(node, output), the first thing we check is if a node has been visited. If node.visited, we return False to 
getOrderedJobs because it means we previously did a dfs on a node and didnt find a cycle so we immediately return False. Next we check if
node.visiting is True ie is the node currently on the recursive stack, in which case we have a cycle and we return True to getOrderedJobs().
If the node wasnt previously visited and is not currently on the recursive stack, we mark the node as now in the recursive stack ie,
node.visiting = True. Then we loop through its prereqs ie for prereq in node.prereqs and for each of these prereqs we call the dfs
ie depthFirstSearch(prereq, output), and store the returned boolean in a containsCycle variable. If any of the prereqs dfs returns a True,
we return a True to getOrderedJobs ie containsCycle = depthFirstSearch(prereq, output). If containsCycle: return True. Otherwise when this
for loop terminates because we started a depth first search for each prereq and didnt find a cycle, we mark the node as visited and take it
off the recursive stack ie node.visited = True , node.visiting = False. Then we append the job to the output array since we didnt find a 
cycle starting from the job node. This solution has the effect of going through all of a job's prereqs until we find a prereq that itself
doesnt have any prereqs ie a job with 0 number of prereqs , add it to the output, then come back to the depenedency that made the call if
if the just added job was the last or only prereq, the for loop would terminate and that job will also be added. Finally after adding the 
job to the output, we return False which will be returned to either from a dfs call from another job or a dfs call from getOrderedJobs.

This is such an interesting application of Cycles In Graph. When determining cycles, we need both visiting and visited. When visiting is 
True, we know we have found a cycle, if visited is True we know we don't have a cycle. If we only ever hit visited for every node, then
there are no cycles, but we can't make a judgement from only one False test. However if we hit visiting even for one node and every other
node hits visited, we know we have a cycle and we can make a judgement from one True test. Thus when visited is True it means we did not
detect a cycle starting from this node. When visiting is True it means we found a cycle from this node and hence a cycle in the graph as 
a whole.


"""



class JobNode:
    def __init__(self,job):
        self.job = job  #job is int
        self.prereqs = []  #list of prereqs
        self.visited = False #at first we havent visited any nodes
        self.visiting = False #for nodes still being visited, because we are going through its prereqs

class JobGraph:
    def __init__(self,jobs):
        self.nodes= []  #to iterate through jobs
        self.graph = {} #maps jobs (integers) to their nodes, for constant time access
        for job in jobs:  #loop throg
            self.addNode(job)

    def addNode(self, job):
        self.graph[job] = JobNode(job)  #create job node and add it as the value to its same key in jobgraph
        self.nodes.append(self.graph[job]) #add the job node created to nodes in jobgraph for easy iteration
    
    def addPrereq(self,job,prereq):
        jobNode = self.getNode(job)
        prereqNode = self.getNode(prereq)
        jobNode.prereqs.append(prereqNode)

    def getNode(self,job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]  

#O(j+d) time | O(j+d) space
def topologicalSort(jobs,deps):
    jobGraph = createJobGraph(jobs, deps) #create a graph for input jobs and prereqs
    return getOrderedJobs(jobGraph)


def createJobGraph(jobs, deps):
    graph = JobGraph(jobs)  #create job nodes and add to graph
    for prereq, job in deps: #adding edges
        graph.addPrereq(job, prereq)
    return graph
        
def getOrderedJobs(graph):
    orderedJobs = []
    nodes = graph.nodes
    while len(nodes):
        node = node.pop()
        containsCycle = depthFirstTraverse(node,orderedJobs) #this function updates orderedJobs as well as returns True or False
        if containsCycle:
            return []
    return orderedJobs

def depthFirstTraverse(node,orderedJobs):#recursive function
    if node.visited:
        return False
    if node.visiting:
        return True #there is a cycle
    node.visiting = True
    for prereqNode in node.prereqs:
        containsCycle = depthFirstTraverse(prereqNode,orderedJobs)
        if containsCycle:
            return True
    node.visited = True  #mark as visited
    node.visiting = False #we're done visiting
    orderedJobs.append(node.job)
    return False

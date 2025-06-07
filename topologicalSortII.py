"""This is the zero-prerequisites approach to the topological sort question. Simply put to have a valid topological sort, a task or job or
class can only be started if all of its prerequisites have been completed. As such in this approach, we always start with all the jobs that
have 0 prerequisites since we are allowed or able to start those right away.

So clearly we will need to create a graph of jobNodes. This is actually the first step of the solution ie calling createJobGraph(jobs,
dependencies) before the main function described above. This method createJobGraph(jobs, dependencies), first creates a graph by calling
the initialization method fof the JobGraph class. The initialization method of the JobGraph class takes in a list of jobs which is an 
input to the question in addition to the dependencies array. This initialization method's attributes includes a self.nodes attribute which 
is an array, a self.graph attribute which is a hashtable, and then a loop which goes through the list of jobs and calls the addNode() 
method with each job as input ie self.addNode(job). Now the purpose of the graph hashtable is to map a job's name (number) to the node 
object ie {1:JobNode(1)}. So when addNode() receives a job, this is the first thing it does, creates a node and map it to its name (number) 
in the graph hashtable ie self.graph[job] = JobNode(job). Next it appends the node object created to the self.nodes array using the mapping 
that was just added ie self.nodes.append(self.graph[job]). So this is all what the initialization method does with a list of jobs ie create 
a hashtable map {job:JobNode(job)} and adds to a nodes array.

Next in createJobGraph() we add the dependencies to the nodes in the graph. At this point we would have an instance of the JobGraph
class, with jobNodes in the nodes array and graph hashtable. So in the next step we go through the dependencies array, unpack each subarray
ie [job, dep] and for each job,dep we call graph.addDep(job, dep) on the JobGraph instance, graph. This addDep() method on the JobGraph
class, takes in a job and dep, access the jobNode and depNode using the graph hashtable, and appends the depNode to the jobNode's 
dep array, and the increments the depNodes.numPreReqs attribute by 1. To avoid errors, we have a separate method fetch the nodes from the
graph hashtable, first checking if the nodes even exists, it not it calls addNode() before returning the node. That is we have another
method getNode(job) which is used by addDep to fetch the jobNode and depNode. This method first checks if the passed job's key is in the
graph hashtable. If it is, we return the node by accessing the graph hashtable. If its not we call addNode(job).

Anyway with the graph created, how do we find all nodes with 0 prereqs. Simple inside a filter() with a lambda function, we loop through the
nodes array attribure of the graph instance, check the numPreReqs on each node and if it that attribute is 0, we add it to the stack.
In the code we use a a filter() wrapped in a list() constructor. Anyway we loop thorough the noes in graph.nodes using the filter() function
where we map every node to a lambda function that takes the node as an input and the expression inside the lambda function is a conditional
expression ie if the prereq attribute on the job node is 0. Since this is a conditional expression it will return a boolean and we use 
filter() to extract the nodes that return True and store those in a list. Thus the filter() function is pretty important here, without it we 
would store all the booleans in the list() but that not what we want; we want nodes not booleans and not all nodes either, just the ones
that returns true from the conditional expression.
So in this solution we create a Job node whose attributes are the job, its dependencies and the number of prerequisites. eg in the deps 
array [[1,2], [2,3], [1,3]] the JobNodes will be JobNode(1): job= 1, deps=[2,3] , numPreReqs = 0; JobNode(2): job=2, deps=[3], numPrereqs=1,
and finally JobNode(3): job=3, deps=[], numPreReqs = 2. The core algorithm here is pretty straightforward. We start by collecting all 
jobNodes where numPreReqs is 0 and add them to a stack. This stack is only going to hold jobs with 0 preReqs. Once we have the initial list 
of nodes with 0 prerequisites, we can start the dfs. So inside the dfs while loop, with the condition to keep running as long as the stack is 
non-empty, we pop a node off the stack, append its job name ie JobNode.job to the output array and then call pass it and the stack to another 
helper function removeDeps(node, stack), and the purpose of this function is to go through the dependencies on the node ie node.deps, pop one 
dependency node at a time, and with the dependency node, access that node's numPreReqs attribute and decrement the count by 1, and if that 
decrement step reduces the numPrePreqs on that node to 0, we add it to the stack. So for example in the example dependency array above, the 
stack will have start with only JobNode(1) since its the only one that that has node.numPreReqs = 0. So inside the while loop we would pop it 
off, add 1 to the output array, then pass 1 and the stack to the removeDeps(1,stack) helper function which will go through 1's deps 
ie [JobNode(2),JobNode(3)], pop JobNode(3) off, go to that node and decrement is numPreReqs by 1 ie JobNode(3).numPreReqs = 2-1 = 1 and then 
check if JobNode(3).numPreReqs == 0, its not so we dont add it to the stack at this time. Next we pop 2 of of 1's deps ie 1's deps will now be 
empty. So with JobNode(2) we decrement the numPreReqs ie JobNode(2).numPreReqs = 1-1=0 , we check if its equal to 0 , which it is, so we add 
it to the stack. So when execution returns to the main function, the stack now has JobNode(2) on it, as such the stack is non-empty so we enter 
the while loop, pop off the stack, append two to the output array ie output = [1,2] at this point, the we call removeDeps(JobNode(2), stack), 
which will end up popping JobNode(3) off 2's deps, decrementing its numPreReqs which will now be 0 so JobNode(3) is added to the stack. When 
execution returns to the main function, JobNode(3) will be on the stack, and after its added to the output, the call to removeDeps will yeild
nothing since 3 has no dependencies. So it should be mentioned that removeDeps() is just a while loop that keeps popping off the node's 
dependency array till its empty and with each pop, decrements the popped dependecies' numPreReqs attributes before checking if that attribute 
is equal to 0 in which case it adds to the stack. So the structure of the graph itself has not been discussed, just the jobnodes. So how do we 
create the job nodes, populate the deps and numPreReqs and how do we even find the nodes with 0 numPreReqs.

Similarly after the stack is empty how do we check if all jobs have empty deps arrays? We use the any() python function to loop through
the nodes array attribute of the graph instance, check if for any node len(node.deps)> 0 or we could check if node.numPreReqs > 0 or
even simply check node.numPreReqs which is 0 or False and True otherwise. If any of these chosen check yields True, we store the result of
the any() function in a varible and if this varialbe, is True we return an empty array otherwise we return the output array. 

So there are three Python functions that are used for simple loops, map(), filter(), any(). map() and filter() take in a function and an 
iterable, and they iterate over the iterable and supply each element in the iterable to the function, ie map(function, iterable) or
filter(function, iterable). 
any() takes in a one line for loop ternery comprehension with a conditional statementn ie any( conditional_expression for element in iterable). 
For map() and filter(), the function may be a custom helper function in which case we write the function name without () or it may be a lambda
function and the corresponding function expression. ie map(lambda element: expression, iterable) or 
filter(lambda element: conditional_expression, iterable). 

map() maps all the iterables' elements to the function and stores output for each element. 

filter() maps all the iterables' elements to the function and stores only the elements that return True ie the function must return a 
boolean for each element. 

any() maps runs the conditional expression for each element from the for loop and returns True if any of the elements' conditionals return 
True, and if all return False any() returns False. any() is essentially asking is any True.

Thus if we have a function that doesnt return a boolean eg returns a number then we use map() to store the result for each element in a 
map object is itself iterable or the map object can be converted to a list. 
If the function returns a boolean and we want to store all the booleans for each element then we still use map(). 
If we want to filter only the elements that return True, we use filter(). 
If we only wantnto know if any element returns True to a conditional expression, we use any()."""


class JobNode:
    def __init__(self,job):
        self.job = job  #job is int
        self.deps = []  #list of dependencies
        self.numOfPrereqs = 0 #number of dependencies, initially 0

class JobGraph:
    def __init__(self,jobs):
        self.nodes= []  #to iterate through jobs
        self.graph = {} #maps jobs (integers) to their nodes
        for job in jobs:  #loop throg
            self.addNode(job)

    def addNode(self, job):
        self.graph[job] = JobNode(job)  #create job node and add it as the value to its same key in jobgraph
        self.nodes.append(self.graph[job]) #add the job node created to nodes in jobgraph for easy iteration
    
    def addDep(self,job,dep):
        jobNode = self.getNode(job)
        depNode = self.getNode(dep) 
        jobNode.deps.append(depNode)
        depNode.numOfPrereqs += 1


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

    for job, dep in deps: #adding edges
        graph.addDep(job, dep)
    return graph
        
def getOrderedJobs(graph):
    orderedJobs = []
    nodesWithNoPrereqs = list(filter(lambda node: node.numOfPrereqs == 0, graph.nodes))
    while len(nodesWithNoPrereqs):
        node = nodesWithNoPrereqs.pop()
        orderedJobs.append(node.job)
        removeDeps(node,nodesWithNoPrereqs)
    graphHasEdges = any(node.numOfPrereqs for node in graph.nodes)
    return [] if graphHasEdges else orderedJobs


def removeDeps(node,nodesWithNoPrereqs):
    while len(node.deps):
        dep = node.deps.pop()
        dep.numOfPrereqs -= 1
        if dep.numOfPrereqs == 0:
            nodesWithNoPrereqs.append(dep)
        
""" You are given three inputs, all of which are instance of an OrgChar class that have a directReports property pointing to their
direct reports. The first input is the top manager in an organizational chart (ie the only instance that isnt anybody else's 
direct report and the other two inputs are reports in the orgainizational chart. The two reports are guaranteed to be distinct.
The question is to write a function that returns the lowest common manager to the two reports.

This question is similar to Youngest Common Ancestor question in essence. However the difference is in the attributes on the node.
In Youngest Common Ancestor question, the nodes have an ancestor attribute that points to the youngest ancestor aka manager in this
case, but in this question we have the directReports attribute that is a list of directReports to a manager. Thus if we have a node
A with three child nodes B,C,D, in the Youngest Common Ancestor question, each of B,C,D has an ancestor attribute pointing to A. In
this question node A has a directReports attribute that is a list of node B, C, D. In both questions, we are being asked to look
at the top of the tree to find the closest ancestor that the descendant nodes have in common. So it is clear that the interface of
this question makes it a little trickier than the other question. In otherwwords, in this question we can only go down, in the 
other question we can only go up, but in both questions we are asked to look up for the closest common ancestor node.
So how do we go about this question? What are we going to do?

We're gonna recursively go through all of the direct reports of any given manager or general person in the organizational chain. 
And for each of the direct reports, we're gonna gather some kind of organizational information about the sub tree rooted at that report 
or at that person. And the information we're gonna be looking for is gonna be the number of important reports in a given sub tree, and
by important reports we are talking about the inputs reportOne and reportTwo. So we want to know how many of these reports are in the
subtree rooted at any node in the tree. The answer will be first manager that reports 2 important reports in its subtree.

In the code, we define a data structure, OrgInfo that takes two instantiation inputs and binds them as attributes for any instance
ie lowestCommonManager, numImportantReports. The lowestCommonManager will be the first node object with numImportantReports = 2,
otherwise it will be None. The recursive call takes a manager node object, reportOne node object and reportTwo node object.
When we first call the recursive call we use the original inputs ie topManager as the manager node object, then reportOne, reportTwo.

So in the recursive function we initialize a variable, numImportantReport as 0, then we check if the manager node is equal to reportOne 
or reportTwo in which case we increment the numImportantReport by 1. Then with a for loop we conduct a depth-first search on the current 
manager's direct reports. This recursive function call returns an instance of the OrgInfo class. This will have the effect of going from
the topManager all the way down the leftmost branch of the OrgChart tree to the lowest employee whose directReports attribute array will
be empty. When we receive the OrgInfo instance from a direct report, we check if the lowestCommonManager attribute is not None. If its
not, None then it means that the answer is stored in there and we return that OrgInfo instance up the tree. If it is None, the next thing
we do is to increment the numImportReport variable with the value stored in the numImportantReports of the OrgInfo class received from
the direct report, this way if a direct report has one of the important  reports in its subtree, we add it to the current manager's
numImportantReports variable since that important report is also in the current manager's subtree. Finally we check if the current manager
is the lowestCommonManager ie if numImportantReports is 2 eg if two different Reports return 1 each or if current manager is one of the
important report and the other is in its subtree. If the numImportantReport is 2, we set lowestCommonManager to current manager, else
None. Then we return an instance of the OrgInfo() class with lowestCommonManager (node or None) and numImportantReports as inputs to the
class. The important part is check if the orgInfo returned by a direct report has a non-None lowestCommonManager and returning that 
instance of orgInfo all the way up the tree. In our main function, we return the node stored in the lowestCommonManager attribute of 
the class instance returned by the recursive helper function. In the code, we check the subtree of a manager before we check the manager's
identity but the order doesnt affect the solution as written.  """


#Input class
class OrgChart:
    def __init__(self,name):
        self.name = name
        self.directReports = []

#this class will be the interface to collect organizational info
class OrgInfo:
    def __init__(self,lowestCommonManager, numImportantReports):
        self.lowestCommonManager = lowestCommonManager
        self.numImportantReports = numImportantReports

""" We're gonna recursively go through all of the direct reports of any given manager or general person in the organizational chain. 
And for each of the direct reports, we're gonna gather some kind of organizational information about the sub tree rooted at that report 
or at that person. And the information we're gonna be looking for is gonna be the number of important reports in a given sub tree, and 
the lowest common manager in the subtree if the number of important reports have been found ie if there are two reports, the first 
manager with number of important reports equal to 2 is the answer."""
#O(n) time | O(d) space
def getLowestCommonManager(topManager,reportOne,reportTwo):
    return getOrgInfo(topManager,reportOne,reportTwo).lowestCommonManager #helper method returns an instance of interface class

def getOrgInfo(manager,reportOne,reportTwo):
    numImportantReports = 0 #we start with 0 numImportantReports

    for directReport in manager.directReports:#loop through the direct reports of each node starting from root
        orgInfo = getOrgInfo(directReport, reportOne,reportTwo) #recursive call on each direct report of current node
        #first check if lcm has been found, if it is, return the orgInfo of the direct report that has lcm
        if orgInfo.lowestCommonManager is not None: #if a direct report reports a lcm, return that orgInfo, we're done
            return orgInfo #if a descendant or direct report has a lcm when it returns to its ancestor or manager
        #either way, add each descendants nir to their manager's nir
        numImportantReports += orgInfo.numImportantReports #update the nir of each ancestor with the nir of descendant when returned

    #base case, when we call the recursive function at the subtree rooted at one of important reports
    if manager == reportOne or manager == reportTwo:
        numImportantReports += 1
    lowestCommonManager = manager if numImportantReports == 2 else None #update lcm attribute when its found
    return OrgInfo(lowestCommonManager,numImportantReports) #this is where we create an instance of OrgInfo interface class to be returned
    
    


    
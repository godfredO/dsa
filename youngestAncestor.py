"""The input consists of three instances of an Ancestral class, where each node has a name and an ancestor attribute which points to its
youngest ancestor. The three inputs are the top ancestor in this ancestral tree and as such its ancestor attribute points to None, and two
descendants in the ancesral tree (ie instances of the ancestral class). The question asks to write a function that returns the youngest
common ancestor to both descendants. First thing to note is that this is a graph traversal problem and since the nodes point to their
youngest ancestor, we can only go up the tree. Second thing to realize is that if both descendants share the same youngest ancestor,then
we would just return the node.ancestor of either node. However the generic case is if they don't share the same youngest ancestor. And
lastly if these descendants are in different subtrees of the top ancestor, the top ancestor would be their only and youngest common 
ancestor, but if they are in the same subtree of the top ancestor, and neither is a direct descendant of the top ancestor, then they 
would have a unique youngest common ancestor, which would be the last node where the two instances sort of diverge. 

So the algorithm is pretty simple really. For both descendants we find their depth in the ancestral tree. To do this we start from a 
descendant with a depth of 0 and increment this depth as we traverse up the tree until we reach the top ancestor. With descendant depths
in hand,  we start from the deepest descendant and backtrack up the ancestral tree until we match the other depth. If the depths are the
same they could be share the same youngest ancestor, or even have different ancestors but be at the same level in the ancestral tree, and
in either case we would do a simultaneous climb up the tree until we arrive at the same ancestor which will be the youngest common ancestor.
You could imagine that if their depths are equal because they share the same ancestor, we would do only one climb. If their depths are the
same but share different ancestors we would do a couple of climbs until we are pointing at the same node from the simultaneous climb up the
ancestral class. Now if one depth is greater, say depthOne is greater, we climb up (decrementing the depth) till the depthOne matches 
depthTwo. So we say if depthOne is greater backtrack from descendant one else back track from descendant two. The helper function that 
backtracks up the ancestral tree takes the start descendant, the end descendant and greaterDepth - lesserDepth, ie using a for loop we know
we need to do exactly greaterDepth - lesserDepth climbing up. This is because it is going to backtrack a total of greaterDepth- lesserDepth 
steps up the ancestral tree to bring both descendants to par depth in the tree (so its repurposes how we got the depths in the first place, 
just that instead of going until we reach the top ancestor, we go from the deeeper descendants until we have taken greaterDepth - lesserDepth 
steps up the tree, until we have a new descendant for the hitherto deepr descendant). Then with the new descdant we get for the deeper 
descendant,we move up the tree, in tandem with the previously higher descendant until they both point to the same youngest ancestor (which
may or may not be the top ancestor). By passing in greaterDepth - lesserDepth, if the two depth information is the same no backtracking is
done at all, otherwise we take exactly greaterDepth - lesserDepth steps back up the ancestral calss from the deeper descendant.

So steps:
    - get depth information
    - bring deeper descendant on par with higher descendant ie replace it with an ancestor at same depth as higher descendant
    - bring both current descendants up the tree until the point to the same youngest ancestor
    - in the code we combine steps two and three for a cleaner code

"""


class AncestralTree:
        def __init__(self,name):
            self.name = name    
            self.ancestor = None

#O(d) time | O(1) space d = depth of deepest depth
def getYoungestCommonAncestor(topAncestor,descendantOne,descendantTwo):
    depthOne = getDescendantDepth(descendantOne,topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)
    if depthOne > depthTwo: #means descendantOne is lower in the tree
        return backtrackAncestralTree(descendantOne,descendantTwo,depthOne-depthTwo)
    else: #this takes the case where both depths are equal for 0 backtracking first
        return backtrackAncestralTree(descendantTwo,descendantOne,depthTwo-depthOne)

def getDescendantDepth(descendant,topAncestor):
    depth = 0
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor
    return depth

def backtrackAncestralTree(lowerDescendant,higherDescendant,diff):
    #bring both descendants to the same level
    while diff > 0:
        lowerDescendant = lowerDescendant.ancestor #go up
        diff -= 1
    #get lowest common descendant, by moving both descendants in tandem up the tree
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerDescendant

#O(d) time | O(1) space where d= depth of deepest descendant
"""Same solution just different coding changes to more clearly show steps"""
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	depthOne = getDepth(descendantOne, topAncestor)
	depthTwo = getDepth(descendantTwo, topAncestor)
	
	updatedDescendant = ""
	staticDescendant = ""
	
	if depthOne > depthTwo:
		updatedDescendant = updateDescendant(descendantOne, depthOne - depthTwo)
		staticDescendant = descendantTwo
	else:
		updatedDescendant = updateDescendant(descendantTwo, depthTwo - depthOne)
		staticDescendant = descendantOne
	
	return backTrackUpAncestralTree(updatedDescendant, staticDescendant)


def getDepth(descendant, ancestor):
	depth = 0
	while descendant != ancestor:
		depth += 1
		descendant = descendant.ancestor
	return depth
	

def updateDescendant(descendant, diff):
	while diff > 0:
		descendant = descendant.ancestor
		diff -= 1
	return descendant


def backTrackUpAncestralTree(descendantOne, descendantTwo):
	while descendantOne != descendantTwo:
		descendantOne = descendantOne.ancestor
		descendantTwo = descendantTwo.ancestor
	return descendantOne
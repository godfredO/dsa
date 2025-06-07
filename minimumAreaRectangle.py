"""There is a graph question that asks to find the number of rectangles that can be formed from a 2-d array of [x,y] points. This question
is an like that one, but simply asks to find the minimum area rectangle that can be formed. Like that question, the diagonals answer is
simpler and more intuitive than the four-corners approach. Here, two approaches are explained, diagonals approach and the parallel sides
approach. I prefer the diagonals approach. Phew!!!"""

"""The brute force approach involves generating quadruple points to represent the points of a 
rectangle, ordered from lower left corner to top right corner, and testing if these points constitute 
a rectangle, not a parallelogram. This brute force approach will have a O(n^4) time complexity. To improve
this time complexity, the optimal solutions generate pairs of edges or diagonals and use these for testing 
if a rectangle is formed and if it is,calculate its area and store the minimum area formed """

"""Optimal solution one. This solution generates edges that are parallel to the y-axis (x-axis can also be used)
making sure these edges are ordered from far left to far right on the x-y plane. Then for every vertical edge, the
algorithm finds other edges of the same length and starting and ending y-coordinates. thus if a pair of vertical
edges have the same length and have the same y-cordianates, then these parallel edges constitute a rectangle whose
area will be calculated and compared to the minimum recatangle area so far. """
#O(n^2) time | O(n) space
def minimumAreaRectangle(points):
    columns = initializeColumns(points) #helper function to store x:[y1,y2,..] in constant-access hashtable
    minimumAreaFound = float("inf") #initialize the min rectangle area at inf for easy comparison
    edgesParallelToYAxis = {}

    """The reason for the time-complexity is due to how the sub-arrays in this problem determine the complexity of each
    step. If all the points have the same x-value and fall in the same column, sortedColumns is O(1) for a single x-value,
    the outer for loop is O(1), yValuesInCurrentColumn.sort() takes O(nlog(n)) and inner for loop takes O(n^2). This gives
    O(1) + O(1*(nlog(n) + n^2) = nlog(n)+ n^2 ~= n^2. In the other extreme where each point has a unique x-value, sortedColums
    takes O(nlog(n)), outer for loop takes O(n), yValuesInCurrentColumn.sort() takes O(1) since each x-value is unique and will
    store one y-value and the inner for loop also takes O(n) again because there is no shared x-value. This gives a overall 
    complexity of O(nlog(n)) + O(n*(1 + n) = nlog(n)+ n^2 ~= n^2. In real cases, a rectangle requires that pairs of points share
    the same x-values and y-values meaning we deal with sub-arrays where sorting never involves n values etc. This means the 
    complexity converges to these extremes which themselves converge to n^2"""
    #sort x-value keys in ascending order so that edges are generated from far-left to far right ie lowest x first
    sortedColumns = sorted(columns.keys())  #a list of x-value columns in sorted order from left to right,O(nlog(n))
    for x in sortedColumns: #loop through current x column, generate edges and check if complementary edge exists
        yValuesInCurrentColuumn = columns[x] #access the y-values for current x column
        yValuesInCurrentColuumn.sort()  #in-place sort of list of y-values for current x column ,sub-array

        for currentIdx, y2 in enumerate(yValuesInCurrentColuumn):#create edges with y-values in current column, y2
            for previousIdx in range(currentIdx): #pick y1 in the y-values that come before y2 ie less than y2
                y1 = yValuesInCurrentColuumn[previousIdx] #for each y2, y1 are the y-values less than y2 in column
                pointString = str(y1) + ":" + str(y2) #to use as keys for our edges dict. Tuples are hashable in Python too

                if pointString in edgesParallelToYAxis: #if a complementary edge already in edges dict
                    currentArea = (x - edgesParallelToYAxis[pointString])*(y2 - y1) #area = xLen* yLen, + cos x,y sorted
                    minimumAreaFound = min(minimumAreaFound, currentArea) #update min rectangle area
                
                edgesParallelToYAxis[pointString] = x #update the x-value stored in edges dict to current x-column
    
    return minimumAreaFound if minimumAreaFound != float("inf") else 0


def initializeColumns(points):#loop to summarize points by x-values for vertical edges parallel to y-axis , O(n)
    columns = {} #hashtable to store all the points that share the same x-value so that the constitute a vertical edge
    for point in points: #loop to store points as x:[y1,y2,..] in constant-access hashtable
        x,y = point
        if x not in columns:
            columns[x] = []
        columns[x].append(y)
    return columns

"""Optimal solution two. This solution is actually much easier to explain. We generate pairs of diagonals,making sure that a
valid diagonal can only be generated by points that have unique x-values and y-values. Edges share the same x or y values. 
Diagonals do not. So we loop through the points, generate valid diagonals and store them in a hashtables. Before adding a 
new diagonal however, we ask if the complementary diagonal exists in the hashtable. For a diagonal made from x1,y1 and x2,y2 
the complementary diagonal to make a valid rectangle will be made from points x1,y2 and x2,y1. Thus if we find a complementary
diagonal we calculate the area of the rectangle and keep track of the minimum area seen"""
#O(n^2) time | O(n) space
def minimumAreaRectangleI(points):
    pointSet = createPointSet(points) #hash points into a set for constant time access
    minimumAreaFound = float("inf") #initialize minimum rectangle area as inf for easy comparison

    for currentIdx,point in enumerate(points): #loop through the points array
        p2x,p2y = point #decompose current point as p2, by choosing p2 first repeated work is avoided
        for previousIdx in range(currentIdx): #inner loop for points that come before p2 ie no repeated work
            p1x,p1y = points[previousIdx] #access p1 and decompose it
            pointsShareValue = p1x == p2x or p1y == p2y #check if p2 and p1 form a valid diagonal
            if pointsShareValue: #if they share any of their coordiantes, they cant form a valid diagonal
                continue #so check next possible value for p1 if any
            point1OnOppositeDiagonalExists = convertPointToString(p1x,p2y) in pointSet #check for diagonal point 1
            point2OnOppositeDiagonalExists = convertPointToString(p2x,p1y) in pointSet #check for diagonal point 2
            oppositeDiagonalExists = point1OnOppositeDiagonalExists and point2OnOppositeDiagonalExists #diagonal found

            if oppositeDiagonalExists:#a diagonal is found if both diagonal points exists, in which case a rectangle is found
                currentArea = abs(p2x-p1x)*abs(p2y-p1y) #calculate area
                minimumAreaFound = min(minimumAreaFound,currentArea) #update minimum area
    return minimumAreaFound if minimumAreaFound != float("inf") else 0 #return answer

def createPointSet(points): #we are hashing to a set because we dont need to store key-value pairs, just values
    pointSet = set() #and a set gives us constant time access
    for point in points:
        x,y = point
        pointString = convertPointToString(x,y) #create hashable object, a string. In python tuples are hashable too
        pointSet.add(pointString) #add to set after converting point to a hashable string
    return pointSet

def convertPointToString(x,y):
    return str(x) + ":" + str(y)

points = [
    [1, 5],
    [5, 1],
    [4, 2],
    [2, 4],
    [2, 2],
    [1, 2],
    [4, 5],
    [2, 5],
    [-1, -2]
]
print(minimumAreaRectangleI(points))

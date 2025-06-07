"""This question gives an array of x,y coordinates and asks how many rectangles can be formed with those coordinates. There are
two main approaches to questions like this, the sides approach and the diagonal approach. The first approach, treates each 
coordinate as a potential bottom left corner of, iterates through the array for points that are on the same x coordinate and
different y coordinate to be the top left corner and if a top left corner is found, iterates through the array for points on the
same y coordinate as the top right corner and different x coordinate to be the top right corner and if a top right corner is found
iterates through the array for points on the same x coordinate but lower y coordinate as the top right corner to be the bottom right
corner and then back to the original bottom left corner point. To avoid having an n^4 complexity, this clockwise loop pattern is 
preceded by creating a hashtable where each key is a point, stringified and hashable, and each value is four keys, up, down, right,
left that points to coordinates that are above, left, right, below the hashtable key. This allows easy constant time access when
determining possible corners. This sides appproach is used by the first two solutions which differ in their space complexity. The 
first of these uses the hashtable of mapping each coordinates to other coordinates that are above,below,left.right of it. The second
of these solutions unpacks each x,y points and stores in the hashtable, x coordinates to y coordinates instead of x,y coordinates to
x,y coordinates but the underlying clockwise pattern remains the same. The third solution uses the simpler and more intuitive diagonal
approach, which again treats each point as a potential left bottom corner and then loops through the hashtable for points that can
be possible top right corners thus focusing on the diagonal of the rectangle. If for a potential bottom left corner a top right corner
is found, then the top left corner and the bottom right corner can be deduced from the coordinates of the bottm left corner and top 
right corner. If the bottom left is x1,y1 and the top right is x2,y2 then the top left is x1,y2 and the bottom right is x2,y1. This 
approach achieves the same time and space complexity as the second solution but in a cleaner more intuitive manner"""

"""First sides-based approach with a worse space complexity because we are mapping points to other points so that in the limiting case
where each point is on the same vertical or horizontal line each point in the hashtable will map to up to every other point in the
input array in the up and down directions"""
#O(n^2) time | O(n^2) space
# def rectangleMania(coords):
#     coordsTable = getCoordsTable(coords) #for each coord bucket points directly above, below, to the left and right, O(n^2) space
#     return getRectangleCount(coords,coordsTable) #clockwise loop logic and rectangle count

# def getCoordsTable(coords):
#     coordsTable = {}
#     for coord1 in coords: #for each point, bucket the other points directly above, below, to the left and right
#         coord1Directions = { UP : [], RIGHT : [], DOWN : [], LEFT : []} #initalize buckets, to empty arrays.
#         for coord2 in coords:
#             coord2Direction = getCoordDirection(coord1,coord2)
#             if coord2Direction in coord1Directions: #we only want directly above,below,left,right not diagonal or same point
#                 coord1Directions[coord2Direction].append(coord2)
#         coord1String = coordToString(coord1) #create hashable key
#         coordsTable[coord1String] = coord1Directions #map coord1 to its up,right,down,left directions buckets
#     return coordsTable

# def getCoordDirection(coord1,coord2):
#     x1,y1 = coord1  #unpack coord1
#     x2,y2 = coord2  #unpack coord2
#     if y2 == y1: #if coord2 is on the same y coordinate as coord1, 
#         if x2 > x1: #and the x of coord2 is greater than the x of coord1 then coord2 is directly to the right of coord1
#             return RIGHT
#         elif x2 < x1: #and the x of coord2 is less than the x of coord1 then coord2 is directly to the left of coord1
#             return LEFT
#     elif x2 == x1: #if coord2 is on the same x coordinate as coord1,
#         if y2 > y1: #and the y of coord2 is greater than the y of coord1 then coord2 is directly above coord1
#             return UP
#         elif y2 < y1: #and the y of coord2 is greater than the y of coord1 then coord2 is directly below coord1
#             return DOWN
#     return "" #return empty string if coord2 is diagonal (x2>x1 and y2>y1) or is the same point (x2==x1 and y2==y1)

# def getRectangleCount(coords,coordsTable):
#     rectangleCount = 0 #initialize rectangle count at 0
#     for coord in coords: #with each coordinate as a bottom left corner 
#         rectangleCount += clockwiseCountRectangles(coord,coordsTable, UP, coord) #recurisive function for finding rectangles
#     return rectangleCount

# def clockwiseCountRectangles(coord,coordsTable,direction,origin):
#     """#this recursive function is initially called with direction == UP from bottom left to top left, then RIGHT from top left
#     #to top right, then DOWN from top right to bottom right then LEFT from bottom right to origin ie bottom left"""
#     coordString = coordToString(coord) #create hashbable key of coord in current recursive call
#     if direction == LEFT: #if direction is LEFT, it means we are going back to origin and completing a rectangle
#         rectangleFound = origin in coordsTable[coordString][LEFT] #check if we can go left to the origin to complete rectangle
#         return 1 if rectangleFound else 0 #return 1 rectangle found else 0 rectangle found if we can(t) go to origin
#     else: #if direction is other than left
#         rectangleCount = 0
#         nextDirection = getNextClockwiseDirection(direction) #get next direction in clockwise pattern from current direction
#         for nextCoord in coordsTable[coordString][direction]:
#             rectangleCount += clockwiseCountRectangles(nextCoord,coordsTable,nextDirection,origin)
#         return rectangleCount

# def getNextClockwiseDirection(direction):
#     if direction == UP: #if current direction is UP from origin, bottom left corner, to top left corner 
#         return RIGHT # then next direction is RIGHT from top left corner to top right corner
#     if direction == RIGHT: #if current direction is RIGHT from top left corner to top right corner 
#         return DOWN #then next direction is DOWN from top right corner to bottom right corner
#     if direction == DOWN: #if current direction is down from top right corner to bottom right corner 
#         return LEFT #then next direction is left from bottom right corner back to origin, bottom left corner.
#     return "" #need to return something if direction is LEFT which is handled in clockwiseCountRectangles explicitly
# def coordToString(coord): #create hashable key for each coordinate
#     x,y = coord #unpack coord before stringifying to create hashable key
#     return str(x) + "-" + str(y)  #using concatenation is okay since x,y has two digits at most so O(5)
# UP = "up" #hardcoded directions, for use in getCoordDirection and getCoordsTable, clockwiseCountRectangle, getRectangleCount
# RIGHT = "right"
# DOWN = "down"
# LEFT = "left"


"""In the second sides-based approach, instead of mapping each point to the other points directly above,below,right,left we
map each x coordinate and y coordinate to the points thus summarizing the input array of coordinates. This makes sense
because when determining whether points are directly above,below,right,left we first check for equal x coordinates for 
above and below and we first check for same y coordinates for left and right. Thus in the limiting case where all points
share the same x or the same y, we will have a single x and y coordinate in the hashtable that maps to the input array"""
#O(n^2) time | O(n) space
# def rectangleMania(coords):
#     coordsTable = getCoordsTable(coords) 
#     return getRectangleCount(coords,coordsTable)

# def getCoordsTable(coords):
#     coordsTable = {"x":{},"y":{}} #initalize empty hashtable for summarizing the unique x and unique y coordinates, O(n) space
#     for coord in coords:
#         x,y = coord #unpack current coordinate, x,y are integers and thus hashable as is
#         if x not in coordsTable["x"]: #if first time encountering current x coordinate
#             coordsTable["x"][x] = []  #then initialize an empty array before appending below
#         coordsTable["x"][x].append(coord) #append current coordinate to its x map in hashtable
#         if y not in coordsTable["y"]: #if first time encountering current x coordinate
#             coordsTable["y"][y] = []  #then initialize an empty array before appending below
#         coordsTable["y"][y].append(coord) #append current coordinate to its x map in hashtable
#     return coordsTable

# def getRectangleCount(coords,coordsTable):
#     rectangleCount = 0
#     for coord in coords: #loop and treat each point as a potential lower left corner 
#         lowerLeftY = coord[1] #access the y coordinate for current point, then go UP in the y direction 
#         rectangleCount += clockwiseCountRectangles(coord,coordsTable,UP,lowerLeftY) #recursive function, go UP
#     return rectangleCount

# def clockwiseCountRectangles(coord1,coordsTable,direction,lowerLeftY):
#     x1,y1 = coord1 #unpack current coordinate
#     if direction == DOWN: #base case, when going from top right corner to lower rigt corner
#         relevantCoords = coordsTable["x"][x1] #all points of same x but different y
#         for coord2 in relevantCoords: #loop through all points with same x as top right corner
#             lowerRightY = coord2[1] #for each point, access the y coordinate as a possible lower right y
#             if lowerRightY == lowerLeftY: #if the lower right corner has the same y as the origin's lowerLeftY
#                 return 1 #then a rectangle is found so 1, no need to go LEFT, can just check if same y
#         return 0 #if none of the top right corner points of same x share y coordinate with lower left y
#     else:
#         rectangleCount = 0
#         if direction == UP: #when going from lower left corner to upper left corner
#             relevantCoords = coordsTable["x"][x1] #points of same x different y
#             for coord2 in relevantCoords: #loop through all points with same x as top left corner
#                 y2 = coord2[1] #access y coordinate as possible upper left corner
#                 isAbove = y2 > y1 #from lower left to upper left, y2 must be greater than y1, same x
#                 if isAbove:
#                     rectangleCount += clockwiseCountRectangles(coord2, coordsTable, RIGHT,lowerLeftY) #go RIGHT
#         elif direction == RIGHT:
#             relevantCoords = coordsTable["y"][y1]
#             for coord2 in relevantCoords:
#                 x2 = coord2[0]
#                 isRight = x2 > x1
#                 if isRight:
#                     rectangleCount += clockwiseCountRectangles(coord2,coordsTable,DOWN,lowerLeftY)
#         return rectangleCount
                
# UP = "up" #hardcoded directions, for use in getCoordDirection and getCoordsTable, clockwiseCountRectangle, getRectangleCount
# RIGHT = "right"
# DOWN = "down"


"""Last solution which is diagonal based and cleaner to code out. Basically, treating each point as a potential lower left corner,
we find all other points are could be a potential upper right corner, ie greater x and greater y. Then with the potential lower
left corner coordinates and the potential upper right corner coordinates we check if the upper left corner coordinates and 
lower right corner coordinates needed to form a rectangle are present in the hashtable we create by hashing each point to allow
for constant time access. If the potential lower left corner coordiantes are x1,y1 and the potential upper right corner coordinates
are x2,y2 then the upper left corner coordinates will be x1,y2 and the lower right corner coordinates will be x2,y1."""
#O(n^2) time | O(n) space
def rectangleMania(coords):
    coordsTable = getCoordsTable(coords)
    return getRectangleCount(coords,coordsTable)

def getCoordsTable(coords):
    coordsTable = {}
    for coord in coords:
        coordString = coordToString(coord)
        coordsTable[coordString] = True
    return coordsTable

def getRectangleCount(coords,coordsTable):
    rectangleCount = 0
    for x1,y1 in coords: #directly unpack potential lower left corner
        for x2,y2 in coords: #directly unpack potential upper right corner
            if not isInUpperRight([x1,y1],[x2,y2]): #check if upperleft,upper right
                continue
            upperCoordString = coordToString([x1,y2])  #upper left corner coordinates
            rightCoordString = coordToString([x2,y1])  #lower right corner coordinates
            if upperCoordString in coordsTable and rightCoordString in coordsTable:
                rectangleCount += 1 #if upper left and lower right coordinates exist
    return rectangleCount

def isInUpperRight(coord1,coord2):
    x1,y1 = coord1
    x2,y2 = coord2
    return x2 > x1 and y2 > y1

def coordToString(coord):
    x,y = coord
    return str(x) + "-" + str(y)

coords = [
    [0, 0],
    [0, 1],
    [1, 1],
    [1, 0],
    [2, 1],
    [2, 0],
    [3, 1],
    [3, 0]
]
print(rectangleMania(coords))
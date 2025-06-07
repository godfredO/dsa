
"""The question gives a 2d matrix and asks to transform it into a 1-d array where the integers of the 2-d matrix are in spiral order
in the 1-d array. Moving in spiral order involves traversing the perimeter of the full matrix, ie the top border, the right border,
the bottom border and the left border, moving left to right, top to bottom, right to left, bottom to top. With this outer perimeter
done, we traverse the perimeter of the inner remaining matrix in spiral order until we've added all the integers to the 1-d array.
To describe the perimeter, we use the dimensions of the matrix, in the form of startRow, endRow, startColumn, endColumn. After using
startRow, endRow, startColumn, endColumn to traverse the outer perimeter, we adjust these markers to traverse the inner perimeter.
We keep traversing and adjusting until the endRow crosses the startRow or the endColumn crosses the startColumn. That is the loop
condition is while startRow <= endRow and startColumn <= endColumn. The = is because for a odd-length row / col, these pointers will
meet on the middle value when its time to add this value to the 1-d matrix. It is also essential to not double count the middle row
or column for rectangular matrices, and as such we add a break statement for the bottom and left borders of the current perimeter 
when startRow == endRow , startCol == endCol. To traverse the values inside a single border inside the current perimeter we use for 
loops. To define the perimeter as a whole, we use a while loop. After traversing the borders of the current perimeter, we adjust the
perimeter pointers. We reverse the for loops when traversing the bottom and left borders of the current perimeter and we make sure to
not double count the first element of the top border or the last element of the right border. Same thing, when traversing the right
border we make sure not to double count the last element of the top border. And adjustments have to be made for Python's zero indexing
and range functionalities. Thus this question uses the two pointer techniques twice ie for rows and columns for a total of four pointers."""

# Iterative solution, O(N) time and space where N is total number of elements in 2d array
def spiralTraverse(array):
    result = []
    #pointers of outer perimeter. A perimeter is defined by start/end Row, start/end Col
    startRow,endRow = 0, len(array) - 1
    startCol,endCol = 0 , len(array[0]) - 1 #we are not told this is an nxn matrix

    # The while loop is for traversing perimeters, for loops traverse borders of a perimeter
    while startRow <= endRow and startCol <= endCol: 

        # for loop to traverse the top border of perimeter
        for col in range(startCol,endCol + 1):  # endRow + 1, endCol +1 is because of Python's range func
            result.append(array[startRow][col])

        # for loop to traverse the right border of perimeter
        for row in range(startRow + 1, endRow + 1): # startRow + 1 is to avoid double counting
            result.append(array[row][endCol])       # endRow + 1 is due to Python's range function
        
        # for loop to traverse the bottom border of the perimeter
        for col in reversed(range(startCol, endCol)):
            if startRow == endRow: #to avoid double counting middle row which has been added by top border
                break
            result.append(array[endRow][col])
        
        # for loop to traverse the left border of the perimeter
        for row in reversed(range(startRow + 1,endRow)):
            if startCol == endCol: #to avoid double counting the middle column which has been added by bottom border
                break
            result.append(array[row][startCol])
        
        startRow += 1      #update the row / column markers to go to inner perimeter
        endRow -= 1
        startCol +=1
        endCol -=1

    return result


# Recursive solution
#O(n) time | O(n) space
def spiralTraverseII(array):
    result = []
    startRow,endRow = 0, len(array) - 1
    startCol,endCol = 0 , len(array[0]) - 1
    spiralFill(array,startRow,endRow,startCol,endCol,result) 
    return result

def spiralFill(array,startRow,endRow,startCol,endCol,result):
    if startRow > endRow or startCol > endCol:
        return
    
    # for loop to traverse the top border of perimeter
    for col in range(startCol,endCol + 1):  # endRow + 1, endCol +1 is because of Python's range func
        result.append(array[startRow][col])

    # for loop to traverse the right border of perimeter
    for row in range(startRow + 1, endRow + 1): # startRow + 1 is to avoid double counting
        result.append(array[row][endCol])       # endRow + 1 is due to Python's range function
        
    # for loop to traverse the bottom border of the perimeter
    for col in reversed(range(startCol, endCol)):
        if startRow == endRow:
            break
        result.append(array[endRow][col])
        
    # for loop to traverse the left border of the perimeter
    for row in reversed(range(startRow + 1,endRow)):
        if startCol == endCol:
            break
        result.append(array[row][startCol])
    
    spiralFill(array,startRow + 1, endRow -1, startCol + 1, endCol -1,result)

    


array = [
    [1,2,3,4],
    [12,13,14,5],
    [11,16,15,6],
    [10,9,8,7]
]

print(spiralTraverse(array))
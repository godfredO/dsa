"""Given an m x n integers matrix, return the length of the longest increasing path in matrix. From each cell, you can either move in 
four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
The integers are non-negative ie 0 or positive.

Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.



Starting from any integer in the matrix, we can always form a path of length 1 consisting only of that integer. So we can start a dfs
from each value and go to its neighbors, and we can only continue the path via a neighbor if the neighbor value is greater than the 
original node's values . Eg if node with value 5 has four neighbors, [1,5,6,7], we can only continue the path that includes neighbors
[6,7]. Now an interesting observation is that because of the way the question is structured, we actually wont ever get stuck in a loop.
That is in the example of a node with value 5 that has four neighbors [1,5,6,7], while we will go from 5>6 or 5>7 we will not go from 6
or 7 to 5, since we only visit a neighbor if its value is greater than the original node. Another observation is that if we can use 
memoization to avoid doing repeated work. For example lets say that in the previous example the 7 is also a neighbor of the 6 so that 
the longest increasing path for node with value 5 is 3 ie 5>6>7 and we come to some node of value 4 which is a neighbor of 5. The we
know that if we go down the path that includes 5, the longest path of node 4 in that path is 4 ie 4>5>6>7 ie 1+longest(5). So if we
store the intermediate results for each node, we can avoid repeating work for its neighbors in the path that includes the node. So we
will keep a matrix which will store the longest increasing path found for each position. Thus while we dont need a visited matrix, we
still have the same time and space complexity of a regular dfs because we are effectively using the visited matrix in a clever ways as 
the longest increasing path matrix. 

So the algorithm is that we start a dfs from each position, and we initialize a lip variable equal to 1, call on the neighbors that 
have a value greater than the current value, and whenever we find an answer, store it in the lip matrix. If we already have a value
for the neighbor in the lip matrix, we dont do the neighbor call, we just do add 1 to the neighbor's value and update our variable by
doing a maximum comparison. The reason for the maximum compariosn is that different neighbors can yield different lip results. If 
however the neighbor is greater than the current value but we havent made a dfs call on that neighbor yet, then we do the dfs call, 
and when the call completes, we read the stored value in the matrix, add 1, and update via a maximum comparison. After going through
all the neighbors, skipping those that are equal or less, directly using the values for neighbors that already have a lip value stored
or using the lip value after calling a dfs on valid neighbors, we then set the value for the current node in the lip matrix. Now we 
can keep track of the maximum value throughout the matrix, or we can do a second pass through the lip matrix to find the maximum value.

So how can we cleanly and cleverly code this solution up? We have an outer loop that makes a dfs call from each node and we pass in 
a previousValue of -1. By using the previous value method instead  we can really clean up the code. So in the dfs, if the call is 
invalid or the current value is less than or equal to the previous value we return 0. Then if the current position has a value stored
in the lip matrix, we return that value. Otherwise we initialize our lip variable to 1. The we update the lip variable to the maximum 
of the current value and adding 1 to the result of the making the neighboring calls, passing in the current node value as the previous
value. When all neighboring call updates are completed, we store the updated lip value in the lip matrix and return the value we just 
stored. By using a previous value of -1 we are able to ensure that each node passes the equal to or less than test since we know that 
the matrix contains only non-negative numbers. I also initialize the longest matrix with None to determine positions that havent had 
a dfs call on them yet. I also use a custom object to do a maximum comparison whenever we have the answer for a particular position,
instead of going through the longest matrix a second time to determine what the longest path is.
"""
class LongestPath:
    def __init__(self,value):
        self.value = value
#O(n*m) time | O(n*m) space
def longestIncreasingPath(matrix):
    rows, cols = len(matrix), len(matrix[0])
    longest = [[None for i in range(cols)] for j in range(rows)]

    maxLength = LongestPath(0)
    for row in range(rows):
        for col in range(cols):
            if longest[row][col] is not None:
                continue
            findLongest(row, col, matrix, -1, longest, rows, cols, maxLength)
    
    return maxLength.value
    

def findLongest(row, col, matrix, prevValue, longest, rows, cols, maxLength):
    if row < 0 or col < 0 or row >= rows or col >= cols or matrix[row][col] <= prevValue:
        return 0
    
    if longest[row][col] is not None:
        return longest[row][col]
    
    result = 1
    result = max(result, 1+findLongest(row - 1, col, matrix, matrix[row][col], longest, rows, cols, maxLength))
    result = max(result, 1+findLongest(row + 1, col, matrix, matrix[row][col], longest, rows, cols,maxLength))
    result = max(result, 1+findLongest(row, col - 1, matrix, matrix[row][col], longest, rows, cols, maxLength))
    result = max(result, 1+findLongest(row, col + 1, matrix, matrix[row][col], longest, rows, cols, maxLength))
    longest[row][col] = result
    maxLength.value = max(maxLength.value, result)
    return result



matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
print(longestIncreasingPath(matrix))
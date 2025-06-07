"""Given a triangle array, return the minimum path sum from top to bottom. For each step, you may move to an adjacent number of the 
row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).


So we are given a triangle array, which is basically a nested array where the first array has 1 element, the second has two element,
the thrid has three elements ie the kth array has k elements. And we are asked to calculate the minimum path from the first array to
the last array with the caveat that we can only move to adjacent numbers when moving from one level to the next. What does this mean?
It means that when moving from one level to the next, we can go straight down, to the left. ie array[nextRow][col], or 
array[nextRow][col + 1]. You get my drift, this is looking like neighbors function in graphs, but not any graph, but a binary tree
because each node has two children as we go from top to bottom, with the only value in the first array as the root node. 

Now how do we minimize the path sum ? One idea would be to choose from each node the minimum child at each level, but that would be 
problematic because we would have no way of knowing if the minimum value child has lower values chidren two. Say we have to choose
between 1,2 and we choose 1 but 1 has as children nodes 10,20 and 2 has as children 3,4. Clearly choosing leads to a sum options of 
1+10 or 1+20 but choosing 2 leads to sum options of 2+3 or 2+4 which are both lower. So this approach even though wrong is giving
a big hint coupled with the fact that we have modeled the question as a binary tree. Note here this is a typical binary tree because
adjacent nodes on the same level all share one common child ie the array[next][col + 1] for node on a particular level goes to the same 
value as the array[nextRow][col] for its adjacent node on the same row ie array[currentRow][col] and array[currentRow][col + 1 ] share
a common child. One cool realization about modeling this as a tree is that, because adjacent values on the next row are
array[nextRow][col], array[nextRow][col + 1], we are assured that each node will have two children since each row, has one more value
than the preceding row.

So the first idea is to solve this recursively ie from each node we want to know what is the minimum path sum we can get for its children,
and so on and so forth. This means we will need to go all the way down to the bottom of the tree and work our way back up. So depth-first
search. But which tree depth-first search will we use? Is it preorder, inorder, or postorder. Its looking like we will have to go left,
go right and then visit ie find the minimum path sum for the left, right child before choosing the minimum path sum for the current node
to be sent up the tree to its paent as a child minimum path sum. So its looking like postorder dfs like binaryTreeDiameter.

However, we have our base case that for each node at the bottom of the tree, the since it has no chidlren , its minimum path sum will be 
itself (in the code we will assume 0 if we go out of bounds for the children of the last level nodes). Now my only concern is that since 
there will be shared child node's between adjacent nodes on the same level, we will be repeating work.So how do we code this up and avoid 
repeated work in the code? Memoization. And since memoization will take up to n^2 space the binary tree solution takes O(n^2) time and
O(n^2) space where n is the number of rows, and there are roughly n^2 elements in the tree. Now usually we can go from a memoization
solution to a dynamic array solution to improve space complexity.

Now before jumping into the code, we should discuss the dynamic programming solution which will be to start initialize 0's for our base
case (child nodes of leaf nodes) of length equal to length of lastRow + 1, and row 1 has 1 element, row 2 has two elements etc, the last
row has as many elements as there are row in the input, so we need to just add 1 to this length. Anyway, for each successive row going up 
ie reversed order, and for each element in the current row, we access the minimum path sum of the element in our result array, which will 
represent the minimum path sum values of the previous row, and update the values with the sum of the value at that indes and the minimum 
child node ofeach index. Then these updated values will be the new previous row. So we get to the first row with the minimum path, and at
the end we return the value at index 0 which represents the overall minimum path sum in the tree.
Now if there are n rows, the time complexity is O(n^2) and a memory of O(n) since there are roughly n^2 elements in the input, and we 
store n+1 values in the result array. 

"""


"""Dynamic programming solution"""

#O(n^2) time | O(n) space
def minimumTotal(triangle):
    rows = len(triangle)
    dp = [0]* (rows+1)
    

    for row in reversed(range(rows)):
        for col ,value in enumerate(triangle[row]):
            dp[col] = value + min(dp[col], dp[col+1])
    return dp[0]





"""Recursion soluton - postorder dfs"""
#O(n^2) time | O(n^2) space
def minimumTotal(triangle):
    rows = len(triangle)
    return helper(triangle,0,0, rows, {})


def helper(triangle, row, col, rows, memoize):
    if row >= rows:
        return 0
    
    key = str(row) + ":" + str(col)
    if key in memoize:
        return memoize[key]

    leftChild = helper(triangle,row+1, col, rows)               #go left
    rightChild = helper(triangle, row+ 1, col + 1, rows)        #go right

    minChild = min(leftChild, rightChild)                       #the following lines is the visit step
    value = triangle[row][col]
    memoize[key] = value + minChild
    return memoize[key]

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
print(minimumTotal(triangle))
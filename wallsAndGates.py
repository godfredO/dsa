"""
You are given a m x n 2D grid initialized with these three possible values.
-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate 
is less than 2147483647. Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should 
remain filled with INF.

Input: [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output:  [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Explanation:
the 2D grid is:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

the answer is:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

Example2
Input: [[0,-1],[2147483647,2147483647]]
Output: [[0,-1],[1,2]]

So we have a matrix with empty rooms, doors and walls represented by inf, 0, -1 and we are asked to replace every room (inf) with the distance
to the nearest gate. If a room is completely walled off, then we should leave if as inf. So if a specific room is distance 2 away from one gate
and distance 3 from another gate we replace the inf with 2. Now the naive or brute force solution is to loop through the matrix, and from each
empty room, we start a dfs to find all the gates that are reachable from the room, calculate their distance to the room and replace the inf 
with the minimum distance. Since dfs takes O(n*m), and there could be up to n*m rooms, repeating the dfs for every possible room will yield a
time complexity of O((n*m)^2). 

Now the more optimal approach would be to loop through the matrix, and start a bfs from each gate, knowing that a gate is 0 distance from 
itself, so if there is a neighboring room, it will be 0+1=1 distance away from the current gate. And from the gates neighboring rooms we know
that their neighboring rooms are now 1+1=2 and all the rooms distance 2 away, if they have neighboring rooms, those rooms are distance 3 away.
Now a specific room may be a distance of 3 from the first gate we encounter but a distance of 2 from the second gate we encounter. How do we
then detect this and make sure we are storing the minimium gate distance for the room? The answer is to do a simultaneous bfs from all gates 
in the matrix. So we first find all rooms that are a distance of 1 from each gate. Then from all rooms that are a distance of 1 from a gage we
find all the other rooms that are a distance of 2 from each gate ie 1+1. Then from the rooms that are a distance of 2, we find all the other
rooms that are a distance of 2+1=3 from a gate. So this is a simultaneous bfs solution, like minimumPassesOfMatrix.py. We initalize our queue 
with all the gates in our matrix. Then our main while loop runs our queue is non-empty, we take the current size of our queue and decrement 
this variable each time we pop and process a node on the queue until the currentSize variable is equal to 0. So we initialize the queue with 
the gate positions in our matrix, take the size of the queue, pop and process all rooms that are distance 1 from each gate, add the processed 
room positions to our queue and decrement the size variable. When the size variable reaches 0, we return to the top of the loop, now with the 
positions of rooms that are distance 1 from a gate, take the size of the queue and each time we pop a room from the queue, and process its 
neighboring rooms with a distance of 1+1 from a gate, add each neighboring room to the queue and when all four neighbors are processed, we 
decrement the size variable by 1.  And once our queue is empty, we stop the algorithm. This simultaneous bfs is also used in wordLadder.py.
And the time complexity of this solution is O(n*m) time and space. The space complexity is for the visited matrix so that we dont visit the
same room twice. And since we only add unvisited neighbors in bfs, we can skip the visited check after popping but adding it doesnt affect it
since we will never add a visited position to our queue.
"""
from collections import deque
def wallsAndGates(rooms):
  rows, cols = len(rooms), len(rooms[0])
  
  queue = deque()
  for row in range(rows):
    for col in range(cols):
      if rooms[row][col] == 0:
        queue.append([row,col, 0])  #initialize queue with gate positions and distance 
  

  visited = [[False for col in range(cols)]for row in range(rows)]  #visited matrix to avoid re-processing a node
  while queue:
    currentSize = len(queue)

    while currentSize > 0:
      position = queue.popleft()
      row, col, distance = position
      

      if visited[row][col]:
        continue
      visited[row][col] = True

      directions = [[1,0],[-1,0],[0,1],[0,-1]]

      for direction in directions:
        deltaX, deltaY = direction
        nrow, ncol = row + deltaX, col + deltaY #use the direcitons to calculate neighbor positions
        if nrow < 0 or nrow >= rows or ncol < 0 or ncol >= cols or visited[nrow][ncol]: #if neighbor position visited or invalid
          continue
        if rooms[nrow][ncol] == 2147483647: #only process rooms ie no neighboring walls or gates
          rooms[nrow][ncol] = distance + 1
          queue.append([nrow,ncol,distance + 1])
          print(distance+1)

      currentSize -= 1  #decrement currentSize by 1 after processing all the neighbors of popped node
    
  
  return rooms




rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# Output=  [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

rooms = [[0,-1],[2147483647,2147483647]]
# Output = [[0,-1],[1,2]]
print(wallsAndGates(rooms))
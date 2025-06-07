"""
You have a bag of fixed weight capacity, and you have items of different weights and values. The aim is to
fill the bag without exceeding the bag's weight capacity, while maximizing the value of the bag's contents
As a dynamic programming problem, this involves a grid of values. The rows represent the items, the columns
represent the possible weights of the bag up to the capacity. The reason for the columns is because the aim 
of dynamic programming is to solve sub-problems that will help solve the big problem. So if the capacity is 
4lbs, we solve for a capacity of 1lb, then 2lb, then 3lb to solve for 4lb capacity. The columns break the
problem down to sub-problems, per the constraint. 

Each cell represents the maximum value of a bag that fits in a bag of the column's capacity, which may or 
may not contain the item of that row. Say we are in column of 2lbs, the current row's item can't go into a 
2lb bag if its weight exceeds 2lbs. To track the maximum value for that weight, when an item doesn't fit 
into a bag, we copy the value of the preceding cell. Even if the item could go in, we want to make sure we 
don't lower the maximum value. So we take the maximum of the previous row and same column versus the sum
of the items value and the maximum value of the additional weight we need to partially fill up the bag of
the current weight. Thus we propagate the value of the preceding cell either because its value exceeds the 
value of a bag including the current item and another weight or because the current item can't fit into the
current bag gives us. This way, to find the partially filled bag we want, we only have to subtract the 
item's weight from the column's weight, go to that column of the preceding row and read the maximum value 
for that additional weight. This is how we use the solutions of sub-problems, here smaller bag weights, to 
find the solution of bigger problems.

To easily handle edge cases, its customary in dynamic programming to include a buffer column and row. In 
this question, that will be a 0lb column and a empty item. The empty item row ensures that for the first 
item, there is a row with 0 value to compare to. The 0lb column ensures that if after subtraction the 
current item needs to go in the current bag alone because its weight fills up the current bag entirely,
we simply add 0 to the current item's value before comparing to the current maximum value for the current
weight which is stored in the previous row. This also ensures that the value at the bottom right corner of 
the grid will always contain the maximum value of the actual bag's capacity, and the answer to the problem.

We are assured that each item has an integer weight. What if we have items of non-integer weights? 
That affects the range of column indices. Say we are solving for a bag of 4lbs but one item is 0.5lb.
We need to account for 0lb, 1lb, 1.5lb, 2lb, 2.5lb, 3lb, 3.5lb, 4lb. Default range() function only takes 
integer steps so you can generate the columns a while loop and use range(0, len(columns) +1), for the
indices.

We know that the final value is stored in the bottom right corner of the grid. How do we get the items 
that comprise our maximum value? We just backtrack on the logic, starting from the bottom right corner 
of the grid and remembering that we have a buffer empty item row and a buffer empty item column. We
start by storing a pointer for the last row and last capacity as our current grid item and current grid
capacity. Inside a while loop, we check if the current item was added by comparing the value in the 
current cell, with the value in the cell directly above it. If the value is the same, we didnt add the 
current item, so we decrement our row pointer by one, to check the previous item. Otherwise, we store 
the actual current item index, which is staggered from the grid item index by 1 due to the buffer row. 
We also remove the current item's weight from the current capacity and decrement row pointer. Make sure
to read the current item's weight before decrementing the row pointer. We keep doing this until we reach 
a buffer row or column. We reverse the stored item index values to get the order in which the items 
were added. 

"""

#O(nc) time | O(nc) space
def knapsackProblem(items,capacity):
    #items vs capacity, starting from empty and 0 capacity, initializing with 0's everywhere for base cases 0 items, 0 capacity
    knapsackValues = [[0 for x in range(0,capacity+1)] for y in range(0, len(items) + 1)] #capacity + 1 to ensure actual capacity is included
    #loop to update maximum values in capacity
    for i in range(1, len(items) + 1): #choose the row, ie current item, starting from second row ie avoiding 0 items row which should stay 0
        currentWeight = items[i-1][1] # current items's weight, 
        currentValue = items[i-1][0]  # current items value (since i is 1-indexed, i-1 to get item index)
        for c in range(0, capacity+ 1): #choose column ie current capacity, capacity + 1 to ensure actual capacity is included
            if currentWeight > c: #we cant fit current item 
                knapsackValues[i][c] = knapsackValues[i-1][c] #value directly above, maximum value without current item
            else:#else if we can fit the item in the current capacity
                knapsackValues[i][c] = max(knapsackValues[i-1][c], knapsackValues[i-1][c-currentWeight] + currentValue) #choose max value
    return [knapsackValues[-1][-1],getKnapsackItems(knapsackValues, items)]

def getKnapsackItems(knapsackValues,items):
    sequence = []  #sequence of items
    i = len(knapsackValues) - 1  #current item index, start backtracking from last item and last value 
    c = len(knapsackValues[0]) - 1 #current capacity index, start backtracking from last item and last value
    while i > 0: # while not at first row, which is the empty item buffer row
        if knapsackValues[i][c] == knapsackValues[i-1][c]:#if current value is same as value above, then current item is not included in knapsack
            i -= 1 #so move up
        else: #if the two values are not equal, the current item is in the knapsack
            sequence.append(i-1) #so add its index in items array to return array ie i -1
            c -= items[i-1][1] #then remove the current items weight from current capacity
            i -= 1  #and move up
        if c == 0: #if capacity is 0, we reached the buffer column, we are done
            break   #so break
    return list(reversed(sequence)) 


items = [
    [1, 2],
    [4, 3],
    [5, 6],
    [6, 7]
  ]
capacity = 10
print(knapsackProblem(items,capacity))
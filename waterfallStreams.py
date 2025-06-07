
"""The input is a 2-d array that represents the structure of a waterfall and a integer. The 2-d array contains 0's and 1's. A 0 means open 
space, a 1 indicates an obstruction like a block. The first and last rows of the array will always be 0's for open space. The integer
in the input represents the column in the first row where the source of the water is situated. Upon starting, the water flows straight
down until it reaches an obstruction at which point it divides into two; one half of thestream goes right and the other goes left and 
then around the obstruction if there is open space to the right or left. If a stream has no way to go, it becomes stuck. We can assume 
that all of the water will always be inside the walls of the waterfall ie the bounds of the 2-d array. This is a traversal style problem 
like spiral traverse or zigzag traverse just with different boundary conditions and allowable movements. We can also assume tha the last
row of the 2-d array represents buckets where the water reaching each column is collected. The question asks to write a function that
returns the percentage of water inside each of the bottom buckets after the water has flowed through the entire structure.

Optimal solution basically starts from the second row, first column, having already updated the appropriate source column(s) in the first 
row with -1 to represent water, since 0 represent space and 1 represents block. At each stage of the iteration through the matrix we check 
if there is water in the row above. If there is, we check if there is a space or a block at the current position. If there is a space at the 
current position, we move the water in the row above to the current iteration position. If there is a block at the current position, we divide 
the water above to the left and to the right. This entails looping to the left / right of the water above (left/right boundary technique). If 
there is a block on the left / right, that split water is stuck. If there is a space, then we check if the position below has a space or a 
block. If there is space below the left / right split water, we move the water down in that column. Thus we keep going left / right in search 
of a space on the left / right (left/right boundary technique) that also has a space below to move the split water to. If we encounter a block 
on the left / right or if we encounter left / right spaces that have blocks below, the water will be trapped. Also, when we move water down, 
we actually just increment by adding to the 0 (for space). This allows us to easily merge two flows by first adding a first negative number 
to 0 then a second negative number to the first negative number. At the last row, we multiply by -100 to convert the water representation to 
positive whole numbers.

We start by making a copy of the first row of the 2-d array as the initial rowAbove pointer. Then we update the source column with -1 as this
represents the prescence of water, 0 represents the presence of open space and 1 is a block. Then we loop from the second row up to the last
row. We make a copy of the current row in the loop for the currentRow pointer(reference). The reason for making copies of rowAbove and 
currentRow is to ensure that we can make modifications without altering the input array itself. We then loop through each column of the 
currentRow and first thing is to store a valueAbove reference to the value at the current column in rowAbove ie 0,1 -num. Then we store two 
booleans, one hasWaterAbove stores if the valueAbove is negative, the second hasBlock checks if the current column in the current row is a 
block. Then if there is no water ie hasWaterAbove == False, we continue to next column in the current column.  If we don't continue here, it 
means that there is water in valueAbove ie valueAbove = rowAbove[idx] < 0 == True. Next if the current position is open space,ie not hasBlock, 
meaning currentRow[idx] == 0,  we move the water in valueAbove to it by 'incrementing' the 0 at current postion with the water in valueAbove, 
then continue to the next column. If we havent hit any of the previous continue statements, it means we have water above but there is a block 
at the current position. Thus we need to split this water. To do this we use a variation of the left / right boundary technique. First , we
split the water above by dividing valueAbove / 2. We then initilize rightIdx at the current columnIdx and we loop rightwards as long as
there is a position to move to ie, rightIdx + 1 < len(rowAbove) since remember the split water is going left and right until it finds an open
space. So if there is space to the right, we entire a while loop and increment rightIdx ie rightIdx + 1. We then check the position at rightIdx
is a block ie rowAbove[rightIdx] == 1. If it is, we break out of the rightward while loop meaning the split water is stuck. If we don't break 
out of this rightward while loop it means that we found an open space for the rightward split stream. Next thing, we check if the position in
our current row below rightIdx is an open space, with or without water. Here it is essential to not use == 0 because we might have 'incremented'
a position with water so is currently negative. So we check if currentRow[rightIdx] != 1 ie as long as the position is not a block, we 
'increment' the value at this position, 0 or neg, with splitwater, then we break out of the while loop. It is essential to use break not 
continue because we either case we are done with the rightward exploration, continue will jump back to the while loop condition.
Now we do something similar with the leftward split water. As long as there is a leftward position to move into (after initializing leftIdx to
idx), ie leftIdx - 1 >= 0, we move into the while loop and make the leftward jump ie leftIdx -= 1. Then we check if the position above has a
block ie rowAbove[leftIdx] == 1 in which case we break out of the leftward while loop. Othewise, if the leftIdx in the currentRow isnt a block
ie 0 or neg, we move the split water to it then break. For both the leftward and rightward movement of split water, as long as the rowAbove at 
leftIdx or rightIdx has open space and the corresponding position below in the currentRow has a block, neither break statement will actually be
hit meaning the split water keeps moving rightward and leftward until the loop terminates or it meets a block in rowAbove and breaks or it
finds an opens space with or withour water below to flow into. Both the rightward and leftward while loops are nested inside the for loop, that 
is looping through each column of the currentRow.  Thus at after updating each column, in the current row with this for loop, we move the 
rowAbove pointer to point to the current currentRow so that the outer for loop will choose the next currentRow. At the end of this outer for 
loop the last row of 2-d matrix will have rowAbove pointing to it, so we use a loop, a map() function here, to convert each number in each 
column to a positive whole number by multiplying by -100 and we retun a list of these values as the final answer.
"""

#O(w^2*h) time | O(w) space
def waterfallStreams(array,source):
    rowAbove = array[0][:] #make a copy of the first row to initialize rowAbove
    rowAbove[source] = -1 #update rowAbove at the source column to hold -1 for initial water flowing
    for row in range(1,len(array)): #current row starts from second row to last row, Python range bound exclusivity
        currentRow = array[row][:] #make a copy of current row so that modifying the copy doesnt modify the input array
        for idx in range(len(array[row])): #loop through each column / position in current row
            valueAbove = rowAbove[idx] #access the value above, which maybe water (<0=water) or not (1=block,0=space)
            hasWaterAbove = valueAbove < 0 #check if there is water above current position. 1=block, 0=space, < 0=water
            hasBlock = currentRow[idx] == 1 #check if there is a block in current position. 1=block, 0=space, < 0=water
            if not hasWaterAbove: #if there is no water above the current position, ie valueAbove is not negative
                continue #do nothing just move to the next column in current row
            if not hasBlock: #at this point, there is water above. So if there is no block (space or water) at current position
                currentRow[idx] += valueAbove #then move the value above, which is water, below ,by incrementing value below
                continue #and then continue to next column in current row
            
            #if we dont hit any of the continue statements above then there is water above and a block below so we split 
            splitWater = valueAbove / 2 #split water above into 2
            rightIdx = idx #initialize the right side index, starting from current column
            while  rightIdx + 1 < len(rowAbove): #use a while loop to keep moving rightward until we out of bounds
                rightIdx += 1
                if rowAbove[rightIdx] == 1: #if there is a block in row above at right idx, water is trapped
                    break #so break our of inner loop since water has no where to go
                #if we dont break, its because there is a space in rowAbove[rightIdx] so we check if there below there isnt a block
                if currentRow[rightIdx] != 1:#thus if current row at rightIdx isnt a block ie space or water
                    currentRow[rightIdx] += splitWater #we increment the value in current row at right idx with split water
                    break # since we moved right split water down, so we break out of this while loop bcos no need to keep going right
            
            leftIdx = idx #we mve the remaining half of split water left, initializing at current column
            while leftIdx - 1 >= 0: #note the >= 0 because if the next left position is the first column we are still in bounds
                leftIdx -= 1  #move leftward since we checked that this position is valid
                if rowAbove[leftIdx] == 1:  #if we are blocked by this leftward move
                    break #water is trapped so break out of inner loop
                if currentRow[leftIdx] != 1: #if we are not blocked by leftward move and we are not blocked below
                    currentRow[leftIdx] += splitWater #then move the split water below by incrementing the value stored below
                    break #then break out of this while looop since we have finished moving the left split water down,

        rowAbove = currentRow #set rowAbove to be equal to the modified currentRow with updated water values
    #use rowAbove for value convertion , since rowAbove is updated with currentRow before inner loop breaks and currentRow is local
    finalPercentage = list(map(lambda num: num * -100 ,rowAbove)) #transform water values from negative fractions to whole + percentages
    return finalPercentage




array = [
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0]
  ]
source = 3
print(waterfallStreams(array,source))
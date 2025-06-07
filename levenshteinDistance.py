"""The input is two strings and the question asks to return the minimum number of edit operations that need to be performed on the first
string to obtain the second string. There are three edit operations: insertion of a character, deletion of a character and substitution
of a character for another. Eg if str1 = 'abc' and str2 = 'yabd' the answer is 2, ie insert 'y' and substitute 'c' for 'd'. 

The first thing is to decide what data structure will be used to build up our solution. In the maxSubsetSumNoAdjacent question we are 
given an array of positive integers and we used an array as the data structure to build up our solution. In the minNumberOFCoinsForChange
and numberOfWaysToMakeChange questions we had a denominations array and an integer ,n, and again we used an array to build up the solution
for change values from 0 to n. In this question we are given two strings, and since we here we use, a matrix. The column indices of this 
matrix will be representing the letters of str2 starting from the empty string. The row indices will be representing the letters of str1 
starting from the empty string. These can also be interchanged for the same solution and thought process. Thus the matrix[0][0] will be 
"" v "". In the code this table is called the editsTable. At each position in this 2D matrix, we're gonna store the minimum number of edit 
operations, that we can perform on a sub-string of the first string to turn it into another substring of the second string. So starting out 
at matrix[0][0] we ask, what is the minimum number of edit operations that need to be performed on the empty string (row) to turn it into 
the empty string (col). Since both substrings are equal to each other, the answer is 0. So to fill out the first row we ask the minimum 
number of edit operations needed to turn the empty string (row) to the substring ending each col index's letter. For the substring with 1 
letter we will need 1 operation ie inserting that letter into the empty string. For the substring with 2 letters, we need two insertions to 
transform the empty string into the substring ending at that index. So since we asking for the minimum edit operations to transform an empty 
string to a substring at each index, the first row of the matrix will read 0,1,2,3...LastColIdx. That is if there are 8 columns (7 letters 
in str2 plus the empty array), the answer will read 0,1,2,3,4,5,6,7 representing the number of insertions needed to convert the empty string 
to the substring ending at the various letters. In the same way, we fill out the first column of the matrix by asking how may edit operations
will be needed to convert the substring ending at each row index to the empty string (col index). At rowIdx = 1, we have 1 letter and we will
need 1 deletion in order to convert to the empty string. At rowIdx = 2, the substring has two letters so we need 2 deletions. In fact the
entire first column will read 0,1,2,3,...,LastRowIdx, representing the minimum number of deletions required to transform the substring ending
with the letter at that index into the empty string. So now we have the first row filled out and the first column filled out.These represent
the base case, ie from empty string to substring (insertions) and from substring to empty string (deletions). 

In the code, we fill these out in the two steps. We first initialize the matrix with the first row base case values and then we use a for loop 
to fill out the update the first column. ie editTable = [[i for i in range(len(str1)+1)] for y in range(len(str2)+1)] will repeat the values 
in range(len(str1)+1) a range(len(str2)+1) number of times. So if str1 has length 3 and str2 has length 5 then [0,1,2,3] representing the 
values in range(3+1) will be repeated for each value in range(5+1) ie 6 times [[0 1 2 3],[0 1 2 3],[0 1 2 3],[0 1 2 3],[0 1 2 3],[0 1 2 3]]. 
Then since the first will be reading 0,0,0,0,0,0 we need it to read 0,1,2,3,4,5. To do this we have a for loop that runs for the total number
of rows in the array, starting from the second row (since matrix[0][0]=0 is correct) and at each point we say the value at the current row,
first column =  1+ value at previous row, first column. We choose the current row with the current index in the for loop and starting at 
row 1, we are able to update it to 1 by adding 1 to row 0 ie matrix[1][0] = 1 + matrix[0][0] = 1. And then at matrix[2][0] = 1 + matrix[1][0]
= 1 + 1 = 2. This pattern is common in dynammic programming questions where the first row / col position represents an empty string or 0 or 
some empty value and we fill the first row and column for the base cases.

So how do we fill in the inner positions ie matrix[1][1] ie converting a 1 letter substring to another 1 letter substring?. In the specific 
case where the row letter and the column letter are the same (that is the two substrings end in the same letter), the answer is always going 
to be to copy the upper diagonal value since these reduces the question to one that has already been answered ie. Therefore if str2[row-1] 
== str1[col-1], the edits[row][col] = edits[row-1][col-1]. Because we started our rows and columns with the empty string, we essentially 
shifted the indices of the characters in the original string by 1 compared to their indices in the edits table. Hence the -1 in str2[row-1]
and str1[col-1] when picking out the current letters to compare. Say we are comparing 'a' vs 'ya', since they both share 'a', we ignore 
this shared 'a' and reduce the quesion t '' vs 'y', thus we choose the answer from the upper diagonal.
For the general case we look at the three adjacent values and choose the mininum and add 1. The three adjacent values are the value in the 
same row, col to the left (matrix[row][col-1]), the value in the row above same column (matrix[row-1][col]) and the value in the upper 
diagonal (matrix[row-1][col-1]) ie a row above and col to the left. So if we are comparing 'a' vs 'yab', then left value represents starting 
from 'a' vs 'ya', the value above represents starting from '' vs 'yab' and the diagonal value represents '' vs 'ya'. The minimum value will 
be to insert b into 'ya' ie we choose the left value and add 1, since that is a value of 1 and the others are valued 2 and 3 respectively.
The final answer that we return is the answer at matrix[lastRow][lastCol].

Now dynammic programming solutions are typically optimized for space only, by storing on the values one needs instead of the entire data
structure. Here we only need the current row and the previous row which will hold a total of 2*col values. Thus to further optimize, we
choose col to represent the letters of whichever string is shortest. The reason is that even though the question is asking to transform
str1 to str2 the answer is the same as asking to transform str2 to str1. Insertions in one statement become deletions in the other and
substitutions just reverse the letters substituted but the minimum number of edit operations remain the same. So we start by initializing
the small string which will represent the number of columns and the big string which will be the number of rows. So we say something like
small = str1 if len(str1) < len(str2) else str2 and big = str1 if len(str1) >= len(str2) else str2. So we put the less than in the small
comparison and the greater than or equal to in the big comparison. We initalize two arrays of len(small) + 1 called evenEdits and oddEdits.
evenEdits (row 0 and even rows edits) represents the current row when we are at a 'even' rowIdx ie 0,2,4 ie rowIdx % 2 == 0. And oddEdits
is rowIdx 1,3, 5 ie rowIdx % 2 == 1. We initialize even edits with the  [value for value in range(len(small) + 1)]ie we know that the 
values in row 0 which is one of the base cases will be these values. And oddEdits we actually initialize to None values ie
[None for value in range(len(small) + 1)]. Compared to the non-optimized solution we will have to fill out the values of the first column
inside the main loop. So we go into our main loop which will run big+1 number of times, ie for rowIdx in range(1,len(big)+ 1), starting from
the second row. Then we check if this rowIdx is even or odd using the modulo 2 operator. If rowIdx % 2 == 1: currentEdits= oddEdits and
previousEdits = evenEdits else: (rowIdx % 2 == 0) currentEdits = evenEdits and previousEdits = oddeEdits. With currentEdits and previousEdits
assigned, we update the first column of currentEdits to be the same value as the rowIdx. That is because the first column of row 0 will
contain 0, the first column of row 1 will contain 1 etc. This shortcut could also have been used for filling out the first column of the
un-optimized solution ie for row in range(1,len(str2)+1): edits[row][0]= row. Conversely, the method used in the unoptimized solution can
also be used here ie currentEdits[0] = 1 + previousEdits[0]. With the base case filled up, we then start looping through the columns starting
from the second colum ie colIdx=1. So for j in range(len(small)+ 1): we first check if the ending letters are the same ie big[rowIdx - 1] ==
small[colIdx - 1]. If ending letters are the same for the substrings, we say the value at the currentEdits[colIdx] = previousEdits[colIdx - 1]
else currentEdits[colIdx] = 1+ min(currentEdits[colIdx - 1], previousEdits[colIdx], previousEdits[colIdx-1]), representing the left value,
the above value and the upper diagonal value. So what do we return from the function? How do we know the last value. We know the number of 
rows are determined by big so if big is the len(str2) and str2 has a length of 3 the know the rowIdx will be 0,1,2,3 ie the lastRowIdx
== big and if the len(big) is odd we know that the lastRowIdx is oddEdits and vice versa. So to return the final value, we choose based on
len(big) %2. So we can say return evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1]
"""

#O(nm) time | O(nm) space
def levenshteinDistance(str1,str2):
    #there are as many columns as there are in str1 and as many rows as there are in str2
    edits = [[x for x in range(len(str1)+1)]for y in range(len(str2)+1)] #str1 + 1 indices repeated str2 +1 # of times
    
    for i in range(1, len(str2) + 1): #taking care of first column
        edits[i][0] = edits[i-1][0] + 1  #update values of first column
    
    for i in range(1,len(str2)+1):  #for each row
        for j in range(1,len(str1)+1): #for each column in chosen row
            if str2[i-1] == str1[j-1]:  #if row and column letter is same
                edits[i][j] = edits[i-1][j-1] #diagonal
            else:
                edits[i][j] = 1 + min(edits[i-1][j-1], edits[i][j-1], edits[i-1][j])
    
    return edits[-1][-1]

#O(nm) time | O(min(n,m)) space
def levenshteinDistanceI(str1,str2):
    small = str1 if len(str1) < len(str2) else str2 #we want smallest amount of columns, so choose the shortest string as small
    big = str1 if len(str1) >= len(str2) else str2  #if equal length small is str1, choose the other string as big
    evenEdits = [x for x in range(len(small)+1)] # starting with row 0, len(columns) = small
    oddEdits = [None for x in range(len(small)+1)] #starting with row 1, len(columns) = small

    for i in range(1,len(big)+1): #the row we would be on had we stored full table
        if i%2 == 1:  #odd numbered row, starting from 1
            currentEdits = oddEdits
            previousEdits  = evenEdits
        else:         #i %2 == 0
            currentEdits = evenEdits
            previousEdits = oddEdits
        currentEdits[0] = i             #fill out the first column base case, equal to the rowIdx
        for j in range(1,len(small)+1):
            if big[i-1] == small[j-1]: #compare ending letters for substrings, -1 for shift, bigString, smallString
                currentEdits[j] = previousEdits[j-1] #copy upper diagonal value
            else:
                currentEdits[j] = 1 + min(previousEdits[j-1], previousEdits[j], currentEdits[j-1])
    
    return evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1]




str1 = "abc"
str2 = "yabd"
print(levenshteinDistanceI(str1,str2))
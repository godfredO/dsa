"""Radix sort is an algorithm that sorts numbers one digits at a time. In this application Radix sort is only for sorting positive numbers. 
Radix sort works because we know something about the possible digits that make up numbers. All the digits will be 0 - 9. Radix sort does 
this with the help of counting sort or bucket sort as seen in the three number sort question. In that question too we were given an order 
array which contained the set of possible numbers in the other array and sorted them by counting the instances of each order array element. 
Radix sort is going to use counting sort in the same way but our order array here is the set of digits in base 10 system ie 0-9. Because 
radix sort sorts the array of numbers by looking at one digit at a time, it starts by looking at the 1's column, then the 10's column, then 
the 100's column, then 1000's column etc, assuming a digit of 0 for any number that doesnt have any of these siginifcant figures. Thus if 
sorting 3 and 100, radix sort assumes 0's for the 10's and 100's column for 3 ie 003 and 100. As a result of this radix sort repeats the 
counting sort helper method d times where d is the number of digits in the maximum number. 

In the code, we do this by first finding the maximum number and using a while loop that floor divides this max number by increasing powers 
of 10 ie number base system as long as this division is greater than 0. The increasing powers of 10 here constitute the place value of the 
digits. 

What happens inside the countingSort helper function? First we have two data structures. The counts data structure counts the instances of 
each digit in the numbering system 0-9 that occurs in the current place value being considered. So if the current place value is the 1's 
column, we count the number of 0-9 that occurs in the 1's column of each number and record it against the appropriate digit index in the 
counts data structure. This data structure starts off with a count of 0 for each digit index and in base 10 numbering system, will be of 
length of 10 ie 0-9. The other data structure is the sorted data structure which is the same length as the input array. So with the place 
value exponent that is passed into the counting sort function, we calculate the current place value as 10 ^ placeValueExponent ie if 
placeValueExponent is 2, then we are currently counting the 10^2 , 100's column. 

For the current digit placement, floor division cuts away the unnecessary number placements, making the current digit placement the last 
value, so that the modulo operation can extract the current digit placement. So when we are on the 123 if we are on the 10's, then floor 
division by 10**1 will yield 12 and the modulo operation will extract the 2. So We loop through the input array, extract the digit at 
the current place value using (num // 10^ placeValueExponent) % 10. Then increment the count of the resulting digit inside the counts 
data structure. Now in the three number sort problem, we determined the start point for modifying the input array for a particular order 
array element by cumulatively summing the counts in the order of the order array. Here, the order array is the digits of the numbering 
system we do something similar. We add the update the count of 1 to a cumulative count by adding the count of 0 and update the count of 
2 to a cumulative count by adding the result to the actual count of 2 and so forth. Thus we get the count of each digit in the array of 
numbers, then we convert that to a cumulative count.

We then loop backwards, again like the three Number Sort question. Note that range(start,stop,step) can be used to loop backwards by using
a negative number as step as well as wrapping in reversed() . Anyway, with a backwards loop starting from the the end of the input array, we
extract the digit at the current place value, using the same formula above, and with the extracted digit we decrement the cumulative count
at that digit in the counts data structure. This decremented value represents the index of the number in the sorted array. That is if
there is a count of 1 at digit 0, the number with that digit will go in first place ie count - 1 = 1 - 1 = index 0. With the sortedIndex
calculated, we place the current number in that position in the sorted array. The reason for looping backwards is to ensure we maintain
the sorted order from the previous run of counting sort which sorted the numbers according to the previous place value. When all the input 
array numbers are have been placed at the appropriate place in the sorted array, we modify the input array to look exactly like the sorted 
array. Thus we the sorted array is an immediary dat structure. 

Thus by repeating this for each digit placement in the largest number,we are able to sort the input array. The counting portion of count sort 
is O(b) where b is the length of the order array ie the digits in the numbering system. When we loop backwards to place the input array 
numbers in the sorted data structure according to the current place value being considered, that runs in O(n) and when we loop over the sorted 
data structure to modify the input array, that also runs in O(n) giving the countingSort method an overall time complexity of O(n+b) and a 
space of O(n+b). And since the counting sort is repeated d times the overall complexity of this solution is O(d*(n+b)). We also need to handle 
the edge case of an empty array because we would throw an error when we determine the maximum number of an empty array.

So like the three Number Sort solution, when using counting sort, count each order array element, convert the counts to cumulative counts,
then loop backwards and place the elements in sorted order according to the order array."""

#O(d*(n+b)) time | O(n+ b) space
def radixSort(array):
    if len(array) == 0 : #edge case, empty array
        return array

    maxNumber = max(array) #maximum number in array to determine the number of times to call countingSort
    digit = 0 #this will be used as an exponent for base numbering system ie ones = 10 ^ 0 to yield place value

    #this while loop will call counting sort d number of times, d is the number of digits in maxNumber, sorting numbers by their digits
    while maxNumber // (10 ** digit) > 0: #10 to exponent digit,so 10 ** 0 = 1, while maxNumber divided place value is not a fraction
        countingSort(array,digit) #call countingSort to modify array till numbers have been sorted by their digits
        digit += 1  #move to the next place value
    return array

def countingSort(array,digit):
    sortedArray = [0]* len(array)  #Python list, length n
    countArray = [0]*10 #there are 10 digits in base 10, length b
    digitColumn = 10 ** digit  #the current place value, 10 ^ digit ie ones is 10^0 = 1

    #counter for number of times each digit appears in array
    for num in array: # O(n)
        countIndex = (num // digitColumn) % 10 #extract place value digit in current number, which is also same as its index in countArray
        countArray[countIndex] += 1 #increment the count of extracted digit in countArray. digit 5 has index 5 in countArray (0 -9)
    
    #updating the furtherest position that numbers containing a particular digit in current place value should be placed
    for idx in range(1,10): #starting from second position to last, O(b)
        countArray[idx] += countArray[idx-1] #cumulatively add previous digit count 
    
    #this is where we loop backwards and place numbers in sorted array based on the digits in the current place value
    for idx in range(len(array)-1, -1, -1): #loop backwards through array and place the numbers include index 0 by going to -1, O(n)
        countIndex = (array[idx]//digitColumn) % 10 #extract digit used for this round of sorting, which is same as its index in countArray
        countArray[countIndex] -= 1  #reduce because a number is gonna be placed because of extracted digit
        sortedIndex = countArray[countIndex] #position in sortedArray, pick the current value stored as furtherest position in countArray
        sortedArray[sortedIndex] = array[idx]
    
    #now modify original array, so that we maintain the order from the previous countSort count
    for idx in range(len(array)):       # O(n)
        array[idx] = sortedArray[idx]





array = [8762, 654, 3008, 345, 87, 65, 234, 12, 2]
print(radixSort(array))
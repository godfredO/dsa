""" In this question, we are given an array of distinct integers and an integer representing a target sum and asked to write a function
that finds all quadruplets in the array that sum up to the target sum and return a 2-d array of all quadruplets. This question is like
the two number sum and three number sum questions and generalizes techniques and ideas from those with a few specific tweaks.

In the two number sum question the optimal solution (when the array is not sorted), is that we iterate through the array and check if
the complement of the current number is in a hashtable and after the check we add the current number to the hashtable. Checking for the
complement before storing the current number in the same loop ensures that we do not double count pairs (as opposed to storing every
number in the hashtable in one loop and later checking for complements in another loop). We do something similar here by first realising 
that the sum of a quadruplet can be expressed as the sum of pairs. So we use a double nested for loop to generate the sum of all pairs
in the array, calculate the complement of the current sum and check if the complement of the current sum is in the hashtable. The outer
loop chooses the first addend and the inner loop chooses the second added. When generating pairs, the first added for loop goes from the
second element to the penultimate element, the second addend loop goes from right after the first loop's current index to the last element
in the array, we skip the last element in the first for loop because if we choose that as a first addend, there is nothing that comes after
it to choose as a second added. So after checking if the complement of the generated sums exist, its time to add the 
generated sums to the hashtable.

To avoid double counting the numbers that generate addends, we loop from index 0 up to the current
index in the outer for loop. That is we choose a first addend, generate pair sums with every number that comes after it, check for the
complements in the hashtable, before we add the sums of the first addend with every number that comes before it and add it to the 
hashtable. This ensures that for example, with a quadruplet [1,2,3,4] which sum up to  10, we dont count 1,2 and 3,4  then 1,3 and 2,4,
then 1,4 and 2,3. Instead when we are at 2 in the first addend loop we generate and check complements of 2's pair sums with  3,4 and after
that we add 2's pair sum with 1 to the hashtagle. This ensures that when we are at 3 we generate a sum with 4, check for the complement of
that sum which will be the sum of 1,2 and this sum will be in the hashtable, so we would have found a valid quadruplets, but when we get 
to 4, we will check for pair sum complements going forward ie we will not check for the complement of the 3,4 pair sum when our first 
addend for loop reaches 4 and when we are done checking for the pair complements with every number that comes after 4, then will we add
the pair sum of 3,4 when we loop backward to update the hashtable. This pattern achieves the purpose of not double counting or double
finding pair sums. Its like we choose a center in the first addend loop, expand right ward to find pair sum complements in the hashtable 
and when we are done expand leftward to add pair sums to the hashtable.
 
Thus the four sum question generalizes the complement,hashtable solution of the two sum question and the key point is that we check for 
complements going forward but add pair sums looking backward. As a result of this, the hashtable will be empty for all generated sums of 
index 0, so we might as well skip this when choosing the first pair sum addend. So the outer loop goes from index 1 to len(array) - 2 
(go to len(array) - 1 for Python's exclusive range function) because at index 0, we cant loop backward to add pair sums to the hashtable
since nothing comes before it. In otherwords, in the first added for loop we skip over index len(array) - 1 because, at that index, there
will be no complement pair sums to check and we skip index 0 because at that index, there will be no pair sums to add to the hashtable.
When we add the sum pairs to the hashtable we add it as sum: [[addend1, addend2]], since many different addends may add up to the same sum 
/ complement. And when we find the complement, we concatenate the current addends with the addends stored in the hashtable which could in 
theory contain n/2 values for some sum. Thus this solution is at best O(n^2) time when we have roughly one pair of addends for each pair 
sum in the hashtable and at worst O(n^3) if we find a complement that is the sum of n/2 different addend pairs. Thus this solution is at 
most two orders better and at worst one order better than the brute force (four nested loops). """

#O(N^2) time | O(N^2) space
def fourNumSum(array,targetSum):
    allPairSums = {}  #hash table to store pairs
    quadruplets = []  #this is the result array 

    #we can skip the first and last values in the array 
    #for the first value in the array, there is nothing in the hashtable
    #for the last value, there is no value after it to generate a pair complement with
    for i in range(1, len(array)-1): #from the second value to the penultimate value

        #first inner for loop, generate pair complements
        for j in range(i+1,len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in allPairSums: #this step can be O(n) giving an overall worse complexity of O(n^3)
                for pair in allPairSums[difference]:
                    #lists concatenation for valid quadruplets
                    #constant time operation because always a four number list no matter size of array
                    quadruplets.append(pair+[array[i],array[j]]) 
        

        #second inner for loop, where we add all sums of backward pairs to hashtable
        for k in range(0,i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairSums:
                allPairSums[currentSum] = [[array[k],array[i]]]
            else:
                allPairSums[currentSum].append([array[k],array[i]])
    
    return quadruplets

array = [7, 6, 4, -1, 1, 2]
targetSum = 16
print(fourNumSum(array,targetSum))
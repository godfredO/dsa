"""The question gives two inputs an array and an order array and asks to sort the elments in the array according to the order array being 
assured that if the array contains any elements, it would only contain instances of the elements in the order array. We are also assured
that the order array will always contain three elements. The question also requires constant space, ie we are required to modify the array 
in place to reflect the order in the order array. If this question allowed the use of auxilliary space, this solution would be trivial. But 
even with the constraint of constant space, we are able to generalize some techniques used in some standard sorting algorithms to solve this 
question. The first solution generalizes techniques from the bucket sort algorithm, the second solution genralizes techniques from bubble sort, 
the third solution generalizes techniques from insertion sort. """

"""The first solution uses the bucket method of couting all the instances of order array elements in the array and then modifies the array in 
place with those counts. Anyway in this first solution you count the instances of each element of the order array in the array and later modify 
the array with the counts and in the order of the order array. We loop through the array and for each element, we use the order.index(element) 
array method to grab the index of the order array element of which it is an instance and then using this index, increment the appropriate count 
in the count array, which doesnt worsen space complexity because we know it will always be three elements. Then with the valueCounts for each 
order element, we modify the array as follows; we start a for loop with a range(3) to generate the index for selecting the order element from 
the order array, and its count from the valueCounts array. Then to know starting index of modification, we add slice up the valueCounts up to
the select index and sum up the contents of the slice. This means for the first select index of 0, the slice will yield an empty list and the
sum of an empty list believe it or not is 0 so we start modifying at index 0. Then we start another for loop in range(valueCount[selectIdx]) 
and inside of this calculate the currentIdx as numBefore + loop index and then modify. Phew!!!"""
#O(n) time | O(1) space
def threeNumberSort(array,order):
    valueCounts = [0, 0, 0]  #buckets

    #loop to get counts of order elements in array
    for element in array:
        orderIdx = order.index(element)
        valueCounts[orderIdx] += 1

    #get value and counts
    for i in range(3):
        value = order[i]
        count = valueCounts[i]

        #update the array
        numElementsBefore = sum(valueCounts[:i]) #when i=0, sum([]) is 0
        for n in range(count):
            currentIdx = numElementsBefore + n
            array[currentIdx] = value

    return array

"""This solution pushes all instances of first order element to the front of array and pushes all instances of last order element to the end 
of the array, using a forwards pass and a backwards pass through the array. In the first pass we intialize the insert index at 0 and as we 
iterate through the array, if we find an instance of the first order element we swap / insert it at the insert index and then increment the 
index so that the next instance of the first order element goes to index 1. In the backward pass we initialize the insert index at the last 
index in the array and whenever we find an instance of the last element of the order array, we swap it with the element at the insert/ modify 
index and decrement the insert index, while looping in reversed order. It is essential that you iterate in reverse order so that we dont undo
correct changes. If you iterate and insert in opposite directions, and say you find an instance of the last element at index 3 and insert it
at the last index of say index 6, eventually when the for loop iterator gets to index 6, it will re-find the previously swapped element and
guess what swaps it again to a wrong position. Thus in pushing instances of the first element to the front we move both for loop iterator and
insert idx in the same direction from front to back. Similary when pushing instqances of the last element to the back, we move both for loop
iterator and insert idx in the same direction from back to front. Thus this solution bubbles all instances of the first order element to
the front and then bubbles all instances of the last order element to the back of the array, by moving two iterators according to the expected
sorted proximity order. This ensures if for example, the first element in the array is already an instance of the first order array element,
you swap it with itself. If you iterated from opposite directions and the first and last elements were both instances of the first order
array element, you would be swapping two instances of the first order element and putting one in the wrong position. So the only way to use
the bubble sort approach is to sort and insert in the same direction according to expected sorted proximity order. Front to back for the first
order element, back to front for the last order element. """
#O(n) time | O(1) space
def threeNumberSortII(array,order):
    firstValue = order[0]
    thirdValue = order[2]

    #forward pass
    #it is essential that you loop and insert forward so that you don't re-swap previously placed or correctly placed elements
    firstIdx = 0
    for i in range(len(array)): #for the first element loop left to right
        if array[i] == firstValue: #value check
            swap(array,i,firstIdx) #swap helper function
            firstIdx +=1 #increment insert idx after swap

    #backward pass
    #it is essential that you loop and insert backwards so that you don't re-swap previously placed or correctly placed elements
    thirdIdx =len(array) -1
    for j in reversed(range(len(array))): #for last element loop right to left
        if array[j] == thirdValue: #value check
            swap(array,j,thirdIdx) #swap helper function
            thirdIdx -= 1 #decrement insert idx after swap
    return array

"""This solution utilizes the relationship between instances of first and middle value of the order array ie all instances of the middle/second 
value should come after instances of the first value. We use three pointers f,s,t to keep track of the next index for an instance of the first
order element, instance of second order element and instance of third order element. While the f,t pointers just mark the next indices to 
insert instances of the first and third order elements, the s also serves as the pointer used to compare values and take actions. We initailize
t at len(array) -1 and we initialize both f,s at 0. So compare the value at index s to the order elements.  If it is equal to the first order
element, we swap the elements at index s and f and increment both pointers. If it is equal to the second order element, we increment only the
s pointer. If it is equal to the third order element, swap the elements at index s and t but decrement only t. This is because these pointers
are supposed to point to where the next instance should be inserted so s pointer is in the right place whiles t pointer needs to move inwards
by 1. If we ever get to a point where s pointer crosses t pointer, we exit out of the loop because every element is in the correct position."""

#O(n) time | O(1) space
def threeNumberSortIII(array,order):
    firstValue = order[0]
    secondValue = order[1]
    

    f,s,t = 0,0,len(array)-1  #pointer for first, second, third order value instances

    while s <= t:
        value = array[s]

        if value == secondValue:
            s += 1
        elif value == firstValue:
            swap(array,s,f)
            f += 1
            s += 1
        else:
            swap(array,s,t)
            t -= 1
    return array



"""This solution is the same as the other solution just utilizes the relationship between instances of the middle order value and last order 
value ie all instances of middle should before all instances of last"""
#O(n) time | O(1) space
def threeNumberSortIV(array,order):
    secondValue = order[1]
    thirdValue = order[2]

    f, s, t = 0, len(array)-1, len(array)-1

    while s >= f:
        value = array[s]

        if value == secondValue:
            s -= 1
        elif value == thirdValue:
            swap(array,s,t)
            t -= 1
            s -= 1
        else:
            swap(array,s,f)
            f += 1
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

array = [1,2,3,3,2,1,2,2,1,3]
order = [1,2,3]
print(threeNumberSortII(array,order))
"""The input is an array of integers and a toMove integer and we are asked to move all instances of toMove to the end of the array
In the solution to this question, we use two pointers, the first pointer is to find the next instance of toMove in the array and the 
second pointer is to find the next point of insertion for the next instance of toMove. Thus we iterate through the array with two 
pointers inside a while loop and the loop condition is that these pointers can't cross. Inside this while loop there is a second
while loop for the second pointer, which starts from the end of the array and decrements itself until it is pointing to a value that
is not the toMove integer. Once we have a new insert position, if the first pointer is pointing to toMove, we swap it with the value
at the insert position. In any case, we increment the first pointer to traverse the array. Since the inner while loop for the second
pointer will keep moving inward until it finds a new insert position, it is essential to add another loop condition that ensures that
the second pointer doesnt cross the first. This is because if we have moved all instances of two move to the end of the array but have
not finished traversing the array with the first pointer, the second pointer will effectively go past index 0 and we will throw an error
on the next iteration. Thus the crux of this solution is remembering to add while l < r and array[r] == toMove: decrement r to the 
inner while loop condition. This is much clearer once we work examples."""

"""
It is essential to add the l<r to the inner while loop to get the correct answer
Otherwise, we move the right pointer until we are at a number that isnt our target
Once we have the right pointer position, we check if the left pointer is our target
If it is we swap. In any case we keep movig the right counter.
"""


def moveElementToEnd(array,toMove):
    l = 0
    r = len(array) - 1

    while l < r:
        while l < r and array[r] == toMove: #it is essential to have l < r again
            r -=1
        if array[l] == toMove:
            array[l], array[r] = array[r], array[l]
        l += 1
    return array




array = [2,1,2,2,2,3,4,2]
toMove = 2

print(moveElementToEnd(array,toMove))
"""
Tags: Sliding Window; Two Pass

The question gives a non-empty array of integers and asks to return an array of equal length where the value at each index is the
product of all values in the input array except the value at the corresponding index of the input array. The question asks to do this
without the use of division. This is because if we are allowed to use division, the question becomes trivial as long as the array
contained non-zero elements only. We would use a single loop to multiply all elements in the array and then use a second loop to divide
this product by the value at value i. This trivial solution however will not work if any of the elements is 0 since we reduce the
numerator to zero for all indices which is wrong and run into division by 0 at some point.

So the restriction not to use division actually saves us from using buggy code. The brute force approach is to use a double for
loop, the first to choose the current index of the output array, the second for loop to go through the array and update a product
as long as the second for loop index is not equal to the first for loop index. This double for loop approach would work even if
the array contained a zero. The optimal approach is to use the left boundary, right boundary approach. Now we can write this code
using a while loop that expands outward from the current index but this is not necessary since we always go to the bounds of the
array itself every time. We can simplify the while loop approach by going from left up to but not including the current index and
then start the right boundary from just after the current index up to the  len(array) - 1.

This approach can still be further simplified by realizing that we can use two separate for loops instead of two separate while loops for
the left boundary / left product exploration / calculation since we know beforehand what our direction and indices will be if we start
from index 0 for the left boundary / left product up to but not including current index, and from index currentIdx + 1 up len(array) - 1
for the right boundary / righ product. With the sub-array products calculated The left/right boundary/products.

The two-pass method is used to improve the sliding window method in apartmentHunting.py"""


"""
Brute force approach of computing product
"""
# O(n^2) time | O(n) space


def arrayOfProducts(array):
    products = [1 for _ in array]   # output array

    for i in range(len(array)):     # choose current index to exclude from multiplication
        runningProduct = 1          # initialize product value
        for j in range(len(array)):  # loop through the values again
            if j != i:              # skip current index
                runningProduct *= array[j]      # multiply up
            products[i] = runningProduct        # update output array
    return products


# O(n) time | O(n) space
def arrayOfProducts(array):
    output = [1]*len(array)         # output array
    idx = 0

    while idx < len(array):

        leftProduct = 1
        leftIdx = 0
        while leftIdx < idx:  # go from 0 up to but not including current idx
            leftProduct *= array[leftIdx]
            leftIdx += 1

        rightProduct = 1
        rightIdx = idx + 1
        while rightIdx < len(array):  # go from after idx to end of the array
            rightProduct *= array[rightIdx]
            rightIdx += 1

        output[idx] = leftProduct * rightProduct
        idx += 1
    return output


array = [5, 1, 4, 2]
print(arrayOfProducts(array))

"""
This solution is O(n) because we go through the array twice to get the right
and left arrays and once through the products, left,right arr (so technically
O(n + n + n) ). Space complexity is O(n) because we return a
new array whose size equals the input.

This technique is the two-pass method which can  be used to improve the sliding
window when it yields O(n^2) solution.


"""


def arrayOfProductsII(array):
    products = [1 for _ in array]       # product of all values not including index val
    left = [1 for _ in array]           # product of values to right of but not including index val
    right = [1 for _ in array]          # product of values to left of but not including index val

    leftRunningProduct = 1      # product of elements to the left of index, initialized at 1
    for i in range(len(array)):         # choose the current index
        left[i] = leftRunningProduct    # store the left product of index, before update
        leftRunningProduct *= array[i]  # update left running product with current val for next

    rightRunningProduct = 1     # product of elements to the right of index, initialized at 1
    for i in reversed(range(len(array))):   # choose the current index
        right[i] = rightRunningProduct      # store the left product of current index, before update
        rightRunningProduct *= array[i]     # update left running product with current val for next

    for i in range(len(array)):             # choose current index
        products[i] = left[i] * right[i]    # multiply left, right products not including index val

    return products


"""
Code efficient version of solution II where we dont store a separate left
and right array. we update the products initial array with the values of the
left array and when we get to the right we multiply with the updated products array
"""


def arrayOfProductsIII(array):
    products = [1 for _ in array]               # initialize with 1, the multiplication identity

    leftRunningProduct = 1
    for i in range(len(array)):
        products[i] = leftRunningProduct        # update single product list directly
        leftRunningProduct *= array[i]          # update left running products

    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= rightRunningProduct      # update single product list directly
        rightRunningProduct *= array[i]         # update left running products

    return products


array = [5, 1, 4, 2]
print(arrayOfProductsIII(array))

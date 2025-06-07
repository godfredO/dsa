"""The question gives an array of integers and asks to return a boolean that represents if the array is monotonic. An array is monotonic if 
it is entirely non-decreasing or non-increasing. An array is non-decreasing if as we traverse it, each element is equal to or greater than 
the previous element. An array is non-increasing if as we traverse it, each element is equal to or less than the previous element. This means 
an array of repeated elements is monotonic as it is both non-decreasing and non-increasing. The cleanest way to code out the solution is to
initialize two flags , for nonDecreasing and nonIncreasing to an initial True for the case of an array with repeated integers. Then as we
traverse the array from the second element, if we find a element to be greater than the previous element we set the nonIncreasing flag to 
False. If we find an element to be less than the previous element we set the nonDecreasing flag to False. At the end of the array we return
whether nonDecreasing is True or nonIncreasing is True as a test for monotonicity. If only one of the flags are False, this returns a True 
for monotonicity. If both flags are True as initialized for an array of repeated integer values, it still returns True for monotonicity. 
However if both flags are False, we return False for monotonicity. The first solution here is more tedious and determines the direction and 
handles a lot more edge cases."""
# O(n) time | O(n) space
def isMonotonic(array):
    # If an array is empty, has one or two elements
    # its monotonic
    if len(array) <= 2:
        return True
    
    # If len(array) > 2 then set direction using first
    # two numbers. direction here just means + or -
    direction = array[1] - array[0]

    for i in range(2, len(array)):
        # if two nums are equal, direction gives no info
        # thus update direction calculation
        if direction == 0:
            direction = array[i] - array[i-1]
            continue
        if breaksDirection(direction,array[i-1], array[i]):
            return False
    return True

def breaksDirection(direction, previous, current):
    difference = current - previous 
    if direction > 0:
        return difference < 0
    return difference > 0

"""
O(n) time and O(1) space
"""

def isMonotonicII(array):
    isNonDecreasing = True  #initialize for the case where array[i] == array[i-1]
    isNonIncreasing = True  #initialize for the case where array[i] == array[i-1]

    for i in range(1, len(array)):

        if array[i] < array[i-1]:
            isNonDecreasing = False
        
        if array[i] > array[i-1]:
            isNonIncreasing = False
    
    return isNonDecreasing or isNonIncreasing

array = [-1,-5,-10,-1100,-1100, -1101, -1102, -9001]
array2 = []
print(isMonotonicII(array))
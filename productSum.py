"""This is a simple recursion solution if you realize that if there were no nested arrays, we would simply start with a multiplier of 1,
sum up all the elements of the array and return product of the sum with the multiplier. If there are nested arrays, we effectively do the
same thing just that the nested arrays will have an incremented multiplier value. Thus this question lends itself well to recursion in that
we keep calling the recursive function with the nested array and the incremented multiplier until we no longer have a nested array. When this
base case of no nested array, we sum up the element in this passed array mulitply this sum with the passed multiplier and return the result to 
the original call, the recursive step is resolved and the result of the recursive step is added to the original running sum .
Thus the key to this problem is identification of the base case of no nested loop and an initial multiplier of 1 and the recursive case of 
incrmenting multipliers and calculating inner sums for nested arrays, using the recursive calls. There will be as many recursive calls as the 
depth of the deepest nested array ie is the space complexity is O(d). The time complexity is O(n) where n is the total number of integers nested 
or otherwise. Even though the nested arrays will lead to recursive calls, the recursive calls are resolved before moving on."""

"""This solution uses memoization to pass an augmented
multiplier variable each time the function is called recursively"""
#O(N) time where N is total number of integers nested or otherwise
#O(D) where D is maximum number of depths ie multipliers
def productSum(array,multiplier=1):
    sum = 0    #initial sum for both recursive and base cases,
    for item in array:
        if type(item) is list:
            sum += productSum(item,multiplier+1)  #recursive case
        else:
            sum += item   #base case
    return sum* multiplier           #both base and recursive cases have same return expression
            
array = [5,2,[7,-1],3,[6,[-13,8],4]]
print(productSum(array))

"""We are given an array of unique integers and asked to write a function that returns an array of all permutations of those integers
in no particular order. If the input list is empty, we should return an empty list. There are two solutions covered.

In the first solution, we loop through the array and choose a value. The chosen value is the value at the current index. We add the
choice to our current permutation. We also slice the array so as to remove the chosen value from the array and then call the function
again on the new array and the updated current permutation array. Eventually the newArray obtained by slicing will be empty and this
is our indication that we have a complete permutation, so we will append the current permutaition to an output array. With this 
algorithm, it is important to keep to concatenate the an array of the current choice with the current permutation array otherwise,
we will throw an error of NoneType if we use an append instead of concatenation. The loop for choosing value has a length of n, the
slicing is n, concatenation is n, and there are n! recursive calls so n^2*n!.

In the second solution, we permute indices. We realize that in the permutations, the value at each array will occupy the elements of
every other array. So we start by creating all permutations that have the value at index 0 at index 0, then at index1, index 2 etc
until the last index. If we get to point where the value at index 0 in the original array is at index len(array) - 1, we have a valid
permutation and we append to the output array. Since there are n! permutations and each value occupies n different positions this is
n*n!. Thus we replace the current permutation and its required slicing and concatenation steps with indices and swap operations. We
replace the slice with a one swap operation and then we re-swap after the middle recursive function returns.
Re-swapping ensures that when execution returns to a previous call on the recursive stack, the array will return to the order of the
existing recursive stack.
Another way of explaining the optimal solution is that the element at index 0, swaps itself with every element that comes after it
in the array including itself. That is it occupies index 0 in the original array, index 1 in one permutation, index 2 in another 
permutation. So that is what the optimal solution does, it swaps the element in each subarray with every element that occurs after
it, including itself, then advances the starting index and recursively swaps that index with every element that comes after it,
including itself until the starting index is the last index when we have a valid permutation since there is nothing to swap it with,
which point we add a copy of the array at that point, and go up the recursive tree but first we re-swap the swapped elements so that
the call one level up the recursive tree can continue its swapping with the 'original' array at that point in the recursive tree.
So at each point we are letting the first element occupy its original position, and every position after it and then advancing the
starting index and calling the recursive function with that starting index. """


"""Written in a dfs backtracking way- there are n! perms so n! rec calls and in each we do a linear time operation, compare with the
blueprint of backtracking, wordSearch.py """
#O(n*n!) time | O()
def permute(nums) :
    result = []
    dfs(nums, result, 0)
    return result

def dfs(nums, result, idx):
    if idx == len(nums): #if out of bounds, perms for current path completed, optimize by len(nums) - 1, only remainig swap with self 
        result.append(nums[:])
        return
    
    for j in range(idx, len(nums)): #list of choices for current position
        swap(nums, idx, j)   #make a choice on current path
        dfs(nums, result, idx + 1) #permute the choices for next position
        swap(nums, idx, j)         #backtrack on current path for another choice on current path

def swap(array,i, j):
    array[i] , array[j] = array[j], array[i]
        


#Upper Bound: O(n^2*n!) time | O(n*n!) space
def getPermutations(array):
    permutations = []
    permutationsHelper(array, [], permutations)
    return permutations

def permutationsHelper(array,currentPermutation,permutations):
    if not len(array) and len(currentPermutation): #array is empty and currentPermutation is not empty
        permutations.append(currentPermutation)
    
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i+1:] #this step is linear since its concatenation
            newPermutation = currentPermutation + [array[i]] #this step has to be concatenation in case of NoneType
            permutationsHelper(newArray,newPermutation,permutations)



#O(n*n!) time | O(n*n!) space
def getPermutationsI(array):
    permutations = []
    permutationsHelperI(0,array,permutations)
    return permutations

def permutationsHelperI(i,array,permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array,i,j)    #visit step
            permutationsHelperI(i+1,array,permutations)
            swap(array,i,j)      #backtracking step

def swap(array,i,j):
    array[i], array[j] = array[j], array[i]

# O(n^2*n!) time | O(n*n!) space like first solution
def getPermutations(array):
    result = []

    #base case
    if len(array) == 1:
        return [array[:]] #a list of lists
        
    
    #[1,2]
    for i in range(len(array)):
        #[2], remove 1
        newArray = array[0:i] + array[i+1:]
        #[[2]]
        perms = getPermutations(newArray)

        # for perm in perms: 
        #     #[[2,1]] add 1 back
        #     perm.append(array[i])  
        newPerm = [[array[i]] + perm for perm in perms]
            
         #[].extend([[2,1]) > [[2,1]]  
        result.extend(newPerm) #add this set of perms to result array
    return result







    
    

    



array=[1,2,3]
arrayII = [5,6]
# print(getPermutations(array))
# print(getPermutations(arrayII))


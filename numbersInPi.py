#O(n^3 + m) time | O(n) space
# def numbersInPi(pi,numbers):
#     numbersTable = {number:True for number in numbers} #store favorite numbers in hashtable for constant access, O(m)
#     minSpaces = getMinSpaces(pi,numbersTable,{},0)
#     return - 1 if minSpaces == float("inf") else minSpaces

# def getMinSpaces(pi,numbersTable,cache,idx):
#     if idx == len(pi):
#         return -1  # - 1 to cancel out + 1 added for suffix ending at i = len(pi) - 1. we dont need a space at the end of pi string

#     if idx in cache:
#         return cache[idx]
    

#     minSpaces = float("inf")

#     for i in range(idx,len(pi)): #O(n)
#         prefix = pi[idx:i+1]  #slicing O(n), i+1 includes i and excludes i+1 to generate prefix
#         if prefix in numbersTable: #if prefix isnt a favorit table, theres nothing to do, if it is, we check at the suffix
#             minSpacesInSuffix = getMinSpaces(pi,numbersTable, cache, i + 1) #minspaces for string starting at i+ 1, O(n), recursion return value
#             minSpaces = min(minSpaces, 1 + minSpacesInSuffix ) #if prefix is in hashtable then we know we have 1 space plus what suffix returns
#     cache[idx] = minSpaces #store the minSpaces found for string starting at idx to avoid repeated work

#     return cache[idx]

"""Same solution as above where we loop backwards, from right to left. Thought it doesnt improve complexity, we compute the smallest
substrings' minspaces first, meaning that we will always find the minSpaces of suffixes in the cache"""
#O(n^3 + m) time | O(n) space
def numbersInPi(pi,numbers):
    numbersTable = {number:True for number in numbers} #store favorite numbers in hashtable for constant access, O(m)
    cache = {}
    for i in reversed(range(len(pi))):
        getMinSpaces(pi,numbersTable,cache,i)
    return -1 if cache[0] == float("inf") else cache[0]

def getMinSpaces(pi,numbersTable,cache,idx):
    if idx == len(pi):
        return -1  # - 1 to cancel out + 1 added for suffix ending at i = len(pi) - 1. we dont need a space at the end of pi string

    if idx in cache:
        return cache[idx]
    

    minSpaces = float("inf")

    for i in range(idx,len(pi)): #O(n)
        prefix = pi[idx:i+1]  #slicing O(n), i+1 includes i and excludes i+1 to generate prefix
        if prefix in numbersTable: #if prefix isnt a favorit table, theres nothing to do, if it is, we check at the suffix
            minSpacesInSuffix = getMinSpaces(pi,numbersTable, cache, i + 1) #minspaces for string starting at i+ 1, O(n), recursion return value
            minSpaces = min(minSpaces, 1 + minSpacesInSuffix ) #if prefix is in hashtable then we know we have 1 space plus what suffix returns
    cache[idx] = minSpaces #store the minSpaces found for string starting at idx to avoid repeated work

    return cache[idx]

pi = "3141592653589793238462643383279"
numbers = ["314159265358979323846", "26433", "8", "3279", "314159265", "35897932384626433832", "79"]
print(numbersInPi(pi,numbers))

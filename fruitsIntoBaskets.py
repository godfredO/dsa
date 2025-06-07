"""You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an 
integer array fruits where fruits[i] is the type of fruit the ith tree produces. You want to collect as much fruit as possible.
However, the owner has some strict rules that you must follow: 
-You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each 
basket can hold.
-Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving 
to the right. The picked fruits must fit in one of your baskets.
-Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].



The question is effectively asking as to find the longest subarray that contains at most 2 unique elements. That is a 
subarray is valid if it contains exactly 1 unique element or 2 but cant contain more unique elements. Now its important
to realize that we an unlimited count of the same element but it still counts as a single unique element. As such when
it gets to shifting the left pointer in this case we may need to shift it repeatedly to remove duplicates values until
the number of unique values is less than or equal to 2. In other words, we need to use a hashmap instead of a set here
and we need a count hashmap for that matter. So we will be using our right pointer to increase counts and we will be 
using the left pointer to decrease counts and remove keys as long as the number of keys in our counts hashmap is greater
than 2. Then once we have a valid subarray, we take its length and track the maximum length.
"""
def totalFruit(fruits):
    maxLength = 0
    unique = {}
    left = 0
    for right in range(len(fruits)):
        increaseCount(unique,fruits[right])
        
        while len(unique.keys()) > 2:
            decreaseCount(unique,fruits[left])
            left += 1
        
        length = right + 1 - left
        maxLength = max(maxLength, length)
    
    return maxLength


def increaseCount(map, char):
    if char not in map:
        map[char] = 0
    map[char] += 1
   
def decreaseCount(map, char):
    map[char] -= 1
    if map[char] == 0:
        map.pop(char)      
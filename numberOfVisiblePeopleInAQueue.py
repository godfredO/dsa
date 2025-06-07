"""There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order. You are given an array 
heights of distinct integers where heights[i] represents the height of the ith person. A person can see another person to 
their right in the queue if everybody in between is shorter than both of them. More formally, the ith person can see the jth 
person if i < j and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]). Return an array answer 
of length n where answer[i] is the number of people the ith person can see to their right in the queue.

Example 1:
Input: heights = [10,6,8,5,11,9]
Output: [3,1,2,1,1,0]
Explanation:
Person 0 can see person 1, 2, and 4.
Person 1 can see person 2.
Person 2 can see person 3 and 4.
Person 3 can see person 4.
Person 4 can see person 5.
Person 5 can see no one since nobody is to the right of them.

Example 2:
Input: heights = [5,1,2,3,10]
Output: [4,1,1,1,0]
 
Constraints:
n == heights.length ; 1 <= n <= 105  ; 1 <= heights[i] <= 105  ; All the values of heights are unique.

So say we have heights = [5,4,3,6], the person at index 0 (height 5) can see the person at index 1 (height 4) and the person
at index 3 (height 6) but not the person at index 2 (height 3) because their view will be blocked by the person at index 1 
(height 4). This is because like the question says, a person can only see another person to the right if everybody in between
has a height that is strictly less than either of them. The first thing we can say then is that, everybody can see the person
directly to their right, welp, because there is no one between them. So say the first person has a height of 5, if a second
person of height 5 joins the queue to the first person's right, then this person will completely block their view of anyone
who comes after. This also includes if another person of height 6 joins the line. This is because the question states that
a person can see another to their right, if everybody in between is shorter than both of them. So for anyone in the line the
next person whose height is equal to or greater will block their view (that is be the last person they can see), since they 
can only see over shorter people. So say we have a person of height 2, and we add a person of height 5, then the person of 
height 2 cant see anyone after that so if using a stack, we would pop of height 2 and add one person to their count. If however 
after after the person of height 2, the next person has a height of 1, then the person on top of the stack, with height 2 can 
still see the new person, so we increment the count of height 2 by 1, but it still stays on our stack in case we have another 
person whose height is still less than height 2 say another person of height 1. In othewords, for any person in the line, the 
last person (after last person their view is blocked) they can see is the next equal to or greater height, but they can be seen 
by the previous strictly greater height. So if the incoming will block peek top we add on to peek top count and pop it of the 
stack since they seeing no more. If incoming will not block peek top then peek top can see them and can see over them, so we add 
1 to peek top count for the current person (still keeping current peek top on stack because they can see over) before appending 
the current height to the stack. We initialize an output array with 0 everywhere, iterate from left to right and decide if the 
incoming height will be seen by as well as block the view of the peek top. If yes, we pop and increment count of stack top. If not 
we increment stack top (without popping) before appending current height to stack. In otherwords, we are interested in the next 
greater or equal and the previous strictly greater heights so we use the appropriate algorithm from monotonicStacks.py. The key is 
to always ask under what conditions does the property of interest come to an end. If it does, what does it say about the stack peek
and the current element. And if the property doesnt come to an end, what does it say about the peek value and the current element. 
"""
def canSeePersonCount(heights):
    answer = [0]*len(heights)

    stack = []
    for i in range(len(heights)):
        while stack and heights[i] >= heights[stack[-1]]:
            stackTop = stack.pop()
            answer[stackTop] += 1
        
        if stack:
            answer[stack[-1]] += 1
        
        stack.append(i)

    return answer
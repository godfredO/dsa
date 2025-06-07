"""The input is an array of distinct positive integers representing coin denominations and a single non-negative integer ie 0 or positive, n
representing a target amount of money. The question is to write a function that returns the number of ways to make change for that target
amount using the given coin denominations. This question reminds of the array question, non-constructible change but its different becuase of 
integer n and what we are being asked to do. Now in the non-constructible change question, in order to solve the question, the array of coin 
denomination needs to be sorted in ascending order, from lowest coin denomination to greatest coin denomination. That will be a nlog(n) step.
This solution here, instead of sorting the array, uses a nested inner loop, of length d, that is we have O(nxd) and since n can vary, log(n) 
of increasing length of the input array will be a larger multiplier than d, therefore the optimal solution here is O(nd). This is actually a
secondary reason for using the O(nd) solution. The primary reason is in the provision that we have unlimited amounts of each coin denomination,
which was not the case in the non-constructible case question. How does this primary reason feature in the solution and how does it relate to
the inner for loop of time O(d). Since we have unlimited coin denomination, we are going to ask how many of any coin denomination we could use
to form a change of integer n. So if the coin is $1 and the integer is $10, we would need 10x$1 and to find this, we would need to test
multipliers of 1,2,3,..,d supply of the coin denomination is question. So with that said how do we discover a pattern.

The first thing to realize is that the data structure we initialize is bounded not by the length of the denominations array but rather by the
integer ,n, which represents the change we are trying to make. We initialize a numWays array, where each index represents the specific amount
of money from 0 to the target amount and the values stored at each index represents the number of ways of making change for value eqaul to the
index (ie at index 0 we are looking at change $0, at index n, we are looking at change $n), using the given denominations. Since we are going
to build up our solutions array by looking at change from $0 to $n, the numWays array has n+1 elements and we use [0 for _ in range(n+1)]. 
This way, we know that there is 1 way of making a change of $0 with the denominations array, ie using non of the denominations. This is the 
base case, so we update numWays[0] = 1. So lets say n= $10 and denoms = [1,5,10,25], interesting that all the test cases on algoExpert use 
sorted denom arrays, hmm. So in the outer for loop, we loop through the denoms, and in the inner array, we loop over change from 1 to n ie 
amount in range(1+n+1). So the first we check if the current denomination can be used to form the current change ie change <= denom. Why, we 
can't use a $5 to yield a change of $1 in any way. This again hearkens to the non-constructible change question where while looping through 
the denoms, we say if denom > currentChange + 1, the just return currentChange + 1 because at any point in time, we know that the answer is 
currentChange + 1, unless the current denom can be used to yield currentChange + 1 and if we never find a False situation after determining 
currentChange for all denoms, we return currentChange + 1. So for each denomination in the denoms arra, we loop over the numWays array for
each change ranging from $1 to $n and if the current denom can be used to yeild the current change, we say 
numWays[currentChange] += numWays[currentChange - denom]. Why is this so?. So if the currentChange = $1 and denom = $1, how many ways can 
we use denom of $1 to make a change of $1? There is one way, ie using 1x$1 which coincidentally is numWays[currentChange - demom] ie
numWays[1-1] = numWays[0], which we initialized as the base case. That is numWays[1] = 0 + numWays[0]. If currentChange = $2 and denom = $1, 
we have 1 way, ie using 2*$1 and this is the value stored at numWays[2] = numWays[2] + numWays[2-1]. The reason why we increment the existing
value is because the question wants to know how the number of ways using unlimited copies of all denominations in the denoms array and we
break this down to loop at one denom at a time and update all the change from $1 to $n. So in order to reflect the number of ways using
unlimited copies of all denominations in the denoms array add up the number of ways usingn each denom. Eg if denom= [1,5] and n = 6
the answer is 2 ie 6*$1 and $1+$5. We can get to this by having a numWays array from $0 to $6, update the numWays[0] = 1, base case, the
when we are at denom $1, our array will look like [1,1,1,1,1,1,1] and at denom 5 we only update index 5,6 ie numWays[5] = 1 + numWays[5-5]
= 2 and at numWays[6] = 1 + numWays[6-5] = 2.

What is the the rationalization behind num[change - denom]. We are effectively saying if we used 1 copy of denom, we just add how many ways
for the complement change. ie if change = 6 and denom is 4, then we use 1 copy of 4 and how many ways we have for the complement change 2.

So by looking at ways of solving the question for smaller change values, $0 - $n, realizing the base case of numWays[0] = 1 and realising 
we can use the current denom to find the  make the current change by progressively looking at the copies of denom that we will need, using
the looking for smallest change denom can make to the largest change denom can make and at each point we look at the complement change that
we need from smallest complement change from smallest to largest. Okay a lot of words, still confusing but I tried my best.
"""

#O(nd) time | O(n) space
def numberOfWaysToMakeChange(n,denoms):
    #ways array from $0 to $n ie n+1 elements
    ways = [0 for _ in range(n + 1)]  #sorted change from 0 to n
    ways[0] = 1  #base case, there is always 1 way of making $0 whatever the denom

    for denom in denoms:
        for amount in range(1,n+1): #amount represents possible amount ie i
            if denom <= amount: #if current denom can be used to generate current amount
                ways[amount] += ways[amount-denom] #increment numWays of current change by numWays at denom's complement for current change

    # the last value ways[-1] has an index of n so ways[n]
    return ways[n]

n = 10
denoms = [1, 10, 25, 5]
print(numberOfWaysToMakeChange(n,denoms))
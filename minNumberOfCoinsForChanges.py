"""The input is an array of positive integers representing coin denominations and a single non-negative integer representing a target amount
of money. The question is to write a function that returns the smallest number of coins needed to make change, to sum up to the target amount 
using the given coin denominations. The input structure is the same as the numberOfWaysToMakeChange dynammic programming question, but what we 
are being asked to do is different. In that question we were being asked the number of Ways the denominations can be used to generate a change 
of $n, using the as many copies of the denominations as we need. Here we are effectively, saying of those ways, which one uses the minimum 
number of coins. So that if denoms = [$1, $5] and change is $6, the number of ways is 2 ie 6*$1 and 1*$1+ 1*$5 and the first way uses 6 coins 
in total, the second uses 2 coins in total so we would return 2 coins. Thus this question is about the num of copies we use to create the
change. 

So like the numberOfWaysToMakeChange question, we are going to use an array, minNumCoins, that stores the minNumOfChoinsForChange for change 
ranging from $0 to $n and since we are looking for a minimum number we initialize this array with +inf for ease of comparison. So we know that 
for $0 we use 0 number denom coins to yield $0. This is the base case, so we update minNumOfCoins[0] = 0. Then like numberOfWaysToMakeChange, 
we use a double nested loop, the outer loop goes for denoms and the inner loop goes over minNumCoins, but this time include index 0 ie.
The outer loop is for denom in denoms, and the second for amount in range(len(minNumCoins)) or range(n+1). Now we know that the base case
value will never change so we can loop from range(1,n+1) like the previous question. And in the previous question we can actually include
0 because we know that our array will contain positive integers meaning no denom will actually be able to be used for 0 change so won't
get a change to update that value. Then again like the previous question, we check if the current denom can be used create the current change 
ie if denom <= amount. If yes, we then say that the minNumCoins[amount] = min( minNumCoins[amount], 1 + numOfCoins[amount - denom]). That is at 
each change, once we have established that the current denomination or coin can be used to form the coin, the we say to update 
minNumCoins[amount] = min(miNumCoins[amount], 1 + minNumCoins[denomComplement]) ie we compare the current number of coins to the using 1 copy 
of the current denom + the number of coins needed for its complement for the current amount. At the end we return the last value in the data 
structure ie minNunberOfCoins if we updated it (check if still +inf) otherwise return -1 like the question asks.

So I am sensing a coinsChange pattern here, and instead of sorting the denoms we build up the solution with ascending order (sorted) change
from $0 to $n. We fill this array, by considering 1 copy of the current denom + the numberOfWays / numberOfCoins for the complement of the
current denom [amount - denom] to yield the current change once we have established that the current denom can be use to create the current 
change ie if denom <= amount. In the previous solution we incremented the values in the data-structure, in this question we chose the minimum
of possibilities. So far the coinChange pattern consists of minimumChangeWeCannotMake, numberOfWaysToMakeChange and minNumberOfCoinsForChange.
"""


#O(nd) time | O(n) space
def minNumberOfCoinsForChanges(n,denoms):
    #array to store min num of coins for making $index change
    numOfCoins = [float('inf') for amount in range(n+1)] #using inf simplifies our comparison
    
    numOfCoins[0] = 0 #base case,to make $0 change, we use 0 coins of denom

    for denom in denoms:
        for amount in range(len(numOfCoins)):
            if denom <= amount: #can we use current coin to generate amount
                numOfCoins[amount] = min(numOfCoins[amount], 1 + numOfCoins[amount-denom])

    return numOfCoins[n] if numOfCoins[n] != float('inf') else -1 


n = 7
denoms = [1, 10, 5]
print(minNumberOfCoinsForChanges(n,denoms))
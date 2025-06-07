
"""The question gives an array of positive integers representing the values of coins in your possession. And asks to write a function
that returns the minimum amount of change that you cannot create. With this problem, it is a requirement to sort the array , the 
algorithm works on working from the lowest coin to the highest. Sorting ensures thatwe get to this solution. So after sorting the array,
how do we come up with the solution. Suppose we have an empty array, meaning we hav $0 in our possession. Phew!! So if we had $0, then
we can say that the current change we can create with the coins we have is $0 and the minimum change we cannot create is $1. Now suppose 
got $1, the current change we can create is $1 and the minimum change we cannot create is $2. Now suppose we received a $2 coin so
coins = [$1, $2], we currentChange = $3 and minimum we cannot create is currentChange + 1 = $4. So first off this is a dynammic 
programming question even though it doesnt look like it. Secondly because when we talking about money and change, we are dealing with 
the set of non-negative numbers, hence the pattern  of minimumChangeWeCannotCreate = currentChange + 1. But suppose we added a $5 coin
so that coins = [$1, $2, $5], the know that minimumChangeWeCannotCreate = $4 before the addition of $4. So does the addition  of $5
help us create $4? No it doesnt. But suppose instead of $5, we received a $4 so that coins = [$1, $2, $4], does the additon of $4 help
us create the minimumChangeWeCannotCreate, $4, yes, using only the new coin. So what if instead of $4, we received $3 so that 
coins = [$1, $2, $3], does the addition of $3 help us create minimumChangeWeCannotCreate = $4 ? Yes it does, using [$1, $3]. So after
building up the dynammic programming approach, we know that if the new coin > minimumChangeWeCannotCreate, then we return
minimumChangeWeCannotCreate, and minimumChangeWeCannotCreate = currentChangeWeCanCreate + 1. So in this solution, we initialize
the currentChangeWeCanCreate = 0 and after sorting our input we check if the next coin > currentChangeWeCanCreate + 1. If it is
we return currentChangeWeCanCreate + 1. If its not we update currentChangeWeCanCreate by incrementing it with new coin. If we loop
through all the coins and increment currentChangeWeCanCreate with each coin then we return currentChangeWeCanCreate + 1, where
currentChangeWeCanCreate is the maximum change we can create using all the coins at the end of the loop.

So what is  If there is no 1 in th array, the lowest non-constructible change. 
    """
def nonConstructibleChange(coins):
    coins.sort() #first thing is to sort the coins array, we generally need a sorted array for money questions

    change = 0  #the amount of change we can currently create, we can create 0...change 

    for coin in coins: #loop through sorted coins array from smallest to highest
        if coin > change + 1:
            return change + 1
        change += coin
    return change + 1


coins = [5,7,1,1,2,3,22]

print(nonConstructibleChange(coins))
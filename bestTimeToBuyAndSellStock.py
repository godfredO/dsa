"""
Tags: Two-Pointer; Greedy; Medium


You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by
choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you
can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
Note that the values being in descending order means that there is no way to make a profit because the following days all have
lower prices.

Constraints:x
1 <= prices.length <= 105
0 <= prices[i] <= 104

Say you have an array for which the ith element is the price of a given stock on day i. If you were only permitted to complete at
most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit. Note that
you cannot sell a stock before you buy one.

The algorithm here depends on a couple of observations. First we will need two pointers one for our buyIdx and our sellIdx and since
we have to buy a stock before we can sell it, sellIdx has to be greater less than buyIdx. In the code we initialize buyIdx = 0 and
sellIdx = 1. Secondly we initialize our maxProfit at 0, if we don't buy or sell anything that is the maxProfit we make. Then we use
a while loop whose condition is while sellIdx < len(prices) ie while sellIdx is not out of bounds and we only need to worry about
sellIdx because we know that buyIdx will always be less, so sellIdx will go out of bounds before buyIdx. Also note that in the
constraints, we are told that the length of the prices array is at least 1 so in that case, with sellIdx = 1, we wont even enter
the while loop and will immediately return maxProfit of 0.

Now inside the while loop we know that to make a profit, the prices[buyIdx] < prices[sellIdx]. If we come across this we calculate
the profit, then we do a maximum comparison with the maxProfit variable, and then increase sellIdx. In other words, for the current
buying price we want to know if the next selling price will maximize the profit, so we keep buyIdx right where it is, and increment
sellIdx by 1, and if the new sellIdx yields a greater profit that is what we go with. This is because we are only allowed one trade
only so for any buying price, we want to choose the selling price that maximizes the profit.

What do we do if prices[buyIdx] >= prices[sellIdx]? Well that case actually goes to the root of our problem. In order to maximize
profit, we want to buy on the lowest day possible and sell at the highest day possible as long as the sell index comes after the buy
date. So another restating of this situation is to ask, what do we do if prices[sellIdx] <= prices[buyIdx]. And the answer is that
we should actually be buying on our current sellIdx and then checking if there is some day after that that will yield a profit and
who knows it could be the maximum profit. If we find a selling prices that is higher than any we have encoutered before then it will
be more profitable to buy at the current prices than our previous buying prices since again we are only allowed one trade. So if we
find ourselves in a position where the price of the current sellIdx is equal to the price of the current buyIdx, we have actually
found a better buying price so we move our buyIdx pointer to that position, and then again increment sellIdx by 1 so that we can start
finding all the profit that we can make with our new buyIdx price. In otherwords, the algorithm is to find all the profit we can make
for a particular buyIdx, storing the maximum profit until we find a better buyIdx then we move our buyIdx pointer and start calculating
all the profit we can make with the new buyIdx while keeping track of the maximum. In the end we would have chosen the lowest buying
prices and the largest selling prices and stored the maximum profit possible, given the constraint that we can make only one trade
and of course that we must buy the stock before we sell.


This pattern is called the sliding window, ie we use a start, end pointers. Under some condition we move the start pointer, to maintain
the condition of our window. Under other conditions we keep the start pointer where it is ie keep the window open. In the general case,
we always increment the end of the window ie open the window wider.

In this question our window is a profit window and must contain a profit. If we find a situation where there is no profit to be made, we
shut our window by moving the start pointer to the current position of the end pointer. If there is a profit to be made, we keep the
window open and calculate theprofit. In either case, we always increment our end pointer.
"""

# O(n) time  | O(1) space


def maxProfit(prices):
    # initalizing at 0, 1 is actually pretty important for the else condition on the first iteration
    buyIdx, sellIdx = 0, 1      # two-pointer

    maxProfit = 0
    while sellIdx < len(prices):
        if prices[buyIdx] < prices[sellIdx]:  # profit situation
            profit = prices[sellIdx] - prices[buyIdx]
            maxProfit = max(maxProfit, profit)
        else:  # no profit situatiion
            buyIdx = sellIdx
        sellIdx += 1
    return maxProfit

# O(n) time | O(1) space


def maxProfit(prices):
    maxProfit = 0
    startIdx = 0
    for endIdx in range(1, len(prices)):
        if prices[endIdx] > prices[startIdx]:  # profit made if previous lowest is lower still
            profit = prices[endIdx] - prices[startIdx]  # calculate profit
            maxProfit = max(maxProfit, profit)  # update max profit
        else:   # if a profit can be made, prices[endIdx] equals or less than prices[startIdx]
            startIdx = endIdx  # endIdx is the lowest price at subarray ending at endIdx
    return maxProfit            # track maxProfit

# O(n) time , O(n) space


def maxProfit(prices):
    bestPrevSellDay = [0]*len(prices)   # initialize at day index = 0  (Dynamic Programming-esque)

    for i in range(1, len(prices)):
        if prices[i] < prices[bestPrevSellDay[i-1]]:  # minimize selling prices from previous day
            bestPrevSellDay[i] = i
        else:   # if current day has lower price, don't buy on a previous day
            bestPrevSellDay[i] = bestPrevSellDay[i-1]   # (Dynamic Programming-esque)

    dayProfit = [0] * len(prices)
    for i in range(len(prices)):
        dayProfit[i] = prices[i] - prices[bestPrevSellDay[i]]

    return max(dayProfit)


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))

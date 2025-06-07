"""
Tags: Two-Pointer; Greedy; Medium

You are given an integer array prices where prices[i] is the price of a given stock on the ith day. On each day, you may decide to buy
and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on
the same day. Find and return the maximum profit you can achieve.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4. Total profit is 4. Or Buy on day 1 (price = 1)
and sell on day 2 (price = 2), then buy on day 2 (price = 2) and sell on day 3 (price = 3), then buy on day 3 (price = 3) and sell on
day 4 (price = 4), then Buy on day 4 (price = 4) and sell on day 5 (price = 5) for a total price of 1+1+1+1 = 4.


Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104



This is related to bestTimeToBuyAndSellStock.py and the differences in the questions in that in the previous question we were only
allowed one trade so we had to minimize our buying price as much as possible and maximize our selling price as much as possible.
Here however, we are allowed to buy and sell as many times as possible as long as we only hold one stock at a time and of course we
buy before we sell. If you look at example 1 and example 2, you get a hint as to the strategy here which is we want to maximimze the
number of profitable trades as much as possible.

Take an prices array [1,2,3], if we had 1 trade only then we buy at 1 and sell at 3 for a profit of 2. However if we can have as many
trades as possible then we can buy at 1 sell at 2 for a profit of 1 then buy at 2 and sell at 3, for profit of 1 and a total profit
of 2 which is the same as buying at 1 and selling at 3.  If we have [1,1,3], we make a profit of 2 if we buy on day 1 or day 2 and
sell with a price of 1 and sell on day 3. If we have [2,1,3], we still are better off buying on day 2 and selling on day 3. In otherwords,
each day is a potential buy day and we as soon as we determine that we can make a profit, we sell and get a new buy day, adding up our
profits along the way. If we determine that we cant make a profit,  we still move our buy day because it means that we found an equal
or lower buy day price. We don't hold the stock for the best selling price, because if the price rises later, the total profit is the
new profit plus the old profit which is will be equal to or more than holding the stock.

So this is what solution 1 does. We initialize a buyIdx at index 0 and loop over the remaining prices and in
this loop we advance buyIdx to the current sellIdx anyway. But before we do that we wonder we check if we can make a profit in which
case we calculate the profit and add to our maxProfit variable.

Since we know that each day is a potential buy day and since we know that we want to sell as soon as we make a profit, how can we
simplify our code. It is by realizing that the soonest we can make a profit is the next day after buy. So we can loop over our array,
from index 1, compare the current price to the previous day price and if we can make a profit, we sort of retroactively the day
before, sell on the current day and add to our maxProfit.
"""

"""Solution I"""
# O(n) time | O(1) space


def maxProfit(prices):
    buyIdx = 0

    maxProfit = 0
    for sellIdx in range(1, len(prices)):
        if prices[sellIdx] > prices[buyIdx]:
            profit = prices[sellIdx] - prices[buyIdx]
            maxProfit += profit     # this is the difference with bestTimeToBuyAndSellStock.py
        buyIdx = sellIdx    # whether we make a profit or not, new day new selling opportunity
    return maxProfit


"""Solution II"""
# O(n) time | O(1) space


def maxProfit(prices):
    maxProfit = 0
    for sellIdx in range(1, len(prices)):   # each day we sell from previous day if profit possible
        buyIdx = sellIdx - 1                # buy from previous day
        if prices[sellIdx] > prices[buyIdx]:
            profit = prices[sellIdx] - prices[buyIdx]
            maxProfit += profit
    return maxProfit

"""The question provides a list of prices for a stock on different days and an integer k that represents the maximum 
number of transactions, a transaction being the buying and selling of one share of stock. Also we are asked to return 
the maximum profit that can be realized in k transactions with the list of stock prices. The solution, like all dynamic 
array problems is going to build up the answer starting from a base case till we reach the answer we are looking for. 
In this question in particular, we use a 2d array where the columns represent the prices, so number of columns = 
len(prices) and the rows will represent the number of transactions starting from 0. Now this is crucial because we know 
that if we have 0 transactions we make 0 profit, so the first row of the array will be 0. Equally important, the first
column of the array will also store 0 profit because at the fist day price, we can buy but would have to wait a later day
to sell or you could say that if we bought on the first day and sold on the first day, we would make 0 profit. Its also
crucial to add that we don't have to use all k transactions to maximize profit. Thus at transactions k, at price p, we can
decide not to conduct any transactions, in which case the max profit is the same as the max profit from the previous day at
the same transactions, or we can conduct one transaction and at a buying price that maximizes the profit. If we choose to
conduct this transaction the total profit will be the profit at the buying price at one less transaction plus the profit in 
the additional transaction ie profit= selling price - buying price + profitAtBuyingPriceAndOneLessTransaction. Since the 
selling price is fixed for any cell in the array, we can maximize the profit by maximizing (-buying price + profit at buying
price at one less transaction). Thus the profit at transactions k, price p , profit[k][p] = max(profit[k][p-1], 
price[k] + max(price[x]+profit[k-1][x])) where 0<= x< p. By computing the inner max() expression on a rolling basis, we make
that a constant-time operation instead of looping back in a linear-time operation. Storing only the rows we need also improves
the space complexity"""
#O(nk) time | O(nk) space - in this solution we store entire 2d array
def maxProfitWithKTransactions(prices,k):
    if not len(prices): #if the prices array is empty
        return 0 #return 0 profit
    profits = [[0 for d in prices] for t in range(k+1)] #2d-array for profits, 0-k columns ie k+1 columns, 0's for base case
    for t in range(1,k+1): #start filling values from second row,second column ie loop from second row
        maxThusFar = float("-inf") #initial value of inner max expression for each row, initialize at -inf for easy comparison
        for d in range(1,len(prices)):
            maxThusFar = max(maxThusFar,profits[t-1][d-1]-prices[d-1]) #update maxThusFar for each column in row
            profits[t][d] = max(profits[t][d-1], maxThusFar + prices[d]) #hold or sell previously bought at max profit
    return profits[-1][-1]

#O(nk) time | O(n) space - in this solutin we store only two rows at a time
def maxProfitWithKTransactions(prices,k):
    if not len(prices):
        return 0
    evenProfits = [0 for d in prices] #profits array for even numbered transactions(inclucing 0)
    oddProfits = [0 for d in prices] #profits array for odd numbered transactions
    for t in range(1,k+1):
        maxThusFar = float("-inf") #
        if t %2 ==1: #if dealing with an odd-numbered number of transactions, choose current,previous arrays before column loop
            currentProfits = oddProfits #the current row is the profits 
            previousProfits = evenProfits
        else: #otherwise if dealing with an even-numbered number of transactions
            currentProfits = evenProfits
            previousProfits = oddProfits
        for d in range(1,len(prices)):
            maxThusFar = max(maxThusFar, previousProfits[d-1]- prices[d-1]) #previous and current are 1-d array , d-length
            currentProfits[d] = max(currentProfits[d-1], prices[d]+ maxThusFar)
    return evenProfits[-1] if k%2 == 0 else oddProfits[-1] #final row is evenProfits if k is even, if k is odd, final is oddProfits




prices = [5, 11, 3, 50, 60, 90]
k = 2
print(maxProfitWithKTransactions(prices,k))
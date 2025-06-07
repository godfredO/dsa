"""Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the 
current day. The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and 
going backward) for which the stock price was less than or equal to the price of that day. For example, if the prices of the 
stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting 
from today, the price of the stock was less than or equal 2 for 4 consecutive days. Also, if the prices of the stock in the 
last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, 
the price of the stock was less than or equal 8 for 3 consecutive days.

Implement the StockSpanner class:
StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.

Example 1:
Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to 
today's price.
stockSpanner.next(85);  // return 6
 

Constraints:
1 <= price <= 10^5 ; At most 104 calls will be made to next.

So if you really look at this question, and you read monotonicStacks.py, you realize that the question is asking as to count
the number of elements between the current stock price, and its previous greater. This is because the span of the current
stock price is the maximum number of consecutive days (starting from that day and going backward) for which the stock price 
was less than or equal to the price of that day. First thing the span is always going to include the current stock price so
the span is at least 1. So in the first solution, we repurpose the previousGreater algorithm from monotonicStacks.py. Here
we also realize that suppose the stock prices were in ascending order, then each index will have 1+index as its span. So
here we only append the current stock price in next() and return the result of callign the previousGreater() algorithm. This
algorithm stores indices on a stack and when we find a previous greater index for the current index, we store the span to be
the current index - previousGreater index. We do this by using a strictly descreasing monotonic stack, popping off all indices
whose values are less than or equal to the current value and if there is anything on the stack, its the previous greater of 
the current index so we calculate the span using current index - previousGreater and store it in a span array, and whetehr or
not the stack is emtpy or not we append the current index to the stack. At the end we return the last span value which is the 
span of current stock price. This solution thus, stores the stock prices, the uses a stack and also stores all the span values, 
and it receives a TLE on leetcode. 

So how can we improve the core ideas of the first solution, and use space optimally. First, we know that the first stock price 
will always have a span of 1. Next if the second stock price is less than the first stock price, its span is 1 otherwise if the
first stock price is less than or equal to the second stock (aka the second stock price is greater or equal), the the span of 
the second stock price is 1 + the span of the first stock price. Now if the third stock is less than the second stock price,
again its span is 1 otherwise its span is 1+ the span of the second price ie 1+2=3. Now we know that a fourth stock price will
have a span of 1 if its value is less than the third stock value, otherwise if its value is equal to or greater than the third
stock price, then its also greater than the second stock price. In otherwords, we dont need to have the second stock price on
the stocks stack, in order to know that its part of the fourth stock price's stack; since this information is summarized in 
the third stock price's span information. Hence, our stocks span will store [price,span] and when we get a new stock price, we 
compare to the stack peek's price value and if it is we increment its span value with the span value of the peek span before 
popping the peek span, making sure to initialize our current span at 1. In this way we only store the [price,span] we need for
future prices and summarize the informaition we dont need for future prices. Hence in this solution, we will pop and summarize
all [price,span] values that are part of the current price, stopping at the current price's previous greater prices before 
appending the [currentPrice, currentSpan] to the stocks stack which will become our new peek. Thus, instead of using three 
different arrays, we use 1 array that stores two values, one of which summarizes the span of previous values that have been
popped. So if we had [60,70,65], the span of 65 is 1 because it's not equal or greater than 70. If it were, then we dont even
need to look at the 60, we would just add the span of 70 to the current span. In otherwords, this question is about finding
the left boundary of the current price span instead of using the previous greater approach. Read maximumSubarrayMinProduct.py.

"""
#TLE solution 85/99 cases
class StockSpanner:

    def __init__(self):
        self.stocks = []
    

    def next(self, price: int) -> int:
        self.stocks.append(price)
        return self.previousGreater()
    
    def previousGreater(self):
        n = len(self.stocks)
        prevG = list(range(1,n+1))
        stack = []

        for i in range(n):
            while stack and self.stocks[stack[-1]] <= self.stocks[i]:
                stack.pop()
            if stack:
                prevG[i] = i - stack[-1] 
            stack.append(i)
        return prevG[n-1]


"""Passes Leetcode"""

class StockSpanner:

    def __init__(self):
        self.stack = []
    

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        
        self.stack.append([price,span])
        return span




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
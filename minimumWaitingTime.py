"""The question gives an array of query duration. Only one query can be executed at a time, but the queries can be executed in any order. 
A query's waiting time is defined as the time it must wait before its execution starts. If a query is executed second, then its waiting 
time is the duration of the first query; if a query is executed third, its waiting time is the sum of the durations of the first two 
queries. The question asks to write a function that returns the minimum amount of total waiting time for all the queries. So first off,
the greedy way to minimize the total waiting time is to minimize the waiting time for each query. To do that the greedy option is to 
run the shortest query first, since the duration of this query will affect the waiting times of all the queries after it, then the 
second shortest etc. Thus in order to minimize the total waiting time, we have to first sort the queries in ascending order. An important
observation is to realize that the first query will have a 0 waiting time. After that, each query will have a waiting time which 
is thesum of the the waiting time of the previous query plus the duration of the previous query, which represents the fact that each query 
has to wait for all the preceding queries to be run. Thus last query being the last, it duration doesnt affect the total waiting time at all 
since there is no query after it waiting for it to finish. instead of using an O(n^2) approach of repeatedly summing up all the queries that 
come before, we can realize that simply adding the previous query to the waiting time of the previous query will allow us to do this sum
in O(n) time. In the first solution we use this observation to calculate the waiting time for each query after sorting them. And then to
get the total waiting time we sum up all the waiting times at the end. In the second solution we calculate the waiting time of a query 
and the total waiting time as we iterate through the array to avoid storing all the waiting times and thus improve the space complexity. 
In the third solution we use an additional observation that the duration of each query will be part of the waiting times of all the 
queries that are run after it. So the first query's duration will be added to the total waiting time a total of len(array) - 1  times. 
So to directly calculate the total waiting time without first calculating each query's waiting time, we count the number of queries after 
it, and multiply it by the query's duration to represent the number of times that query's duration is added to the total waiting time. It 
doesnt necessarily improve the complexity over the second solution, but it shows a deeper understanding of how each query's duration
actually affects the total waiting time. This is because each duration will be added to the total as many times as there are querys left
to run after it."""


"""Naive solution of generating all waiting times after sorting queries array and returning the sum of the waiting times. This approach
is also dynamic programming-esque in nature."""
#O(nlog(n)) time | O(n) space
def minimumWaitingTime(queries):
    queries.sort()  #need to sort array to yied an execution order that minimizes wait times
    waiting_time = [0 for _ in queries] #initialize waiting time list

    for i in range(1,len(queries)): #start from second query because, first query has a waiting time of 0
        waiting_time[i] = waiting_time[i-1] + queries[i-1]
    return sum(waiting_time[:]) #total waiting time


""""Optimal solution where we calculate the waiting time and the total waiting time at the same time"""
#O(nlog(n)) time | O(1) space
def minimumWaitingTime(queries):
    queries.sort()
    waitingTime = 0
    totalWaitingTime = 0
    for i in range(1,len(queries)):
        waitingTime += queries[i-1] #waiting time of the preceding querie + the duration of the pre
        totalWaitingTime += waitingTime
    return totalWaitingTime

"""Optimal solution of calculating a running total of minimum waiting times for
queries left in the sorted array"""
def minimumWaitingTime(queries):
    queries.sort()
    totalWaitingTime = 0
    for i in range(len(queries)):
        duration = queries[i]
        repeatedAdditions = len(queries) - 1 - i #the -1 is to bridge the count and Python's zero index
        totalWaitingTime += duration * repeatedAdditions
    return totalWaitingTime


"""Optimal solution but we start enumerating at 1 to change len(queries) - 1 - idx to len(queries) - idx 
since idx starts at 1 as opposed to idx starting at 0."""
#O(nlog(n)) time | O(1) space
def minimumWaitingTime(queries):
    queries.sort()
    totalWaitingTime = 0

    for idx,duration in enumerate(queries, start=1): #start enumerating at 1 to calculate queries Left
        queriesLeft = len(queries) - (idx)
        totalWaitingTime += duration * queriesLeft
    return totalWaitingTime

"""Optimal solution but we recognize that the last querie will not affect the total waiting time, small
optimization"""
#O(n) time | O(1) space
def minimumWaitingTime(queries):
	queries.sort()
	totalWaitingTime = 0
	
	for i in range(len(queries) - 1):
		totalWaitingTime += queries[i]*(len(queries) -i -1)
	return totalWaitingTime
	

queries = [3, ]
print(minimumWaitingTime(queries))
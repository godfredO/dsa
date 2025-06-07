"""You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.
You want to share the chocolate with your K friends so you start cutting the chocolate bar into K+1 pieces using K cuts, 
each piece consists of some consecutive chunks. Being generous, you will eat the piece with the minimum total sweetness and 
give the other pieces to your friends. Find the maximum total sweetness of the piece you can get by cutting the chocolate 
bar optimally.

Example 1:
Input: sweetness = [1,2,3,4,5,6,7,8,9], K = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]

Example 2:
Input: sweetness = [5,6,7,8,9,1,2,3,4], K = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.

Example 3:
Input: sweetness = [1,2,2,1,2,2,1,2,2], K = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]

Constraints:
0 <= K < sweetness.length <= 10^4
1 <= sweetness[i] <= 10^5

So this question is related to splitArrayLargestSum.py but whereas in that question you are asked to minimize the largest
subarray sum, in this question you are asked to maximize the smallest subarray sum. So you are given an array of values
sweetness, and an integer k, and we are to divide the array into k+1 subarrays and we want to divide the array such that
we maximize the smallest subarray sum of the k+1 subarrays. In particular, we are told the array represents a chocolate
bar and each value is the sweetness of each chunk of the chocolate bar. You are sharing the chocolate with k friends, hence
you need to divide into k+1 subarrays and you want to take the subarray with the smallest total sweetness and you are asking
how can you maximize this smallest total sweetness contiguous subarray chunks, and to return this maximized smallest total
sweetness. 

So what is the search space for finding the smallest total sweetness. The smallest possible value of the array is 1 from the
constraints, and as such the low end of the search space is 1, though I believe that the minimum of the search space could 
also be the low end of the search space ie if we are to divide the array (chocolate) into exactly len(sweetness) subarrays, 
the smallest subarray sum will be the minimum value in the array. Contrast this with splitArrayLargestSum.py where we want to 
find the minimize the largest subarray sum, so if we divide the array into len(nums) subarrays, the largest subarray sum  is
max(nums). If the number of subarrays is 1, the only option for the smallest subarray sum is the sum of the entire array. 
It turns out that this is the same too in splitArrayLargestSum.py since in either case that is the only option for subarray
sum. So search space minimim is min(sweetness) or 1, and the search space maximum is sum(sweetness). 

The next difference is how we calculate our mid value. Even though we are given the integer k for the k friends, by adding
ourselves, we are actually dividing the chocolate into k+1 subarrays. Thus we calculate mid not with (left + right)//2 but
rather with (left + right + 1)//2 (in the code we go with the overflow resistant left + (right - left + 1)//2). Why? I 
actually dont know. So now we have our guess mid value for the smallest subarray sum. Now the thing to note here is that
since we are looking for the smallest subarray sum, a valid subarray must at least have the guess mid value as its sum. In
otherwords, in our helper function, we iterate over the array, adding up the values, and we check if after the current
addition, the sum is greater than or equal to the guess, since a valid subarray has to at least have the guess as its
subarray sum. This also differs from splitArrayLargestSum.py where a valid subarray cant go over our guess but can be lower.
Here a valid subaray cant have a lower sum than our guess. Anyway, the moment the current subarray sum is greater than or
equal to our subarray, we have one subarray, and so we increment our subarray count by 1 and re-intialize the subarray sum
variable to 0. Again this differs from splitArrayLargestSum.py where if we ever go over the guess, we increment the subarray
count but re-initialize our subarray sum at the current array element since our guess in our largest subarray sum. 

When we have the number of subarrays we can form with the guess as the minimum subarray sum, we check if the number of 
subarrays is greater than or equal to the number of partitons, k+1. Note here that if there are any remaining numbers in
the array whose subarray wasnt counted its because the sum was less than the guess and since guess is the lower bound of the
subarray sums, the remaining numbers don't form a valid subarray sum. As such, we don't add a 1 to the subarray count here
like we do in splitArrayLargestSum.py, where an uncounted subarray is still valid since the guess is the upper bound, not the
lower bound. Anyway we know that for smallest subarray sum, when k+1 = 1 we have sum(sweetness), when k+1=len(sweetness), we
have min(sweetness). In other words, as smallest subarray sum decrease, the number of partitions increase. To put this in
perspective, min(sweetness) < smallest < sum(sweetness) ; n > k+1 > 1. Another way of saying it is this, 'smallest' is the
maximum value when looking at the sweetness values from [min(sweetness), smallest]. In otherwords, if we guess a mid value
that falls in this range, we are supposed to maximize it since the question is asking us to maximize the smallest subarray
sum. In otherwords, we first guess a smallest subarray sum, and then determine which guess we need to maximize. So if
a guess falls between [min(sweetness), smallest], we know that its corresponding number of subarrays falls between [k+1,n].
In otherwords, if chunks >= k+1, then maximize the guess. And how do we do that? We move the left pointer to mid, to 
shorten our window in the direction of bigger values and also because mid could still be our answer. Otherwise ie chunks
< k+1, we move right to mid - 1 to minimize our next guess and also because mid cannot be our answer. At this point it
is helpful to look at binarySearchII.py for the section that talks about how the code is structured when the question is
posed as the maximum value for which a condition is True. Because the loop condition is while left < right, when the loop 
terminates, we have the answer at the left pointer. The way to think about the difference between the min val for which 
condition is True, and max val for which condition is True is this: if we find a True case, in one scenario, we shorten 
our window in the direction of the smaller values and in the other scenario we shorten the window in the direction of the 
larger values.

The smallest subarray sum ranges from min(sweetness) < smallest < sum(sweetness) and for this range the number of partitions 
range from n > k+1 > 1. In othewords, maximizing the smallest subarray sum from min(sweetness) to smallest corresponds to
the range of partitions that frange from k+1 to n ie the number of subarrays greater than or equal to n. Since min(sweetness)
is the left pointer, when we find a smallest guess mid value whose number of subarray is equal to or greater than k+1, we 
move the left pointer to mid, otherwise we move the right pointer to mid - 1.


"""

def splitArray(sweetness, k):
    nums = sweetness                        #repurposed splitArrayLargestSum.py was too lazy to change nums to sweetness
    left, right = min(nums), sum(nums)     #linear search space, can also use 1 as min
    while left < right:
        mid = (left + right + 1)//2
        if canSplit(nums,mid,k):
            left = mid 
        else:
            right = mid - 1
    return left

def canSplit(nums,largest,k):
    subarray = 0
    curSum = 0
    for n in nums:
        curSum += n
        if curSum >= largest:
            subarray += 1
            curSum = 0
    return subarray  >= k + 1

sweetness = [1,2,3,4,5,6,7,8,9]
K = 5



print(splitArray(sweetness,K))
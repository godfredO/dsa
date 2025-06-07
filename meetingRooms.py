"""Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could 
attend all meetings. Note that (0,8),(8,10) is not conflict at 8.
Example1
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict.

So the obvious way to model this question is to model it after merge intervals where we sort and then loop through comparing nextStart
with prevEnd only this time an overlap occurs only when nextStart is less than prevEnd (not less than or equal to). If an overlap 
occurs we return false. If we go through all intevals and never hit false we return True. This approach is O(nlog(n))."""



def can_attend_meetings(intervals):
        
    intervals.sort(key=lambda x:x[0]) #sort based on start times

    for next in range(1, len(intervals)):
        _ , curEnd = intervals[next -1]
        nextStart, _ = intervals[next]
        if nextStart < curEnd:
            return False
    return True


intervals = [(9,15), (5,8)]
print(can_attend_meetings(intervals))
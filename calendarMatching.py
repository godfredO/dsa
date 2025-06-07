"""

The input to this question are two calendar lists, two daily bound lists, and an integer meetingDuration. The calendar lists represents
the calendars of two co-workers and contain appointments of form [startTime, endTime], that is the calendars are 2-d lists. The calendar
lists are also sorted by the start time in ascending order and the times themselves are strings of form ['9:00','10:30']. The daily bounds
are also of form [earliestTime, latestTime] and are also stringified times like the appointments and denote the earliest and latestTime
each co-worker is available. The meeting duration is an integer representing the minutes of a new meeting between co-workers. The question
asks to take these inputs and returns a list of all the time blocks, in the form [startTime, endTime] during which you could schedule a
meeting , sorted from earliest time block to the latest. The solution for this problem is really about breaking the problem into a series
of sub-problems, then stringing  together these series of linear-time solutions to the subproblems to solve the original problem. We use
variation of merging overlapping intervals techniques to find individual and joint unavailabilites and the a reversed variation of the
same techniques to find the empty blocks of availabilities that satisfy our meeting duration all while maintaining sorted order.

First we realize that the question is about finding unavailabilities between the two workers' calendars and bounds. That is the calendars of
each co-worker and the daily bounds of each co-worker denote times when they are not availalbe for a new meeting. So the first linear time
step is merging each individual's bound times with their calendar to reflect individual unavailabilities. The aim of this step is to first
generalize the calendars to reflect 24hours not just the work day and also to covert the hour:minutes into minutes where 00 minutes will be
the 12 midnight. So since we can see that each individual co-worker's first meeting starts at or after their first daily bound and that
their last meeeting ends before or at their second daily bound, so we start by inserting a 'meeting' from 0:00 to dailyBound[0] and appending
a 'meeting' from dailyBound[1] to '23:59' to copies of the calendars. This update step is linear time because inserting at index 0 in an
array is linear time, making a copy of the calendars is linear time. The last thing we do in this update step is to convert all the times
to minutes since the beginning of the day which is also linear time. To do this we map all the intervals, select the startTime and endTime
of each interval and convert them to minutes using a helper function. This helper function splits each time string by ":", then converts each
piece to an integer using the built in int() function, making sure to keep track of the hour and minutes portion of the time, since str.split()
yields a list ['hours', 'minutes']. Then finally we unpack the converted integers and convert to minutes since the beginning of the day using
the formula hours*60 + minutes. So with each co-workers calendar merged with their daily bounds for a 24h reflection and each interval times
converted to minutes since the beginning of the day, we then merge both co-workers updated calendars into one calendar where one or both
co-workers are unavailable for a new meeting.

Thus we iterate through both updated calendars to create a new merged calendar that merges the individual unavailabilities while maintaining
sorted order. To do this we use the two pointer technique similar to the one used for merge sort ie one pointer for each updated calendar and
we compare the start times of each current interval for the co-workers and append interval or meeting with the earlier start times, since
we are comparing minutes since the beginning of the day and increment the pointer of the chosen interval. Thus at the end we have all the
meetings of both co-workers inside a single array, where the meetings are sorted in ascending order according to their start times. Remember
in the merge overlapping intervals question, we start by sorting the intervals according to their start times. That is exactly what we are
doing here, creating a sorted list that contains both calendar meetings in ascending order of their start times.

Next, we flatten the ranges in the merged and updated unavailabilities calendar by merging overlapping intervals like that question of said
name. In that question, we copied the the first element of the sorted intervals into the output array, and this first interval was the first
interval to be the current interval, looped from the second of the sorted intervals for nextInterval pointer, unpacked both current and next
and compared the start of next to the end of current. We do something similar here, although instead of current we name that pointer previous
and instead of next we name that pointer, current. So previous pointer is the last element in the output array and current pointer is the
current interval in the loop. If current start is less than or equal to previous end, we create a new merged meeting with previous start and
the maximum of previous end and current end. Then we update the last item in the output array with this new merged meeting. If the previous
end and the current start don't overlap, we proactively append a copy of the current interval to the output arrray so that it becomes the new
last element of the output array and thus the previous pointer for the next comparison, just like we did in merge overlapping intervals. After
flattening the merge-sorted calendars, we can now safely compare adjacent intervals for available time slots.

Finally we iterate through the flattened merged updated unavailabilities calendar to find blocks of time between unavailabilities ,those blocks
of time denoting availabilites, that are of length equal to or greater than the requested meeting duration. To do this, we start looping from
the second flattened interval as the current pointer and we compare to the preceding flattened interal as the previous pointer. We compare
subtract the current's start from the previous end and if the resulting minutes is greater than or equal to requested meeting duration, we
append an interval of [previousEnd, currentStart] to the output array. Finally, we convert interval in the output array, [startTime, endTime]
into hours:minutes using helper function. At this point each start time is represented as minutes since the beginning of the day. To
convert this to hours:minutes within the hour, we floor (minutes since beginning of day) to yield hour of day, then modulo
(minutes since beginning of day) to yield minutes within the hour. We then strigify both hour of day and minutes within the hour. Since the
question asks for military time, when stringifying minutes within the hour, we concatenate a '0' before minutes within the day, if minutes
within the hour is less than 10 minutes, else we stringify as is. Finally we do a final concatenation between the stringified hour and the
stringified minutes.

This question effectively takes merge overlapping intervals question, expands the required sorting first step to a full merge sort operation,
adds a time convertion step before and after in order for comparison to be done and on top of it adds an additional step of inserting and
appending the daily bounds. Phew!!!"""

# O(c1 + c2) time | O(c1 + c2) space


def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    # update calendars by adding daily bounds to reflect workers's unavailabilties and also transform for easy comparisons
    updatedCalendar1 = updateCalendar(calendar1, dailyBounds1)  # update and transform calendar1
    updatedCalendar2 = updateCalendar(calendar2, dailyBounds2)  # update and transform calendar2
    # merge updated calendars in sorted order
    mergedCalendar = mergeCalendars(updatedCalendar1, updatedCalendar2)
    # flatten overlapping intervals in merged calendars
    flattenedCalendar = flattenCalendar(mergedCalendar)
    return getMatchingAvailabilities(flattenedCalendar, meetingDuration)


def updateCalendar(calendar, dailyBounds):  # O(n)
    # make a copy of original calendar before updating in order not to change information
    updatedCalendar = calendar[:]
    # insert at index 0 unavailability from first hour of day to first daily bound
    updatedCalendar.insert(0, ["0:00", dailyBounds[0]])
    # append unavailability from second daily bound to last hour of day
    updatedCalendar.append([dailyBounds[1], "23:59"])
    # in addition, transform calendar durations to allow for easy comparisons and manipulation, ie convert to minutes of day
    return list(map(lambda m: [timeToMinutes(m[0]), timeToMinutes(m[1])], updatedCalendar))


def timeToMinutes(time):
    # split time along : ie '4:30' becomes ['4','30'] before conveting to integers, [int("4"), int("30")]
    # transform and unpack into integer hour and minutes
    hours, minutes = list(map(int, time.split(":")))
    return hours * 60 + minutes  # convert to minutes since the start of day


def mergeCalendars(calendar1, calendar2):
    merged = []  # initialize empty array
    i, j = 0, 0  # initialize two iterators to point to the start of the calendars
    while i < len(calendar1) and j < len(calendar2):  # loop condition while neither iterator is out of bounds
        meeting1, meeting2 = calendar1[i], calendar2[j]
        if meeting1[0] < meeting2[0]:  # compare starting times , if meeting1 starts before meeting2
            merged.append(meeting1)  # add meeting1 to the merged calendars array
            i += 1  # increment calendar1 iterator
        else:  # otherwise, if meeting2 starts before or same time as meeting1
            merged.append(meeting2)  # add meeting2 to merged calendars array
            j += 1  # increment calendar2 iterator

    # loop terminates if one or both iterators exceed bounds. Add remaining meetings where one pointer is still within bounds
    while i < len(calendar1):
        meeting1 = calendar1[i]
        merged.append(meeting1)
        i += 1
    while j < len(calendar2):
        meeting2 = calendar2[j]
        merged.append(meeting2)
        j += 1
    return merged


def flattenCalendar(calendar):
    # meetings overlap if one meeting is contained in another,extends another, starts right when another is ending
    # seed output list with a copy of first meeting. Use copy in case original is used elsewhere
    flattened = [calendar[0][:]]
    for i in range(1, len(calendar)):  # start with second meeting since first meeting is already in output list
        currentMeeting = calendar[i]
        # last meeting in flattend array, this is why we seed with first meeting
        previousMeeting = flattened[-1]
        currentStart, currentEnd = currentMeeting  # unpack current meeting
        previousStart, previousEnd = previousMeeting  # unpack last meeting in flattened array
        if previousEnd >= currentStart:  # check for overlap where current start is contained in or starts same time as previous end
            # check if current end is contained in or extends previous end
            newPreviousMeeting = [previousStart, max(previousEnd, currentEnd)]
            # overwrite the last meeting in flattened array with updated interval
            flattened[-1] = newPreviousMeeting
        else:  # in the case where there is no overlap ie previousEnd < currentStart
            # append a copy of current meeting, out of precaution
            flattened.append(currentMeeting[:])
    return flattened


def getMatchingAvailabilities(calendar, meetingDuration):
    matchingAvailabilities = []
    # because we call this function with flattened calendar we can safely compare adjancent meeting intervals
    for i in range(1, len(calendar)):  # start from second value
        # this is why we start from second meetiing, then choose end time for comparison
        start = calendar[i-1][1]
        end = calendar[i][0]  # choose start time of next meeting for comparison
        availabilityDuration = end - start  # calcualte the duration between adjacent meetings
        if availabilityDuration >= meetingDuration:  # if duration is sufficient for our meeting
            # add an availability interval between adjacent meetings
            matchingAvailabilities.append([start, end])
    # convert minutes since 0:00 to string times
    return list(map(lambda m: [minutesToTime(m[0]), minutesToTime(m[1])], matchingAvailabilities))


def minutesToTime(minutes):
    hours = minutes // 60  # floor minutes to yield hour of day
    mins = minutes % 60  # modulo minutes to yield minutes within the hour
    # string convertion of hours, note we said 0:00 so no need to concatenate with 0 for hours, US time style
    hoursString = str(hours)
    # concatenate 0 for 09 instead of 9 before stringifying minutes
    minsString = "0" + str(mins) if mins < 10 else str(mins)
    return hoursString + ":" + minsString


calendar1 = [
    ["9:00", "10:30"],
    ["12:00", "13:00"],
    ["16:00", "18:00"]
]
dailyBounds1 = ["9:00", "20:00"]
calendar2 = [
    ["10:00", "11:30"],
    ["12:30", "14:30"],
    ["14:30", "15:00"],
    ["16:00", "17:00"]
]
dailyBounds2 = ["10:00", "18:30"]
meetingDuration = 30
print(calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration))

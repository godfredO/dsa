# Permutation that meets specific criteria
"""
Tags: Backtracking; Medium


The inputs are a array of measuringCups in the form [low,high] and then a low integer and a high integer  A measuring cup only has two
measuring lines, a Low (L) and a High (H) line. This means that these cups can't precisely measure and can only guarantee that the substance
poured into them will be between the L and H line. In addition, you're given one low integer and one high integer representing a range for
a target measurement. We are asked to write a function that returns a boolean representing whether you can use the cups to accurately measure
a volume in the specified low, high range (the range is inclusive). Note once you've measured some liquid, it will immediately be transferred
to a larger bowl that will eventually (possibly) contain the target measurment. You cant pour the contents of one measuring cup into another
cup. eg measuringCups= [ [200,210] ,[450, 465], [800,850]] , low = 2100, high= 2300. Thus you can use a cup multiple times or combinations of
cups to achieve a volume in the specified low, high. In this example we can measure 4 volumes of [450,465] and 2 volumes of [200, 210] for a
total of [2200, 2280] which is within the requested [2100, 2300] ie requestedLow <= finalLow and finalHigh <= requestedHigh. You can also
measure 3 volumes of [450,465] and 4 volumes of [200, 210] for a total of [2150, 2235] which is within the requested [2100, 2300] ie
requestedLow <= finalLow and finalHigh <= requestedHigh. We realize that when we pour out from one measuring cup, the remaining volume to be
measured goes down, and we keep reducing the remaining volumne to be measured until we get to a point where the remaining volumne perfectly
fits in one last measuring cup. This happens when the remainingLow <= cupLow and remainigHigh>=cupHigh. Until that happens we just choose
another cup. Since this is about choosing different measuring cup options, its clearly a backtracking problem. Also since multiple paths can
lead to the same new low and new high, we have to use memoization to avoid repeated work. So we memoize the remaining cup low and cup high
cast as string with a boolean to say if we found a viable path for that new low and new high remaining volume. Also note that if the
remining low value is negative but the remaining high value is positive we could find a cup for that. Eg if the remaining range is [-10,50],
then a cup with range [10,30] technically can measure it. However if both ends of the remaining range are negative then there is no
measuring cup that can fall within that range, so we know that is an inviable path thus we return False. However when we find a cup that
falls within the remaining range we return True and bubble that up the tree.


So the way to solve is to find realize that if low<=cupLow and cupHigh <= high, then cupLow and cupHigh are within low and high and we
return True. If not we measure out one volume, pour into the bowl and now we only have to measure out a voluume that falls within
newLow = low - cupLow , newHigh = high - cupHigh. If we ever get to the point where either or both of these values are negative then we know
that that particular path cannot measure out the volume. This means that both cupLow and cupHigh were both within the range during the last
iteration. Like all 'True/False' backtracking solutions, if a subsequent recursive call returns False, we make another choice and if we are
out of choices then we return False too. However, the first time a subsequent recursive call returns True, we immediately return True and
bubble it up the recursive tree. Now the key thing about this question is that we require memoization. Without memoization, we will exceed
the maximum recursion depth.
 """

# O(low*high*n) time where n= number of cups | O(low*high) space
"""Same idea, slight changes in the code"""


def ambiguousMeasurements(measuringCups, low, high):
    memoization = {}   # store boolean indicating if a volumne could be measured or not
    return canMeasureInRange(measuringCups, low, high, memoization)  # backtracking dfs


def canMeasureInRange(measuringCups, low, high, memoization):
    key = getHashableKey(low, high)         # convert low,high to hashable memoization key
    if key in memoization:                  # if call for low,high was previously resolved
        return memoization[key]             # return the memoized boolean
    if low < 0 and high < 0:                # if remaining range is all negative
        return False                        # no measuring cup can fall within negative range

    for cup in measuringCups:               # go through the measuring cups
        cupLow, cupHigh = cup               # unpack current cup into its range
        if low <= cupLow and cupHigh <= high:   # if current cup falls within remaining range
            return True                         # current cup can measure out remining range
        memoization[key] = canMeasureInRange(   # measure out by reducing range; then backtrack
            measuringCups, low - cupLow, high - cupHigh, memoization)
        if memoization[key]:                # backtracking step where we bubble True up the tree
            return True                     # if current cup returns False, try next
    memoization[key] = False    # if no cups return True, current range cannot be measured
    return memoization[key]     # bubble the result memoization result of current range


def getHashableKey(low, high):
    return str(low) + ":" + str(high)


def ambiguousMeasurements(measuringCups, low, high):
    memoization = {}
    return canMeasureInRange(measuringCups, low, high, memoization)


def canMeasureInRange(measuringCups, low, high, memoization):
    # create a key to store return value for range
    memoizeKey = createHashableKey(low, high)
    # check if we already solved this range
    if memoizeKey in memoization:
        return memoization[memoizeKey]
    # base case 1
    if low < 0 and high < 0:  # if both values for range are negative,
        return False  # then we cannot measure it

    canMeasure = False  # the return value is false until we reach a true case
    for cup in measuringCups:
        cupLow, cupHigh = cup
        # base case 2
        if low <= cupLow and cupHigh <= high:
            canMeasure = True
            break
        canMeasure = canMeasureInRange(measuringCups, low-cupLow, high-cupHigh, memoization)
        if canMeasure:  # if a recursive call returns True
            break  # break out of recursion

    memoization[memoizeKey] = canMeasure  # store the result of recursive function call

    # return True if a recursive call returns True and we break, otherwise, initial canMeasure is False
    return canMeasure


def createHashableKey(low, high):
    return str(low) + ":" + str(high)


measuringCups = [
    [200, 210],
    [450, 465],
    [800, 850]
]
low = 2100
high = 2300
print(ambiguousMeasurements(measuringCups, low, high))

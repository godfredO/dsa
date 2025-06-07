"""The inputs are a string and a potential substring of the main string and the question asks to write a function that returns a version of
the main string with every instance of the substring in it wrapped between underscores. If two or more instances of the substring in the
main string overlap each other or sit side by side, the underscores relevant to these substrings should only appear on the far left of the
leftmost substring and on the far right of the rightmost substring. If the main string doesnt contain the potential substring at all, the
function should return the main string intact. 

This question like most hard questions, builds on the solution to medium questions, sandwiched between additional logic. So the first thing
to do is to find the index locations of all instances of the substring in the main string and for this we use the string method str.find().
str.find() takes in a substring and a starting index to search from and returns the index of the substrings location after starting index.
This step is itself a version of a step in multi string search (inoptimal solution) I can't remember but basically under the hood .find() is 
placing a pointer at starting index and another pointer at starting index + len(substring) - 1 and comparing this to the first and last 
letters of the substring, increments/ decrements the pointers to match all inward letters. Anyway, .find() will return the index of the 
first letter of a found instance of substring and thus we know that we can slice that instance out of the main string using 
[nextIdx:nextIdx+len(substring)] and so this is the location that we save and update startIdx to nextIdx + 1 to keep advancing through the 
main string finding the nextIdx and storing the slice indices until .find() returns -1 meaning it could not find an instance of substring 
after the updated startIdx. So now we slice indices of all instances of substring in the main string. Using slice indices makes it possible 
to merge overlapping intervals since it ensures that instances of substring that sit side by side will have the endIdx of the first instance 
equal to the startIdx of the second instance.

Since the question asks that if instances of substring overlap or sit side by side, we should place the underscores to the left of the leftmost 
instance and to the right of the rightmost instance, we need to collapse these locations array (the array that contains the slice indices for 
instances of substring) using the technique found in the merging overlapping intervals question. This technique works here as follows, we check 
if the the locations array is empty, which would happen if no instance of substring occurs in the main string, in which case we return the same 
empty locations array from the collapse (name of merge overlapping function). In the merge overlapping intervals question, we started by sorting 
the intervals according to their first element but since the locations array but here we know that the locations array is already sorted 
according to first elements because of how we used the string.find() function to obtain it. So then we copy of reference the first interval in 
locations array, into a newLocations array which will house the collapsed interval and we initialize a previous pointer to point to this 
interval. Here we are referencing the first array like we did in the merge overlapping intervals question instead of explicitly copying it like 
in the calendar matching question. The we iterate through the locations array starting from the second array and inside this loop we initialize 
a current pointer for the current interval in the loop. We then unpack the previous interval and the current interval and compare the 
previousEnd and currentStart. If previousEnd is greater than or equal to currentStart, we have an overlapping interval and we collapse by 
updating the last element in the referenced previous interval to the maximum of previousEnd and currentEnd. If the intervals don't overlap, we
move the previous pointer to the current interval and append it to the newLocations array. Again here, we update the last element of the 
previous array if there is an overlap instead of explicitly creating a new array and replacing the last interval in newLocations (previous) like
we did in the calendar matching question.

With the returned newLocations array containing the collapsed intervals, we now add underscores to the string which is effectively the addition
to this question. Clearly we are going to iterate through the newLocations array for underscore indexes as well as iterate through the string 
for the string letters, add them to an output array, which we can then join into a new string using the str.join() method. So we intialize our
empty finalChars array, locationsIdx and stringIdx both starting at 0, index i for the first element of an interval, and a boolean 
inBetweenUnderscores which is initialized to False because at the start we are not between underscores yet. So the while loop for filling up the
finalChars array will run as long as we are in bounds for both locations and the string and as such when the loop terminates we will have to
handle the case where we are still within one of those bounds, in a merge-sort-esque kind of way. So we start iterating by comparing the 
current stringIdx to the first element of the current interval in locations ie stringIdx === locations[locationsIdx][i]. If current stringIdx
is not the start of a substring instance, ie stringIdx != locations[locationsIdx][i], then we append the letter at the current string index
to the finalChars array and increment stringIdx forward. So suppose we have a bunch of letters before the first occurence of substring, we
will keep hitting this line of appending the current letter and advancing stringIdx. In the case where we have to add an underscore, after
we do that we still add the element at the current stringIdx to finalChars after the underscore. That is, we add the current string elements
whether or not we have to add an under score, so we have an if statement with we hit if we need to add an underscore but in either case
we still add string letters. Now when we come to an instance of substring, ie when stringIdx == locations[locationsIdx][i], first thing we do 
is append an underscore '_' to finalChars array, then we flip the boolean inBetweenUnderscores using the not keyword ie if inBetweenUnderscores 
is False it becomes True, if underscores is True, it becomes False. Now it is important to note that we use i to access the elements for our 
current interval ie locations[locationsIdx] becomes at the start of our substring we access i=0 and at the end of our substring we access i=1. 
So when we find the very first instance of substring, i=0 and we match whatever index is at locations[locationsIdx][i=0] and flip 
inBetweenUnderscores to True; and flip i= 1 so that the next time we match the ending index. So when we do match the ending index, again we add 
an underscore and flip inBetweenUnderscores by negating it from True to False and since we are done with our current interval, we increment 
locationsIdx to the next interval. So by correctly sequencing these operations update locationsIdx only when inBetweenUnderscores is False which 
will happen if we just flipped it after accessing the last element of our current interval and follow that by flipping i= 0 if i= 1 else 1. So 
whenever we match the start or endIdx of our current interval, i,  to the current string Idx, we append an underscore, flip inBetweenUnderscores, 
and check with the flipped inBetweenUnderscores, if its time to update locationsIdx, before finally flipping i for the next match. At loop 
termination, if locationsIdx is less than the length of locations array, we append a final underscore to finalChars. If stringIdx is less than 
the length of thestring, we adding all the remaining letters to finalChars array. In the general case where the last instance of substring is 
somewhere in the middle of the string, we add the final underscore and the add the remaining letters, so we use an if elif statment so that we 
check both situations. In the case where the last element of the string is part of the last instance of substring, we add final underscore and
the elif check will be false, so we will still be good. Then of course we use "".join(finalChars) string method to create our return string.
If the there are no instances of substring in the main string, the while loop wouldnt run since locationsIdx, 0 is equal to not less than
the length of the empty locations array, ie 0, and for the same reason there would be no final underscore added for the if part of the
if/elif statement. But stringIdx in this case would still be 0, so we would be able to add all the string elements to the finalChars array,
join them to yield to unaltered original string like the question asks for, so we are covered in this case too. 

This question effectively combines a multi string search (inoptimal approach) , merge overlapping intervals question and a valid subsequence
style iteration to create the final array and return string.

"""

#O(n+m) time | O(n) space
def underscorifySubstring(string,substring):
    locations = collapse(getLocations(string,substring))
    return underscorify(string,locations)

def getLocations(string,substring):
    locations = [] #list to store indices where substring is found
    startIdx = 0 #intially we call string.find() at first string character
    while startIdx < len(string): #while in bounds
        nextIdx = string.find(substring,startIdx) #look for substring starting at startIdx
        if nextIdx != -1: # -1 means substring isnt in main string
            locations.append([nextIdx,nextIdx+len(substring)])
            startIdx = nextIdx + 1 #update to start looking after current found substring, in case of overlapping substrings testest, testtest
        else: #string.find() return -1 that substring was not found
            break #substring was not found in main string or last instance of substring already found 
    return locations #2d array

#this function is from merge overlapping 
def collapse(locations):
    if not len(locations): #edge case where the main string doesnt contain substring
        return locations
    newLocations = [locations[0]] #initialize 2D array with first location of substring
    previous = newLocations[0] #initialize by selecting first location of substring
    for i in range(1, len(locations)): #start iterating from second location
        current = locations[i] #current location array to be collapsed
        #compare starting index of current to ending index of previous
        if current[0] <= previous[1]: #if locations overlap or sit next to each other
            previous[1] = current[1] #update the previous ending index, previous already in newLocations
        else:
            newLocations.append(current) #if they dont overlap, append the current to return array
            previous = current #make the current the previous for next iteration
    return newLocations

def underscorify(string, locations):
    locationsIdx = 0 #iterator for locations 
    stringIdx = 0 #iterator for main string
    inBetweenUnderscores = False #at the beginning we are not between underscores
    finalChars = [] #hold underscores and string characters
    i = 0 #for indexing into subarray of locations, to place underscores before and after substring
    while stringIdx < len(string) and locationsIdx < len(locations):
        if stringIdx == locations[locationsIdx][i]: #if string index same as locations subarray first or last element
            finalChars.append("_") #add an underscore since we are a the
            inBetweenUnderscores = not inBetweenUnderscores #between underscore since within a substring instance
            if not inBetweenUnderscores: #if not in between underscores, ie before or after a substring
                locationsIdx += 1 #if not between underscore move to next locations subarray
            i= 0 if i== 1 else 1 #whether between underscores or not update the index to use for string location matching
        finalChars.append(string[stringIdx]) #append current string character
        stringIdx += 1 #move string iterator

        #take care of appending last underscore and last characters before string joining
    if locationsIdx < len(locations): #if still on the last subarray,
        finalChars.append("_") #append an underscore
    elif stringIdx < len(string): #if last underscore is somewhere in the middle of string
        finalChars.append(string[stringIdx:]) #append the rest of the characters remaining
    return "".join(finalChars) #string join


    
string = "testthis is a testtest to see if testestest it works"
substring = "test"

print(underscorifySubstring(string,substring))
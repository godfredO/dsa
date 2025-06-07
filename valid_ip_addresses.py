"""The input is a string of digits of length 12 or smaller, and the question asks to write a function that returns all the possible IP 
addresses that can be created by inserting three '.' in the string. An IP address consists of four sequences of positive integers and
the sequences are separated by '.' and each sequence is an integer value between 0-255 inclusive. An IP address isnt valid if any of
the individual sequences contains a leading 0 ie '192.168.0.1' is valid but not '192.168.00.1' or '192.168.0.01' because of the leading
0's in 00 and 01. The address '99.1.1.10' is valid but not '991.1.1.0' because 991 is greater than 255. The returned ip addresses must
be strings, and if no valid ip addresses are found, we are to return an empty array. The restriction of ip address sequence values is
due to the fact that in memory, each sequence is represented by 8 bits ie 0 - 255 in value.

The approach is to try all valid positions of the three periods '.', keeeping track of the valid IP addresses. The rationale for this
is that we know that a valid section (sequence) can only contain 1 - 3 digits. So if the input string is '1921680', the valid positions
for the first period are 1.9, 19.2 and 192.1 and each of the resulting sequences fall within 0-255. So let's say the first position for
the period is 1.9, we know 1 is valid as it falls between 0-255. If the first section were invalid, there would be no point generating 
the rest of the sections. So for the second section, the options are 1.9.2, 1.92.1 because the next option 1.921 would have 3 digits
but be greater than 255. So say we go with 1.9.2, we have to place the final '.' which would simultaneously generate the third and fourth
sections. So the new options are 1.9.2.1680, 1.9.21.680, 1.9.216.80 and of these only '1.9.216.80' generates valid third and fourth 
sections, 216 and 80; the other options generate invalid fourth sections 680 and 1680. So with the current choices, we've generated
a valid IP addres in '1.9.216.80' since no section contains a leading zero and all section values are between 0-255 inclusive. Now we 
can go back and try other possible positions for the first two '.' and repeat the over and over till all valid ip addresses are found.

In the code we use three nested for loops to place each '.', generate sections via string slicing, and then use a helper function to 
test for validity of the section. If a slice is found to be invalid, we continue to the next possible slice for a particular section. 
Each for loop chooses the end indices for slicing ie in the first loop i= range(1, min(4, len(string))), ie the first loop end index 
since we slice starting from index 0; the second for loop j = range(i+1, min(i+4, len(string)) and the final for loop 
k = range(j+1, min(j+4, len(string))). That is the first slice is string[:i], the second slice is string[i:j], the third and fourth slices 
are string[j:k] and string[k:]. Inside the first for loop, we initialize an array of four empty strings, to store the intermediary slices so 
that if all the slices are found to be valid all the way to the fourth, we join them into a string and append to the final output array. 
After that we go back to the third for loop to try out the next slice for third and fourth sections until that is exhausted, then back to 
the second loop till that is also exhausted, then back to the first for loop , and if a new valid slice is found, we go make a new choice 
for the second and if that is also valid, down to the third loop and so on and so forth until all valid ip addresses are found and all loops 
are exhausted. The helper function that tests for validity takes in a string, converts it to an integer, which will strip all leading zeros. 
We first test if the integer is greater than 255 in which case we return False. There is no need to test for the integer being less than 0 
we will not be passed a string with a negative number inside. If the value check doesnt return False, we return the result of the leading
0 check, which in the code below is done by asking if the result of re-converting the integer into a string and the sliced string have the 
same length. The reason is because if the sliced string is just '0', then converted integer 0 is re-converted to a string to yeild '0' and
thus the sliced string and the re-converted string both have a length of 1 so there are no leading 0's  but a string of '00' has a leading 
zero, and when converted into an integer will become just 0 which afte re-conversion yeilds '0' and thus of length 1 whiles the passed
sliced string '00' has a length of 2. A string of '01' has a leading zero and its converted integer is 1 which after re-convertion becomes
'1' and thus has length of 1 which is different from the length of the original string '01' which has a length of 2. Thus by converting the 
sliced string into an integer we are able to correctly do a value check by checking if greater than 255 and a leading zero check by comparing 
the lengths of the sliced string and the re-converted integer. 
"""

#O(1) time | O(1) space
def validIPAddresses(string):
    ipAddressesFound = []

    """ for loop for position of first period, which can be
    after first, second or third digits unless the input 
    string has less than for digits
    """
    for i in range(1,min(len(string),4)): #a section can contain 1-3 digits, to avoid a loop, end at len(sting) if less than 4
        currentIPAddressParts = ["","","",""] #initialize an array of empty strings to store the the four sections

        currentIPAddressParts[0] = string[:i]  #the first section is a slice of up to the 3rd digit in string
        if not isValidPart(currentIPAddressParts[0]): #check if sliced section is valid, 
            continue #if sliced section is invalid, continue to next slice option
        #if first section is valid
        for j in range(i+1, min(len(string), i+4)): #loop to select section option, up to 3 digits, after current end of first section
            currentIPAddressParts[1] = string[i:j] #slice of 2nd section of up to the 3rd digit after end of first section
            if not isValidPart(currentIPAddressParts[1]): #check if second section is valid
                continue #if 2nd section is invalid, to next choice of 2nd section ending idx

            for k in range(j+1, min(len(string), j+ 4)): #the 3rd section '.'malso creates 4th section; up 3 digits after 2nd section end
                currentIPAddressParts[2] = string[j:k] #slice for 3rd section
                currentIPAddressParts[3] = string[k:] #slice for 4th section
                if isValidPart(currentIPAddressParts[2]) and isValidPart(currentIPAddressParts[3]): #if both 3rd and 4th sections are valid
                    ipAddressesFound.append('.'.join(currentIPAddressParts)) #append to the output after joining array with '.'
    
    return ipAddressesFound #return list of all valid ip addresses
                
            

def isValidPart(string): #helper function to test for the validity of a section
    """this step removes leading zeros"""
    stringAsInt = int(string) #convert to section string to an integer, stripping leading zeroes in the end
    if stringAsInt > 255: #check if section integer value is invalid, ie greater than 255, no need to worry about less than 0 ie negative
        return False #return False to main function

    """Check for leading zeros"""
    return len(string) == len(str(stringAsInt)) #can't we use string[0] == '0'

string = "1921680"

print(validIPAddresses(string))
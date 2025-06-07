#Permutation that meets specific criteria

"""The question is to write a function that takes in a positive integer numberOfTags and returns a list of all the valid strings that you
can generate with that number of matched <div></div> tags. A string is vlid and contains matched <div></div> tags if for every opening
tag <div>, theres a closing tag </div> that comes after the opening tag and that isnt used as a closing tag for another opening tag.
For example if numberOfTags = 2, the valid strings to return would be [ '<div></div><div></div>', '<di><div></div></div>' ].

Now the brute force approach here, would be to generate every single possible string with opening and closing tags, and check every single
possible string and see if those strings are valid. This would lead to an atrocious time complexity because not only do we need to generate
every single possible string, which is an exponential amount, we also need to check every single possible string. So clearly we need to
come up with a better way to do this. Rather than building strings that are possibly invalid, we only want to generate strings that are
valid. So how do we generate valid strings? Well the first thing that we need to realize is that our string must start with an opening
tag. And once we've added an opening tag, we can potentially add a closing tag and more opening tags and so on and so forth. 

Now there are two patterns we can use to add more tags to a valid matched string. We can add another valid matched string to the end of the
previous one or we can move the previous matches string with to the center and surround it with an opening tag and a closing tag. So we
recursively generate valid strings by first placing a opening string and then we have the option of closing it immediately or letting it 
be the opening tag that surrounds a matched string. So if numberOfTags equals 2 we first place '<div>' an opening tag and then we can
close it immediately and have subsequent matched strings tack on to the end or we can have this opening tag surround a subsequent matched
string. So which option do we undertake first. We first try to generate all strings where the current opening tag surrounds other matched
string because that option places an opening tag first ie if we start out with (numOpening, numClosing) = (2,2) and we always start by 
placing an opening tag <div>, we first complete the option <div><div> which will use up all the opening tags and then we add closing tags
ie <div><div></div></div>. Then we can recursively go back to the step where we had placed one opening tag and decided to generate all the
centered tags first ie <div> rec(1,2). So we go back and place a closing tag because we went down the path of placing a subsequent opening
tag first already. So we have <div></div> so now we call our recursive function with (1,1) and again we place the opening tag fist and 
keep doing that until we reach the end of that path then backtrack and explore some other options. So we place the last remaining opening
tag <div></div><div> and  call rec(0,1).  That is if we start with rec(3,3) we have to first place one opening tag and call either
<div> + rec(2,3) or place a closing tag and call <div></div> + rec(2,2). We go with the option rec(2,3) so that we can generate all 
options where an opening tag is chosen first until all opening tags are used up. Then we add closing tags until they are used up and then
backtrack to a point where we can place a closing tag directly after an opening tag before the recursive call. As such if the number of
tags =3, the valid strings are generated in the order [ <div><div><div></div></div></div> ], [<div><div></div><div></div></div> 
<div><div></div></div><div></div>, <div></div><div><div></div></div>, <div></div><div></div><div></div>]. So place an opening tag after 
that there are two choices, make another recursive call or place a closing tag and make another recursive call, and these options have
to be excecuted in that order as long as there are opening tags. If there are no opening tags, the only option is option two. If there
are no closing tags, we finished so append to result array. Another way of say it is that place an opening tag and then make a call to
place a valid sting inside these opening tag or place an closing tag after the current opening tag and make a call to place a valid
string at the end of this current matched string.

The conditions are if openingTags > 0 and if openingTags < closingTags because if they are equal, our only option is to place an opening
tag. That is for rec(3,3) we only have the option of placing an opening tag and making a recursive call. But at rec(2,3), we have two
options, we can add another opening tag and call rec(1,3) or we can add a closing tag to balance the already placed opening tag and
make rec(2,2)

So we start with a numberOfTags worth of opening tags and closing tag and in each step we place the opening tag first, make a recursive
call all the way down till we have used up the number of opening tags, then we start placing all of the closing tags and when we have used
up all the closing tags, we append the string we have, then backtrack to a point where we made a recursive call after placing an opening
tag but this time we place a closing tag after the opening tag and make a recursive call.

This pattern can be used to generate set of all balanced parentheses of one kind since parenthesis follow the same matching principles as
div tags. In some ways this question feels like interweaving strings but the order of placement is the specific criteria here. As long as
we have opening tags, we can place one and then make a closing tag. We can only place a closing tag if there is a corresponding opening
tag already placed ie closingTag < openingTag, this means when we have equal amounts of opening and closing tags, we can place an opening
tag but  we cannot place a closing tag. I
 """


#O((2n)!/(n!*(n+1)!)) time | O((2n)!/(n!*(n+1)!)) space
def generateDivTags(numberOfTags):
    matchedDivTags = []
    generateDivTagsFromPrefix(numberOfTags,numberOfTags,"",matchedDivTags)
    return matchedDivTags

def generateDivTagsFromPrefix(openingTagsNeeded,closingTagsNeeded,prefix,result):
    if openingTagsNeeded > 0:
        newPrefix = prefix + "<div>"
        generateDivTagsFromPrefix(openingTagsNeeded-1,closingTagsNeeded,newPrefix,result)
    
    if openingTagsNeeded < closingTagsNeeded:
        newPrefix = prefix + "</div>"
        generateDivTagsFromPrefix(openingTagsNeeded,closingTagsNeeded-1, newPrefix,result)
    
    if closingTagsNeeded == 0:
        result.append(prefix)


numberOfTags = 2
print(generateDivTags(numberOfTags))
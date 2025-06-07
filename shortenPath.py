""" The question asks to write a function that takes in a non-empty string representing a valid Unix-shell path and returns a shortened
version of that path. A path is a notation that represents the location of a file or directory in a file system. The shortened version
of the path must be equivalent to the original path. In otherwords, it must point to the same file or directory as the original path.
A path can be an absolute path, meaning it starts at the root directory in a file system, or a relative path, meaning that it starts at 
the current directory in a file system. In a Unix-like operating system, a path is bound by the following rules:
    - The root directory is represented by a '/'. This means a path that starts with / is an absolute path. If it doesnt its a relative path.
    - The symbol '/' othewise represents the directory separator. eg /foo/bar is the location of 'bar' inside 'foo' inside the root directory
    - The symbol '..' represents the parent directory. eg /foo/bar/.. is equivalent to accessing /foo, the parent directory of 'bar'
    - The symbol '.' represents the current directory. This means /foo/bar/. is equivalent to accessing /foo/bar
    - The symbol '/' and '.' can be repeated sequentially without consequence. eg /foo/bar/baz/././. is equivalent to /foo/bar/baz
    - The symbol '..' however cannot be repeated sequentially without consequence because repeating it sequentially means going further up the 
    parent directories. The only exception is with the root directory /../../.. and / are equivalent because the root directory has no parent
    directory.

So the solution below follows a few simple steps. First we store a boolean for if the path is an absolute path ie path[0] == '/'. Then we
split the string by '/' the directory separator and filter out the unimportant tokens ie '.'; to do this we write a helper function that
checks each item in the array resulting from split is either the empty "" or ".', since if the path is absolute, the beginning '/' will 
result in a an empty string "". So we say tokens = filter(isImportantToken, path.split('/')) where isImportantToken: return token !=
"" or token != '.', allowing us to only extract the parts of the path we need to shorten it. This step is also why we store a boolean for
if the input path is an absolute path. So after this we get to the main part of the solution, which uses a stack.

So now that the unnecessay /././. has been removed via splitting and the isImportantToken function, the first thing we check is if the
path is an absolute path ie via the boolean, we add a "" empty string to the stack. This is so that when we join the shortened path with
"/".join(stack), we dont lose vital information. With that said it should become clear that the only remaining symbol that can shorten
a path is the go to parent directory symbol '..'. So the general pattern is to append every token in our important tokens array to the
stack unless we get to the parent directory '..' symbol. When we find '..', in the general case we pop() off the stack to simulate going 
to the parent directory. The only situation where we dont pop() is if the peek element on top of the stack is "" (the empty string we
for absolute paths); in that case we do nothing. In addition if the stack is empty or the peek value is '..', we actually append the 
current '..'. Why? If we have a relative path that starts with double dots, we need to keep the double dots because the parent directory
in that case could be anything. So if we have ../../foo we keep both '..' since we don't know what parent directory its going to. This
corresponds to adding the first '..' because the stack would be empty at that point and adding the second '..' because the peek element
on the stack would be '..'. However if we have /../../foo, when we get to the first '..' the stack will have "" for the absolute path 
'/' so we do nothing, the stack still only has "" so at the second '..' we do nothing. At the end we check if the stack is of length 1
and that element is "" (ie if len(stack) == 0  and stack[0] == "') in which case we return '/' because we are left with the root path
and calling '/'.join(stack) would actually throw an error in python since str.join() more than one element in the array. Otherwise we
return '/'.join(stack).
    
"""


#O(n) time , O(n) space
def shortenPath(path):
    startsWithSlash = path[0] == "/" #check if absolute path

    #split function will yield an array, whose elements go through the helper function which returns False for "" and "." 
    # and True otherwise the filter function will then filter the elements that return True into the tokens array
    tokens = filter(isImportantToken,path.split("/")) #use the split function to split along and remove all separators "/"

    stack = [] #stack to build shortened path

    if startsWithSlash:#if original path is an absolute path
        stack.append("") #add the empty string to add back the leading forward slash in a later join operation
    for token in tokens:#token has "." and "" filtered out leaving "dir_name" or ".."
        if token == "..": #if current token is "..", check if stack is empty or peek value is "..", ""(for abs path /), dir name 
            if len(stack) == 0 or stack[-1] == "..":# if ".." is relative path's first token or comes after another ".."
                stack.append(token) #in that case append the current ".."
            elif stack[-1] != "": #if the peak value is an empty string for the absolute path do nothing
                stack.pop() #otherwise the preceding value of ".." is a directory name, pop the dir name   
        else: #if current token is a directory name
            stack.append(token)
    
    if len(stack) == 1 and stack[0] == "":#if path is just the root ie stack will only contain an empty string
        return "/"  #return the root directory

    return "/".join(stack)  #return shortened path by joining stack elements with path separator


def isImportantToken(token):
    return len(token) > 0 and token != "." #empty string, representing a forward slash, has length 0


#path = "/foo/../test/../test/../foo//bar/./baz"
path = '/home/..'
print(shortenPath(path))
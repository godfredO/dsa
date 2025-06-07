"""Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style 
file system, convert it to the simplified canonical path. In a Unix-style file system, a period '.' refers to the 
current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes 
(i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated 
as file/directory names.

The canonical path should have the following format:
The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no 
period '.' or double period '..')

Return the simplified canonical path.

Example 1:
Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
 
Constraints:
1 <= path.length <= 3000 ; path consists of English letters, digits, period '.', slash '/' or '_'. ;
path is a valid absolute Unix path.


So this is an interesting question that demonstrates how a stack can be used to solve some string problems. The
reason why we are able to use a stack is that the meaning of any of the path symbols depends on the previous
symbol. A how do we use a stack to solve this problem?

The first thing we do is to split the path along the separator , / , so that '/home' becomes ["", home]. Note 
that wherever we had a separator, we will have an empty string in the output of the split operation. The reason
behind the split operation is because it provides a convenient way of removing double slashes and trailing 
slashes such that '/home//foo/'.split('/) = ["",'home',"","",'foo',""] so that if we just filter out all the
empty strings we get ['home','foo'], and then we can join with a separator  '/'.join(['home','foo'])  to get
'home/foo'. Now we just have to add a slash at the beginning for the root directory, so '/'+'home/foo' will
give '/home/foo'. Now suppose we had a single dot, such as '/home/./foo/' then the split operation will give
['','home','','.','','foo','']. So here we treate the single dot '.' like the empty strings, in that we filter
it out to yield ['home','foo'] and then we join and concatenate with a slash ie '/' + ('/').join(['home','foo'])
to get '/home/foo'. Next symbol is the double dot '..'. If the double dot is the first symbol in the path such
as '/../home/, then the split will yield ['..','','home',''] . If the double dot is the first symbol in the path,
again we filter it out before our join and concatenation step to get '/home'. If however the double dot is not 
the first symbol in the path, then it means we have to remove the preceding directory name ie go back to the
parent directory. So the solution here is pretty simple. We split the path along the separator, and store a 
filter or reduce set containing the symbols we filter out ie set("",".",".."). Then as we iterate over the list
we get from the split operation we first check if the symbol is a double dot and the stack is not empty, pop
from the stack. Otherwise, if the symbol is not in the filter or reduce set, then it must be a directory name
so we append to the stack. This means if the stack is empty and the symbol is a double dot or if the symbol is
a single dot, or if the symbol is an empty string we will do nothing. At the end we join  the contents of the
stack with the separator, before concatenating with a separator at the front to yield our simplified path.
Being assured that all paths are absolute simplifies the solution a lot compared to shortenPath.py.

This solution can be rigged to work for both absolute and relative paths as shown in the second solution, which
is another way of re-writing shortenPath.py. The first difference is that we take if a double dot is the first
token, how we handle it depends on whether its an absolute path or a relative path. So we store a boolen 
isAbsolute = path[0] == '/' and then remove the double dot from the reduce set so that we can handle it properly.
Also we first check if the current token is '..'. If it is and the path is absolute and stack is non-empty, we pop. 
Note that if the path is absolute and the stack is empty, we do nothing (like in the previous solution where we
added '..' to the reduce set to handle this edge case). Otherwise if the path is a relative path, we have two 
options. If the stack is empty ie the '..' is the first token, or we already appended a previous token of '..', then
we append the current token. This is because if we have a relative path, we want to keep all the beginning double
dots. However, (if the previous token is not '..') we pop. After handling the case of the double dot, we check if the
current token is not in the reduce set. If its not, we append it. At the end if our stack is emtpy, we return '/',
otherwise if the path is not absolute, we return '/',join(stack) else '/'+'/'.join(stack)
"""


def simplifyPath(path) :
    stack= []
    tokens = path.split('/')
    reduce = set(['.' , "" , ".."])
        
    for token in tokens:
        if stack and token == '..' :
            stack.pop()
        if token not in reduce :  #directory name
            stack.append(token)
    if stack:
        return '/' + '/'.join(stack)
    return '/'



def simplifyPath(path):
    reduce = set(["","."])
    isAbsolute = path[0] == '/'
    
    tokens = path.split('/')
    
    stack = []
    
    for token in tokens:
        if token == '..':
            if isAbsolute and stack:
                stack.pop()
            elif not isAbsolute:
                if not stack or stack[-1] == '..':
                    stack.append(token)
                else :
                    stack.pop()
        elif token not in reduce:
            stack.append(token)

    if not stack:
        return '/'
    elif not isAbsolute:
        return '/'.join(stack)
    return '/' + '/'.join(stack)
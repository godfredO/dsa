""" 
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> 
s2 -> ... -> sk such that, every adjacent pair of words differs by a single letter and every si for 1 <= i <= k is in wordList, where 
sk == endWord. Note that beginWord does not need to be in wordList, but endWord has to be in wordList. Given two words, beginWord and 
endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 
if no such sequence exists.

Example 1: Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]  Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2: Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"] Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

Constraints: 1 <= beginWord.length <= 10 ; endWord.length == beginWord.length ; 1 <= wordList.length <= 5000 ; wordList[i].length == 
beginWord.length ; beginWord, endWord, and wordList[i] consist of lowercase English letters ; beginWord != endWord, All the words in 
wordList are unique.

So this is surprisingly a graph problem and for each word has edges to every otherword in the wordList that has a one character difference 
from it, and we can use this one character difference to generate a pattern for determining edges. So if the currentWord is hit, then the
one character difference patterns are  *it, h*t, hi* and if the currentWord is hot, the one character difference patterns are *ot, h*t, ho*.
So we can see that hit and hot share a pattern h*t and so we create an adjacency graph by mapping patterns to the list of words that match
that pattern ie {pattern : [word1, word2, etc]}. So that is the first obeservation here, to go through the wordList, generate patterns and
fill the adjacency graph. Now since we are told that beginWord does not need to be in wordList, we will first add beginWord to the wordList
before creating the graph. Going through the list of words is O(n), generating the patterns is O(m) and for each pattern we append the current 
word to the pattern's list value in the graph where the pattern is the key. So we append the current word O(m) times, so generating the graph 
is O(n*m*m), where m is the legth of beginWord (and every other word for that matter) and n is the number of words in wordList (technically
its n+1 because we add beginWord to wordList before creating the graph of {pattern:[word1, word2, etc]}). This means that each pattern will
have at least one word in its list.

So with the graph created, we start a breadth-first search because the question boils down to finding the shortest path from beginWord to
endWord, if such a path exists and in shortest path questions like Dijkstra's, breadth first search is more efficient. So we have a queue
and we first add our beginWord to it. Inside of the bfs while loop, we will be popping, generating patterns and using the patterns to 
access the graph and since we know that the current word will be in the list value of each of its patterns, we dont want to keep returning
to the current word node over and over again, so we need a visited set, like every bfs. So we have our queue, and visited set. We also need
a numberOfTransformations variable, which will count the number of words from beginWord to endWord. So the other base case is when the popped
word is the endWord we return this numberOfTransformations variable. And when do we increment this numberOfTransformations variable? Well we
start with only the beginWord in the queue and in the visited set, generate all of its pattern, and for each pattern we add all the unvisited 
word neighbors to the queue ie process one entire layer of the graph in a breadth first search way. So when we add all the unvisited neighbors
of all the words currently on the queue, we increment this numberOfTransformations variable by 1. The simplest way is to use a for loop to
go through the range of the length of the queue and whenever this for loop terminates we can increment the numberOfTransformations variable.
I reckon we can also take the size of the queue at the start and decrement this size variable each time we process a word node in the current
layer and when this size variable reaches 0, we know that we have completed each word in the current layer and so we found one step forward.

Before we even create the graph we have to handle the edge case where the endWord is not in the wordList in which case we just return 0, since
no transformation can exist. Also in the way that we do this question, we have a mental model of an undirected graph with word nodes starting
from beginWord to the endWord where edges exist from one word node to all other word nodes which are one character difference away, but in
reality use an adjacency graph of patterns and use the generatePatterns helper function to effectively go between these graphs. Also we return
0 if we break out of the bfs while loop before finding endWord otherwise when we add the beginWord to the queue we initialize the result as 1
for the current layer. This question's pattern is like minimumPassesOfMatrix.py question breadth-first search style question. Also i am storing
all the patterns for any word but this is actually not necessary and uses more space than is needed. I only did it to demonstrate the pattern
generation and to put this in a helper function. It is actually more efficient to loop through the current word and generate the pattern on 
the fly as you and match the pattern to the adjacency 

A word about set() and deque() objects initialized with a single element
The set builtin makes sets out of iterables. Iterating over a string yields each character one-by-one, so wrap the string in some other 
iterable: set(['Tom']) , set(('Tom',)) and in either case this yields set('Tom'). If you dont do this, a='Tom', b = set(a), yields 
set(['m',''T','o']). Same with deque objects deque(['Tom']) yields deque('Tom') but deque('Tom') yields deque(['T','o','m']). Child!!!
"""

from collections import deque
def ladderLength(beginWord, endWord, wordList):
        if endWord not in wordList: #O(nm)
            return 0 

        
        wordList.append(beginWord)
        graph = {} 
        patternsMap = {word:[] for word in wordList}
    
        for word in wordList: #O(n)
            patterns = generatePatterns(word) #O(m)
            patternsMap[word] = patterns
            for pattern in patterns: #O(m)
                if pattern not in graph:
                    graph[pattern] = []
                graph[pattern].append(word)
                
    
    

        visited = set([beginWord]) 
        queue = deque([beginWord]) 
        transformations = 1
        while queue:
            size = len(queue)
            while size > 0 :
                currentWord = queue.popleft() 
                if currentWord == endWord:
                    return transformations 

                for pattern in patternsMap[currentWord]:
                    for word in graph[pattern]:
                        if word in visited:
                            continue
                        queue.append(word)    
                        visited.add(word)
                size -= 1
            transformations += 1
        return 0


def generatePatterns(word): #O(m)
    patterns = []
    for i in range(len(word)):
        pattern = word[:i] + "*" + word[i+1:]
        patterns.append(pattern)
    return patterns


#O(nm^2) time | O(nm^2) space
from collections import deque
def ladderLength(beginWord, endWord, wordList) :
        if endWord not in wordList: #O(nm)
            print(1)
            return 0 

        wordList.append(beginWord)
        graph = {} 
        for word in wordList: #O(n)
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:] #replace current character with wildcard
                if pattern not in graph:
                    graph[pattern] = []
                graph[pattern].append(word)
        print(graph)
                
        visited = set([beginWord]) 
        queue = deque([beginWord]) 
        transformations = 1
        while queue:
            size = len(queue)
            while size > 0 :
                currentWord = queue.popleft() 

                if currentWord == endWord:
                    return transformations 

                for i in range(len(currentWord)):
                    pattern = currentWord[:i] + "*" + currentWord[i+1:]
                    for word in graph[pattern]:
                        if word in visited:
                            continue
                        queue.append(word)
                        visited.add(word)
                size -= 1
            transformations += 1
        return 0



        

beginWord = "hit"
endWord = "cog"

wordList = ["hot","dot","dog","lot","log","cog"]  
print(ladderLength(beginWord,endWord, wordList))
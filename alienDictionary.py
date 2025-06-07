"""
Tag: Topological Sort, Cycles; Hard

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You are given a list of
strings of words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.
Return a string of the unique letters in this new alien language sorted in lexicographically increasing order by the new language's rules. If
there is no solution, return "". If there are multiple solutions, return any of them. A string s is lexicographically smaller than a string t
if at the first letter where they differ, the letter in s comes before the leter in t in the alien language. If the first min(s.length,t.length)
letters are the same, then s is smaller if and only if s.length < t.length.

Example 1:                                                              Example 2:
Input : ["wrt","wrf","er","ett","rftt"]                                 Input : ["z","x"]
Output : "wertf"                                                        Output : "zx"
Explanation :                                                           Explanation :
from "wrt"and"wrf" ,we can get 't'<'f'                                  from "z" and "x" , we can get 'z' < 'x'
from "wrt"and"er" ,we can get 'w'<'e'                                   So return "zx"
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'
So return "wertf"

So this is a topological sort problem, and topological sort is used for directed acyclic graphs (DAG) ie a graph that has directed edges
and no cycles. Lexicographical order is nothing but the dictionary order or preferably the order in which words appear in the dictonary.
For example, let's take three strings, "short", "shorthand" and "small". In the dictionary, "short" comes before "shorthand" and "shorthand"
comes before "small". This is lexicographical order. So the question gives us two conditions for lexicographical order. Now these examples
use normal English words, not the alien language. So first of for the English words 'apple' and 'banana', the first letter where these differ
is 'a', 'b' and since we know that in the English language 'a' < 'b', apple is lexicographically smaller than banana and therefore will
appear before banana if the words were sorted lexicographically ie ['apple', 'banana']. Secondly for the words 'apple' and 'app', since the
first min('apple'.length, 'app'.length) , 3 letters are the same, 'app' is lexicographically smaller than 'apple' becomes 'app'.length <
'apple'.length. So from these two examples the sorted lexicogrphical list would be ['app', 'apple', 'banana'] and we can say that in the
dictionary 'a'<'b' but we dont have enough examples of sorted words to make judgements on the rest of the letters.

So we know that these words are sorted lexicographically, meaning based on the first differing characters. So we can compare the sorted words
for the first differing character for adjacent words and make judgements based on the first differing characters (unless the first word is a
prefix of the second word). So in example 1, comparing 'wrt', 'wrf', the first differing character is 't','f' so we can say that 't' < 'f' in
the alien dictionary. Then we compare 'wrf' and 'er' and the first differing character is 'w', 'e', so we can say that 'w' < 'e' in the alien
dictionary. Then 'er' and 'ett', the differing characters are 'r','t' so 'r' < 't' . Then finallly 'ett' and 'rftt' the first differing
character is 'e', 'r' so we can say that 'e' < 'r' in the alien dictionary. So 't' < 'f', 'w' < 'e' , 'r' < 't', 'e' < 'r' giving a valid
topological sort of 'w' < 'e' < 'r' < 't' < 'f' and all the unique characters are in here so we can say 'wertf' is the answer. So this is a
graph problem using topological sort and as such we know there is no valid ordering if there is a cycle ie if the list of sorted words were
['we','ew','wee'], then 'w' < 'e' and 'e' < 'w' which would constitute a cycle so we return "". Now in topological sort, the graph doesnt
need to be connected anyway. So if in Example 1, 'rftt' wasnt in the list we would have 't' < 'f', 'w' < 'e', 'r' < 't' and this would yield
a disconnected but valid order of 'r' < 't' < 'f' and then 'w' < 'e', since we cant place 'e' before 'r' without comparing 'ett' and 'rftt'.
So in this case we would have multiple solutions, 'wertf' or 'rtfwe' or 'wretf' etc are all are topological sort valid since in all of them
'r' < 't' < 'f' and 'w' < 'e'.

So we are going to have a graph where the nodes are the unique letters in the list of words. So to create the adjacency hashmap, we loop
through the words and for each word we loop through the letters and we initialize each letter as a key pointing to a set. The reason we
use a set here and not a list is to ensure that when we populate the prerequisites, we are not adding duplicates. And since a dictionary
or hashmap also stores unique keys, we will not have duplicate keys for the same letter. Mapping elements prerequisites is standard for
topological sort and in this case it maps each letter to all the letters that come before it in the alphabet of the alien dictionary.
In otherwords a list of prerequisites is a list or preceding letters in the alphabet. A set suffices because from the viewpoint of each
letter we only need the preceding letters that come before it is the alphabet. We find the order among the preceding characters using
topological sort.

Then we have to fill in the nodes:[list of prerequsites] needed for topological sort. We compare adjacent pairs of words in the sorted
list. So in a for loop we choose the index of the first by going up to the penultimate word. For each chosen first word, the adjacent
word is at index + 1. Thus because index for the first word goes to the penultimate index, the adjacent word index + 1 will be the last
word.

After unpacking adjacent pairs of words, we take the minimum length of the two words. We use the minLength to find the first differing
character by comparing the first minLength letters. We do this by choosing an index from range(minLength), and for each index, we
compare the corresponding letters in word1 and word2. The moment the letters are not equal we can say that the current letter in word1
is a prerequisite of the current letter in word2. In the adjacency hashmap, we update the set value of graph[word2[index]].add(word1[index])
and then break because we found the first differing letter. But before we find the first differing character, we need to handle an edge
case that has to do with when one word is a prefix of the other. We are told that in that case the shorter word has to come first. So if
the slice of word1 up to minLength is the same as the slice of word2 up to minLength and word1 is longer than word2 then we have a case
where the longer word appears first so we couldnt possibly have a valid topological sort. In the regular English alphabet this will be
similar to having 'apple' come before 'app'. Note that if 'app' came before 'apple' the for loop for finding the first differing letter
would run up for the first minLength (3) letters, and make no update to the adjacency map. But if 'apple' came before 'app', then there
is no valid English alphabet order and the for loop will not find a first differing character and the dfs we do afterwards wont detect
this as a cycle. Anyway, with the adjacency graph completed, we literally do the topological sort from questions such as courseScheduleII.py
and thats it. If we detect a cycle, we return "", otherwise we get an array of a valid topological sort and join the elements in it using
the string join method "".join(validOrder) before returning.

Our aim is to find prerequisites using the first differing corresponding letter. If the first minLength letters are the same and word1
is shorter than word2, there is no differing letter since all corresponding letters. If the first minLength letters are the same and word1
is longer than word2, there is no valid topological sort. Otherwise, at the first index where corresponding letters differ, the letter
in word1 is a prerequisite of the letter in word2 (the letter in word1 precedes the letter in word2 in the alien dictionary). After
creating the prequisites adjacency hashmap, its regular topological sort.

"""


def alienOrder(words):
    # initialize adjacency hashmap with unique letter keys and empty set values
    adj = {letter: set() for word in words for letter in word}

    for i in range(len(words) - 1):     # first word index of adjacent word pairs
        w1, w2 = words[i], words[i+1]   # words are lexicographically sorted, compare adjacent words
        minLen = min(len(w1), len(w2))  # we compare the first minLen letters
        # edge case, if one word is a prefix, it has to be word 1
        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:    # first word longer but no diff char
            return ""                       # no valid topological order, edgecase for this question
        # to create letter: [prerequisites / preceding letters ]
        for j in range(minLen):         # compare first minlen chars
            if w1[j] != w2[j]:          # different letters at current index in words
                # directed graph of node: prerequisites, word 1's letter comes before word 2's
                adj[w2[j]].add(w1[j])   # word 1 letter is a prerequisite of word 2
                break                   # break out of inner for loop, first differing letter has been found

    nodes = list(adj.keys())        # for our outer loop
    visited = set()                 # a set is enough to track visited nodes
    visiting = set()                # a set is enough to track nodes currently in visting mode
    validOrder = []                 # topological sort
    for letterNode in nodes:        # topological sort is for DAG (doesnt need to be connected)
        if letterNode in visited:   # if current node was previously visited, dont repeat dfs
            continue
        if containsCycle(letterNode, adj, visited, visiting, validOrder):  # DAG (A=acyclic ie no cycles)
            return ""               # if a cycle was detected, there is no valid order
    return "".join(validOrder)      # return valid order as a string with no delimiters


def containsCycle(node, graph, visited, visiting, validOrder):
    if node in visited:     # if node was previously visited no need to re-do a dfs
        return False        # there is no cycle
    if node in visiting:    # if there node is still being visited, there is a cycle
        return True         # there is a cycle
    visiting.add(node)      # add node to visiting set
    for neighbor in graph[node]:    # start dfs from all prerequisites of node
        if neighbor in visited:     # prerequisited visited save repeated work
            continue
        if neighbor in visiting:    # detect a cycle
            return True
        if containsCycle(neighbor, graph, visited, visiting, validOrder):  # start cycle dfs
            return True
    visiting.remove(node)   # no cycle was detected from
    validOrder.append(node)  # valid order starts with lowest prerequisted (leaf node) first
    visited.add(node)       # visited node and valid order created
    return False


#words = ["wrt","wrf","er","ett","rftt"]
#words = ["z","x"]
#words = ["baa","abcd","abca","cab","cad"]
words = ["caa", "aaa", "aab"]
print(alienOrder(words))

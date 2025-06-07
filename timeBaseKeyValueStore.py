"""Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and 
retrieve the key's value at a certain timestamp.
Implement the TimeMap class:
TimeMap() Initializes the object of the data structure.
set(String key, String value, int timestamp) : Stores the key key with the value value at the given time timestamp.
get(String key, int timestamp): Returns a value such that set was called previously, with timestamp_prev <= timestamp. 
If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, 
it returns "".

Example 1:
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, 
then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
 
Constraints:
1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 107
All the timestamps timestamp of set are strictly increasing.
At most 2 * 105 calls will be made to set and get.


So we are going to need a hashmap (key-value pairs), and each key can have multiple values and each value is actually a
(val,time) pair. So {'foo':[['bar',1],['car',2]]}. Apart from the constructor, this class should support two methods, a
set method and a get method. The set(key,val,time), we add the (val, time) to the key's value list in the dictionary. The
get(key, time) will retrieve the value given the associated key such that the timestamp at which the value was stored is
less than or equal to the time in the get call ie timeStampStored <= time. In otherwords, if we addeed set('foo','bar',1),
we can return 'bar' when we call get('foo',1) or get('foo',2) but not for get('foo',0), That is time in the get method
represents the maximum time we can consider and if this time isnt in the map, we can decrement it for lower and lower times
and return the first value whose time we encounter as we go down from the maximum time ie the time passed into get(). Phew!
That is if we dont find the exact time, return the value of the closest time that is less than the time passed into get().

Now the set() operation is a constant time operation, since finding a key in a hashmap is constant time; appending to the
end of a list is also constant time. Now if we have to search for the value of the greatest timestamp that is less than or
equal to the time passed into get(), we can do a linear search in O(N), but the question is can we do better, such using
binary search which would be O(log(n)). However binary search requires that the search space be sorted ie we will need to
always maintain the [val,timestamp] pairs sorted by the time stamp in order. But how do we do this? Are we to sort the
value list of a key every time we call the get() function? That is actually a worse idea, because it would lead to a
worse time complexity of O(nlog(n)) . Now this is where reading the constraints of the question helps. In there we are 
told that all the timestamps of set() are strictly increasing. In other words, the [val,timestamp] pairs will be added in
strictly increasing (sorted ascending order) eg [val,1], [val, 3], [val,4] etc. We also know that the mimimum time is 1 a
and the maximum time will be the time of the peek value of the value list. Now if you think of a real world application,
the timestamp would be the current time at which one would be setting the value and time as we know goes forward, never
stands still and never ever ever goes back. Phew!!!. In otherwords, we we discovered a property of monotonicity and the 
binary search pattern here will be the maximum value whose timestamp is less than or equal to the passed timestamp in the
get() function, so we use the concise form of binary search for maximum for which condition is True (binarySearchII.py).

"""

class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:

        values = self.store.get(key) if key in self.store else [] #access the key's value list, default to []
        
        #binary search
        res = ""  #initialize 
        left, right = 0, len(values) - 1 #search space of binary search is the indices
        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
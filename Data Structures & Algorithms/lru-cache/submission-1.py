# we can create an array to store the key, value pair
# for get() func, we iterate through array and find whether key exists
# we also have to delete key from the array and append it to the end
# this makes sure that most recently used is at the end of the  array
# for put() func, we iterate through array and if present update the value
# remove the original and append with the new value
# if length of array reached capacity remove least recently used key array[0]
# the issue with this solution is both put() and get() is TC: O(n)

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        # iterate through cache to check whether key exists
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                pair = self.cache[i]
                self.cache.pop(i)
                self.cache.append(pair)
                return pair[1]
        return -1

    def put(self, key: int, value: int) -> None:
        # iterate to check whether key exists
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                self.cache.pop(i)
                self.cache.append([key, value])
                return
        
        if len(self.cache) == self.capacity:
            self.cache.pop(0)
        
        self.cache.append([key, value])
        return
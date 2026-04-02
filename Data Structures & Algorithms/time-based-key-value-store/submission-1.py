# we can create a hashmap and store the key: (value, timestamp) pairs
# the timestamp is in increasing order so we can use binary search to optimize TC to O(logn)
# TC for get func O(logn), set func: O(1)

class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = '', self.hashmap.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res
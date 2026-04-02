# we can solve the problem using an array but TC for both put() and get() funcs will be O(n)
# we can improve on TC by solving the problem with hashmap and doubly linked list
# for each node stored, we store the key-value pair and prev and next pointers
# we create 2 dummy pointers, left and right
# we store the nodes in the middle
# nodes close to the right are most recently used
# TC for both put() and get() will be O(1)
# SC: O(n)

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        nxt, prev = node.next, node.prev
        nxt.prev, prev.next = prev, nxt
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
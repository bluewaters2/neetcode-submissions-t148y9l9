# we can use a linkedlist to keep track of the added elements
# search will be O(n), remove will be O(1), in worst case O(n)

class Node:
    def __init__(self, val = -1, next = None):
        self.val = val
        self.next = next

class MyHashSet:
    def __init__(self):
        self.head = Node()

    def add(self, key: int) -> None:
        dummy = self.head
        newNode = Node(key)

        if self.contains(key):
            return

        while dummy.next:
            dummy = dummy.next
        
        dummy.next = newNode
        dummy = dummy.next
        return

    def remove(self, key: int) -> None:
        dummy = self.head
        while dummy.next:
            if dummy.next.val == key:
                dummy.next = dummy.next.next
                return
            dummy = dummy.next
        
        return

    def contains(self, key: int) -> bool:
        dummy = self.head
        while dummy:
            if dummy.val == key:
                return True
            dummy = dummy.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
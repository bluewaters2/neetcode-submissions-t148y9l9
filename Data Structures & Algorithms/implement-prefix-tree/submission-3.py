class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.search_prefix(word)
        return True if curr and curr.end else False

    def startsWith(self, prefix: str) -> bool:
        curr = self.search_prefix(prefix)
        return True if curr else False
        
    def search_prefix(self, word: str) -> TrieNode:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return None
            curr = curr.children[char]
        
        return curr

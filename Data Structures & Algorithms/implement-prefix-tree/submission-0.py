class PrefixTree:

    def __init__(self):
        self.children = [None] * 26
        self.end = False
        

    def insert(self, word: str) -> None:
        current_start = self

        for char in word:
            idx = ord(char) - ord('a')
            if current_start.children[idx] is None:
                current_start.children[idx] = PrefixTree()
            current_start = current_start.children[idx]
        
        current_start.end = True


    def search(self, word: str) -> bool:
        find_word = self.find_prefix(word)
        return find_word is not None and find_word.end


    def startsWith(self, prefix: str) -> bool:
        find_pre = self.find_prefix(prefix)
        return find_pre is not None
        
    
    def find_prefix(self, word: str) -> 'PrefixTree':
        current_start = self

        for char in word:
            idx = ord(char) - ord('a')
            if current_start.children[idx] is None:
                return None
            current_start = current_start.children[idx]
        return current_start
        
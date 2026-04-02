# we can use an array to store all the word and iterate through each to check whether it's equal to given
# TC with brute force would be O(n*m) for search which can be reduced to O(n) for search using prefix tree
# n is the length of word

class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char]
        curr.end = True


    def search(self, word: str) -> bool:
        def dfs(i, root):
            curr = root

            for j in range(i, len(word)):
                c = word[j]
                if c == '.':
                    for child in curr.children.values():
                        if dfs(j + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
                    
            return curr.end

        return dfs(0, self.root)

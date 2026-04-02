# we have an array of words and a given order of alphabets
# compare each word with the next to see whether the order is followed
# return false if the position of the letter in word is higher than the next word
# return False if words[i], words[i+1] for cases like applepie and apple, apple should come before applepie

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        counter_index = {key:i for i, key in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]

            for j in range(len(w1)):
                if len(w2) <= j:
                    return False
                
                if w1[j] != w2[j]:
                    if counter_index[w1[j]] > counter_index[w2[j]]:
                        return False
                    
                    break
        
        return True
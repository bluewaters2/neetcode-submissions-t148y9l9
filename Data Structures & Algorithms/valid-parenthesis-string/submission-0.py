# we can use 2 stacks to solve this problem
# separate stacks to store '(' and '*', because '*' can be used as '(', ')', ' '
# we iterate through the string and check whether the s1 is empty, then we treat '*' and '('
# if at the end of traversal len(s1) > 0, then we treat '*' as ')' if the index of '*' is more than '('
# TC: O(n), SC: O(n)  

class Solution:
    def checkValidString(self, s: str) -> bool:
        s1, s2 = [], []

        for i, char in enumerate(s):
            if char == '(':
                s1.append(i)
            elif char == '*':
                s2.append(i)
            else:
                # first we pop '(' if len(s1) > 0
                if len(s1) > 0:
                    s1.pop()
                # else we check if len(s2) > 0
                elif len(s2) > 0:
                    s2.pop()
                # this is an invalid string
                else:
                    return False
        
        # we check if s1 is not empty
        while len(s1) > 0:
            if len(s2) == 0:
                return False
            
            idx = s1.pop()
            idx1 = s2.pop()
            if idx1 < idx:
                return False
        
        return True

# we can use a stack to find whether the given string is a valid parenthesis
# we append the stack when its an open bracket and when its a close bracket then we pop the stack and check for the match
# since each character is visited only once, TC: O(n), SC: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in [')', '}', ']']:
                if len(stack) == 0:
                    return False
                else:
                    ch = stack.pop()
                    if (char == '}' and ch == '{') or (char == ']' and ch == '[') or (char == ')' and ch == '('):
                        continue
                    else:
                        return False
            
            else:
                stack.append(char)
        
        return len(stack) == 0

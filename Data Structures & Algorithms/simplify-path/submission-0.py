# we use stack since we have to remove the last entry when char == '..'
# for multiple '/', it will be treated as single '/'
# each character is visited only once so TC:O(n), SC:O(n)

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []

        for curr in path:
            if curr == '..':
                if stack:
                    stack.pop()
            
            elif curr != '.' and curr != '':
                stack.append(curr)
        
        return '/' + '/'.join(stack)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid < 0:
                while stack and stack[-1] > 0 and stack[-1] < (asteroid * -1):
                    stack.pop()
                
                if stack and stack[-1] == (asteroid * -1):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(asteroid)
            
            else:
                stack.append(asteroid)
        
        return stack

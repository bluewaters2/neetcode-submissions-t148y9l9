# we use a stack to keep track of the temp of ith index
# when temp is greater than temp of top index in stack we pop it from stack and update the value

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                ans[idx] = i - idx
            
            stack.append(i)
        
        return ans
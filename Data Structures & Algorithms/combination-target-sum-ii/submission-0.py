# we sort the given array candidates and then we dfs the given array to find the sum
# if the length of the array exceeds or the sum is more than target we return
# we also check for duplicates and continue

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(idx, curr, temp):
            if curr == target:
                ans.append(temp[:])
                return
            
            if idx >= len(candidates) or curr > target:
                return
            
            temp.append(candidates[idx])
            dfs(idx + 1, curr + candidates[idx], temp)
            temp.pop()

            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1

            dfs(idx + 1, curr, temp)
        
        candidates.sort()
        ans = []
        dfs(0, 0, [])
        return ans
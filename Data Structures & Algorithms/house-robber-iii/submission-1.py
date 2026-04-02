# we can recursively solve the problem, a node can either be counted or not
# the rucursive solution will be TC: O(2^n), SC: O(n)
# to avoid same calculations we can use memoization to store values
# TC:O(n), SC:O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {None: 0}

        def dfs(root):
            if root in dp:
                return dp[root]
            
            dp[root] = root.val

            if root.left:
                dp[root] += dfs(root.left.left) + dfs(root.left.right)
            
            if root.right:
                dp[root] += dfs(root.right.left) + dfs(root.right.right)
            
            dp[root] = max(dp[root], dfs(root.left) + dfs(root.right))
            return dp[root]
        
        return dfs(root)
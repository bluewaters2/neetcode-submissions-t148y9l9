# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root, level):
            if root is None:
                return
            
            if level < len(ans):
                ans[level].append(root.val)
            
            else:
                ans.append([root.val])
            
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        
        ans = []
        dfs(root, 0)
        return ans
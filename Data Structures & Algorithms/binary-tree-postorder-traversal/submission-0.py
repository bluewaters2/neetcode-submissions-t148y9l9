# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root):
            if root is None:
                return
            
            helper(root.left)
            helper(root.right)
            ans.append(root.val)
            return root
        
        ans = []
        helper(root)
        return ans
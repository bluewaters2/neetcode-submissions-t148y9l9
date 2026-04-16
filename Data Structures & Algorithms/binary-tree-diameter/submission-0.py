# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diff(node):
            if node is None:
                return 0
            
            nonlocal ans
            
            leftsub = diff(node.left)
            rightsub = diff(node.right)
            
            ans = max(ans, leftsub + rightsub)

            return 1 + max(leftsub, rightsub)
        
        ans = 0
        diff(root)
        return ans
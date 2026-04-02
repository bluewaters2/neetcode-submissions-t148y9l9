# we can use dfs to find whether the binary tree is balanced
# we perform a preorder traversal 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            nonlocal height_diff
            if root is None:
                return 0
            
            leftsub = height(root.left)
            rightsub = height(root.right)
            height_diff = max(height_diff, abs(rightsub - leftsub))

            return max(leftsub, rightsub) + 1
        
        height_diff = 0
        height(root)

        return True if height_diff <= 1 else False
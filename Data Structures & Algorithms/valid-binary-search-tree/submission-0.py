# we check the property of bst, make sure that the max element in leftsub is less than the node val
# and min element in right subtree is greater than the node val

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, leftval, rightval):
            if root is None:
                return True
            
            if root.val >= rightval or root.val <= leftval:
                return False
            
            return helper(root.left, leftval, root.val) and helper(root.right, root.val, rightval)
        
        return helper(root, -math.inf, math.inf)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        
        if root.left is None and root.val > val:
            root.left = TreeNode(val)
        
        elif root.right is None and root.val < val:
            root.right = TreeNode(val)
        
        elif root.val < val:
            self.insertIntoBST(root.right, val)
        
        else:
            self.insertIntoBST(root.left, val)
        
        return root
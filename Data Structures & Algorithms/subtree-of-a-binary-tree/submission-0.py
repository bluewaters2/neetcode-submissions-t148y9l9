# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(p, q):
            if p is None and q is None:
                return True
            
            elif p is None or q is None or p.val != q.val:
                return False
            
            return check(p.left, q.left) and check(p.right, q.right)
            
        if root is None and subRoot is None:
            return True
        
        elif subRoot is None or root is None:
            return False
        
        elif subRoot.val == root.val and check(subRoot, root):
            return True
        
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
# the delete node in bst can either be a leave node, or with a single subtree or both subtrees
# if both subtrees are present, we replace the inorder successor with the key node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        else:
            if root.left is None:
                return root.right
            
            elif root.right is None:
                return root.left
            
            else:
                prev = root.right
                while prev.left:
                    prev = prev.left
                root.val = prev.val
                root.right = self.deleteNode(root.right, prev.val)
            
        return root

# Inorder traversal arranges the tree in increasing order
# we can recursively or iteratively traverse the tree
# both will have space complexity of O(n) because recursively it will use recursive stack
# and iteratively we initialize a stack
# if we use morris traversal, the space complexity will reduce to O(1)
# visit the left subtree
# find the inorder predecessor (rightmost node of the left subtree)
# create a temporary right link from inorder predecessor to the current node
# then we again move to the left subtree of the leftnode of current
# If the inorder predecessor of the leftnode of current is current then we remove the temporary link and move to the right side of current
# else we find the inorder predecessor and create temporary right link to the leftnode of current
# TC: O(n), SC: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        while curr:
            if curr.left is None:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                # we find the inorder predecessor
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if prev.right is None:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right
        
        return -1
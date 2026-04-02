# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        q = deque([root])
        ans = []

        while q:
            level = []
            for _ in range(len(q)):
                r = q.popleft()
                level.append(r.val)

                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
            
            ans.append(level)
        
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inOrder(self, root):
        if root is None:
            return None
        a = self.inOrder(root.left)
        if a is not None:
            return a
        self.k -= 1
        if self.k == 0:
            return root.val
        return self.inOrder(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int):
        self.k = k
        return self.inOrder(root)
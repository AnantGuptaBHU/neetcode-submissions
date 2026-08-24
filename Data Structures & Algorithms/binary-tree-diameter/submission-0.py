# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxi = 0
    def diameter(self, root) -> int:
        if root is None:
            return 0
        a = self.diameter(root.right)
        b = self.diameter(root.left)
        self.maxi = max(self.maxi, a+b)
        return 1+max(a, b)
    def diameterOfBinaryTree(self, root) -> int:
        self.diameter(root)
        return self.maxi
        
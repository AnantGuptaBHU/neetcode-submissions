# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def fun(self, root, maxi):
        if root is None:
            return 0
        if root.val >= maxi:
            return 1 + self.fun(root.right, root.val) + self.fun(root.left, root.val)
        else:
            return self.fun(root.right, maxi) + self.fun(root.left, maxi)
    def goodNodes(self, root):
        return self.fun(root, root.val)
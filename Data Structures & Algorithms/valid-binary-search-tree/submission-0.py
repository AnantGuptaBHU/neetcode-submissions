# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findValid(self, root, mini, maxi):
        if root == None:
            return True
        if root.val >= maxi or root.val <= mini:
            return False
        return self.findValid(root.right, root.val, maxi) and self.findValid(root.left, mini, root.val)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.findValid(root, -1000000000, 1000000000)
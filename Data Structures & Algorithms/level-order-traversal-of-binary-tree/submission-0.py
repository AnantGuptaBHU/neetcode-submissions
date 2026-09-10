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
        stack = []
        r = []
        stack.append(root)
        while len(stack) > 0:
            l = []
            rr = []
            for i in range(len(stack)):
                a = stack.pop(0)
                rr.append(a.val)
                if a.left:
                    l.append(a.left) 
                if a.right: 
                    l.append(a.right)
            stack = l
            r.append(rr)
        return r
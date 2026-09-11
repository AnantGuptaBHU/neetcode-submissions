# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root, target, arr):
        if root is None:
            return arr
        arr.append(root)
        if root.val == target.val:
            return arr

        if target.val < root.val:
            return self.searchBST(root.left, target, arr)
        return self.searchBST(root.right, target, arr)
    def lowestCommonAncestor(self, root, p, q):
        arr1 = self.searchBST(root, p, [])
        arr2 = self.searchBST(root, q, [])
        l1 = len(arr1)
        l2 = len(arr2)
        common = arr1[0]
        i = 0
        while l1 and l2:
            if arr1[i].val == arr2[i].val:
                common = arr1[i]
                i+=1
                l1-=1
                l2-=1
            else:
                break
        return common




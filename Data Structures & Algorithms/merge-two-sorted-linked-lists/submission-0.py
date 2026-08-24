# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, h1, h2):
        nh = itr = ListNode(0)
        while h1 and h2:
            if h1.val < h2.val:
                itr.next = h1
                h1 = h1.next
            else:
                itr.next = h2
                h2 = h2.next
            itr = itr.next
        itr.next = h1 if h1 else h2
        return nh.next
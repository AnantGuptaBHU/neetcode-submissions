# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        if head.next == None:
            return None
        l = 0
        itr = head
        while itr:
            l+=1
            itr = itr.next
        count = 1
        itr = head
        if l == n:
            return head.next
        while count<(l-n):
            itr = itr.next
            count+=1
        print(itr.val)
        itr.next = itr.next.next
        return head
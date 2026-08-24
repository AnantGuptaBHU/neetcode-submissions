# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        if head == None or head.next == None:
            return head
        pre = head
        itr = head.next
        head.next = None
        while itr:
            temp = itr.next
            itr.next = pre
            pre = itr
            itr = temp
        return pre
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None:
            return 
        slow = fast = head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        second_half = self.reverse(slow)
        h1 = itr = head
        h2 = second_half
        while h1:
            t1 = h1.next
            t2 = h2.next
            h1.next = h2
            if t1 is None:
                break
            h2.next = t1
            h1 = t1
            h2 = t2
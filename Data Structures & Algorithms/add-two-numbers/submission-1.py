# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def print(self, head):
        a = []
        while head:
            a.append(head.val)
            head = head.next
        print(a)
    def addTwoNumbers(self, l1, l2):
        head = r1 = l1
        r2 = l2
        carry = 0
        while r1 and r2:
            a = r1.val+r2.val+carry
            carry = a//10
            val = a%10
            r1.val = val
            if r2.next and r1.next:
                r2 = r2.next
                r1 = r1.next
            else:
                break
        self.print(r1)
        if r1.next == None:
            r1.next = r2.next
        while r1.next:
            r1 = r1.next
            a = r1.val + carry
            carry = a//10
            val = a%10
            r1.val = val
        if carry != 0:
            node = ListNode(carry)
            r1.next = node
        return head



























        # while r1.next:
        #     r1 = r1.next
        #     a = r1.val + carry
        #     carry = a//10
        #     val = a%10
        #     r1.val = val           
        # if r2.next:
        #     r1.next = r2.next
        #     r2 = r2.next
        # while r2.next:
        #     a = r2.val + carry
        #     carry = a//10
        #     val = a%10
        #     r2.val = val
        #     r1 = r2
        #     r2 = r2.next
        #     if r2.next == None:
        #         a = r2.val + carry
        #         carry = a//10
        #         val = a%10
        #         r2.val = val
        #         r1 = r2
        #         r2 = r2.next
        #         break

        # if carry != 0:
        #     node = ListNode(carry)
        #     r1.next = node
        # return l1



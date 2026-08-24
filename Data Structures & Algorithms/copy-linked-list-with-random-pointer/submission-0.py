# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d= {}
        itr = head
        nh = pre = Node(0)
        while itr:
            if itr in d:
                pre.next = d[itr]
                pre = d[itr]
                node = d[itr]
            else:
                node = Node(itr.val)
                pre.next = node
                pre = node
                d[itr] = node
            if itr.random == None:
                node.random = None
            elif itr.random != None:
                if itr.random in d:
                    node.random = d[itr.random]
                else:
                    random_node = Node(itr.random.val)
                    node.random = random_node
                    d[itr.random] = random_node
            itr = itr.next
        return nh.next
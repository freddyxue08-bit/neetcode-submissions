# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes=[]
        while head is not None:
            if head in nodes:
                return True
            elif head.next is None:
                return False
            else:
                nodes.append(head)
                head=head.next
        return False
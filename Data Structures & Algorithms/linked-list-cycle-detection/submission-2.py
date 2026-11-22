# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes={}
        while head is not None:
            if nodes.get(head,0)!=0:
                return True
            else:
                nodes[head]=1
                head=head.next
        return False
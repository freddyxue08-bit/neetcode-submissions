# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=ListNode()
        prev=None
        node=None
        while head is not None:
            nxt=head.next
            node=head
            node.next=prev
            prev=node
            head=nxt
        return node
            
            
        
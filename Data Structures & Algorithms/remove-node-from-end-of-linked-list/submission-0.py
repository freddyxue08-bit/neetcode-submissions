# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first=head
        second=head
        prev=head
        ans=prev
        for i in range(n): 
            first=first.next
        if first==None:
            ans=ans.next
        while first is not None:
            first=first.next
            prev=second
            second=second.next
        prev.next=second.next
        return ans
        
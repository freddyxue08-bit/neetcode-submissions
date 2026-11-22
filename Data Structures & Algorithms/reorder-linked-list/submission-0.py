# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        new=head
        fast=head
        slow=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        reverse=ListNode()
        prev=None
        reverse=None
        reverse=slow.next
        slow.next=None
        while reverse is not None:
            nxt=reverse.next
            reverse.next=prev
            prev=reverse
            reverse=nxt
    
        reverse=prev

        while reverse is not None:
            head=new
            new=new.next
            head.next=reverse
            reverse=reverse.next
            head=head.next
            head.next=new


    
        





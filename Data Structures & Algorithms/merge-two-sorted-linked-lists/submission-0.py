# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node=ListNode()
        prev=ListNode()
        ans=prev
        node=None
        while list1 is not None and list2 is not None:
            if list1.val>list2.val:
                node=list2
                prev.next=node
                prev=prev.next
                list2=list2.next
            else:
                node=list1
                prev.next=node
                prev=prev.next
                list1=list1.next
        while list1 is not None:
            node=list1
            prev.next=node
            prev=prev.next
            list1=list1.next
        while list2 is not None:
            node=list2
            prev.next=node
            prev=prev.next
            list2=list2.next
        return ans.next

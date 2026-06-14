# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        second=slow.next
        slow.next=None
        curr=second
        prev=None

        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        second=prev
        first=head
        while second:
            t1, t2=first.next, second.next
            first.next=second
            second.next=t1
            
            first=t1
            second=t2

        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast, slow= head, head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        cur=slow.next
        slow.next=None
        prev=None

        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        
        p1=head # return
        p2=prev
    
        while p2:
            temp1, temp2=p1.next, p2.next
            p1.next=p2
            p2.next=temp1
            p1, p2=temp1, temp2
        



        
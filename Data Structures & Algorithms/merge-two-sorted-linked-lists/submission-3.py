# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy=node=ListNode()
        p1=list1
        p2=list2

        while p1 and p2:
            if p1.val<p2.val:
                node.next=p1
                p1=p1.next
            
            else:
                node.next=p2
                p2=p2.next
            node=node.next
        if p1:
            node.next=p1
          
        if p2:
            node.next=p2
            

        return dummy.next

        
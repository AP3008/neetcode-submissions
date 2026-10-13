# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr =head 
        tracker = list()
        while curr:
            tracker.append(curr)
            curr = curr.next 
        remove = len(tracker) - n
        if remove == 0:
            return head.next 
        
        tracker[remove-1].next = tracker[remove].next 
        return head 

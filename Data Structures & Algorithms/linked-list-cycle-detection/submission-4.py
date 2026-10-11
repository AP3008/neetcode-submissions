# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # We can keep track of the visited nodes in a map for O(n) solution, but it would be faster to use a slow and fast pointer that returns true when they intersect and false when fast reaches null. 
        if not head: return False 
        if head.next == None:
            return False
        slow = head 
        fast = head.next.next  
        while fast:
            if fast.next == None:
                break 
            if slow == fast:
                return True 
            slow = slow.next 
            fast = fast.next.next 
        return False 
            
            
        

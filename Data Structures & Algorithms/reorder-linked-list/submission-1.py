# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Couple of patterns come to mind, two pointers and array. 
        # Array: we can put the entire linked list in an array, order the array using two pointers switching the slots in the array, and either during the switch connect the ListNode.next to the re-ordered node, or at the end with the sorted list just iterate through and connect the ListNodes. 

        res = []
        curr = head 
        while curr:
            res.append(curr)
            curr = curr.next 
        l, r = 0, len(res)-1
        while l < r:
            res[l].next = res[r]
            l+=1 
            if l == r:
                break
            res[r].next = res[l]
            r-=1
        res[l].next = None

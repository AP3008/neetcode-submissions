class ListNode:
    def __init__(self,key):
        self.key = key
        self.next = None
    
class MyHashSet:

    def __init__(self):
        self.sett = [ListNode(0) for _ in range(10**4)] 

    def add(self, key: int) -> None:
        index = key % len(self.sett)
        # We use curr.next because we want to skip the dummy node
        curr = self.sett[index]
        while curr.next:
            if curr.next.key == key:
                return 
            curr = curr.next
        curr.next = ListNode(key)
        

    def remove(self, key: int) -> None:
        curr = self.sett[key%len(self.sett)]
        while curr.next:
            if curr.next.key == key:
                # If we find the key we just want to disconnect it from the linked list and add the following value on. 
                curr.next = curr.next.next
                return 
            curr = curr.next 

    def contains(self, key: int) -> bool:
        curr = self.sett[key%len(self.sett)]
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next 
        return False 


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
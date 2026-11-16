# This is a valid solution but we are creating too large of an array. 
class ListNode:
    def __init__(self, key, value):
        self.key = key 
        self.value = value
        self.next = None 
class MyHashMap:

    def __init__(self):
        self.hashMap = [ListNode(-1,-1) for _ in range(10**2)]

    def put(self, key: int, value: int) -> None:
        curr = self.hashMap[key%len(self.hashMap)]
        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return
            curr = curr.next 
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        curr = self.hashMap[key%len(self.hashMap)]
        while curr:
            if curr.key == key:
                return curr.value 
            curr = curr.next 
        return -1

    def remove(self, key: int) -> None:
        curr = self.hashMap[key%len(self.hashMap)]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next 
        return 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
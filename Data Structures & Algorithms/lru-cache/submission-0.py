class Node:
    def __init__(self, value=0, key=0):
        self.key = key 
        self.value = value
        self.prev, self.next = None, None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node() # Left, LRU
        self.tail = Node() # Right, Most recent use 
        self.head.next = self.tail
        self.tail.prev = self.head 

    def insert(self, node):
        # inserts before tail (right)
        prevTail = self.tail.prev
        prevTail.next = node 
        node.next = self.tail
        node.prev = prevTail 
        self.tail.prev = node 

    def remove(self, node):
        # removes from left 
        nxt, prev = node.next, node.prev
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(value, key) 
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]


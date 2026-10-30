class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        # Two sentinel (dummy) nodes stay constant, and we build everything in the middle of them.
        # Renamed from head/tail to left/right so the names match the picture:
        # left = sentinel BEFORE index 0 (the front of the list)
        # right = sentinel AFTER the last index (the end of the list)
        # left -> 0 -> 1 -> 2 -> right
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
        self.length = 0

    def get(self, index: int) -> int:
        # It is zero indexed: index 0 is the node right after the left sentinel.
        # left -> 0 -> 1 -> 2 -> right
        # get 2
        # curr = left.next (idx 0) -> 1 -> 2
        if index < 0 or index >= self.length:
            return -1
        curr = self.left.next  # @ idx: 0
        for i in range(index):
            curr = curr.next
        return curr.val

    def addBetween(self, n1, n2, newNode):
        # Helper: n1 <-> newNode <-> n2 (n1 and n2 must be neighbours)
        n1.next = newNode
        n2.prev = newNode
        newNode.next = n2
        newNode.prev = n1

    def addAtHead(self, val: int) -> None:
        # "Head" in LeetCode = the FRONT, so the new node becomes index 0.
        # FIX: this used to insert at the end (before the right sentinel).
        # left -> (new) -> 0 -> 1 -> right
        self.addBetween(self.left, self.left.next, Node(val))
        self.length += 1

    def addAtTail(self, val: int) -> None:
        # "Tail" in LeetCode = the END, so the new node becomes the last index.
        # FIX: this used to insert at the front (after the left sentinel).
        # left -> 0 -> 1 -> (new) -> right
        self.addBetween(self.right.prev, self.right, Node(val))
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # Valid indices are 0..length (inclusive).
        # index == length means "append at the end", so it must be allowed.
        # FIX: the old check (index > length - 1) rejected index == length,
        # which also broke addAtIndex(0, x) on an empty list.
        if index < 0 or index > self.length:
            return

        # FIX: no special cases needed for index 0 or the last index.
        # Walk to the node currently at `index` and insert just before it.
        # If index == length, curr lands on the right sentinel, which still works:
        # left -> 0 -> 1 -> right     addAtIndex(2, x)
        # curr = right  ->  insert between 1 and right
        curr = self.left.next  # @ idx: 0
        for i in range(index):
            curr = curr.next
        self.addBetween(curr.prev, curr, Node(val))
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        # left -> 0 -> 1 -> 2 -> right
        # rm 1
        # curr = left.next (idx 0) -> 1
        if index < 0 or index >= self.length:
            return
        curr = self.left.next  # @ idx: 0
        for i in range(index):
            curr = curr.next
        # Now we want to rm curr: link its neighbours to each other, skipping it.
        # 0 <-> (1) <-> 2   becomes   0 <-> 2
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
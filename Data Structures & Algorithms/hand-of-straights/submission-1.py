class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # If the length of hand is not divisible by the group size we know it doesn't work so we return False 
        if len(hand) % groupSize: return False
        
        # We want to count all occurences of each number 
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n,0)
        
        # We create a min heap from the keys, so all of the values from hand 
        minH = list(count.keys())
        heapq.heapify(minH)
        # While there are elements in the min heap we loop
        while minH:
            # The top of the min heap is the smallest value, which is how we will be building up our hand 
            first = minH[0]
            # we iterate from the first value to the first value plus the size of our group for example [1...5] if we have a group size of 5
            for i in range(first, first+groupSize):
                # If i is not in our counter hashmap, we know a valid straight can't be built, so we return false
                if i not in count:
                    return False
                # If i exists in count we decrement 
                count[i] -= 1
                # If count[i] is 0 we want to pop the value from the minHeap 
                if count[i] == 0:
                    # If the value of count[i] is not at the top of the minHeap we want to return false
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        # If we make it through the list we return true 
        return True 
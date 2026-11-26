class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # We sort the array so we can have it in ascending order 
        people.sort()
        # This is our result variable
        res = 0
        # We want pointers and the beginning and end of the array. 
        l, r = 0, len(people) - 1
        # We use l<=r because if l and r overlap there is still 1 person left in the array so we have to add them to the boat
        while l <= r:
            # We calc. the ramin by taking away the people[r] from teh limit 
            remain = limit - people[r]
            # Since we take that person we can decrement the right pointer. 
            r -= 1
            # We increase the amount of boats we use no matter what because it will at min. be the person at people[r] 
            res += 1
            # If we can use some of the elements on the left we increment, and fit them onto the boat. 
            if l <= r and remain >= people[l]:
                l+=1 
        return res
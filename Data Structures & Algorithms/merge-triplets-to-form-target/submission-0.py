class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # iterate through every triplet and filter out the ones that have any values that are too great, for any position. This leaves us with only triplets that are less than or equal to the target. 

        good = set()

        for t in triplets:
            if t[0] > target[0] or target[1] < t[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                # If the value appears in target we can append it to our good set because we found a value that matches the target.
                if v == target[i]:
                    good.add(i)
        # If we have found 3 good values, that means we have found a match. 
        return len(good) == 3
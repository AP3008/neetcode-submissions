class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # Sliding window problem 
        l, r = 0, 1
        res, prev = 1, ""
        while r < len(arr):
            if arr[r-1] > arr[r] and prev != ">":
                res = max(res, r-l+1)
                r+=1 
                prev = ">"
            elif arr[r-1] < arr[r] and prev != "<":
                res = max(res, r-l+1)
                r+=1 
                prev = "<"
            else:
                # We do this to skip the equals signs, and still grab the length from them 
                r = r + 1 if arr[r] == arr[r-1] else r
                # We move the left pointer right before the right one because the longest subarray could include the previous sign, as an alternating or equal to pattern can still follow. 
                l = r - 1
                # We reset as if it is the beginning again. We do this instead of making in the actual relation at r-1 and r so we don't have to use nested if statements. 
                prev = ""
        return res 


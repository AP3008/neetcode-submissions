class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize our trackers and res
        res = 0
        curSum = 0
        # In this hashmap the key is the prefix sum, and the value is the current count of occurences for each subarray. Essentially how many times it has been seen. 
        # We add 0 : 1 because in all cases there is a prefix of 0 technically that exists. We need this so we can increment res if the nums[i] == k.
        prefixSums = { 0 : 1 }

        # We iterate through nums
        for n in nums:
            # The current sum is accounting for nums[i]
            curSum += n
            # The difference i.e what currSum needs to reach k is stored in diff
            diff = curSum - k
            # If diff exists in the hashmap for each occurence it has we can add that to res, for instance if diff = 1, and in the map we had 1 : 2, we would increment res by 2 because there are two prefix sums of 1, that we can remove, that have appeared earlier. 
            res += prefixSums.get(diff, 0)
            # We want to keep track of the current prefix Sum and increment the count associated to it. 
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        # We want to return the total res. 
        return res 
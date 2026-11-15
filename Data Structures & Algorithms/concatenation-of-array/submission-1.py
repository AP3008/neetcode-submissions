class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # You can also just append nums onto nums so the space complexity is slightly less (O(n)) still but we don't have to go through n twice, just once. 
        res = [0] * (len(nums)*2)
        for i in range((len(nums)*2)):
            res[i] = nums[i%(len(nums))]
        return res 
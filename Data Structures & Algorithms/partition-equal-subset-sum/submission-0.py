class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Brute force O(2^n): Test every subset against each other validating for our condition. Think decision tree where we can keep or not keep an element, and do that for every element in the array.  
        
        # IDEA: We want to find out if an array can be plit into two equal subsets with equal sums, each subset must sum up to total / 2, because if you can find one that sums to total / 2, the leftover element automatically sum to total / 2. So we reframe the question to finding the subset that equals total / 2.
        # DP sol: 
        
        # Our bottom up approach will be looking at every value and seeing if we can include it in our set. This follows the same logic as the backtracking but we can add a DP element by having a set that includes all of the possible sums, and if we find our target (half of the sum of the array) we know there is a valid paritition, if not we return false. The set will include the value at every index plus the sum of every subset seen before that value with it added on, plus 0. We add the 0 to the set because no matter what we can create a subset with 0 in it, and we need a way to include just the element in. This method works because how you reach the sum doesn't matter it's the fact that there exists a sum where you can reach the sum.  

        # If the sum of nums is odd, it will be impossible for us to partition it, into equal halves 
        # This syntax works because 0 is falsey, and any other value (1) will be truthy. 
        if sum(nums) % 2: return False

        # dp holds every sum that some subset of the numbers processed so far can produce. 
        dp = set()
        # This is the base case, and it allows us when iterating through the set to add the current value to the set. "nums[i] + 0 = nums[i]"
        dp.add(0)  
        # Half of the input array, and our target value that we are searching for. 
        target = sum(nums) // 2  

        # Which side of the array this is done from doesn't matter as this works decrementing to 0 and incrementing to len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            # We build a new set because python creates an error when modifying a set while looping over it. Also this may raise an error in teh fact that we might use nums[i] multiple times. 
            nextDp = set()
            # This is the decision tree logic to keep the current value or not to, we need to add t because it woudln't be in our new dp set and if we don't include it we lose information that we already used. 
            for t in dp:
                nextDp.add(t+nums[i])
                nextDp.add(t)
            # Now we newDp holds everything dp did plus all of the subsets with nums[i] so we replace our old dp. 
            dp = nextDp
        # After all elements are processed dp contains every possible subset sum for the whole array and if target exists, we know that a valid partition exists. 
        return True if target in dp else False 
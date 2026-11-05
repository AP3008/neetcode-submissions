class Solution:
    def rob(self, nums: List[int]) -> int:
        # We want to maximize how much we steal, but we cannot steal from adjacent houses. This seems greedy but we know this is a dp sol. The length is gaurenteed to be between 1 and 100, so at minimum we can always rob one house. 

        # We can steal from alternating houses, either starting at 0 or 1, once we choose one way, we cannot change it unless we decide to skip a house and go to a house i+2 away, switching us onto the the other path. 
        # What we want to essentially find the maximum we can steal from a house and the ones previous to it, we can do this bottom up. 

        rob1, rob2 = 0,0

        # [rob1, rob2, n, n+1]
        for n in nums:
            # If we rob on this square which is rob1, we can include n, but if we rob2 we can't rob n, only n+1, this way we can solve the subproblems and work upwards 
            tmp = max(n+rob1, rob2)
            # Now we are incrementing so we want to store rob2 which is the curent index + 1 in rob1 which is the index we are moving towards
            rob1 = rob2
            # Then we store the max of the current square in rob2
            rob2 = tmp
        # By the end of the loop, the sum of the best choices will be rob2.
        return rob2
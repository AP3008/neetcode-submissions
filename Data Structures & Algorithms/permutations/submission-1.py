class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # IDEA: Bottom up approach to permutation, recursively building up the array by starting with an empty list inserting each element from the end of the array at every position. 

        # If nums is empty we return an empty list of lists 
        if len(nums) == 0:
            return [[]]
        
        # We recursively run the permutation function to get a resulting list of characters with progressively less numbers in it until nums[1:] is of length 0. On that iteration where perms = [[]] we add the first values of nums to the beginning and append whatever is left in nums which will be 1 value, then it builds up and returns to the previous recursive call, until we get all permutations back. 
        perms = self.permute(nums[1:])
        # resulting array
        res = []
        # For each element of perms, at minimum this will be a list containing a list 
        for p in perms:
            # For the length of the list inside + 1, we iterate. It is +1 because we want to insert the values from the front all the way to the back, so that will be at an index greater than the length of p. 
            for i in range(len(p)+1):
                # We copy p, because we don't want to change anything inside of p, as in python mutating the array will change it within perms aswell
                p_copy = p.copy()
                # inserting nums[0] at every position 
                p_copy.insert(i, nums[0])
                # adding this permutation to res 
                res.append(p_copy)
        # returning the result 
        return res 


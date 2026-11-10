class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # If the sum of the lengths of s1 and s2 don't make s3 we know we can't interweave them to create s3, so we return False
        if len(s1) + len(s2) != len(s3):
            return False
        # We create our 2D dp with false in all of the indexes 
        dp = [[False] * (len(s2)+1) for i in range(len(s1)+1)]
        # We want to set the index of the bottom right to True as our base case
        dp[len(s1)][len(s2)] = True
        # We iterate backwards through the dp, thats why it is important to have the basecase 
        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):
                # We check if i is still in s1 and check if it matches the value in s3, if it does we set the current index to True and we check the value of the index to the right to see if it is True
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j]=True
                # This is the same thing except we check the index of the column below, and instead of s1 we use s2
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True 
        # Once the loop finishes executing we can check the value of the first index, if there was a valid solution it will have a true, if not it will still be False.
        return dp[0][0]

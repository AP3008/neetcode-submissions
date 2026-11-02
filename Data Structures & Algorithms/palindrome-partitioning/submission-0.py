class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #IDEA: we brute force backtrack our way through checking every single partition, if any substring we find is a palindrome we can add it to the list. We perform a dfs whenever we find a palindrome to see if a larger palindrome can be created, and to add it to the list

        # Our resulting list and a list of partitions we use to backtrack. 
        res = []
        part = []

        # Our dfs function that takes in the index that we are looping from 
        def dfs(i):
            # If the index is out of bounds, we have found a valid palindrome and want to copy it to our res and stop exploring 
            if i >= len(s):
                res.append(part.copy())
                return 
            # For every letter in between the range of index i and the end of the string we want to test for letters to see if we have a palindrome
            for j in range(i, len(s)):
                # A helped funciton that takes in the string we are looking over to see if it contains a palindrome from the left to right indicies 
                if self.isPali(s,i,j):
                    # If we do have a palindrome we want to append this partition to our part function and perform dfs from there to see if we can get all palindromes that are within it.
                    part.append(s[i:j+1])
                    # So we start the dfs from index j+1 
                    dfs(j+1)
                    # At the end of the dfs we want to remove the partition so it doens't intefere with subsequent recursive calls.
                    part.pop()

        # We start exploring from index 0 of s 
        dfs(0)
        # returning the resulting string 
        return res
    # Helped palidrome function, it takes in a string s and the left and right bounds we want to check 
    def isPali(self, s, l, r):
        # If a string has the outside characters equal and we move towards each other until l surpasses r we know that we have a palindrome in one pass
        while l < r:
            # If at any point s[l] and s[r] do not equal each other we return false
            if s[l] != s[r]:
                return False 
            # increment the left pointer and decrement the right pointer moving closer to each other. 
            l+=1 
            r-=1
        # return true 
        return True 
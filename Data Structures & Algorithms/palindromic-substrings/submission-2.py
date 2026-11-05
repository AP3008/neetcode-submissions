class Solution:
    def countSubstrings(self, s: str) -> int:
       # We can do the same thing as finding the longest substring except we increment a count and have a hashset to check if a substring already in there. 

       # The idea works but only for unqiue palindromic substrings, it doesn't really hold for duplicates. ## NOTE if you put the set inside of each loop it then holds, but this is not the fastest solution.

       # NOTE: I overcomplicated this by adding a set to it thinking I needed to account for the duplicates, but it is still valid with the exact same code as longest palindrome.  

        res = 0 
        for i in range(len(s)):
            res += self.countPalindrome(i,i,s) + self.countPalindrome(i,i+1,s)
        return res 

    def countPalindrome(self, l, r, s):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res+=1 
            l-=1 
            r+=1 
        return res 



class Solution:
    def countSubstrings(self, s: str) -> int:
       # We can do the same thing as finding the longest substring except we increment a count and have a hashset to check if a substring already in there. 

       # The idea works but only for unqiue palindromic substrings, it doesn't really hold for duplicates. ## NOTE if you put the set inside of each loop it then holds, but this is not the fastest solution. 

        res = 0 
        for i in range(len(s)):
            # odd logic 
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res+=1 
                l-=1 
                r+=1
            
            # even logic
            l, r = i, i+1
            while l>=0 and r < len(s) and s[l] == s[r]:
                res+=1
                l-=1 
                r+=1 
        return res 


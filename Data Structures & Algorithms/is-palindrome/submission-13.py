class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Just have a left and right pointer at the end of the string and beginning. comparing each letter, ignoring case so use .lower() and if the char is isalnum() we can decrement or increment ignoring it. 

        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l+=1 
            while r > l and not s[r].isalnum():
                r-=1 
            if s[l].lower() != s[r].lower(): return False
            l+=1 
            r-=1  

        return True 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False 
        seen1 = {}
        seen2 = {}
        for i in range(len(s)):
            seen1[s[i]] = seen1.get(s[i], 0)+1
            seen2[t[i]] = seen2.get(t[i], 0)+1
        
        return seen1 == seen2 
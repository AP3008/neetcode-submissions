class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        maxL = 0 
        for r in range(len(s)):
            length = r - l + 1
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
                length-=1
            seen.add(s[r])
            maxL = max(maxL, length)
        return maxL
            
                
            

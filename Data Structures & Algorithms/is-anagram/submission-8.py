class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # trivial solution 
        return sorted(s) == sorted(t)
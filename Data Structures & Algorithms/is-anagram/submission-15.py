class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       # trivial 
       # return set(s) == set(t)

        seen = {}
        for c in s:
            seen[c] = seen.get(c, 0)+1 
        for c in t:
            if c not in seen or seen[c] <= 0:
                return False 
            seen[c] -= 1
        return True if sum(seen.values()) == 0 else False 
    
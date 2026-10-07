class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # trivial solution 
        # return sorted(s) == sorted(t)

        # 1. if lengths don't match = false
        if not len(s) == len(t):
            return False

        # 2. since they are strings of the same length, we want to do one pass tracking all seen values and store them in a hashmap 
        ## For now we can use 2 hashmaps but I believe we can use one and check if any of the values are odd, meaning they appeared in one but not the other
        seen1 = {}
        seen2 = {}
        for i in range(len(s)):
            seen1[s[i]] = seen1.get(s[i], 0) + 1
            seen2[t[i]] = seen2.get(t[i], 0) + 1
        
        # 3. Since all of the values should be even if it is an anagram, I just need to make sure it isn't off

        return seen1 == seen2

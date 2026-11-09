class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If the string is empty we return "" 
        if not t: return "" 

        # A hashmap for the letter count in t
        # A hashmap for the letters in our current letter. 
        countT, window = {}, {}

        # gathering the count for each letter in t 
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # The amount of letters we have compared to how many we need, which will be all of the letters in t 
        have, need = 0, len(countT)
        # We keep track of res as indexes, and the length of the result will infinity to start 
        res, resLen = [-1,-1], float("inf")
        # our left pointer starting at index 0 
        l=0
        # Our right pointer will be going through the entire list and initialized by the for loop.
        for r in range(len(s)):
            # the char we are looking at will be at s[r]
            c = s[r]
            # Our window count needs to be incremented so we can keep track of the letters in the window 
            window[c] = 1 + window.get(c, 0)

            # If c is in t and the amount of letters we have matches we want to increment the amount that we have
            if c in countT and window[c] == countT[c]:
                have+=1
            # If have equals need, we ahve found a valid substring that includes t, so now we want to find if there exists a smaller version, we can do this by decrementing the size of the window and moving the l index up until the amount we have doesn't match need, so we can continue to search for substrings. 
            while have == need:
                # update our result
                if (r-l+1) < resLen: # if this substring is better than what we have, we take it as our new answer 
                    res = [l, r]
                    resLen = r-l+1
                # we remove l from the window counter, because we are moving the left pointer forward 
                window[s[l]] -= 1
                # If s[l] was a letter in t, we need to decrement have 
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1
                # finally increment the left pointer to slide the window
                l += 1
        # we store the indexes from res in l and r so we can return the substring 
        l, r = res
        # if resLen is still infinity, we want to return an empty string
        return s[l:r+1] if resLen != float("inf") else ""  
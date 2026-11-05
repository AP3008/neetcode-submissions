class Solution:
    def longestPalindrome(self, s: str) -> str:
        # res string 
        res = ""
        # resulting strings length so we can compare
        resLen = 0
        for i in range(len(s)):
            # odd length 
            # this works because we assuming that s[i] is the middle and expand out, so via this loop we can only get odd answers
            l, r = i, i
            # We loop while the pointers are in bound and s[l] = s[r], since this was true before we don't have to recheck the inside if it was a palindrome 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If the length between r and l is greater than the result strings length we have found a new result string 
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                # If the while loop condition is true we want to increment the right pointer and decrement the left pointer. 
                l-=1
                r+=1

            # even length 
            # If we encounter an even string we need to look at the look at the char at the current index and the following index and increment and decrement pointers in the same fashion. This is essentially the same logic of odd length except imagine we are building the palindrome around some invisible char between these two pointers. 
            l, r = i, i+1
            while l>= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
        # We can return the res after the loop finishes executing. 
        return res 
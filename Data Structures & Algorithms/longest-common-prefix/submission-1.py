class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        # We can save the first string then loop through the following elements and go until there is a match, if not we cut off the string at that index. 

        res = strs[0]
        for i in range(1,len(strs)):
            if len(res) > len(strs[i]):
                res = res[:len(strs[i])]
            for j in range(len(res)):
                if res[j] != strs[i][j]:
                    res = res[:j]
                    break 
        return res 
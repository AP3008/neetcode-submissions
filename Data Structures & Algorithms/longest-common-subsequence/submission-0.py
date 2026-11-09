class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # creating a 2D DP with the length of text2 + 1 as the rows and text1 + 1 as the columns, this is so we have the extra 0's on the edge. Each cell represents that Longest Common Substring between each letter from text[i:] and text2[j:], so our solution is a bit brute force. The plus 1's are because we need the suffixs of text1 and text2 to be empty to cover the full string, they also make sure that we never go out of bounds. 
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        # We loop backwards through the array from the last character down to index 0, in both strings. We do it in this order because each cell depends on the cells below it, and to its right. We fill information from the bottom right corner and walk towards the left. 
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                # Case 1: if the text at i and j match, that means the first characters of the two suffixes match, so you can make this letter apart of the subsequence. This just gives 1 but the dp[i+1][j+1] is coming from the best lowest common subsequence of whatever is left of after both characters, which will be in the diagonal cell. 
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                # Case 2: they don't match, so we can't pair text1[i] and text2[j] so one of them has to be left out. We dont know which one to drop, so we try both and keep the max result. dp[i+1][j] drops text1[i] and keeps all of text2[j:]. This is the cell below, while dp[i][j+1] drops text2[j] and keeps all of the text1[i:]. This would be the cell to the right
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        # The top left cell is the lowest common subsequence of text[0:] and text2[0:], which are the full strings.
        return dp[0][0]
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Idea: (Naive approach) Create a hashmap that maps digits to a list of letters. Iterate through the digits, retrieve a list and iterate through it adding letters to a result string and appending it to a result list. Esspentially performing a DFS and once there are no digits left we append the string to the res list.  

        # Notes: the length of each output string is also the length of the digits, digits can be at most 4 digits long. 

        # If there are no digits we can return back an empty list 
        if not digits:
            return []

        # Map for the number to letter combination 
        dtol = { "2" : ["a","b","c"],
                 "3" : ['d','e','f'],
                 "4" : ['g','h','i'],
                 "5" : ['j','k','l'],
                 "6" : ['m','n','o'],
                 "7" : ['p','q','r','s'],
                 "8" : ['t','u','v'],
                 "9" : ['w','x','y','z']}
        # Our resultuing list
        res = list()
        # The dfs that takes in the current string being built, the next index of digits we need to explore, and the current letter to be added
        def dfs(s, idx, toAdd):
            # Adding the letter to our string this iteration. 
            s+=toAdd
            # If the index is out of range in digits we don't need to continue the dfs and can append s to our res, and end this DFS. 
            if idx >= len(digits):
                res.append(s)
                return 
            # For each letter that the next digit maps to we need to perform individual DFS's on then adding the current letter. 
            for let in dtol[digits[idx]]:
                dfs(s,idx+1,let)
        # We can just call dfs from index of 0 and put empty strings as the arguments becuase it works from index 0 to index len(digits)-1
        dfs("", 0, "")
        # The resulting array will have all of the strings appended so we can return res. 
        return res 
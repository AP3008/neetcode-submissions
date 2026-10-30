class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Idea: (Naive approach) Create a hashmap that maps digits to a list of letters. Iterate through the digits, retrieve a list and iterate through it adding letters to a result string and appending it to a result list. Esspentially performing a DFS and once there are no digits left we append the string to the res list.  

        # Notes: the length of each output string is also the length of the digits, digits can be at most 4 digits long. 

        if not digits:
            return []
        dtol = { "2" : ["a","b","c"],
                 "3" : ['d','e','f'],
                 "4" : ['g','h','i'],
                 "5" : ['j','k','l'],
                 "6" : ['m','n','o'],
                 "7" : ['p','q','r','s'],
                 "8" : ['t','u','v'],
                 "9" : ['w','x','y','z']}
        
        res = list()
        def dfs(s, idx, toAdd):
            if idx >= len(digits):
                s+=toAdd
                res.append(s)
                return 
            s+=toAdd
            for let in dtol[digits[idx]]:
                dfs(s,idx+1,let)


        dfs("", 0, "")
        return res 
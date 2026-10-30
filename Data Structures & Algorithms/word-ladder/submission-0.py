class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # IDEA: Treat as a graph problem performing BFS because it is shortest path problem. 

        # If the final word is not in the list, we cannot reach the word. So we return 0 
        if endWord not in wordList:
            return 0 
        
        # We need to create a an adj. list with the keys as word patterns of all the possible 1 letter off variations each word in the list  
        nei = defaultdict(list)
        # We need the beginning word in teh adjacency list so we append it onto the wordList which we are going to iterate over to make our list 
        wordList.append(beginWord)
        # Iterating through the list 
        for word in wordList:
            # Now for each letter in the word we are going to replace the jth index with an asterix and call it a pattern that we can create from this word. 
            for j in range(len(word)):
                # adding all the letters in word left of j adding the asteriks as j and adding the letters right of j 
                pattern = word[:j] + "*" + word[j+1:]
                # appending that word to this pattern so we have a list to see what words to explore.
                nei[pattern].append(word)
        # After this executes the adj. list has been created, and we now start out bfs 
        # We create a visit set with begin word already in it because we know that is where we are starting. 
        visit = set([beginWord])
        # Creating our q for dfs 
        q = deque([beginWord])
        # we start with the result as 1 because at a minimum we will have to make on transformation to reach the word.
        res = 1 
        while q:
            # We want to loop through each layer while the q is not empty 
            for i in range(len(q)):
                # Taking the word from the front of the queue 
                word = q.popleft()
                # if the word is the end word, that means the previous word was one letter off and found it from matching. So we just want to return the res. 
                if word == endWord:
                    return res 
                # Now we want to find all of the patterns this word belongs to and perform BFS on them if they have not already been visited.  
                for j in range(len(word)):
                    # Creating the same pattern we did for the keys of the adj. list 
                    pattern = word[:j]+"*" + word[j+1:]
                    # For each word in the list associated with this pattern we want to add that list to the queue and visiting set, if it has not already been visited. 
                    for neiWord in nei[pattern]:
                        # If they have not been seen we append and add
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            # When one full layer of BFS has been completed we can increment resulting counter by 1 
            res+=1 
        # If we went through the list and didn't find a way to reach the end word meaning the graph is unconnected, we have to return 0. 
        return 0 
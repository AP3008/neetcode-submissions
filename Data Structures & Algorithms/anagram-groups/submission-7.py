class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            sortedS = "".join(sorted(s)).lower()
            if sortedS not in anagrams:
                anagrams[sortedS] = [] 
            anagrams[sortedS].append(s)
        return [x for x in anagrams.values()]

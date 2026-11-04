class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for word in strs:
            s = "".join(sorted(word))
            seen[s].append(word)
            
        return list(seen.values())
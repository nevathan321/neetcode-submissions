class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for anagram in strs: 
            count = [0] * 26 
            for c in anagram:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(anagram)
        
        return list(res.values())

        

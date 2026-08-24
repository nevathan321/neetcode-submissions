from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        i = 0
        HashMap = {}
        EndResult = []

        for strings in strs:
            sortedkey = "".join(sorted(strings))
            if sortedkey in HashMap:
                EndResult[HashMap[sortedkey]].append(strings)
            else:
                HashMap[sortedkey] = i
                i += 1 
                EndResult.append([strings]) 
        
        return EndResult
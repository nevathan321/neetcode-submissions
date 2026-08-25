from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        EndResult = []
        HashMap = defaultdict(int)
        i = 0 

        for string in strs:

            StrHash = "".join(sorted(string))
            if  StrHash in HashMap:
                EndResult[HashMap[StrHash]].append(string)
            else:
                EndResult.append([string])
                HashMap[StrHash] = i
                i += 1
        return EndResult

        
        




        
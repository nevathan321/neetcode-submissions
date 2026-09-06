from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        EndResult = []
        Groupi = 0

        HashMap = {}

        for word in strs:
            Pointer = "".join(sorted(word))
            if Pointer in HashMap:
                index = HashMap[Pointer]
                EndResult[index].append(word) 

            else:
                EndResult.append([word])
                HashMap[Pointer] = Groupi
                Groupi += 1 
        
        return EndResult
        
        
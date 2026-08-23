from collections import defaultdict
from heapq import nlargest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 


        dicti = defaultdict(int)

        for num in nums:
            dicti[num] += 1

        # newlist = sorted(dicti.items(), key = lambda x: x[1])
    
        # return newlist[:k] 

        test = heapq.nlargest(k, dicti.items(), lambda x: x[1])
        return  [item[0] for item in test]
 
        
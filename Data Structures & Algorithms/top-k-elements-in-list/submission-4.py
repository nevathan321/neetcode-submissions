from collections import defaultdict
from heapq import nlargest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        HashMap = defaultdict(int)

        for num in nums:
            HashMap[num] += 1

        returner = heapq.nlargest(k, HashMap.items(), lambda x: x[1])


        return [item[0] for item in returner]


        
        
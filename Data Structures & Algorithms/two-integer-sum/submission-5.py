class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, num in enumerate(nums):
            Remaining = target - num
            if Remaining in seen:
                return[seen[Remaining], i]

            if num not in seen:
                seen[num] = i
            


        

 
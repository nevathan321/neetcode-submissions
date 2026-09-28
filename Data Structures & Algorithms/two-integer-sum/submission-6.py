class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        Hash = {}

        for i, num in enumerate(nums):
            need = target - num
            if need in Hash:
                return [Hash[need], i]
            else:
                Hash[num] = i
        
        
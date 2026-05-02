class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        Hash = {}

        for i, num in enumerate(nums): 
            diff = target - num 

            if diff in Hash: 
                return [Hash[diff], i]
            Hash[num] = i



'''
This is me retrying it to stick it in my head, Practice makes perfect 
''' 
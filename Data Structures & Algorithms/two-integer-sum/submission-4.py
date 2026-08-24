class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        endresult = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    endresult.append(i)
                    endresult.append(j)

        return endresult
        

        


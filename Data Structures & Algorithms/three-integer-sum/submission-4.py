class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        output = []
        nums.sort()  
        for i in range(len(nums)): 
            left = i + 1 
            right = len(nums) - 1 
            target = -nums[i]

            if i > 0 and nums[i] == nums[i - 1]: 
                continue

            while left < right: 
                if nums[left] + nums[right] < target: 
                    left += 1 

                elif nums[left] + nums[right] > target: 
                    right -= 1
                
                else:
                    output.append([nums[i], nums[left], nums[right]])
                    right -= 1 
                    left += 1 

                    while left < right and nums[left] == nums[left - 1]: 
                        left += 1 
                    
                    while left < right and nums[right] == nums[right + 1]: 
                        right -= 1 
        return output 





'''
-- retrying 3sum 
-- target is 0 
-- we can turn this into a 2 sum question by using the first number subtracted from 0 as the target 
-- avoiding duplicates is the tricky part of this question 
-- if we .sort(), and find every combination with the first element then we can move on to the next number make sure its not a duplicate number to avoid duplicates and then go on 
-- output = [] is what we will return  
'''












     
 
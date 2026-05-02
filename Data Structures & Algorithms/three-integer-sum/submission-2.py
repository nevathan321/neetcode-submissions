'''
        -- Related to 2SUM SOMEHOW
        -- we can take one number out the equation by using it in the target, like 0 - first number 
        -- the rest should act like 2SUm then 

'''


'''
        SO INEFFICENT EVEN NEETCODE DONT WANT TO PUSH IT TO MY GITHUB REPO :) 
        output = []
        duplicates = set()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                for k  in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        
                        triplet = tuple(sorted((nums[i], nums[j], nums[k])))

                        if triplet not in duplicates:
                            duplicates.add(triplet)
                            output.append([nums[i], nums[j], nums[k]])

        return output
'''



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        output = []
        nums.sort() # n log n 
        for i in range(len(nums)): 

            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            target = -nums[i] 
            left = i + 1 
            right = len(nums) - 1

            while left < right: 
                if nums[left] + nums[right] > target: 
                    right -= 1 
                
                elif nums[left] + nums[right] < target: 
                    left += 1 

                else: 
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1 
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]: 
                        right -= 1

        return output

                

            














     
 
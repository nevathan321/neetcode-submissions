class Solution:
    def maxArea(self, heights: List[int]) -> int:

        '''
        -- now lets optmize this 
        -- we are trying to find the max area 
        -- area = width * best height
        -- two pointer approach to find a bigger height 
        -- 

        '''
                
        left = 0
        right = len(heights) - 1 
        currmax = 0
        while left < right:


            area = min(heights[left], heights[right]) * (right - left)
            currmax = max(currmax, area) 

            if heights[left] > heights[right]: 
                right -= 1 
               
            else: 
                left += 1 
            
            
        return currmax


        
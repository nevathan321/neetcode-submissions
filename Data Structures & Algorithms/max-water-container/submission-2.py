class Solution:
    def maxArea(self, heights: List[int]) -> int:

        '''
        -- redoing maxArea
        -- we want to try every possible pair without going to O(n^2) which is a double for loop 
        -- 
        '''

        left = 0 
        right = len(heights) - 1 
        Tmax = 0
        while left < right: 
            height = min(heights[left], heights[right])
            distance = right - left
            currmax = height * distance
            if Tmax < currmax: 
                Tmax = currmax

            if heights[left] < heights[right]: 
                left += 1 
            else: 
                right -= 1
            
        return Tmax
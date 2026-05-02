class Solution:
    def maxArea(self, heights: List[int]) -> int:




        biggest = 0 
        for i in range(len(heights)): 
            for j in range(i + 1, len(heights)): 
                if heights[i] > heights[j]: 
                    curr = j
                else:
                    curr = i

                distance = j - i

                newbiggest = heights[curr] * distance

                if newbiggest > biggest: 
                    biggest = newbiggest
        return biggest
                
                


        
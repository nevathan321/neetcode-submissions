class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        seen = []

        for i, num in enumerate(numbers): 
            for j, s in enumerate(seen): 
                if s + num == target: 
                    return [j + 1, i + 1]
            seen.append(num)


            
            
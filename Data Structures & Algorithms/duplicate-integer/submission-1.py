class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        -- we have a list 
        -- > 1 return true -- Any value 
        -- otherwise return false 
        '''

        checker = []

        for num in nums: 
            if num in checker: 
                return True
            checker.append(num)
        return False
        
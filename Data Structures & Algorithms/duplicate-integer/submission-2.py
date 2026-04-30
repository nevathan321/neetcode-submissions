class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        -- we have a list 
        -- > 1 return true -- Any value 
        -- otherwise return false 
        '''

        checker = set()

        for num in nums: 
            if num in checker: 
                return True
            checker.add(num)
        return False
        

        ''' 
        -- maybe look for a hashmap solution O(1)
        -- would this make the solution faster?

        '''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        EndResult = [0] * len(temperatures)
        MStack = []

        for i in range(len(temperatures) - 1, -1, -1):
            
            while MStack and temperatures[i] >= temperatures[MStack[-1]]:
                MStack.pop()
            
            if MStack and temperatures[i] < temperatures[MStack[-1]]:
                EndResult[i] = MStack[- 1] - i
                
            MStack.append(i) 

        
        return EndResult

        
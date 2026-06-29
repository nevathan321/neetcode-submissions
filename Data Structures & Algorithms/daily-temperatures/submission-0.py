class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = []

        for j in range(len(temperatures)):
            found = False

            # Only check future days
            for i in range(j + 1, len(temperatures)):
                if temperatures[i] > temperatures[j]:
                    result.append(i - j)  # number of days waited
                    found = True
                    break  # stop at FIRST warmer day

            if not found:
                result.append(0)

        return result
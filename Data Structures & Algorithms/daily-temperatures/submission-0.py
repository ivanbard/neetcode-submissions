class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        # start @ day, look forward at the days after it,
        # push days to stack until future day's temp exceeds current
        # count num of days in the stack, and set result[i] to that num, unless no warmer days
        for i in range(len(temperatures)):
            stack = []
            # check if next warmest day was found, in case there are multiple warmer in future than current day
            warmest = 0
            j = i+1
        
            while j < len(temperatures) and warmest == 0:
                if temperatures[j] > temperatures[i]:
                    stack.append(temperatures[j])
                    result[i] = len(stack)
                    warmest = 1
                else:
                    stack.append(temperatures[j])
                    j += 1

        return result
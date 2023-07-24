# The insight here is that a stack can be a useful tool if you can craft it such that you get a
# guarantee about the relationship of elements to each other
# if you only put in elements > top or elements < top, you have a guarantee
# it can be used to solve problems where an element can be removed from consideration once it satisfies a condition
class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        """
        Memory: O(n)
        Runtime: O(n)
        """
        # return array, initialized to 0 for no hotter day
        answer: list[int] = [0] * len(temps)
        # array of (temperature, day) containing days that haven't yet found a hotter day
        # critical insight: stack[i] >= stack[j] if i < j
        stack: list[tuple(int, int)] = [] 
        
        for i, temp in enumerate(temps):
            # pop elements from the stack until empty or stack top >= temp
            while stack and temp > stack[-1][0]:
                _, prev_day = stack.pop()
                answer[prev_day] = i - prev_day
            
            # put new temp onto stack with current day
            stack.append((temp, i))
        
        return answer

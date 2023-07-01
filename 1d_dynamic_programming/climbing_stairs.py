# could be a more elegant explanation
class Solution:
    def climbStairs(self, n: int) -> int:
        # This dict stores # of steps to # of steps it takes to climb a staircase of that many steps
        memo: dict[int, int] = {1: 1, 2: 2, 0: 0}
        current_steps: int = 2
        
        # iterate through each 
        while current_steps < n:
            # calculate how many ways to get up a current_steps + 1 staircase
            current_steps += 1

            one_step_ways = memo[current_steps - 1]
            two_steps_ways = memo[current_steps - 2]
            total_ways = one_step_ways + two_steps_ways

            # save it to the memo to use to calculate later steps
            memo[current_steps] = total_ways
        
        return memo[n]
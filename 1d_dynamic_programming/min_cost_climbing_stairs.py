class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Memory: O(n)
        Runtime: O(n)
        """
        min_costs: list[int] = [9999] * len(cost)
        min_costs[-1] = cost[-1]
        min_costs[-2] = cost[-2]
        for current in range(len(cost) - 3, -1, -1):
            min_cost = min(min_costs[current + 1], min_costs[current + 2]) + cost[current]
            min_costs[current] = min_cost
        return min(min_costs[0], min_costs[1])
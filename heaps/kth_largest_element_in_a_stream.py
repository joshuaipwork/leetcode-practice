# The key insight here is that you can create a heap from a subset of the
# data in a stream and use that to solve problems.
# Other insights:
#   1. Always read the question.
#   2. heapify doesn't return the heapified list!!!!!!
#   3. Use heap[0] to access the smallest item in a heap, but it is not guaranteed that
#       heap[n] is the nth smallest item in a heap.

import heapq 

class KthLargest:
    """
    Memory: O(k) since we get to use nums inplace
        would be O(n) otherwise to create a copy of the list
    Runtime: O(n log n)
    """
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)
        self.k = k

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        """
        Memory: O(1)
        Runtime: O(log n)

        Adds an element from the stream of data, then returns the kth largest item.

        Args:
            val (int): The element to add to the stream
        Returns:
            (int): The kth largest element in the stream.
        """
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
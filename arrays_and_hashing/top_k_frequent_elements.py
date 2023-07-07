# counts.items(), not counts.entries()
# defaultdict needs a callable or None. If passed int, default is 0. If passed list, default is []
# if passed dict, default is {}, if passed set, default is {}

#
class Solution:
    def topKFrequentHeaps(self, nums: List[int], k: int) -> List[int]:
        """
        Memory: O(n)
        Runtime: O(n + k log n)
        """
        # define data structures
        counts: dict[int, int] = collections.defaultdict(int)
        
        # for each num in nums
        for num in nums:
            counts[num] += 1
        
        # convert occurrences dict to heap
        counts_list = [(-value, key) for key, value in counts.items()]
        heapq.heapify(counts_list) # O(n)

        # pop the top k elements from the heap
        ret = []
        for i in range(0, k):
            num = heapq.heappop(counts_list)[1]
            ret.append(num)
        
        return ret
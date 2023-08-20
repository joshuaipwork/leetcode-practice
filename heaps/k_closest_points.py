class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # define data structures
        heap = []

        # insert distances into the heap
        for point in points:
            heap.append(
                (
                    (point[0] ** 2 + point[1] ** 2) ** 0.5,
                    point[0],
                    point[1]
                )
            )
        
        heapq.heapify(heap)

        result = []
        for i in range(0,k):
            point = heapq.heappop(heap)
            result.append([point[1], point[2]])
        
        return result
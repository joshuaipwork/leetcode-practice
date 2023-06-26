class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # init variables
        min_k = 1
        max_k = max(piles)
        best_k = max_k

        # while we haven't checked the whole range
        while min_k <= max_k:
            # find the midpoint
            mid_k = (min_k + max_k) // 2
            h_mid_k = 0

            # check how many hours it would take to eat all bananas at current k
            for pile in piles:
                h_mid_k += math.ceil(pile / mid_k)
            
            # if it's too many hours, remove all k values <= mid_k from the range
            if h_mid_k > h:
                min_k = mid_k + 1
            else:
                # store this as a solution
                best_k = min(best_k, mid_k)
                # remove this value of k and all larger values of k from the search range
                max_k = mid_k - 1
            
        return best_k
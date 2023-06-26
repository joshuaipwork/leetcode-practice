# Insights:
#
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Memory: O(1)
        Runtime: O(log n + log m)
        """
        # binary search the column
        top = len(matrix) - 1
        bottom = 0

        while top >= bottom:
            mid = (top + bottom) // 2
            # if the first element in the row is greater than the target, all elements in the row are greater than the target
            if matrix[mid][0] > target:
                # shift indices to remove this row and all rows with greater values 
                top = mid - 1
            # if the last element in the row is less than the target, all elements in the row are less than the target
            elif matrix[mid][-1] < target:
                # shift indices to remove this row and all rows with smaller values
                bottom = mid + 1
            else:
                # we found a row that may contain the target
                break
        
        # check to see if we searched and never found a row that may contain the target
        if top < bottom:
            return False

        # binary search the row that may contain the target
        row = (top + bottom) // 2
        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                return True
        
        return False
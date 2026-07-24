class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first int of each row is larger than last int of prev row
        low = 0
        high = len(matrix) - 1

        # find which row to go into, then look through row
        while low <= high:
            # row search
            mid = low + (high-low) // 2#@

            if matrix[mid][0] == target:
                return True
                break
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid-1

        if high < 0:
            return False

        # second binary search for target in col
        row = matrix[high]
        low = 0
        high = len(row) - 1

        while low <= high:
            # column search
            mid = low + (high - low) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
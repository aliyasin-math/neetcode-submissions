class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        u, d = 0, len(matrix)-1
        l, r = 0, len(matrix[0])-1
        
        while u<d:
            mid = (u+d) // 2
            if matrix[mid][-1] < target:
                u = mid + 1
            elif matrix[mid][-1] > target:
                d = mid
            elif matrix[mid][-1] == target:
                return True
            

        while l<=r:
            mid = (l+r) // 2
            if matrix[u][mid] < target:
                l = mid + 1
            elif matrix[u][mid] > target:
                r = mid - 1
            else:
                return True
        return False
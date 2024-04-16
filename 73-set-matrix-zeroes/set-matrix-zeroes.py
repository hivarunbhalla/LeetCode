class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row_arr = set()
        col_arr = set()
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    row_arr.add(row)
                    col_arr.add(col)

        mark = [0] * n
        for row in row_arr:
            matrix[row] = mark

        for row in range(m):
            for col in col_arr:
                matrix[row][col] = 0


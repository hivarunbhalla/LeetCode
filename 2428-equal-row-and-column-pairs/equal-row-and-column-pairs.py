class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        transpose = [[0] * len(grid) for _ in range(len(grid[0]))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                transpose[j][i] = grid[i][j]


        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i] == transpose[j] :
                    ans += 1

        return ans
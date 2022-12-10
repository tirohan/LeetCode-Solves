class Solution:
    def num_of_Islands(self, grid):
        if len(grid) == 0:
            return 0
        RowB, ColumnB = [1, -1, 0, 0], [0, 0, -1, 1]
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            grid[r][c] = '2' # visited island will be denoted as 2
            for i in range(4):
                nr, nc = r + RowB[i], c + ColumnB[i]
                if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == '1':
                    dfs(nr, nc)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans

if __name__ == '__main__':
    Islands1 = Solution().num_of_Islands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
    Islands2 = Solution().num_of_Islands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
    print("output of Number of Islands for Islands1 : ", Islands1)
    print("output of Number of Islands for Islands2 : ", Islands2)
class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
     if not grid:
            return 0
        
    rows, cols = len(grid), len(grid[0])
        
def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W':
                return
            grid[r][c] = 'W'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        total_isles = 0
        
for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L':
                    total_isles += 1
                    dfs(i, j)
        
return total_isles

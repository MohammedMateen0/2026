from collections import deque
class Solution:
    def num_islands(self,grid):
        if not grid:
            return 0
        rows=len(grid)
        cols=len(grid[0])
        island_count=0
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>= cols:
                return
            if grid[r][c]==0:
                return
            grid[r][c]='0'
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    island_count+=1
                    dfs(r,c)
        return island_count
    def num_island(self,grid):
        if not grid:
            return 0
        rows=len(grid)
        cols=len(grid[0])
        island=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    island+=1
                    queue=deque([(r,c)])
                    grid[r][c]='0'
                    while queue:
                        row,col=queue.popleft()
                        direction=[(1,0),(-1,0),(0,1),(0,-1)]
                        for dr,dc in direction:
                            nr=row+dr
                            nc=col+dc
                            if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=='1':
                                queue.append((nr,nc))
                                grid[nr][nc]='0'
        return island
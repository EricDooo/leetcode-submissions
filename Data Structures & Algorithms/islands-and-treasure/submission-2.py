class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Multi source BFS from treasures
        q = deque()
        visit = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        
        def addCell(r,c):
            if (min(r,c) < 0 or
                r == ROWS or c == COLS
                or grid[r][c] == -1 # No Walls
                or (r,c) in visit # No duplicates
            ):
                return
            visit.add((r,c))
            q.append([r,c])

        depth = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = depth
                for dr, dc in directions:
                    addCell(r+dr, c+dc)
            depth += 1
        



        
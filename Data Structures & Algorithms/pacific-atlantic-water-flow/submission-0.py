class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(heights), len(heights[0])

        # Pacific -> row 0 col 0
        # Atlantic -> row len(heights) col len(heights[0]) - 1
        # dfs each from the borders, reversed order

        def dfs(r,c,visit,prevHeight):
            if ((r,c) in visit or 
                r < 0 or 
                c < 0 or 
                r == ROWS or 
                c == COLS or 
                heights[r][c] < prevHeight): # We want to find only greater heights
                return
            visit.add((r,c))
            for dr,dc in directions:
                dfs(r+dr, c+dc, visit, heights[r][c])

        pacific, atlantic = set(), set()
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res

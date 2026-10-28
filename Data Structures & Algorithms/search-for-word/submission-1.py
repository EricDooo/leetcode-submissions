class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS # Bounds
                or board[r][c] != word[i]): # Current word doesnt match
                return False

            temp = board[r][c] 
            board[r][c] = "#" # Take this element out

            res = False 
            for dr, dc in directions: # Explore all 4 directions
                if dfs(r + dr, c + dc, i + 1):
                    res = True
                    break

            board[r][c] = temp # Backtrack
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False
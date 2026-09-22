class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r, row in enumerate(board):
            for c, element in enumerate(row):
                if element == '.':
                    continue
                mask = 1<<(int(element) - 1)
                if (mask) & rows[r]:
                    return False
                if (mask) & cols[c]:
                    return False
                if (mask) & squares[(r // 3) * 3 + (c // 3)]:
                    return False
                
                rows[r] |= mask
                cols[c] |= mask
                squares[(r // 3) * 3 + (c // 3)] |= mask
        return True

                
                
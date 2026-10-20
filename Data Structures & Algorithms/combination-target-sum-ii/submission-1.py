class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, path = [], []

        def dfs(i, total):
            if target == total:
                res.append(path.copy())
                return
            # When i reaches end of iteration
            if total > target or i == len(candidates):
                return

            path.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            path.pop()

            # Make sure [1, 1, 2] doesnt choose [1,2] twice
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total)

        dfs(0, 0)

        return res

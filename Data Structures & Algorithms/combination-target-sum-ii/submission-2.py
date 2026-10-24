class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(ind, path, total):
            if total == target:
                res.append(path.copy())
                return

            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i - 1]: # if duplicate
                    continue
                
                if total + candidates[i] > target: # next total is over
                    break
                
                path.append(candidates[i])
                dfs(i + 1, path, total + candidates[i])
                path.pop()
        
        dfs(0, [], 0)
        return res

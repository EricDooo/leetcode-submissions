class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res

    def backtrack(self, perm: List[int], nums: List[int], pick: List[bool]):
        if len(perm) == len(nums): # Save if full permutation length
            self.res.append(perm.copy())
            return
        for i in range(len(nums)):
            if not pick[i]: # Pick number that hasnt been used yet
                perm.append(nums[i]) # Add to current permutation
                pick[i] = True 
                self.backtrack(perm, nums, pick) # recursively build
                perm.pop()
                pick[i] = False # Backtrack/undo and try a different number
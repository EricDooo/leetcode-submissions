class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]: # Left side is in order
            # target < nums[l] means target has section in the rotated
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else: # pivot is in the left half
                if target < nums[mid] or target > nums[r]:
                    # target is left side in order or left side pivoted
                    r = mid - 1
                else:
                    l = mid + 1

        
        return -1
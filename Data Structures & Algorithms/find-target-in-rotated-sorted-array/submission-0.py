class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0 , len(nums) - 1

        # to find which half contains target off pivot:
        # [3, 4, 5, 6, 1, 2]
        # l <= mid then this means left split is correctly sorted
        # target > nums[mid] or target < nums[l] -> 
        # can be greater or smaller than what we have so its in the right split
        # Otherwise its in the left section and we keep searching

        # Right split target < nums[mid] or target > nums[r]
        # These two are the key checks after we established which split it is, we still dont know if
        # it has split cleanly so target > nums[r] and target < nums[l] check if our target could possibly
        # be in which nested split in that region
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

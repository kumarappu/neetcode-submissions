class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        l = 0
        r = length-1

        while l < r-1:
            m = int((l + r) / 2)
            if target < nums[m]:
                r = m -1
            elif target > nums[m]:
                l = m +1
            else:
                return m
        
        if target == nums[l]:
            return l
        elif target  == nums[r]:
            return r
        else:
            return -1


        
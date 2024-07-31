class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0
        elif nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums)-1


        l, h = 0, len(nums) -1
        while l <= h:
            m = (l+h)//2

            if nums [m-1] < nums[m] and nums[m] > nums[m+1]:
                return m

            elif nums[m] < nums[m+1] : #right side increasing
                l = m+1
            
            else:
                h = m-1

        return -1

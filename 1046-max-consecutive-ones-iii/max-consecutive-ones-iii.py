class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left = right = 0
        ans = zero = 0
        n = len(nums)
        while (right < n ):

            if nums[right] == 0: 
                zero += 1

            if zero > k: 
                if nums[left] == 0: 
                    zero -= 1
                left += 1

            if zero <= k:
                ans = max(ans, right-left+1)

            right += 1

        return ans
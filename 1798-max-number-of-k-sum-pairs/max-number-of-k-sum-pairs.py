class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, right = 0, len(nums) -1 
        if len(nums) == 1 and nums[0] == k: return 1
        opr = 0
        while i < right:
            if nums[i] + nums[right] == k:
                opr += 1
                i+=1
                right -=1

            elif nums[i] + nums[right] < k:
                i += 1
            
            else: 
                right -= 1

        return opr


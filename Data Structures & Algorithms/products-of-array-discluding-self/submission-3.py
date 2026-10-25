class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n 
        # 1. Left Pass: Har element ke left side ka product calculate karna
        left_prod = 1
        for i in range(n):
            output[i] = left_prod
            left_prod *= nums[i]
        
        # 2. Right Pass: Right side ka product multiply karna
        right_prod = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_prod
            right_prod *= nums[i]
        
        return output
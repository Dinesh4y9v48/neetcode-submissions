class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # bruteforce approach but complexity is o(n2)and space complexity = o(1)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        # return False

# optimized code.
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False 


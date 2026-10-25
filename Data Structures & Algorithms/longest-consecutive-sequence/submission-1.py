class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
                # time complexity is o (nlogn)
        # seen = set()

        # for num in nums:
        #     seen.add(num)

        # sorted_num = sorted(seen)

        # if not sorted_num:
        #     return 0

        # count = 1
        # longest = 1

        # for i in range(1, len(sorted_num)):
        #     if sorted_num[i] - sorted_num[i - 1] == 1:
        #         count += 1
        #         longest +=1
        #     else:
        #         count = 1
        #         logest= 1
        # return longest

                    #optimized complexity o(n)

        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                count = 1
                current = num

                while current + 1 in num_set:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest

class Solution:
    def topKFrequent(self, nums, k):
        freq = {}

        # Step 1: Count frequency
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Step 2: Sort numbers by frequency
        sorted_nums = sorted(
            freq, key=freq.get, reverse=True
        )

        # Step 3: Return top k elements
        return sorted_nums[:k]
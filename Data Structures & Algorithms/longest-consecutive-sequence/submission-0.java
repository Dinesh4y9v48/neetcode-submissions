class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num); // duplicates (like the second 4) are ignored
        }

        int best = 0;
        for (int num : set) {
            if (!set.contains(num - 1)) {  // num is the start of a sequence
                int cur = num;
                int len = 1;
                while (set.contains(cur + 1)) {
                    cur++;
                    len++;
                }
                best = Math.max(best, len);
            }
        }
        return best;
    }
}
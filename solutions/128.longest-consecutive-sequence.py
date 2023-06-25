#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
from typing import List

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in num_set:
                length = 0
                while (num + length) in num_set:
                    length += 1
                longest = max(longest, length)

        return longest
        
# @lc code=end


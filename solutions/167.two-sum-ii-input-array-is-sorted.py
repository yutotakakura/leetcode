#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        My first answer
        It's a small chacnge of 1.two-sum.py
        """
        cache = {}
        for i, num in enumerate(numbers):
            val = target - num
            if val in cache:
                return [cache[val]+1, i+1]
            cache[num] = i
        
# @lc code=end


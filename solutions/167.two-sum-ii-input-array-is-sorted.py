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

        23/23 cases passed (138 ms)
        Your runtime beats 71.68 % of python3 submissions
        Your memory usage beats 95.11 % of python3 submissions (17.2 MB)

        cache = {}
        for i, num in enumerate(numbers):
            val = target - num
            if val in cache:
                return [cache[val]+1, i+1]
            cache[num] = i
        """

        """
        23/23 cases passed (147 ms)
        Your runtime beats 27.99 % of python3 submissions
        Your memory usage beats 19.35 % of python3 submissions (17.4 MB)
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if target < total:
                r -= 1
            elif target > total:
                l += 1
            else:
                return [l + 1, r + 1]

        
# @lc code=end


#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        My first answer.

        This doesn't pass pattern of nums=[3,3] and target=6.
        Useing set isn't appropriate. Should use dict to have index and num of nums.

        cache = set()
        for num in nums:
            val = target - num
            if val in cache:
                return [nums.index(val), nums.index(num)]
            cache.add(num)
        """

        cache = {}
        for i, num in enumerate(nums):
            val = target - num
            if val in cache:
                return [cache[val], i]
            cache[num] = i
# @lc code=end


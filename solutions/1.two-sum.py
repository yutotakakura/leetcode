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

        """
        Practice of Hash Table

        Operation
        Average Time Complexity

        Search
        O(1)

        Insert
        O(1)

        Remove
        O(1)
        """

        # Initialize an empty dictionary and assign it to the variable 'cache'
        cache = {}
        # Start a for loop iterate 'num' over each 'num' in the variable 'nums'
        for index, num in enumerate(nums):
            # If (target - num) is seen in cache
            if (target - num) in cache:
                # We can return index of target - num and index of num
                return [cache[target - num], index]
            # Add the key-value pair "num"-"index" to the variable 'cache'
            cache[num] = index
# @lc code=end


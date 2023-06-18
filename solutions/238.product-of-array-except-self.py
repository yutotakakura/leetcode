#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        nums    = [1, 2, 3, 4]
        prefix  = [1, 2, 6, 24]
        postfix = [24, 24, 12, 4]
        output  = [24, 12, 8, 6]

        output[i] = prefix[i-1] * postfix[i+1]
        If None value, defalut 1
        """
        
        answer = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer
# @lc code=end


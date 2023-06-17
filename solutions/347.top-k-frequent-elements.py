#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from typing import List
from collections import Counter
import heapq

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        My answer using heapq
        O(n)
        """
        count_num = Counter(nums)
        data = [(-count_num[num], num) for num in count_num]
        heapq.heapify(data)
        return [heapq.heappop(data)[1] for _ in range(k)]

        """
        Other answer
        O(n)
        """
        """
        count = {}

        # Index is count of nums, so range is len(nums) + 1
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        """
        
# @lc code=end


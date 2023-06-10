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
        count_num = Counter(nums)
        data = [(-count_num[num], num) for num in count_num]
        heapq.heapify(data)
        return [heapq.heappop(data)[1] for _ in range(k)]
        
# @lc code=end


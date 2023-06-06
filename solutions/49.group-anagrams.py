#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from typing import List
from collections import defaultdict


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        answer = defaultdict(list)

        for str in strs:
            count = [0] * 26
            for char in str:
                count[ord(char) - ord('a')] += 1
            # Convert type of answer list to tuple because dict can't have list as key.
            answer[tuple(count)].append(str)

        return answer.values()
# @lc code=end


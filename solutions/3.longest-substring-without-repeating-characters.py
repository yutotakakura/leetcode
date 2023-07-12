#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """
        Practice of Array
        
        Array 

        Operation
        Average Time Complexity

        Search
        O(n)

        Search (sorted array)
        O(log(n))

        Insert
        O(n)

        Insert (at the end)
        O(1)

        Remove
        O(n)

        Remove (at the end)
        O(1)
        """

        """
        s[r] not in seen
        Not in current window (In this case, c is not in current window)
        index  0 1 2 3 4 5 6 7
        s      a b c a b c b b
               |   | 
               l   r
        seen = {a: 0, b: 1}


        s[r] in seen
        # case 1
        s[r] is not inside of the window, we can keep increase the window
        index  0 1 2 3 4 5 6 7
        s      a b c a b c b b
                       | | 
                       l r
        seen = {a: 3, b: 4, c: 2}
        seen[s[r]] = 2

        # case 2
        s[r] is inside of the window, we need to change the window by moving left pointer to seen[s[r]] + 1
        index  0 1 2 3 4 5 6 7
        s      a b c a b c b b
               |     | 
               l     r
        seen = {a: 0, b: 1, c: 2}
        r = 3
        s[r] = a
        seen[s[r]] = 0

        index  0 1 2 3 4 5 6 7
        s      a b c a b c b b
                     | |
                     r l
        """

        # Assign the dictionary to the variable 'seen'
        seen = {}
        l = 0
        output = 0

        # Start a for loop, iterate 'r' over the range of length of s
        for r in range(len(s)):
            if s[r] not in seen:
                # If the condition is true, update 'output'
                # r-l+1 equals the length of current window 
                output = max(output, r-l+1)
            else:
                if seen[s[r]] < l:
                    # case2
                    output = max(output, r-l+1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output

# @lc code=end


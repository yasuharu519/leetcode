#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return '0'
        elif x > 0:
            return ''.join(list(reversed(str(x).rstrip('0'))))
        else:
            return '-' + ''.join(list(reversed(str(abs(x)).rstrip('0'))))
        
# @lc code=end


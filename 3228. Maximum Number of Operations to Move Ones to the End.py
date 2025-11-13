class Solution(object):
    def maxOperations(self, s):
        result = curr = 0
        for i in range(len(s)):
            if s[i] == '1':
                curr += 1
            elif i+1 == len(s) or s[i+1] == '1':
                result += curr
        return result

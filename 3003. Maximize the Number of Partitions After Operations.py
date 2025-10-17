class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        
        def helper(i, mask, changed):
            if i == n:
                return 1
            
            if (i, mask, changed) in memo:
                return memo[(i, mask, changed)]
            
            char_bit = 1 << (ord(s[i]) - ord('a'))
            new_mask = mask | char_bit
            distinct = bin(new_mask).count('1')
            
            if distinct <= k:
                res = helper(i + 1, new_mask, changed)
            else:
                res = 1 + helper(i + 1, char_bit, changed)
            
            if not changed:
                for c in range(26):
                    if c == ord(s[i]) - ord('a'):
                        continue
                    char_bit_new = 1 << c
                    new_mask_changed = mask | char_bit_new
                    distinct_changed = bin(new_mask_changed).count('1')
                    
                    if distinct_changed <= k:
                        res = max(res, helper(i + 1, new_mask_changed, True))
                    else:
                        res = max(res, 1 + helper(i + 1, char_bit_new, True))
            
            memo[(i, mask, changed)] = res
            return res
        
        memo = {}
        return helper(0, 0, False)

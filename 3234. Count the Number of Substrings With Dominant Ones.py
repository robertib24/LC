class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        max_zeros = int(n ** 0.5) + 1
        
        for num_zeros in range(max_zeros + 1):
            min_ones = num_zeros * num_zeros
            
            zeros = 0
            ones = 0
            left = 0
            last_invalid = -1
            
            for right in range(n):
                if s[right] == '0':
                    zeros += 1
                else:
                    ones += 1
                
                while left < right:
                    if s[left] == '0' and zeros > num_zeros:
                        zeros -= 1
                        last_invalid = left
                        left += 1
                    elif s[left] == '1' and ones - 1 >= min_ones:
                        ones -= 1
                        left += 1
                    else:
                        break
                
                if zeros == num_zeros and ones >= min_ones:
                    ans += left - last_invalid
        
        return ans
        
        return ans

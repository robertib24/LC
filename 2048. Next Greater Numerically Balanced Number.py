class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(num):
            s = str(num)
            digit_count = {}
            
            for digit in s:
                digit_count[digit] = digit_count.get(digit, 0) + 1
            
            for digit, count in digit_count.items():
                if int(digit) != count:
                    return False
            
            return True
        
        candidate = n + 1
        while True:
            if is_balanced(candidate):
                return candidate
            candidate += 1
            
            if candidate > 10**7:
                break
        
        return -1

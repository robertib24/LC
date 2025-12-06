class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        dp = [0] * (n + 1)
        prefix = [0] * (n + 2)
        dp[0] = 1
        prefix[1] = 1
        
        min_deque = deque()
        max_deque = deque()
        left = 0
        
        for right in range(n):
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            while nums[max_deque[0]] - nums[min_deque[0]] > k:
                if min_deque[0] == left:
                    min_deque.popleft()
                if max_deque[0] == left:
                    max_deque.popleft()
                left += 1
            
            dp[right + 1] = (prefix[right + 1] - prefix[left] + MOD) % MOD
            prefix[right + 2] = (prefix[right + 1] + dp[right + 1]) % MOD
        
        return dp[n]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        left, right = 0, 1
        ans = 0

        while right < len(prices):
            ans = max(ans, prices[right] - prices[left])

            if prices[left] > prices[right]:
                left = right
            
            right += 1
        
        return ans
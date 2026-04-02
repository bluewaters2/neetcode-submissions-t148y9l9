class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_found = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < min_found:
                min_found = prices[i]
            
            ans = max(ans, prices[i] - min_found)
        
        return ans
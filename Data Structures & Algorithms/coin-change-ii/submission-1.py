class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins)-1, -1, -1):
            nextdp = [0] * (amount + 1)
            nextdp[0] = 1

            for amt in range(1, amount+1):
                nextdp[amt] = dp[amt]
                if amt - coins[i] >= 0:
                    nextdp[amt] += nextdp[amt-coins[i]]
            
            dp = nextdp
        
        return dp[amount]
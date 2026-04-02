# we have to find the fewest no.of coins to make up the exact target amount
# we create a dp and then we iterate through the coins to find all combs
# greedy cannot be used here because of the example coins = [1,3,4] amount = 6
# TC: O(n*c) where n = amount and c = len(coins)
# SC: O(n)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        
        return dp[-1] if dp[-1] != amount + 1 else -1
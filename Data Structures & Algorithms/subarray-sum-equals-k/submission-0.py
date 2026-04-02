class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0: 1}

        presum, cnt = 0, 0

        for num in nums:
            presum += num
            if presum - k in mp:
                cnt += mp[presum - k]
            mp[presum] = mp.get(presum, 0) + 1
        
        return cnt

# we can use a counting array to keep track of the nums

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums)

        buckets = [[] for _ in range(len(nums)+1)]
        for i, num in mp.items():
            buckets[num].append(i)
        
        ans, i = [], len(nums)

        while k > 0 and i >= 0:
            curr = 0
            if len(buckets[i]) > 0:
                if len(buckets[i]) - k <= 0:
                    ans.extend(buckets[i])
                    curr = len(buckets[i])
                else:
                    for j in range(k):
                        ans.append(buckets[i][j])
                    return ans
        
            k -= curr
            i -= 1

        return ans
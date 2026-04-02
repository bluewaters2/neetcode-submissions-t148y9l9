# there can be atmost 2 elements with cnt > n/3
# keep two candidates (a, b) and track their counts
# when we see a number, if it matches a, increment cnt_a
# else if it matches b, increment cnt_b
# else if cnt_a is 0 set a to num and cnt_a to a
# else if cnt_b is 0 set b to num and cnt_b to b
# else decrement both counts
# decrement to voting out the candidate

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_a, num_b = 0, 0
        cnt_a, cnt_b = 0, 0
        for num in nums:
            if num_a == num:
                cnt_a += 1
            elif num_b == num:
                cnt_b += 1
            elif cnt_a == 0:
                cnt_a += 1
                num_a = num
            elif cnt_b == 0:
                cnt_b += 1
                num_b = num
            else:
                cnt_a -= 1
                cnt_b -= 1
        
        cnt_a = cnt_b = 0
        for num in nums:
            if num == num_a:
                cnt_a += 1
            elif num == num_b:
                cnt_b += 1
        
        res = []
        if cnt_a > n // 3:
            res.append(num_a)
        if cnt_b > n // 3:
            res.append(num_b)
        
        return res
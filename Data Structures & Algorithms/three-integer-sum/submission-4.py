# we can use 3 for loops to solve this problem but TC - O(n^3)
# reduce TC by sorting and then use left and right pointers to find the pairs - TC: O(n^2)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        nums.sort()
        ans = set()
        i = 0

        while i < l:
            if nums[i] > 0:
                break
            left, right = i+1, l-1
            while left < right:
                if nums[left] + nums[right] + nums[i] == 0:
                    ans.add((nums[left], nums[right], nums[i]))
                    left += 1

                elif nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                
                else:
                    left += 1
                

            i += 1
            while i < len(nums) and nums[i-1] == nums[i]:
                i += 1
        
        return list(ans)

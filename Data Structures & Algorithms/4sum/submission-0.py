# sort the array, initialize 2 for loops to get the i and j indexes
# 2 pointers to get the 3rd and 4th nums
# if sum is equal to target, we sort the 4 nums and put it in a set
# this will help avoid dups

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        nums.sort()

        i = 0
        while i < len(nums)-1:
            for j in range(i+1, len(nums)):
                left, right = j + 1, len(nums)-1
                while left < right:
                    currsum = nums[left] + nums[i] + nums[j] + nums[right]
                    if currsum == target:
                        curr = [nums[left], nums[i], nums[j], nums[right]]
                        curr.sort()
                        ans.add(tuple(curr))
                        left += 1
                        right -= 1
                    
                    elif currsum > target:
                        right -= 1
                    
                    else:
                        left += 1
                
                while i + 1 < len(nums) and nums[i] == nums[i+1]:
                    i += 1
            i += 1
        
        return list(ans)
                

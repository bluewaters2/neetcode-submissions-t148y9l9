# sol_1: we can sort the array and then duplicate elements will be next to each other TC: O(nlogn), SC:O(1)
# sol_2: we can use binary search on range [1, n] assign a mid, if there are no duplicates in [1, mid] then the number of 
# elements in that range will be mid then the duplicate element should be in tha half [mid+1, right] TC: O(nlogn) SC:O(1)
# sol_3: we can use a hashset to keep track of each element in nums and return the duplicate TC: O(n), SC: O(n)
# sol_4: create a bool array of n ints, keep track of the element visited, return duplicate TC: O(n), SC: O(n)
# sol_5: we can flyod's slow and fast pointer, we start from 0, then move the fast pointer 2 places and slow pointer by 1, 
# we move to the next index based on the current index value, both pointers will meet in the cycle, 
# then we create a new pointer at head move one step at a time and the fast pointer move 1 step, 
# the meet point bet the 2 is the start of the cycle TC: O(n), SC:(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if slow == fast:
                break
        
        new_pointer = 0
        while new_pointer != fast:
            fast = nums[fast]
            new_pointer = nums[new_pointer]
        
        return fast
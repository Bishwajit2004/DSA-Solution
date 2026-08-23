class Solution:
    def findDuplicate(self, nums):
        slow = 0
        fast = 0

        # Phase 1: find a meeting point in the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2: find the cycle entrance
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
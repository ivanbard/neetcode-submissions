class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # assume 1-indexed array
        # index 1 = 1, index 72 = 72, etc.
        # if number is not equal to index + 1, then there is a dupe before it
        slow, fast = nums[0], nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # slow & fast have now met
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        # both slow pointers have met
        return slow2
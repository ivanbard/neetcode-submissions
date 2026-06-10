class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        hashset = set(nums)

        bidx, eidx, curr_len, max_len = 0,0,0,0

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                if i == 0:
                    curr_len = 1
                else:
                    if (nums[i] - 1) not in hashset:
                        #bidx = i
                        max_len = max(curr_len, max_len)
                        curr_len = 1
                    else:
                        #eidx = i
                        curr_len += 1

        max_len = max(curr_len, max_len)
        return max_len
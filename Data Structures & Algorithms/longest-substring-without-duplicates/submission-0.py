class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0
        left = 0
        # right = 1
        # seen.add(s[left])
        # seen.add(s[right])

        for right in range(len(s)):
            while s[right] in seen:
                # max_len = max(max_len, left - right)
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            max_len = max(max_len, right-left + 1)

        return max_len
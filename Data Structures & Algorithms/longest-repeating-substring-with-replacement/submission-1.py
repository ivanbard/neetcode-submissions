class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # make the longest single char string possible with k amount of replacements at MOST
        left, max_len, swaps = 0, 0, 0
        counts = {}
        max_freq = 0

        #find most common char in current window
        #see if len - that num exceed k or not
        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            max_freq = max(max_freq, counts[s[right]])

            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
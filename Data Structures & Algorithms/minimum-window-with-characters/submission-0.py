from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        letters = Counter(t)
        seen = Counter()
        shortest_substring = ""
        left = 0

        for right in range(len(s)):
            seen[s[right]] += 1

            # while letters has at least the same elements as seen
            while (letters & seen) == letters:
                if not shortest_substring or (right - left + 1) < len(shortest_substring):
                    shortest_substring = s[left : right + 1]

                seen[s[left]] -= 1
                left += 1

        return shortest_substring
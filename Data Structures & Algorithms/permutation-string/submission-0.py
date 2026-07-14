from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if s2 contains a permutation of s1, return true
        # permutation is a string but letters dont need to follow same order
        letters = Counter(s1)
        seen = Counter()

        left = 0
        for right in range(len(s2)):
            seen[s2[right]] += 1
            if letters == seen:
                return True

            if right - left + 1 >= len(s1):
                seen[s2[left]] -= 1
                if seen[s2[left]] == 0:
                    del seen[s2[left]]
                left += 1

        return False
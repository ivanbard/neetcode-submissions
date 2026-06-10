class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(c for c in s if c.isalnum())
        string = string.lower()

        i = 0
        j = len(string) - 1

        while i < j:
            a = string[i]
            b = string[j]

            if a != b:
                return False
            else:
                i += 1
                j -= 1

        return True
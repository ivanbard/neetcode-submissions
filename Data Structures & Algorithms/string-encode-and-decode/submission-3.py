class Solution:

    def encode(self, strs: List[str]) -> str:
        # combine length of string and a delimiter to handle any character in strs
        encoded = "".join(f"{len(s)}#{s}" for s in strs)
        return encoded
    
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            # Find the delimiter to know the length of the next string
            j = s.find("#", i)
            length = int(s[i:j])
            # Extract the string based on the parsed length
            decoded.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return decoded
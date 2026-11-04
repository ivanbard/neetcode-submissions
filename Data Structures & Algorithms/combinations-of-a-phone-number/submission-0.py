class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # create hashmap to hold possible letters for each digit
        letter_map = {2: ["a","b","c"],
                      3: ["d","e","f"],
                      4: ["g","h","i"],
                      5: ["j","k","l"],
                      6: ["m","n","o"],
                      7: ["p","q","r","s"],
                      8: ["t","u","v"],
                      9: ["w","x","y","z"],
                      }
        results = []
        temp_string = ""

        def backtrack(digit, temp_string):
            if digit==len(digits):
                #base case, length matched
                results.append(temp_string)
                return
            
            for letter in letter_map[int(digits[digit])]:
                # Recurse using the next digit position
                # and temp_string with this letter added.
                temp_string += letter
                backtrack(digit + 1, temp_string)

                # "pop" the added elem to try the next
                temp_string = temp_string[:-1]

            return results


        return backtrack(0, "")
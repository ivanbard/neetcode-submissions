class WordDictionary:

    def __init__(self):
        self.root = {"children": {}, "is_end": False}

    def addWord(self, word: str) -> None:
        curr_node = self.root

        for char in word:
            if char not in curr_node["children"]:
                new_node = {"children": {}}
                curr_node["children"][char] = new_node

            # move to next node
            curr_node = curr_node["children"][char]

        # mark end of word 
        curr_node["is_end"] = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            # processed all chars, end of word
            if i == len(word):
                return node.get("is_end", False)

            char = word[i]
            if char == ".":
                # try every possible child/val if curr char is a dot
                for child in node["children"].values():
                    if dfs(child, i+1):
                        return True

                return False

            else:
                # non-dot char handling
                if char not in node["children"]:
                    return False

                return dfs(node["children"][char], i + 1)

        return dfs(self.root, 0)
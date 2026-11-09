class PrefixTree:

    def __init__(self):
        # empty root with a dictionary at each node
        self.root = {"children": {}, "is_word": False}

    def insert(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node["children"]:
                # create new node if not in tree
                new_node = {"children": {}, "is_word": False}
                # add new node to current's children
                curr_node["children"][char] = new_node

            # move to child node
            curr_node = curr_node["children"][char]

        # curr node is end of word
        curr_node["is_word"] = True

    def search(self, word: str) -> bool:
        if not word:
            return False
        
        curr_node = self.root
        for char in word:
            # letter not in any nodes
            if char not in curr_node["children"]:
                return False

            curr_node = curr_node["children"][char]

        # end of word, but not marked as word
        if curr_node["is_word"] == False:
            return False
        else:
            return True

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return False
        
        curr_node = self.root
        for char in prefix:
            # letter not in any nodes
            if char not in curr_node["children"]:
                return False

            curr_node = curr_node["children"][char]

        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # find + return all words in 'words' that can be found in 'board'
        # cell can only be used once in a word

        # make trie from the word list
        # then perform dfs + backtracking through board to find words
        root = {"children": {}, "is_word": False, "is_found": False, "the_word": ''}
        for i in range(len(words)):
            # reset to root before every new word
            curr_node = root
            for char in words[i]:
                if char not in curr_node["children"]:
                    new_node = {"children": {}, "is_word": False, "is_found": False}
                    curr_node["children"][char] = new_node

                #move to next node
                curr_node = curr_node["children"][char]

            # mark end of current word in the trie
            curr_node["is_word"] = True 
            curr_node["the_word"] = words[i]
            # !! when word is found in board, set is_word flag to false
            # !! this will allow us to handle duplicate + longer words with same prefixes

        used = set()
        results = []
        def dfs(row, col, node):
            # if r/c outside of board, or letter at r,c is already in curr path
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or ((row, col) in used):
                return

            # letter in board, continue
            if board[row][col] in node["children"]:
                node = node["children"][board[row][col]]
                # check if end of word/word found
                if node["is_word"] == True:
                    results.append(node["the_word"])
                    node["is_word"] = False

                used.add((row, col))
                
                # check down direction
                dfs(row+1, col, node)
                # up
                dfs(row-1, col, node)
                # right
                dfs(row, col+1, node)
                # left
                dfs(row, col-1, node)

                # remove letter to allow backtrack to next combination
                used.remove((row, col))

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root)

        return results
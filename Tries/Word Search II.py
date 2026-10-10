class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        # Step 1: Build Trie
        root = {}

        for word in words:
            node = root

            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]

            node["$"] = word

        rows = len(board)
        cols = len(board[0])
        result = []

        # Step 2: DFS + Backtracking
        def dfs(r, c, parent):

            char = board[r][c]

            if char not in parent:
                return

            node = parent[char]

            # Step 3: Word found
            if "$" in node:
                result.append(node["$"])
                del node["$"]

            # Mark current cell as visited
            board[r][c] = "#"

            # Explore up, down, left, right
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":

                    dfs(nr, nc, node)

            # Backtrack: restore original character
            board[r][c] = char

            # Optimization: remove exhausted Trie branches
            if not node:
                del parent[char]

        # Step 4: Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result

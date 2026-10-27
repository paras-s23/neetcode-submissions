
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(i, string, open_count, close_count):
            if i == 2 * n:
                result.append(string)
                return

            if open_count < n:
                dfs(i + 1, string + "(", open_count + 1, close_count)

            if close_count < open_count:
                dfs(i + 1, string + ")", open_count, close_count + 1)

        dfs(0, "", 0, 0)
        return result

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        res = [[0] * ROWS for _ in range(COLS)]

        for i in range(rows):
            for j in range(cols):
                res[i][j] = matrix[j][i]

        return res
        
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        candidates.sort()

        def dfs(curr, i, currSum):
            if currSum == target:
                results.append(curr.copy())
                return
            elif currSum > target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                curr.append(candidates[j])
                dfs(curr, j+1, currSum + candidates[j])
                curr.pop()

        dfs([], 0, 0)
        return results
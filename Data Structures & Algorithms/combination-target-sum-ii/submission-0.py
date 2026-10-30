class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        candidates.sort()

        def dfs(curr, i):
            if sum(curr) == target:
                results.append(curr.copy())
                return
            elif sum(curr) > target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                curr.append(candidates[j])
                dfs(curr, j+1)
                curr.pop()

        dfs([], 0)
        return results
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        result = 1

        for pattern in range(2):
            l, r = 0, 0

            while r < len(arr) - 1:
                if r % 2 == pattern and arr[r] > arr[r+1]:
                    r += 1
                elif r % 2 != pattern and arr[r] < arr[r+1]:
                    r += 1
                else:
                    result = max(result, r-l+1)
                    r += 1
                    l = r

            result = max(result, r-l+1)

        return result
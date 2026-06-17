class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        current = [0, 1, 1]
        for i in range(3, n+1):
            current.append(current[i-3] + current[i-2] + current[i-1])
        return current[n]



        
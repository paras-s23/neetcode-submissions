class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
    
        while True:
            res = i*i
            if res == x:
                return i
            elif res > x:
                return (i-1)
            i+=1

            
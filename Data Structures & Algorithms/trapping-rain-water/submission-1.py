class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        water = 0
        maxLeft = []
        mL=0
        maxRight = [0] * len(height)
        mR=0
        
        for i in range(len(height)):
            maxLeft.append(mL)
            mL = max(height[i],mL)
        for i in range(len(height)-1,-1,-1):
            maxRight[i] = mR
            mR = max(height[i],mR)
        
        for i in range(len(height)):
            cur = min(maxLeft[i],maxRight[i])
            m = cur - height[i]
            water += max(0, m)
        return water
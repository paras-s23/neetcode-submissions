class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        maxLeft = []
        maxRight = [0] * len(height) 
       
        mL = 0
        mR = 0
        water = 0

        for i in range(len(height)):
            maxLeft.append(mL)
            mL = max(mL, height[i])
        for i in range(len(height)-1,-1,-1):
            maxRight[i] = mR
            mR = max(mR, height[i])
        for i in range(len(height)):
            cur = min(maxLeft[i],maxRight[i]) - height[i]
            water += max(0, cur)
        
        return water
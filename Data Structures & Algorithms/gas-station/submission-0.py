class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 0:
            return 0 
    
        
        for i in range(len(gas)):
            if gas[i] < cost[i]:
                continue
            j = i
            tank = 0
            while tank >= 0:
                tank+= gas[j % len(gas)] - cost[j % len(gas)]
                j+=1
                if (j %len(gas)) == i and tank >=0:
                    return i
    
        return -1
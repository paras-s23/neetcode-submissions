class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        seconds = [0] * len(position)
        fleets = 0

        for i in range(len(position)):
            seconds[i] = int((target-position[i])/speed[i])
        return len(set(seconds))
        
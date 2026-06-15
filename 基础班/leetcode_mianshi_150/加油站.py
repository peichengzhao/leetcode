from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_cost = 0
        total_gas = 0
        start = 0
        cur_cost = 0
        cur_gas = 0
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            cur_cost += cost[i]
            cur_gas += gas[i]
            current_tank = cur_gas - cur_cost
            if current_tank < 0:
                start = i + 1
                current_tank = 0
                cur_cost = 0
                cur_gas = 0
        return start if total_gas >= total_cost else -1
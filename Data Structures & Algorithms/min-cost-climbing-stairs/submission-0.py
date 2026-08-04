class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        ln = len(cost)

        cost_tot = [0]*(ln+1)

        cost_tot[0] = 0

        cost_tot[1] = 0

        for i in range(2, ln+1):

            if(cost[i-1] + cost_tot[i-1] < cost[i-2] + cost_tot[i-2]):

                cost_tot[i] = cost[i-1] + cost_tot[i-1]

            else:

                cost_tot[i] = cost[i-2] + cost_tot[i-2]


        return cost_tot[ln]        

        
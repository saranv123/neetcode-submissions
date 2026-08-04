class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ln = len(prices)

        stck = [[0]*(i+1) for i in range(ln)]

        for i in range(0, ln):

            for j in range(0, i+1):

                stck[i][j] = prices[i] - prices[j]


        stck_flt = [x for row in stck for x in row]

        if(max(stck_flt) > 0):

            return max(stck_flt)

        else:

            return 0             
        
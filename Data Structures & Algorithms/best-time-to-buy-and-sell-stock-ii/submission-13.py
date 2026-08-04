class Solution:
    def maxProfit(self, prices: List[int]) -> int:
         
        ln = len(prices)

        stck = [[0]*(i+1) for i in range(ln)]

        best = [0]*(ln-1)

        if(ln == 1):
            return 0
        if(ln == 2):
            if(prices[1] - prices[0] > 0):
                return prices[1] - prices[0]
            else:
                return 0    
            

        def max2(S, l):

            mx = S[0][0]

            for i in range(0, l):

                for j in range(0, i+1):

                    if(mx < S[i][j]):

                        mx = S[i][j]

            return mx   


        for i in range(ln-1, -1, -1):

            for j in range(i, -1, -1):                

                stck[i][j] = prices[i] - prices[j]

             #   if(i < ln-2):

                #    stck[i][j] = stck[i][j] + max(stck, i+1, j+1, ln)

            
        best[ln-2] = stck[ln-1][ln-1]

        for i in range(ln-3, -1, -1):

            column = [stck[j][i+1] for j in range(i+1, ln)]
            max_col = max(column)
            best[i] = max(max_col, best[i+1])
            max_col = 0

            for j in range(i, -1, -1):

                stck[i][j] = stck[i][j] + best[i]
                   

       # print(best)   
      
        return max2(stck, ln)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        dfs = [-1]*(amount+1)

        coins.sort()
        dfs[0] = 0

        if coins[0] == 1:
            dfs[1] = 1
        else:
            dfs[1] = -1


        for i in range(1, amount+1):
            
            n = 0

            while(n < len(coins) and coins[n] <= i):

                if dfs[i] == -1 and dfs[i-coins[n]] != -1:
                    dfs[i] = dfs[i-coins[n]] + 1   
                elif dfs[i] != -1 and dfs[i-coins[n]] != -1:
                    dfs[i] = min(dfs[i], dfs[i-coins[n]] + 1)
                
                n = n + 1
        
        print(dfs)
        
        return dfs[amount]
        
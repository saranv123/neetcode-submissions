class Solution:
    def countSubstrings(self, s: str) -> int:
        ln = len(s)

        size = 0
        st = 0
        end = 0
        count = ln
        
        dp = [[-1 for _ in range(ln)] for _ in range(ln)]

        dp[ln-1][ln-1] = 1
        
        for i in range(0, ln-1):

            dp[i][i] = 1

            if s[i] == s[i+1]:
                dp[i][i+1] = 1

                count = count + 1
       
            else:
                dp[i][i+1] = 0

        for i in range(ln-3, -1, -1):
            for j in range(ln-1, i+1, -1):

              

                if s[i] == s[j] and dp[i+1][j-1] == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0

                if(dp[i][j] == 1):
                    count = count + 1  
        
        return count




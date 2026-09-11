class Solution:
    def longestPalindrome(self, s: str) -> str:

        ln = len(s)

        size = 0
        st = 0
        end = 0
        
        dp = [[-1 for _ in range(ln)] for _ in range(ln)]

        dp[ln-1][ln-1] = 1
        
        for i in range(0, ln-1):

            dp[i][i] = 1

            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                size = 2
                st = i
                end = i+1
            else:
                dp[i][i+1] = 0

            

      #  print(dp)
        for i in range(ln-3, -1, -1):
            for j in range(ln-1, i+1, -1):

               # print(i,j)

                if s[i] == s[j] and dp[i+1][j-1] == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0

                if dp[i][j] == 1:
                    if(j-i + 1 > size):
                       # print(size)
                        size = j-i+1
                        st = i
                        end = j

       # print(dp)
        return s[st:end+1]                


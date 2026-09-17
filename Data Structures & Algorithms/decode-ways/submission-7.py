class Solution:
    def numDecodings(self, s: str) -> int:


        nums = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']
        ln = len(s)

        dp = [0]*(ln)

        if s[0:1] == '0':
            return 0
        else:
            dp[0] = 1

        if ln == 1:
            return dp[0]    

        if s[0:2] in nums:

            if s[1:2] == '0':
                dp[1] = 1
            else:
                dp[1] = 2
        else:
            if s[1:2] == '0':
                dp[1] = 0
            else:
                dp[1] = 1                 
    

        for i in range(2, ln):

            if s[i-1:i+1] in nums:
                
                if s[i:i+1] == '0':
                    dp[i] = dp[i-2]
                else:
                    dp[i] = dp[i-1] + dp[i-2]
            else:
                if s[i:i+1] == '0':
                    dp[i] = 0
                else:
                    dp[i] = dp[i-1]                

                    

        print(dp)        

        return dp[ln-1]                


        
        
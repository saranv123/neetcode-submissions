class Solution:
    def tribonacci(self, n: int) -> int:

        Tn = [0]*(n+1)

        Tn[0] = 0


        if(n == 0):
            return 0

        if(n == 1):
            return 1    

        
        Tn[1] = 1
        Tn[2] = 1

        for i in range(3, n+1):

            Tn[i] = Tn[i-3] + Tn[i-2] + Tn[i-1]


        return Tn[n]    


        
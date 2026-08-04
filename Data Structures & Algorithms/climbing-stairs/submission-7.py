class Solution:
    def climbStairs(self, n: int) -> int:

        count = 1

        def comb(m, n):

            if(m == n):
                return 1
            if(n == 0):
                return 1

            cmbntrl = comb(m-1, n-1) + comb(m-1, n)

            return cmbntrl     

        cmbn = 1           

        

        for l in range(1, int(n/2) + 1):

            cmbn = cmbn * int(n-(2*l) + 1)*(n-(2*l)+2)//((n-l+1)*l)

            print(n-l,l, cmbn)

            count = count + cmbn

             



        return count            
        
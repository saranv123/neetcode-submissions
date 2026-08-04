class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:


        def rec(i,j):

            if(i == len(s)):

                return 1

            elif(j == len(t)):

                return 0

            if(s[i] == t[j]):

                return rec(i+1, j+1)

            else:

                return rec(i, j+1)
        

        n = rec(0, 0)

        if(n == 1):
            return True
        else:
            return False



       

      


                


                



        
        
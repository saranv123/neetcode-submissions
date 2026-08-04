class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        array = [0]*(rowIndex+1)


        def fact(n):

            factorial = 1

            for i in range(1,n+1):

                factorial = factorial*i
            
            return factorial


        def combination(n, k):

            comb = int(fact(n)/(fact(n-k)*fact(k)))

            return comb

        for i in range(0, rowIndex+1):

            array[i] = combination(rowIndex, i)

        return array    




        
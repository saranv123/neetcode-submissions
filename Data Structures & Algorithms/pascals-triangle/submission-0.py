class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        trngle = [[0 for _ in range(r+1)] for r in range(numRows)]

       # print(trngle)

        trngle[0][0] = 1
        
        if(numRows > 1):
            trngle[1][0] = trngle[1][1] = 1


        for i in range(2, numRows):
            
            trngle[i][0] = trngle[i][i] = 1

            for j in range(1, i):

                trngle[i][j] = trngle[i-1][j-1] + trngle[i-1][j]


        return trngle        
        
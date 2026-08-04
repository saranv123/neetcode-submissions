class Solution:
    def countBits(self, n: int) -> List[int]:


        def countone(m):

            count = 0

            while (m > 0):

                if(m%2 == 1):
                    count = count + 1

                m = m//2

            return count        
        
        array = [0]*(n+1)

        for i in range(0, n+1):

            array[i] = countone(i)

        return array    



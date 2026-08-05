class Solution:
    def rob(self, nums: List[int]) -> int:

        ln = len(nums)

        cash = [0]*(ln)


        if(ln == 1):
            return nums[0]


        cash[0] = nums[0]
        cash[1] = max(nums[0], nums[1])

        if(ln == 2):
            return cash[1]

        if(cash[1] == nums[1]):

            if(cash[0] + nums[2] > cash[1]):
                cash[2] = cash[0] + nums[2]
            else:
                cash[2] = cash[1]
        else:
            cash[2] = cash[1] + nums[2]      

        if(ln == 3):
            return cash[2]      

        


        for i in range(3, ln):


            if(cash[i-1] - cash[i-2] == nums[i-1] or cash[i-1] - cash[i-3] == nums[i-1]):

                if(cash[i-2] + nums[i] > cash[i-1]):
                    cash[i] = cash[i-2] + nums[i]
                else:
                    cash[i] = cash[i-1]
            
            else:

                cash[i] = cash[i-1] + nums[i]

            print(cash[i])    


        return cash[ln-1]        





        
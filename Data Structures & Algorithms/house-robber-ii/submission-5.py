class Solution:
    def rob(self, nums: List[int]) -> int:
        
        ln = len(nums)

        cash1 = [0]*ln
        cash2 = [0]*ln

        if (ln == 1):
            return nums[0]

        if (ln == 2):
            return max(nums[0], nums[1])

        cash1[0] = nums[0]
        cash1[1] = cash1[0]
        cash1[2] = cash1[1] + nums[2]

        cash2[0] = -1
        cash2[1] = nums[1]
        cash2[2] = max(cash2[1], nums[2])

        for i in range(3, ln-1):

            if(cash1[i-1] - cash1[i-2] == nums[i-1]or cash1[i-1] - cash1[i-3] == nums[i-1]):
                cash1[i] = max(cash1[i-1], cash1[i-2] + nums[i])
            else:
                cash1[i] = cash1[i-1] + nums[i]

        cash1[ln-1] = cash1[ln-2]

        for i in range(3, ln):

            if(cash2[i-1] - cash2[i-2] == nums[i-1] or cash2[i-1] == nums[i-1] or cash2[i-1] - cash2[i-3] == nums[i-1]):
                cash2[i] = max(cash2[i-1], cash2[i-2] + nums[i])
            else:
                cash2[i] = cash2[i-1] + nums[i]

        return max(cash2[ln-1], cash1[ln-1])

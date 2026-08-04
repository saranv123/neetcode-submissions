class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        n = len(nums)

        seen = set()

        a = 0

        for i in range(0, n):

            if nums[i] in seen:
                a = 1
                break
            seen.add(nums[i])


        if(a == 1):
            return True
        else:
            return False
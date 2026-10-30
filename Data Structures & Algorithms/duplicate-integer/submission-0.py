class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for num in nums:
        #     duplicate = 0
        #     for nbr in nums:
        #         if nbr == num:
        #             duplicate += 1
        #     if duplicate > 1:
        #         return True
        # return False
        seen = set()

        for num in nums: 
            if num in seen:
                return True
            seen.add(num)
        return False
        
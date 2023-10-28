class Solution(object):
    def singleNumber(self, nums):
        xor_result = 0
        for num in nums:
            xor_result ^= num

        mask = xor_result & -xor_result

        group1 = 0
        group2 = 0
        for num in nums:
            if num & mask:
                group1 ^= num
            else:
                group2 ^= num

        return [group1, group2]

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        

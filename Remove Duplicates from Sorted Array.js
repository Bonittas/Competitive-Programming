class Solution(object):
    def removeDuplicates(self, nums):
        val = set()
        i = 0
        while(i<len(nums)):
            if(nums[i] in val):
                nums.remove(nums[i])
            else:
                val.add(nums[i])
                i+=1
                
        #print(nums)
        return len(val)
        """
        :type nums: List[int]
        :rtype: int
        """

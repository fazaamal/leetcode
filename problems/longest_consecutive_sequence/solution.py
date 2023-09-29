from collections import defaultdict

def def_value():
    return 'Not Present'

class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        # numDict = defaultdict(def_value)
        # if(len(nums) == 0):
        #     return 0
        # maxCount = 0
        # counter = 0
        
        # for num in nums:
        #     numDict[num] = True
        
        # nums.sort()
        # for num in nums:
        #     if(numDict[num] == True):
        #         c = True
        #         counter = 1
        #         curr = num
        #         while(c):
        #             if(numDict[curr+1] == True):
        #                 numDict[curr+1] = False
        #                 counter += 1
        #                 curr += 1
        #             else:
        #                 c = False
                
        #         if(counter > maxCount):
        #             maxCount = counter 

        # if(counter > maxCount):
        #     maxCount = counter

        # return maxCount
        longest = 0
        num_set = set(nums)

        for n in num_set:
            if (n-1) not in num_set:
                length = 1
                while (n+length) in num_set:
                    length += 1
                longest = max(longest, length)
        
        return longest

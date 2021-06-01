# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if nums == []:
            return []
        elif len(nums) < 3:
            return []
        
        nums = sorted(nums) 
        tripletsResult = {}
        
        for k in range(0, len(nums)-2):
            i = k + 1
            j = len(nums)-1
            
            while(i<j):
                
                if nums[k] + nums[i] + nums[j] == 0:
                    if (nums[k], nums[i], nums[j]) not in tripletsResult.keys():
                        tripletsResult[ (nums[k], nums[i], nums[j]) ] = 1 
                    i += 1
                    
                    while(nums[i] == nums[i-1] and i<j):
                        i += 1
                    
                elif nums[k] + nums[i] + nums[j] > 0:
                    j -= 1
                else:
                    i += 1
                    
        return(tripletsResult.keys())
    
    
    
    
    

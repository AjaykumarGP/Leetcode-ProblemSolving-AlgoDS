# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        #Calculate ideal sum of the sequence limit
        sumOfSequence = (len(nums) + 1) * (0+len(nums)) // 2
        
        sumOfGivenSequence = 0
        
        for i in range(0, len(nums)):
            sumOfGivenSequence += nums[i]
            
        #Difference of ideal summation and given summation is the answer
        missingNumber = sumOfSequence - sumOfGivenSequence
        return missingNumber
      
      
# Note: I have used Gauss formula to find summation of first n natural number, and used it to find the difference of the given array summation, which will result in missing numer.
# Note: This problem can be solved by sorting, hashset, Bit manipultion(XoR), Gauss formula.

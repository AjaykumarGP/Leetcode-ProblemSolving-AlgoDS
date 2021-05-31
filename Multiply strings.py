# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        num1Converted = 0
        num2Converted = 0
        count = 0
        
        while(count < len(num1)):
            numericValue = ord(num1[count]) - ord("0")
            num1Converted = (num1Converted * 10) + numericValue
            count += 1
        
        count = 0
        while(count < len(num2)):
            numericValue = ord(num2[count]) - ord("0")
            num2Converted = (num2Converted * 10) + numericValue
            count += 1
            
        return str(num1Converted*num2Converted)
      
      
# Note: Instead of using built-in string to integer converter use Ascii value to deduce integer value from character value
        
        
        

# Given a non-negative integer x, compute and return the square root of x.

# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

class Solution:
    def mySqrt(self, x: int) -> int:
        
        currentInteger = 1
        previousInteger = 0
        
        while(True):
            square = currentInteger * currentInteger
            if square > x:
                return previousInteger
            currentInteger += 1
            previousInteger += 1 
            
#  Note: Another solution is to use binary search with the monotonic search space concept

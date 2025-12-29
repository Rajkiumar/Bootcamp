class Solution:
    def myPow(self, x, n):
        if n == 0 or x == 1.0:
            return 1
        temp = n
        
        if n < 0:
            x = 1 / x
            temp = -1 * n

        ans = 1

        for i in range(temp):
            ans *= x 
        return ans

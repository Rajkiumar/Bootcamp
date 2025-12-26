class Solution:
    def generateParenthesis(self, n):
        #your code goes here
        ans = []

        def func(s,l,r):
            if len(s)==2*n:
                ans.append(s)
            
            if l<n:
                func(s+"(",l+1,r)
            
            if r<l:
                func(s+")",l,r+1)

        func("",0,0)
        return ans

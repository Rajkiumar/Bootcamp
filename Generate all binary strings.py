class Solution:
    def generateBinaryStrings(self, n):
        # Your code goes here
        result =[]

        def generate(curr):
            if len(curr) == n:
                result.append(curr)
                return
            generate(curr + "0")

            if not curr or curr[-1] != '1':
                generate(curr + "1")
        
        generate("")
        return result

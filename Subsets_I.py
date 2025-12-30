class Solution:
    def findSums(self, index, currentSum, arr, sums):
        if index == len(arr):
            sums.append(currentSum)
            return
        self.findSums(index + 1, currentSum + arr[index], arr, sums)
        self.findSums(index + 1, currentSum, arr, sums)

    def subsetSums(self, arr):
        sums = []
        self.findSums(0, 0, arr, sums)
        sums.sort()
        return sums

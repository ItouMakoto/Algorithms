class NumArray(object):
    numList=None
    def __init__(self, nums):
        self.numList=list(nums)


    def sumRange(self, i, j):
        res=sum(self.numList[:j])-sum(self.numList[:i])

        return res


if __name__ == '__main__':
    test=NumArray([1,2,3,4,5])

    print(test.sumRange(1,3))
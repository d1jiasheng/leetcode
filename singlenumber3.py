class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        result = []
        for num in nums:
            d[num] = 0
        for num in nums:
            d[num]+=1
        for i , item in d.items():
            if item==1:
                result.append(i)
        return result

#这个可以更加简化，第一个用于赋值的for循环可以与第二个合并。做这类题目用python真的简单
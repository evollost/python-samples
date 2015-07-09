def rob(self, nums):
#    a = b =0
#    for i, value in enumerate(nums):
#        if i % 2 ==0:
#            a = max(a + value, b)
#        else:
#            b = max(b + value, a)
#    return max(a, b)
    before = after = 0
    for i in nums:
        before, after = after, max(i + before, after)
    return after

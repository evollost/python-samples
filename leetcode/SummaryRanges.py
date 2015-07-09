def SummaryRanges(nums):
    ranges, r = [], []
    for n in nums:
        if n-1 not in r:
            r = []
            ranges += r,
        r[1:] = n,
    return ['->'.join(map(str, r)) for r in ranges]

if __name__ == "__main__":
    nums = [1,2,3,4,6,7,8,15]
    result = SummaryRanges(nums)
    print result

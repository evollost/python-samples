def majorityElement(self, nums):
    #return sorted(nums)[len(nums)//2]
    count = 0
    for element in nums:
        if count == 0:
            majority = element
            count += 1
        elif element == majority:
            count += 1
        else:
            count -= 1
    return majority

def ContainsNearbyDuplicate(self, nums, k):
    d = {}
    for i, value in enumerate(nums):
        if value in d and i - d[value] <= k:
            return True
        d[value] = i
    return False

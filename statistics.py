def variance(nums):
    mean = sum(nums) / len(nums)
    return sum(((n - mean)**2 for n in nums)) / len(nums)


def standard_deviation(nums):
    return variance(nums) ** 0.5

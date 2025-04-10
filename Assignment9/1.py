def find_max_negative_min_positive(nums):
    negatives = list(filter(lambda x: x < 0, nums))
    positives = list(filter(lambda x: x > 0, nums))
    max_negative = max(negatives) if negatives else None
    min_positive = min(positives) if positives else None
    return max_negative, min_positive

# 示例
nums = [-5, -1, -3, 2, 4, 6]
# nums = [1,2,-3,4,-5]
print("原始数据:",nums)
max_negative, min_positive = find_max_negative_min_positive(nums)
print(f"负数中的最大值：{max_negative}\n正数中的最小值：{min_positive}")
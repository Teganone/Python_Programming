def two_sum(nums, target):
    all_pairs = [(i,j) for i in range(len(nums)) for j in range(len(nums))]
    print("所有可能两两组和对：",all_pairs)
    new_pairs = list(filter(lambda x:x[0]!=x[1] and nums[x[0]]<=nums[x[1]],all_pairs))
    print("新的两两组和对：",new_pairs)
    ans =  list(filter(lambda x:nums[x[0]]+nums[x[1]]==target,new_pairs))
    return ans
print("答案：",two_sum([2,7,7,15],9))

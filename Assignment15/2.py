def right_shift(orgList, times):
    times = times % len(orgList)  # 避免不必要的重复移位
    return orgList[-times:] + orgList[:-times]

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(f"original list:{lst}")
print(f"shifted  list:{right_shift(lst, 3)}")  # 输出: [70, 80, 90, 10, 20, 30, 40, 50, 60]
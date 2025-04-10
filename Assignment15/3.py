def calculate_cost(S, V, bike_type):
    time_in_minutes = (S / V) * 60  # 将时间转换为分钟
    cost = 0

    if bike_type == '哈哈单车':
        if time_in_minutes <= 15:
            cost = 1.5
        else:
            cost = 1.5 + ((time_in_minutes - 15) // 15 + 1) * 1.5

    elif bike_type == '呵呵单车':
        if time_in_minutes <= 30:
            cost = 1.5
        else:
            cost = 1.5 + ((time_in_minutes - 30) // 15 + 1) * 1

    elif bike_type == '嘻嘻单车':
        if time_in_minutes <= 15:
            cost = 1.5
        else:
            cost = 1.5 + ((time_in_minutes - 15) // 10 + 1) * 1

    return cost

def min_cost_choice(S, V):
    haha_cost = calculate_cost(S, V, '哈哈单车')
    hehe_cost = calculate_cost(S, V, '呵呵单车')
    xixi_cost = calculate_cost(S, V, '嘻嘻单车')

    min_cost = min(haha_cost, hehe_cost, xixi_cost)
    best_choice = '哈哈单车' if min_cost == haha_cost else '呵呵单车' if min_cost == hehe_cost else '嘻嘻单车'
    return min_cost, best_choice

# 示例输入
S = 10  # 距离，单位：公里
V = 15  # 速度，单位：公里/小时

min_cost, best_choice = min_cost_choice(S, V)

print(f"The most cost-effective bike is {best_choice} with a cost of {min_cost:.2f} yuan.")
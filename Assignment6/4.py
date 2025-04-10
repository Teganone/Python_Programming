def count_seats(n, bookings):
    # 初始化一个长度为n的列表，用于存储每个航班的座位总数
    answer = [0] * n
    answers = []
    # 遍历预订记录
    for first, last, seats in bookings:
        single_answer = [0] * n
        # 计算当前预订记录覆盖的航班编号范围
        for i in range(first - 1, last):
            answer[i] += seats
            single_answer[i] = seats
        answers.append(single_answer)
    return answer, answers

# 示例输入
n = 5
bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
answer, answers = count_seats(n, bookings)
# 调用函数并打印结果
print(f"航班数={n}, bookings={bookings}")
for i in range(len(answers)):
    print(f"answer{i} = {answers[i]}")
print(f"座位总数 = {answer}")
    
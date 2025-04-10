# 3）百鸡百钱（20分）

def find_chickens():
    solutions = []
    for x in range(21):  # 鸡翁最多20只
        for y in range(34):  # 鸡母最多33只
            z = 100 - x - y
            if 5*x + 3*y + z/3 == 100 and z % 3 == 0:
                solutions.append((x, y, z))
    return solutions

solutions = find_chickens()
i = 0
for solution in solutions:
    i+=1
    print(f"买法{i}: 公鸡: {solution[0]}, 母鸡: {solution[1]}, 小鸡: {int(solution[2])}")
print(f"共有 {i} 种买法")
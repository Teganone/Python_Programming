def find_square_numbers():
    results = []
    for i in range(0, 10000):  # 限制一个合理的搜索范围
        root1 = (i + 100) ** 0.5
        root2 = (i + 268) ** 0.5
        if root1.is_integer() and root2.is_integer():
            results.append(i)
            if len(results) == 3:
                return results
    return results

print(find_square_numbers())
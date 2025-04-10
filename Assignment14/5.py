import os

def sleepy_cow_sorting(n, cows):
    # 找到从后向前的最长排序段的起始位置
    sorted_idx = n - 1
    while sorted_idx > 0 and cows[sorted_idx - 1] <= cows[sorted_idx]:
        sorted_idx -= 1

    # 结果是未排序部分的数量
    return sorted_idx

def compare_with_output(input_folder, output_folder):
    results = {}
    for filename in os.listdir(input_folder):
        if filename.endswith('.in'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace('.in', '.out'))
            
            # 读取输入文件
            with open(input_path, 'r') as file:
                n = int(file.readline().strip())
                initial_order = list(map(int, file.readline().split()))
                # print(input_path, n, initial_order)
            # 计算最小操作次数
            calculated_operations = sleepy_cow_sorting(n, initial_order)
            
            # 读取预期输出
            with open(output_path, 'r') as file:
                expected_operations = int(file.readline().strip())
            
            # 比较结果
            results[filename] = calculated_operations == expected_operations

    return results

# 设置输入和输出文件夹路径
folder_name = 'sleepy_bronze_jan19'
input_folder = os.path.join(os.getcwd(), folder_name)
output_folder = input_folder

# 比较结果
results = compare_with_output(input_folder, output_folder)

# 打印结果
for test, passed in results.items():
    print(f"Test {test}: {'Passed' if passed else 'Failed'}")
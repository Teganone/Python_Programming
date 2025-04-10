def convert_to_float(str_list):
    return list(map(float, str_list))

# 示例
str_list = ["1.1", "2.2", "3.3"]
float_list = convert_to_float(str_list)
print(f"输入：{str_list}")
print(f"输出：{float_list}")
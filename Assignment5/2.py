def swap_case(s):
    result = ""
    for char in s:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        else:
            result += char
    return result

input_str = input("请输入一段英文:")
swapped_str = swap_case(input_str)
print(swapped_str)



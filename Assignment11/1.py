
# 假设填报选项.txt文件中的每一行都是一个选项
def read_options(filename):
    with open(filename, 'r') as file:
        options = file.readlines()
    return [option.strip() for option in options]

def save_information(filename, information):
    with open(filename, 'w') as file:
        for key, value in information.items():
            file.write(f"{key},{value}\n")

def main(input_file,output_file):
    options = read_options(input_file)
    information = {}
    for option in options:
        if '：' in option:  
            option_title, option_class = option.split('：')
            classes = option_class.split('、')
            print_classes = '\n'.join([f'  {i+1} -- {classes[i]}' for i in range(len(classes))])
            user_input = input(f"请选择 {option_title}:\n{print_classes}\n输入选择数字:")
            information[option_title] = classes[int(user_input)-1]
        else:
            user_input = input(f"请输入{option}: ")
            information[option] = user_input
    save_information('填报信息.csv', information)

if __name__ == "__main__":
    input_filename = './填报选项.txt'
    output_filename = './填报信息.csv'
    main(input_filename,output_filename)
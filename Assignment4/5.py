# 4）大数字2 （20分）

Zero  = ['*****',  # 1行
         '*   *',# 2行
         '*   *',# 3行
         '*   *',# 4行
         '*   *',# 5行
         '*   *',# 6行
         '*****']# 7行
One   = ['  *  ',' **  ','* *  ','  *  ','  *  ','  *  ','*****']
Two   = ['*****','    *','    *','*****','*    ','*    ','*****']
Three = ['*****','    *','    *','*****','    *','    *','*****']
Four  = ['  *  ',' **  ','* *  ','*****','  *  ','  *  ','  *  ']
Five  = ['*****','*    ','*    ','*****','    *','    *','*****']
Six   = ['*****','*    ','*    ','*****','*   *','*   *','*****']
Seven = ['*****','    *','    *','   * ','  *  ',' *   ','*    ']
Eight = ['*****','*   *','*   *','*****','*   *','*   *','*****']
Nine  = ['*****','*   *','*   *','*****','    *','    *','*****']
Digits= [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

# 定义函数，将 '*' 替换为对应的数字
def replace_star_with_number(line, number):
    # 将字符串中的 '*' 替换为数字
    return line.replace('*', str(number))

def big_number():
    while True:
        try:
            digits = input("请输入一串数字：")
            if(digits=='quit'):
                break
            for row in range(7):
                line = " "

                for col in range(len(digits)):
                    number = int(digits[col])
                    Digit = Digits[number]
                    add = Digit[row]
                    add = ''.join([replace_star_with_number(line, number) for line in add])
                    line += add+" "
                print(line)
        except:
            print('输入的不是一串有效数字！')

big_number()

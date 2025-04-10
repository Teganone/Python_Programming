id_number = input("请输入您的身份证号码:")
birthday = id_number[6:14]
if int(id_number[16])%2==1:
    gender = '男'
else: gender = '女'
code = id_number[17]
print(f'您是{int(birthday[:4])}年{int(birthday[4:6])}月{int(birthday[6:])}出生的')
print(f'您的性别是:{gender}')
print(f'您的身份证校验码是:{code}')

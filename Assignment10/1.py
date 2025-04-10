# 电话簿管理
phone_book = {
    "顺丰速运": "95338",
    "申通快递": "95543",
    "韵达快递": "95546",
    "圆通速递": "95554",
    "中通速递": "95311",
    "天天快递": "4001888888",
    "京东物流": "950616",
    "百世快递": "95320"
}

def query_company(name):
    return phone_book.get(name, "未找到该快递公司")

def add_company(name, number):
    if name in phone_book:
        print("该公司已经存在，无需添加")
    else:
        phone_book[name] = number

def update_company(name, number):
    if name in phone_book:
        phone_book[name] = number
    else:
        print("未找到该快递公司")

def delete_company(name):
    if name in phone_book:
        del phone_book[name]
    else:
        print("未找到该快递公司")

def traverse_companies():
    for name, number in phone_book.items():
        print(f"{name}\t{number}")

# 测试
menu = '1--快递公司查询\n2--快递公司增加\n3--快递公司修改\n4--快递公司删除\n5--快递公司遍历\0--退出'
while True:
    print(menu)
    select = input('输入您的选择（0～5）：')
    if select.isdigit():  # 检查输入是否为数字
        select = int(select)
    else:
        print("请输入有效的数字选项。")
        continue
    if select == 0:
        break
    if select == 1:
        company = input('输入快递公司名称:')
        print(query_company(company))
    elif select == 2:
        company = input('新增的快递公司名称:')
        phone = input('该公司的电话号码：')
        add_company(company,phone)
        print(f'已经增加了{company}')
    elif select == 3:
        company = input('要修改的快递公司名称：')
        phone = input('该公司的电话号码：')
        update_company(company, phone)
        print(f'已经修改了{company}')
    elif select == 4:
        company = input('要删除的快递公司名称：')
        delete_company(company)
        print(f'已经删除了{company}')
    elif select == 5:
        traverse_companies()
    else:
        print("无效的选项，请重新输入。")
        
# add_company("新快递", "12345678")
# print(query_company("顺丰速运"))
# update_company("申通快递", "99999999")
# delete_company("韵达快递")
# traverse_companies()
def BMI1(name, height, weight):
    bmi = round(weight / (height ** 2), 1)
    if bmi < 18.5:
        print(f"{name}，您的BMI={bmi}，体重过瘦，正常范围：18.5～25，请加强营养")
    elif bmi <= 24.9:
        print(f"{name}，您的BMI={bmi}，体重正常")
    elif bmi <= 29.9:
        print(f"{name}，您的BMI={bmi}，体重超重，正常范围：18.5～25，请增加锻炼")
    elif bmi <= 34.9:
        print(f"{name}，您的BMI={bmi}，一级肥胖，正常范围：18.5～25，请科学减肥")
    elif bmi <= 39.9:
        print(f"{name}，您的BMI={bmi}，二级肥胖，正常范围：18.5～25，请科学减肥")
    else:
        print(f"{name}，您的BMI={bmi}，三级肥胖，正常范围：18.5～25，请马上就医检查")

def BMI2(*persons):
    for person in persons:
        name, height, weight = person
        bmi = round(weight / (height ** 2), 1)
        if bmi < 18.5:
            print(f"{name}，您的BMI={bmi}，体重过轻，正常范围:18.5~25，请加强营养。")
        elif 18.5 <= bmi < 25:
            print(f"{name}，恭喜，您的BMI={bmi}，体重正常，正常范围:18.5~25。")
        elif 25 <= bmi < 30:
            print(f"{name}，您的BMI={bmi}，体重超重，正常范围:18.5~25，请增加锻炼。")
        elif 30 <= bmi < 35:
            print(f"{name}，您的BMI={bmi}，1级肥胖，正常范围:18.5~25，请科学减肥。")
        elif 35 <= bmi < 40:
            print(f"{name}，您的BMI={bmi}，2级肥胖，正常范围:18.5~25，请马上就医检查。")
        else:
            print(f"{name}，您的BMI={bmi}，3级肥胖，正常范围:18.5~25，请马上就医检查。")


# 使用示例
BMI1("李四", 1.60, 50)
BMI1("张三", 1.83, 60)

# 示例调用
BMI2(("张三", 1.80, 99), ("李四", 1.55, 98))
BMI2(("圆圆", 1.70, 65), ("芳芳", 1.68, 50))
print('---传入列表----')
list_m = [('zhangsan',1.80,99),('lisi',1.55,98)]
list_w = [('圆圆',1.70,65),('芳芳',1.68,50)]
BMI2(*list_m,*list_w)


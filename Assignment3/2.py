height = float(input("请输入您的身高(cm):"))/100
weight = float(input("请输入您的体重(kg):"))
bmi = round(weight/(height*height),1)
if bmi < 18.5:
    print("您的BMI=",bmi,"体重过瘦，正常范围：18.5～25，请增加饮食")
elif bmi <= 24.9:
    print("您的BMI=",bmi,"体重正常")
elif bmi <= 29.9:
    print("您的BMI=",bmi,"体重超重，正常范围：18.5～25，请增加锻炼")
elif bmi <= 34.9:
    print("您的BMI=",bmi,"一级肥胖，正常范围：18.5～25，请增加锻炼")
elif bmi <= 39.9:
    print("您的BMI=",bmi,"二级肥胖，正常范围：18.5～25，请增加锻炼")
else:
    print("您的BMI=",bmi,"三级肥胖，正常范围：18.5～25，请增加锻炼")
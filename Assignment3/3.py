weight = float(input("请输入快递重量:"))
print("地区编号:\n1:华东地区\n2:华南地区\n3:华北地区")
district = int(input("请输入地区编号:"))
PREMIUM_WEIGHT = 2.0
if district==1:
    fee = 13+(weight-PREMIUM_WEIGHT)*3 
elif district == 2:
    fee = 12+(weight-PREMIUM_WEIGHT)*2
else:
    fee = 14+(weight-PREMIUM_WEIGHT)*4
print("快递费为",fee,"元")
        
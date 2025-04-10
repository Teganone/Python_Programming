def calculate_blood_concentration(dose:int)->float:
    """
    计算服药后1小时的血药浓度。

    参数:
    dose (int): 口服剂量（单位：片）

    返回:
    float: 血药浓度（单位：mg/L）
    """
    if not isinstance(dose, int):
        raise TypeError("口服剂量必须是整数")
    y = 0.8 * dose + 3.25
    return y


# 1号患者口服剂量为2片
patient_codes = [1,2,3,4]
patient_doses = [2,3,1,4]
for patient_code, patient_dose in zip(patient_codes,patient_doses):
    print(f"{patient_code}号患者口服剂量为: {patient_dose}, 1小时后的血药浓度为: {calculate_blood_concentration(patient_dose):.2f}")

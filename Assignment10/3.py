students = {
    "200001": {"姓名": "张三", "性别": "男", "年龄": 19, "成绩": 598},
    "200016": {"姓名": "芳芳", "性别": "女", "年龄": 19, "成绩": 605},
    "202201": {"姓名": "圆圆", "性别": "女", "年龄": 18, "成绩": 586},
    "202336": {"姓名": "李四", "性别": "男", "年龄": 18, "成绩": 635},
    "202318": {"姓名": "王五", "性别": "男", "年龄": 18, "成绩": 618},
    "202112": {"姓名": "佳佳", "性别": "女", "年龄": 18, "成绩": 620}
}

def display_student_info(id):
    student = students.get(id)
    if student:
        print(f"ID是{id}的姓名:{student['姓名']}")
        print(student)
    else:
        print("未找到该学生信息")

def query_student_by_id():
    id = input("请输入学生的ID:")
    display_student_info(id)

def display_all_students():
    for id, student in students.items():
        print(f"{id} {student['姓名']}{student['性别']} {student['年龄']} {student['成绩']}")

def count_gender_and_age():
    male_count = sum(1 for student in students.values() if student["性别"] == "男")
    female_count = sum(1 for student in students.values() if student["性别"] == "女")
    age_over_18 = [student["姓名"] for student in students.values() if student["年龄"] > 18]
    print(f"男={male_count},女={female_count}")
    print(f">18岁: {age_over_18}")

def display_top_student():
    top_student = max(students.keys(), key=lambda x: students.get(x)["成绩"])
    print(f"最大值:{top_student}")
    print(students.get(top_student))

def main():
    while True:
        print("1--显示ID是202201的姓名,及其全部信息")
        print("2--按照输入的ID进行查询")
        print("3--显示全部信息")
        print("4--统计男女各有多少人,输出年龄大于18岁的学生姓名")
        print("5--显示成绩最高的学生信息")
        print("0--退出程序")
        choice = input("请输入您的选择:")
        if not choice.isdigit():  # 检查输入是否为数字
            print("请输入有效的数字选项。")
            continue
        if choice == '1':
            display_student_info("202201")
        elif choice == '2':
            query_student_by_id()
        elif choice == '3':
            display_all_students()
        elif choice == '4':
            count_gender_and_age()
        elif choice == '5':
            display_top_student()
        elif choice == '0':
            print("退出程序")
            break
        else:
            print("无效的选项，请重新输入。")

if __name__ == "__main__":
    main()
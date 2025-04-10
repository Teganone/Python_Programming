# 假设的调查问卷结果
survey = {
    "吴": {"Python": False, "VB": True, "C": True},
    "王": {"Python": False, "VB": False, "C": True},
    "孙": {"Python": False, "VB": True, "C": False},
    "钱": {"Python": True, "VB": True, "C": False},
    "陈": {"Python": False, "VB": False, "C": True},
    "李": {"Python": True, "VB": False, "C": False},
    "褚": {"Python": True, "VB": True, "C": False},
    "周": {"Python": True, "VB": True, "C": False},
    "郑": {"Python": False, "VB": True, "C": False},
    "卫": {"Python": True, "VB": True, "C": False},
    "赵": {"Python": True, "VB": True, "C": False},
    "冯": {"Python": True, "VB": False, "C": False},
}

def print_student_list(message, student_list):
    print(message)
    print(",".join(student_list))

def main():
    all_students = list(survey.keys())
    print_student_list("参加调查问卷的所有学生名单:", all_students)

    two_languages = [name for name, langs in survey.items() if sum(langs.values()) == 2]
    print_student_list("学过两门计算机语言的学生名单:", two_languages)

    only_python = [name for name, langs in survey.items() if langs["Python"] and not langs["VB"] and not langs["C"]]
    print_student_list("仅学过Python语言的学生名单:", only_python)

    only_vb = [name for name, langs in survey.items() if not langs["Python"] and langs["VB"] and not langs["C"]]
    print_student_list("仅学过VB语言的学生名单:", only_vb)

    only_c = [name for name, langs in survey.items() if not langs["Python"] and not langs["VB"] and langs["C"]]
    print_student_list("仅学过C语言的学生名单:", only_c)

    one_language = [name for name, langs in survey.items() if sum(langs.values()) == 1]
    print_student_list("仅学过一门计算机语言的学生名单:", one_language)

if __name__ == "__main__":
    main()
import random
import math

def generate_question():
    operators = ['+', '-', '*', '/']
    num1 = random.randint(1, 11)
    num2 = random.randint(1, 11)
    op = random.choice(operators)

    if op == '/' and num2 == 0:
        return generate_question()  # 避免除以零

    question = f"{num1} {op} {num2}"
    answer = eval(question)  # 计算答案
    if op == '/':
        answer = round(answer, 2)
    return question, answer

def main():
    total_questions = 0
    correct_answers = 0

    while True:
        question, answer = generate_question()
        print(question+" =")

        user_input = input()

        if user_input.lower() == 'q':
            break
        

        if user_input == str(answer) or math.isclose(float(user_input),answer,rel_tol=1e-2):
                print("right")
                correct_answers += 1
        else:
            print("wrong")
       

        total_questions += 1

    print(f"共有{total_questions}个题目，做对{correct_answers}道，正确率为:{(correct_answers / total_questions * 100):.2f}%")

if __name__ == "__main__":
    main()
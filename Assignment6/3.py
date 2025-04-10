
scores = []
while(True):
    _ = input("请输入一个成绩（直接输入回车退出）")
    if _=="": break
    scores.append(int(_))
print(f"总共输入{len(scores)}个成绩")
print(f"最高分:{max(scores)}")
print(f"最低分:{min(scores)}")
print(f"平均分:{sum(scores)/len(scores)}")
scores = sorted(scores)
if len(scores) % 2==1:
    mid = scores[len(scores)//2]
else:
    mid = (scores[len(scores)//2] + scores[len(scores)//2-1])/2
print(f"中位数:{mid}")

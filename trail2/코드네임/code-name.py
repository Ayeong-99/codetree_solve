MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.

class Student:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

students = []   
min_score = scores[0]
min_num = 0
for i in range(MAX_N):
    if min_score > scores[i]: # 더 작은 점수면 작은 점수 위치로 숫자 바꿔줌
        min_num = i
        min_score = scores[i]

    students.append(Student(codenames[i], scores[i]))

answer = students[min_num]
print(answer.codename, answer.score)
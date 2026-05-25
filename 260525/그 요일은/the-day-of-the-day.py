m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.

num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days = 0

def cal_day(m, d):
    day = 0
    for i in range(1, m):
        day += num_of_days[i]
    day += d
    return day

def check_day(a):
    for i in range(7):
        if weeks[i] == a:
            return i

num_day = check_day(A)

days = cal_day(m2, d2) - cal_day(m1, d1)
sol = num_weeks = days // 7
rest_day = days % 7

if num_day <= rest_day: # 주어진 요일이 남은 요일보다 작으면 반복된 주 + 1
    sol += 1

print(sol)
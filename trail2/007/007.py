secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class Message:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

answer = Message(secret_code, meeting_point, time)
print("secret code :", secret_code)
print("meeting point :", meeting_point)
print("time :", time)
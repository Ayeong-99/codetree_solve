unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class Bomb:
    def __init__(self, code, color, sec):
        self.unlock_code = code
        self.wire_color = color
        self.seconds = sec

input = Bomb(unlock_code,wire_color,seconds)
print(f"code : {input.unlock_code}")
print(f"color : {input.wire_color}")
print(f"second : {input.seconds}")

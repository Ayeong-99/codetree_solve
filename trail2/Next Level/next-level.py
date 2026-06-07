user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class G_message:
    def __init__(self, id = "codetree", level = 10):
        self.id = id
        self.level = level

user1 = G_message()
user2 = G_message(user2_id, user2_level)
print(f"user {user1.id} lv {user1.level}")
print(f"user {user2.id} lv {user2.level}")
    
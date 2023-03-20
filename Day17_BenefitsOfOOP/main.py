class User:
    def __init__(self, userid, username):
        self.id = userid
        self.user_name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "kishore")
user_2 = User("002", "william")

user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)
#
# # user_1.id = "kishore457"
# print(user_1.id)
# print(user_1.user_name)
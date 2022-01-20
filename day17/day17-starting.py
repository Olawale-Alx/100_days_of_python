class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def users(self):
        print(f'Welcome to Hades, User {self.username} with number {self.id}'
              f' with a following of {self.followers} people')

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User(2011, 'Frank')
user2 = User(1211, 'Larry')

user1.follow(user2)
print(user1.followers)
print(user1.following)
# user_1 = User(5087, 'Olawale')
# user_1.followers = 500
#
# user_1.users()
# print(user_1.followers)


# class Car:
#     def __init__(self):
#         self.seats = 5
#
#     def race_mode(self):
#         self.seats = 2
#         print(self.seats)
#
#
# car1 = Car()
# print(car1.seats)
# car1.race_mode()
#

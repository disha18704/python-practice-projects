class User:
    pass 

    def __init__(self,id):
        
        self.id = id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers +=1
        # increase the following count of the user who is doing the following.
        self.following += 1


user_1 = User(10)

user_2 = User(20)

# user_1 decided to follow user_2
user_1.follow(user_2)

# This is just for your understanding, [next 2 comments]

# self = user_1

# user = user_2

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
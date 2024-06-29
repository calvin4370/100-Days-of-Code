class User:
    # The init function (The constructor) is called every time an object is initialised
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

        self.followers = []
        self.following = []

    # class methods that were initialised need the self parameter to know which obj
    # is being called; When you call a class method in the future, it will ownself
    # put itself as the first argument, e.g. intro(), it will plop in inself as an argument
    def follow(self, user_followed):
        if user_followed.username not in self.following:
            user_followed.followers.append(self.username)
            self.following.append(user_followed.username)
            print(f"{self.username} followed {user_followed.username}")
        else:
            print(f"{self.username} is already following {user_followed.username}!")

    def print_info(self):
        print(f"{self.username} has {len(self.followers)} followers and is following {len(self.following)} users")

user1 = User(1, "Altair")
user2 = User(2, "Basim")
user3 = User(3, "Connor")

user1.follow(user2)
user1.follow(user3)
user2.follow(user1)
user2.follow(user3)
user3.follow(user1)

print()
user1.print_info()
user2.print_info()
user3.print_info()


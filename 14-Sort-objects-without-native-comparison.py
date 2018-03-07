from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


user1 = User('001')
user2 = User('002')
user99 = User('099')

users = [user1, user2, user99]

# sort by user_id
# print(sorted(users, key=lambda user: user.user_id, reverse=True))

# using attrgetter
print(sorted(users, key=attrgetter('user_id')))

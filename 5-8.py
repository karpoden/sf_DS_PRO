users_list = ['admin', 'ivan', 'ivan_ivan']

def chek(func):
    def chek_chek(user_name):
        
        if user_name in users_list:
            return True
        else:
            print('User not found')
    return chek_chek
@chek
def get_data_from_database():
    print("Super secure data from database")

print(get_data_from_database('aaadmin'))
#

users_list = ["admin", "ivan", "ivan_ivan"]

def user_auth(func):
    def wrapper():
        user = input("Enter username: ")
        if user in users_list:
            print("User authed")
            func()
        else:
            print("Unknown user!")

    return wrapper


@user_auth
def get_data_from_database():
    print("Super secure data from database")

get_data_from_database()

list_chek=['admin', 'danil', 'daniil']
def chek(func):
    def check_chek():
        users = input('users')
        if users in list_chek:
            return print('users in list')
            func()
        else:
            print('users not in list')
    return check_chek
@chek
def chek_user_in_list():
    print("user in list zaembumba")

chek_user_in_list()


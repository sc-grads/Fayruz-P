user = {'username': 'js', 'level': 'admin'}

def user_has_permission(func):
    def wrapper_user_has_permission():

        if user['level'] == 'admin':
            return func
        else:
            return None
    return wrapper_user_has_permission

def show_pass():
    return 'dfafUIS, .s'

my_function = user_has_permission(show_pass)
print(my_function())

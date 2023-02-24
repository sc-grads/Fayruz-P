user = {'username': 'js', 'level': 'admin'}


def only_admin(func):
    def wrapper_only_admin(*args, **kwargs):
        if user['level'] == 'admin':
            return func(*args, **kwargs)
        else:
            raise PermissionError('Permission Denied')

    return wrapper_only_admin


@only_admin  # @ or pie syntax
def remove_file(f=None):
    import os, os.path
    if os.path.isfile(f):
        os.remove(f)
        print(f'{f} removed')
    else:
        print('Argument is not in a file')

@only_admin
def create_user_and_group(user, group):
    print(f'This function create user {user} and group {group}')
    #code that creates user and group here

@only_admin
def update_system():
    print(f'This function updates the OS')



try:
    remove_file('a.txt')
except PermissionError as e:
    print(e)

create_user_and_group('admin', 'sudo')
update_system()
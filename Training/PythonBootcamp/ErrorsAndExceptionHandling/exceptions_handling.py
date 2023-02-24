while True:

    try:
        a = int(input('Enter a:'))
        b = int(input('Enter b:'))
        d = '7'
        c = a / b + d
        print(c)
    except ZeroDivisionError as e:
        print(f'Division by zero is not permitted{e.args}')
    except TypeError as e:
        print(f' Operations of different types not permitted: {e}')
    except Exception as e:
        print(f'A generic exception has occured: {e}')

    else:
        print('No errors')
        print(c)
        break
    finally:
        print('Good bye!')

x = 10
print(x ** x)
print('some other code')

age = -1
if age < 0:
    raise Exception('Age below zero is not permitted')
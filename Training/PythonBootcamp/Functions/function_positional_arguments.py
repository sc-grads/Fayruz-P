def difference(a, b):
    result = a - b
    print(result)


difference(1, 5)


# parameters vs. arguments
def func1(x, y, z):
    print(f'1st parameter x is {x}')
    print(f'1st parameter y is {y}')
    print(f'1st parameter z is {z}')


func1(y=7, x=3, z=9)
func1(10, 20, 30)
func1(6, z=1, y=9)
# func1(x=6, 1, z=9) # ERROR


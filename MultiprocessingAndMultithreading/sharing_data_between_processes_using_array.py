## Sharing data between processes using multiprocessing.Array
#################################################


import multiprocessing as mp


## Target function1
## The 2nd parameter is a list that will be modified inside the forked process
def squares(numbers, squares_list):
    for n in numbers:
        squares_list.append(n ** 2)
    print(f'square_list inside process {squares_list}')


## Target function2.
## The 2nd parameter is an Array used for sharing data between processes
def cubes(numbers, result):
    i = 0
    for num in numbers:
        result[i] = num ** 3
        i += 1
    print(f'result Array inside process/function: {result[::]}')


## This will be run only if the script is run directly (not imported as a module in another script)
## This is necessary!
if __name__ == '__main__':
    ## Calculating the square of these numbers in a new process
    ## Adding the result (the squares) in a list inside a process
    numbers = [1, 2, 3]
    squares_list = list()

    ## Creating, Starting and Joining the process
    p = mp.Process(target=squares, args=(numbers, squares_list))
    p.start()
    p.join()

    ## Printing the squares_list
    ## !! It hasn't been modified inside the process. The main process and the forked process didn't work on the same data
    print(f'squares_list outsite process {squares_list}')

    ## Creating an Array to share data beetween main process and the forked process
    result = mp.Array('i', len(numbers))

    #################################
    ## Creating, Starting and Joining the process
    p1 = mp.Process(target=cubes, args=(numbers, result))
    p1.start()
    p1.join()

    ## Printing the Array. It has been modified inside the forked-process. The array was shared between main and forked process
    print(f'result Array outside process {result[::]}')
################################################
## Sharing data between processes using multiprocessing.Value
#################################################


import multiprocessing as mp


## Target function that increments a counter (multiprocessing.Value)
def increment(counter):
    counter.value += 1


## Target function that increments a counter (integer)
def my_increment(my_counter):
    my_counter += 1


if __name__ == '__main__':
    my_counter = 1  # type integer
    counter = mp.Value('i', 1)  # type multiprocessing.Value

    ## Creating, starting and joining 10 processes. They increment the counter. This is of type multiprocessing.Value
    for i in range(10):
        process = mp.Process(target=increment, args=(counter,))
        process.start()
        process.join()

    print(f'counter of type multiprocessing.Value is {counter.value}')

    ## Creating, starting and joining 10 processes. They increment my_counter. This is of type integer
    for i in range(10):
        process = mp.Process(target=my_increment, args=(my_counter,))
        process.start()
        process.join()

    print(f'my_counter of type integer is {my_counter}')
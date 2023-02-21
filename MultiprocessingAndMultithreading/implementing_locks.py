################################################
## Using Locks to share data between processes
#################################################

import multiprocessing as mp
import time


## Target function. It increments a balance by 0.01  100 times
def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value += 1
        lock.release()


## Target function. It decrements a balance by 0.01  100 times
def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value -= 1
        lock.release()


if __name__ == '__main__':
    balance = mp.Value('i', 500)  ## starting balance
    print(f'Balance BEFORE running processes: {balance.value}')

    lock = mp.Lock()  # lock Object

    ## Creating, starting and joining 2 processes. They increment and decrement the shared value
    p1 = mp.Process(target=deposit, args=(balance, lock))
    p2 = mp.Process(target=withdraw, args=(balance, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    ## The final value of balance
    print(f'Balance AFTER running processes: {balance.value}')
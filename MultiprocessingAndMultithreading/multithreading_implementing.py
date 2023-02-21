##############################
## Implementing Threading
## The threading module
##############################

## Importing the module
import threading
import time


## Creating the target function. Each thread will execute this function in parallel
def name_and_time(name):
    print(f'Hello {name}, current time is {time.time()}')
    print('Sleeping for 2 seconds ...')
    time.sleep(2)
    print('After sleeping ... exiting function.')


## This will be run only if the script is run directly (not imported as a module in another script)
## This is necessary!
if __name__ == '__main__':
    thread_list = list()  # list that stores the threads

    ## Creating 10 threads
    for i in range(10):
        ## Creating each thread. 1st argument si the target function
        ## 2nd argument is a TUPLE (target function's arguments)
        thread = threading.Thread(target=name_and_time, args=('Andrei',))
        thread_list.append(thread)  # Appending each thread to the list

    ## Iterating over the list and start each thread
    for t in thread_list:
        t.start()

    ## Join the threads back to the main thread OR
    ## The main thread will wait for forked-threads to finish
    ## This is optional
    for t in thread_list:
        t.join()

    print('Other instructions of the main module...')
    print('End of Script')
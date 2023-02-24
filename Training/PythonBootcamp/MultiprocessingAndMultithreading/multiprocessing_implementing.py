##############################
## Implementing Multiprocessing
## The multiprocessing module
##############################

## Importing the module as an alias (a shorter name)
import multiprocessing as mp
import time


## Creating the target function. Each process will execute this function in parallel
def name_and_time(name):
    print(f'Hello {name}, current time is {time.time()}')
    print('Sleeping for 2 seconds ...')
    time.sleep(2)
    print('After sleeping ... exiting function.')


## This will be run only if the script is run directly (not imported as a module in another script)
## This is necessary!
if __name__ == '__main__':
    process_list = list()  # list that stores the processes

    ## Creating 10 processes
    for i in range(10):
        ## Creating each process. 1st argument si the target function
        ## 2nd argument is a TUPLE (target function's arguments)
        process = mp.Process(target=name_and_time, args=('Andrei',))
        process_list.append(process)  # Appending each process to the list

    ## Iterating over the list and start each process
    for p in process_list:
        p.start()

    ## Join the processes back to the main process OR
    ## The main process will wait for forked-processes to finish
    for p in process_list:
        p.join()

    print('Other instructions of the main module...')
    print('End of Script')
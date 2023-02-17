# Coding - The Sys module
##############################
## The sys module
##############################

## Importing the module
import sys

## Returns the version of the Python interpreter
sys.version

## Other info about the interpreter
sys.implementation

## Returns the platform (linux, win32 or mac)
sys.platform

## Returns the PATH (directories where it searches for modules)
sys.path

my_list = list(range(100))
sys.getsizeof(my_list)  # returns the size of the list in memory

## Redirecting output to a file instead of stdout (console)
original_stdout = sys.stdout  # saving the original stdout

## Using a file as stdout, redirecting output to a file
with open('stdout.txt', 'w') as sys.stdout:
    print('Printing a string')
    x = 10
    print(f'x is {x}')

sys.stdout = original_stdout  # restoring the original stdout
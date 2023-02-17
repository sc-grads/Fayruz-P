# Coding - The Os Module
##############################
## The OS module
##############################

## Importing the module
import os

## IMPORTANT!
## You should always use a valid path according to your operating system


## Returns the file that defines the module
os.__file__  # => '/usr/lib/python3.7/os.py'

cwd = os.getcwd()  # => returns the current working directory
print(cwd)

## changes the current working directory, OS specific
os.chdir('/home/user1/python')  # Linux specific
os.chdir('C:\\Users')  # Windows specific

os.path.isfile('/etc/passwd')  # returns True if argument is a file
os.path.isdir('/tmp')  # returns True if argument is a directory

## Splits the extension from a pathname, returns a tuple
name, extention = os.path.splitext('/var/log/kern.log')  # name is 'kern', extention is '.log'

## Listing a directory
os.listdir('.')  # returns the entries in the current working directory as a list
os.listdir('C:\\Users')  # returns the entries in the directory as a list

os.path.getmtime('/etc/passwd')  # => 1547047769.9049096, returns file's last modification time as a timestamp
os.path.getsize('/etc/passwd')  # => 2691, returns the size of a file

os.mkdir('PATH/dir')  # creates a new directory in PATH, os specific

## Creates a new directory called dir1 in Windows (permissions required)
os.mkdir('C:\\dir1')

## Creates a new directory called dir1 in Linux
os.mkdir('~/dir1')

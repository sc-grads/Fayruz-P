# Coding - The Shutil Module
##############################
## The shutil module
##############################

## Importing the module
import shutil

## Copying a.txt to b.txt. a.txt is in the current working directory
## It copies only file's content and not permissions or times
## If the destination file exists, it will be overwritten
shutil.copyfile('a.txt', 'b.txt')

# Copying a.txt to c.txt. a.txt is in the current working directory
# It copies the file data and the file’s permission mode. Other metadata is not preserved
shutil.copy('a.txt', 'c.txt')

## Use absolute PATHs specific to your OS
# shutil.copy('C:\\Users\\ad\\Desktop\\dir1\\file1.txt','C:\\Users\\ad\\Desktop\\dir2')


## copy2() function preserves all file's metadata
## It copies a.txt from the current directory to c.txt in dir1 directory which is in the current directory
shutil.copy2('a.txt', 'dir1/c.txt')

## Copying an entire directory. dir1 is a directory in the current working dirrectory
shutil.copytree('dir1', 'dir2')

## Moving or renaming files or directory
## It moves c.txt from the current directory to dir2/ which is another directory in the current directory
shutil.move('c.txt', 'dir2/')
shutil.move('dir2', 'dir1')  # moves a directory into another directory

## Renaming a file
## If the source and the destination are in the same directory, move() renames the file
shutil.move('b.txt', 'x.txt')  # renaming b.txt to x.txt

## Removing a directory. dir2 is a directory in the current working directory
shutil.rmtree('dir2')

## If trying to remove a file, it raises an exception
# shutil.rmtree('a.txt')     # => ERROR

## You should use os.remove() to remove a file
import os

os.remove('b.txt')
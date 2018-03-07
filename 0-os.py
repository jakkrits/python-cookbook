import os 

# show attributes and methods of the module
# print(dir(os))

# get current working directory
print(os.getcwd())

# change directory
# os.chdir('/Users/jakks/Desktop')
# print(os.getcwd())

# show files and directories
# print(os.listdir(os.getcwd()))

# create folder
# os.makedir('Made_By_PyOS') -- Not in python3.6

# create folder - multilevels
# os.makedirs('PyOS/subfolder1/sub2')
# os.makedirs('Made_By_PyOS')

# os.rmdir('Made_By_PyOS')  # remove only this dir
# os.removedirs('PyOS/subfolder1/sub2')
# print(os.listdir())

"""
USE ONLY os.makedirs & os.rmdir FOR SECURITY MEASURE
"""

# rename
# os.rename('test.txt', 'demo.txt')

# show file info
print(os.stat('demo.txt'))
# show stat time in human format
from datetime import datetime
print(datetime.fromtimestamp(os.stat('demo.txt').st_mtime))


# show directory tree
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print(f'{dirpath} - {dirnames} - {filenames}')

print('-+-*'*30)

# show HOME enviornment
HOME_DIR = os.environ.get('HOME')
print(HOME_DIR)

# create file path
file_path = os.path.join(HOME_DIR, 'text.txt')
print(file_path)  # /Users/jakks/text.txt

# show only filename
print(os.path.basename(file_path))

# show only dirnmae
print(os.path.dirname(file_path))

print(os.path.curdir)

# split fname into tuple
list_of_dir = os.path.split(file_path)
print(list_of_dir)

# check if file exists
print(os.path.exists(file_path))

# check if it's dir
print(os.path.isfile(file_path))

# check if it's file
print(os.path.isdir(file_path))

# split path and extension
print(os.path.splitext(file_path))
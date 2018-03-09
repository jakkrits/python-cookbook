import os

# change to dir that holds the files

os.chdir('/Users/jakks/Desktop/test')
print(os.getcwd())

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    print(file_name.split('-'))
    var1, var2, var3 = file_name.split('-')
    print(var1, var2, var3)
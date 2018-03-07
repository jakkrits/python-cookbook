f = open('demo.txt','r')
# r = read only
# r+ = read and write

print(f.name)
print(f.mode)

# close the file when done, if not -> mem leaks
f.close()

# or use WITH context manager
# auto close file when done

with open('demo.txt', 'r') as f:
    f_content = f.readlines()
    print(f_content)

print('*!'*40)

with open('demo.txt', 'r') as f_1:
    f_content = f_1.readline()
    print(f_content, end='')

    f_content = f_1.readline()
    print(f_content, end='+++++')

print('*!'*40)

with open('demo.txt', 'r') as f_2:
    for line in f_2:
        print(line, end='')

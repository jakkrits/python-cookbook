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

print('*'*80)

# read whole file or some amount
with open('demo.txt', 'r') as f_3:
    content = f_3.read(100)
    print(content, end='')

print('-'*40)

# read x characters at time
with open('demo.txt', 'r') as f:
    size_to_read = 10
    f_content = f.read(size_to_read)

    # current read position
    print(f.tell())

    # set position of cursor
    f.seek(0)  # set at the beginning

    while(len(f_content)) > 0:
        print(f_content, end='*')
        f_content = f.read(size_to_read)


# write
with open('new_text.txt', 'w') as f:  # if not exist, it will create. if it does, overwrite it.
    f.write('TEST')

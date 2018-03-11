try:
    pass
except Exception:
    pass
else:
    pass
finally:
    pass

try:
    f = open('tet.txt')
except Exception:
    print('ไม่มีไฟล์เหอะ ไอ้ควย')

try:
    with open('RegEx/snippets.txt') as f:
        for text in f:
            print(text)
        var = bad_var
except FileNotFoundError:
    print('Sorry No file')
except Exception as e:
    print(e)

# if TRY doesnt raise EXCEPTION, execute ELSE
try:
    f = open('RegEx/snippets.txt')
    print(text)
except FileNotFoundError:
    print('Sorry No file')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()

# FINALLY executes regardless
try:
    f = open('RegEx/snippets.txt')
    print(text)
except FileNotFoundError:
    print('Sorry No file')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('FINALLY')

print('*' * 30)

# RAISE your own
# if TRY doesnt raise EXCEPTION, execute ELSE
try:
    f = open('BAD_RegEx/snippets.txt')
    if f.name == 'snippets.txt':
        raise Exception
except Exception as e:
    print(f'GODDAMN IT! --> {e}')
else:
    print(f.read())
    f.close()
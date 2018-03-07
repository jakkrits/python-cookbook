def worker_info(*args, **kwargs):
    print(args)
    print(kwargs)

worker_info('Jakk', 'Fon', 'Ping', name="jakkrit", age=39)
workers = ['Jakk', 'Fon', 'Ping']
person_property = {'name': 'jakkrit', 'age': 39}

print('*'*50)
worker_info(workers, person_property)
# this will prints nothing
# put * and ** to unpack

worker_info(*workers, **person_property)


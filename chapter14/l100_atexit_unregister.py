import atexit

def my_cleanup(name):
    print('my_cleanup({})'.format(name))
atexit.register(my_cleanup, 'first')

atexit.register(my_cleanup, 'second')
atexit.register(my_cleanup, 'third')
atexit.unregister(my_cleanup)
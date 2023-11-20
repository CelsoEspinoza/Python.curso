
# Decorator Pattern
# This is how a decorator is created(function decorator -> wraper -> the func -> returns wraper)
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*********')
        func(*args, **kwargs)
        print('*********')
    return wrap_func

@my_decorator
def hello(greeting, emoji=':D'):
    print(greeting, emoji)


hello('Hello Celso!!!')
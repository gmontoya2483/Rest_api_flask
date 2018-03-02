# Decorators: it is a function that gets called before another function
# To create a decorators it is needed to import the functools library

import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator!")
        func()
        print ("After the decorator!")
    return function_that_runs_func


@my_decorator
def my_function():
    print("I´m the function!!!")


my_function()


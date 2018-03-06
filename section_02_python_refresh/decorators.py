# Decorators: it is a function that gets called before another function
# To create a decorators it is needed to import the functools library

import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator!")
        func()
        print ("After the decorator!\n")
    return function_that_runs_func


@my_decorator
def my_function():
    print("I´m the function!!!")
    
my_function()


## Decorators with arguments, suma un nivel al wrapping

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func():
            print("In the decorator, decorator parameter: {}".format(number))
            func()
            print("After the decorator, decorator parameter: {}\n".format(number))
        return function_that_runs_func
    return my_decorator


@decorator_with_arguments(56)
def my_function_too():
    print("Hello")

my_function_too()


## decoradores with arguments in the function, agrega *args, **kwargs

def my_decorator_three(func):
    @functools.wraps(func)
    def function_that_runs_func(*args, **kwargs):
        print("In the decorator!")
        func(*args, **kwargs)
        print ("After the decorator!\n")
    return function_that_runs_func


@my_decorator_three
def my_function_with_parameters(number_1, number_2):
    print("I´m the function!!!, the sum is {}".format(number_1 + number_2))
    
my_function_with_parameters(3,5)


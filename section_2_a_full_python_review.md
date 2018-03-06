# Section 2: A full Python refresh

## Variables

```python
    a = 5
    b = 10
    my_variable = 56

    string_variable = "hello"
    string_quotes = 'string can have single quotes'

    boolena = True
```

[Video: Explicacion sobre variables](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960054?start=0)

## Methods

```python
    def my_print_method(my_argument):
    print(my_argument)


    my_print_method("Hola, Mundo")


    def my_multiply_method (number_1, number_2):
    return number_1 * number_2


    result = my_multiply_method (5, 3)
    my_print_method (result)
```

[Video: Explicacion sobre Mthods](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960060?start=0)

## List, Tuples and sets

### list

```python
    list_grades = [77, 80, 90, 95, 100]
    list_grades.append(125)
    print(sum(list_grades) / len(list_grades))
```

### Touples

it is inmutable (you cannot increase the size)  

```python
    touple_grades = (77, 80, 90)
    print(sum(touple_grades) / len(touple_grades))
```

### sets

They unique & unordered, in the exaple below there will be only one 77. The print won´t be in the orer 77,80,90...  

```python
    set_grades = {77, 80, 90, 77, 95}
    print (set_grades)
```

[Video: Explicación de List, tuples and sets](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960062?start=0)

[Video: Explicación List, tuples and sets operations](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960064?start=0)

[Video: Explicación Advance sets operations](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960066?start=0)

## Loops

iterables are strings, lists, sets, tuples and more  

### for

```python
my_variable = "hello"
for character in my_variable:
    print (character)


my_list = [1, 2, 3, 5, 7, 9]
for number in my_list:
    print (number ** 2)
```

### while

```python
    user_wants_number = True
    while user_wants_number == True:
        print(10)
        user_input = input("Should we print again? (y/n)")
        if user_input == 'n':
            user_wants_number = False
```

[Video: explicación sobre loops](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960068?start=0)

## if statement

### if

```python
    should_continue = True
    if should_continue:
        print("Hello")
```

### if XX [not] in

```python
    know_people = ["John", "Anna", "Mary"]
    person = input("Enter the person you know: ")

    if person in know_people:
        print("You know {} !!".format(person))
    else:
        print("You don´t know {}".format(person))
```

### elif

```python
    a = 1

    if a == 0:
        print (Es igual a 0)
    elif a == 1:
        print (Es igual a 1)
    else:
        print (No es ni 0, ni 1)
```

[Video: explicación sobre if, if x in xxx, else, elif](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960070?start=0)

## List comprehension

[Video: Explicacion sobre List comprehension](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960074?start=0)

## Dictionaries

[Video: Explicacion sobre Dictionaries](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960078?start=0)

## Objects and Classes

[Video: Explicacion sobre Objects and classes](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960086?start=0)

## @classmethod and @staticmethods

[Video: Explicacion sobre @classmethod and @staticmethod](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960090?start=0)

## Inheritance

[Video: Explicacion sobre Inheritance](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960092?start=0)

## *args and **kwargs

[Video: *args and **kwargs](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960094?start=0)

## Passing functions as arguments

### Ejemplo 1:

```python
    def methodception(another):
   return another()

    def add_two_numbers():
    return 35 + 77

    print(methodception(add_two_numbers))
```

usando ```lambda``` wich is an anonymus function

```python
    print(methodception(lambda: 35 + 77))
```

### Ejemplo 2:

```python
    my_list = [13, 56, 77, 484]
    print(list(filter(lambda x: x !=13, my_list)))
```

usando funciones normales

```python
    def not_thirteen(x):
    return x != 13

    my_list = [13, 56, 77, 484]
    print(list(filter(not_thirteen,my_list)))
```

usando list comprenhension

```python
    my_list = [13, 56, 77, 484]
    print ([x for x in my_list if x != 13])
```

### Ejemplo 3:

```python
    def methodception_2 (number, another, *args):
        return another(*args) + number

    def multiply_two_numbers(number_1, number_2):
        return number_1 * number_2

    print (methodception_2(2,multiply_two_numbers,2,5))
```

[Video: Explicacion sobre Passing functions as arguments](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960096?start=0)

## Decorators

Decorators: it is a function that gets called before another function. To create a decorators it is needed to import the functools library

### Basic decorator without argumants

```python
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
```

## Decorators with arguments

Se agrega un nivel al wrapping.

```python
    import functools

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
```

### Decorators with arguments in the fuction

Se agregan los argumentos ```*args``` and ```**kwargs```

```python
    import functools

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
```

[Video: Explicacion sobre Decorators](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960098?start=0)

[Video: Explicacion sobre Advance Decorators](https://www.udemy.com/rest-api-flask-and-python/learn/v4/t/lecture/5960100?start=0)



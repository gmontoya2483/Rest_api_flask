def my_method (arg1, arg2):
    return arg1 + arg2
print ("my_method(arg1, arg2) -> my_method (5, 6): {}\n".format(my_method (5, 6)))



def my_list_method (list_arg):
    return sum(list_arg)
print ("my_list_method (list_arg) -> my_list_method ([2, 4, 6, 8, 9]): {}\n".format(my_list_method([2, 4, 6, 8, 9])))


def my_addition_method_simplified(*args):
    return sum(args)
print ("my_addition_method_simplified(*args) -> my_addition_method_simplified(2, 4, 6, 8, 9) : {}\n".format(my_addition_method_simplified(2, 4, 6, 8, 9)))

##

def what_are_kwargs (*args, **kwargs):
    print(args)
    print(kwargs)
    print("\n")

print ("what_are_kwargs(*args, **kwargs) -> what_are_kwargs(2, 4, 8)" )
what_are_kwargs(2, 4, 8)

print ("what_are_kwargs(*args, **kwargs) -> what_are_kwargs(2, 4, 8, name='Jose', location='UK')" )
what_are_kwargs(2, 4, 8, name='Jose', location='UK')

def what_are_kwargs_2 (name, location):
    print(name)
    print(location)
    print("\n")
print ("what_are_kwargs_2(name, location) -> what_are_kwargs_2(location='UK', name='Jose')" )
what_are_kwargs_2(location='UK', name='Jose')





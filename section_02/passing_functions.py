# Passing functions as parameters
# Generalize code

def methodception(another):
   return another()


def add_two_numbers():
    return 35 + 77


print(methodception(add_two_numbers))

print(methodception(lambda: 35 + 77)) # lambda -> anonymus function

my_list = [13, 56, 77, 484]
print(list(filter(lambda x: x !=13, my_list)))


## lambda tranlation to normal functions
def not_thirteen(x):
    return x != 13
print(list(filter(not_thirteen,my_list)))

## translate lambda to list comprehension
print ([x for x in my_list if x != 13])






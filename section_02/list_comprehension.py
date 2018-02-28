## list comprehension it´s a way to create lists programatically

# Create an equal list
my_list = [0, 1, 2, 3, 4]
an_equal_list_1 = [x for x in my_list] # we are adding x to the an_equal_list 1 for each x in my_list
print ("Create an equal list:")
print("original list:")
print (my_list)
print("an equal list 1:")
print (an_equal_list_1)
print ("\n")

# Create a list from a range with stop 
list_from_range = [x for x in range(7)] #creates a range from 0 to 6 of integers
print("Create a list from range(7) - [x for x in range(7)]")
print (list_from_range)
print ("\n")


# Create a list from a range multipying each value by 3
list_from_range_by_3 =  [x * 3 for x in range(7)]
print("Create a list multipying each value by 3 - [x * 3 for x in range(7)")
print (list_from_range_by_3)
print ("\n")

# Create a list from a range with start and stop 
list_from_range_4_7 =  [x for x in range(4, 7)]
print("Create a list from the range (4, 7) - [x for x in range(4, 7)")
print (list_from_range_4_7)
print ("\n")

# Create a list from a range with start and stop 
list_from_range_4_7 =  [x for x in range(4, 7)]
print("Create a list from the range (4, 7) - [x for x in range(4, 7)")
print (list_from_range_4_7)
print ("\n")

# Create a list from a range with start, stop and step 
list_from_range_7_3__1 =  [x for x in range(7, 3, -1)]
print("Create a list from the range (7, 3, -1) - [x for x in range(7, 3, -1)")
print (list_from_range_7_3__1)
print ("\n")

# Create a reverse list 
my_string_list = ['one', 'two','three', 'four', 'five']
list_string_inverted = [my_string_list[x-1] for x in range(len(my_string_list),0,-1)]
print("Create a list from  [my_string_list8[x-1] for x in range(len(my_string_list),1,-1)]")
print("original list: my_string_list")
print(my_string_list)
print("reversed list:")
print (list_string_inverted)
print ("\n")


# create a list with if statement
list_even_numbers = [n for n in range(50) if n % 2 == 0]
print("even numbers list: [n for n in range(50) if n % 2 == 0]")
print (list_even_numbers)
print ("\n")

# Create a normalized list
people_you_know = ["Rodolf","  joHn","anna","GREG"]
normalized_people = [person.strip().lower() for person in people_you_know]
print("Unnormalized list - people_you_know")
print (people_you_know)
print("Normalized list - [person.strip().lower() for person in people_you_know]")
print (normalized_people)
print ("\n")

















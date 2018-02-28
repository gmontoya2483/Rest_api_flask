

## Excersice 19


def who_do_you_know():
    # Ask the user for a list of people they know
    persons = input("Enter the list of persons you know, separated by commas: ")
    # Split the string into a list
    list_persons_with_spaces = persons.split(",")
    
    # remove the spaces
    list_persons_without_spaces = [person.strip() for person in list_persons_with_spaces]
    
    # Return that list
    return list_persons_without_spaces

def ask_user():
    # Ask user for a name
    person = input("Enter a name of someone you know: ")
    # See if their name is in the list of people they know
    # Print out that they know the persosn
    if person in who_do_you_know():
        print("You know {} !!".format(person))
    else:
        print("You don´t know {}".format(person))


ask_user()






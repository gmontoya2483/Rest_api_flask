my_variable = "hello"

## Without Lists

grade_one = 77
grade_two = 80
grade_three = 90
grade_four = 95
grade_five = 100

print ((grade_one + grade_two + grade_three + grade_four + grade_five) / 5)


## Lists

list_grades = [77, 80, 90, 95, 100, 105, 107, 120]
list_grades.append(125)
print(sum(list_grades) / len(list_grades))

## Touple - it is inmutable (you cannot increase the size)
touple_grades = (77, 80, 90, 95, 100, 105, 107)
print(sum(touple_grades) / len(touple_grades))


## Sets - unique & unordered -> in the exaple below there will be only one 77 and one 100
##                              the print won´t be in the orer 77,80,90...

set_grades = {77, 80, 90, 95, 100, 100, 105, 107,77}
print (set_grades)


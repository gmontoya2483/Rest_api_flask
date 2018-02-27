my_variable = "hello"

## Without Lists

grade_one = 77
grade_two = 80
grade_three = 90
grade_four = 95
grade_five = 100

print ((grade_one + grade_two + grade_three + grade_four + grade_five) / 5)


## Lists

list_grades = [77, 80, 90, 95, 100]
list_grades.append(125)
print(sum(list_grades) / len(list_grades))

## Touple - it is inmutable (you cannot increase the size)
touple_grades = (77, 80, 90)
print(sum(touple_grades) / len(touple_grades))


## Sets - unique & unordered -> in the exaple below there will be only one 77 and one 100
##                              the print won´t be in the orer 77,80,90...

set_grades = {77, 80, 90, 95}
print (set_grades)

## Operations with lists
list_grades.append(450)
print (list_grades)
print (list_grades[0])
list_grades[0] = 60
print (list_grades)

## Operations with Touple
touple_grades = touple_grades + (100,)
print(touple_grades)
print(touple_grades [0])


## Operation with grades
set_grades.add (61)
print(set_grades)




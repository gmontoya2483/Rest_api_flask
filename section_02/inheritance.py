class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        return sum(self.marks) / len(self.marks)
    

    def friend(self, friend_name):
        #return a new Student called 'friend_name' in the same school as self
        return Student (friend_name, self.school)
    

##

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary



anna = WorkingStudent ("Anna", "Oxford",1234.56)
friend = anna.friend ("Greg")
print(anna.name)
print(anna.salary)
print(friend.name)



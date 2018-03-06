class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        return sum(self.marks) / len(self.marks)
    
    @classmethod
    def friend(cls,origin, friend_name, *args, **kwargs):
        #return a new Student called 'friend_name' in the same school as self
        return cls (friend_name, origin.school, *args, **kwargs)
    

##

class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title



anna = WorkingStudent ("Anna", "Oxford",1234.56, "Team Leader")
friend = Student.friend (anna,"Greg")

print(anna.name)
print(anna.salary)
print(anna.job_title)
print(friend.name)


friend_2 = WorkingStudent.friend(friend,"Maria",23.15,"Analista")
print(friend_2.name)
print(friend_2.salary)
print(friend_2.job_title)


friend_3 = WorkingStudent.friend(anna,"Jose",job_title="corredor", salary=231.45)
print(friend_3.name)
print(friend_3.salary)
print(friend_3.job_title)

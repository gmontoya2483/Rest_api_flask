lottery_player_dict = {
    'name':'Rolf',
    'numbers':(5, 9, 12, 3, 1, 21)
}


class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)
    
    def total(self):
        return sum(self.numbers)



player_one = LotteryPlayer('Rolf')
player_two = LotteryPlayer('John')

print(player_one.name)
print(player_one.numbers)
print(player_one.total())

print(player_one == player_two)
print(player_one.name == player_two.name)


## Student class

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average (self):
        return sum(self.marks)/len(self.marks)
    
    @classmethod
    def go_to_school(cls):
        print("I'm going to school.")
        print("I'm a {}".format(cls))
    
    @staticmethod
    def comming_back_from_school():
        print("I'm comming back from school.")

    

anna = Student("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(71)
print(anna.marks)
print(anna.average())
Student.go_to_school()
Student.comming_back_from_school()

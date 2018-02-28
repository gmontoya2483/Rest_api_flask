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
